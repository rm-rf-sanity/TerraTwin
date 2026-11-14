"""Bounded, resumable downloads of authenticated NASA science granules.
Only canonical NASA URLs enter manifests. Credentials and signed redirect URLs never do.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlencode, urlparse
import requests
from .earthdata_access import load_token, session_for, nasa_host, science_file_prefix

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / 'data/protected-manifest.json'
MIB = 1024 * 1024

class DownloadError(RuntimeError):
    pass

def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    temporary.replace(path)

def sha256_file(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(MIB), b''):
            digest.update(chunk)
    return digest.hexdigest()

def canonical_url(url):
    parsed = urlparse(url)
    if not nasa_host(url) or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise DownloadError('Expected a canonical HTTPS NASA data URL without credentials or query parameters')
    return url

def expected_size(headers, status):
    if status == 206:
        match = re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)', headers.get('Content-Range', ''))
        if not match:
            raise DownloadError('NASA byte-range response has no valid total length')
        return int(match[3])
    length = headers.get('Content-Length')
    if status == 200 and length and length.isdigit():
        return int(length)
    raise DownloadError('NASA response has no bounded object size')

def normalize_granule(entry, *, site_id='salda', bbox=None):
    links = [link['href'] for link in entry.get('data_links', entry.get('links', []))
             if link.get('rel', '').endswith('/data#') and nasa_host(link.get('href', ''))
             and not urlparse(link['href']).query and urlparse(link['href']).path.lower().endswith(('.hdf','.h5','.nc','.tif','.tiff','.zip'))]
    if not links:
        raise DownloadError('No official NASA data link found for granule')
    url = canonical_url(links[0])
    granule = entry.get('granule_ur', entry.get('producer_granule_id', entry.get('title')))
    product = entry.get('short_name')
    if not product or not isinstance(granule,str) or not granule:
        raise DownloadError('Granule product short name and identifier are required')
    return {'id': product + ':' + granule, 'shortName': product, 'version': str(entry.get('version', '')),
            'granuleId': entry.get('granule_id', entry.get('id')), 'granuleUr': granule,
            'acquisitionPeriod': {'start': entry.get('time_start'), 'end': entry.get('time_end')},
            'url': url, 'selection': {'siteId': site_id, 'bbox': bbox or entry.get('aoi_bbox')},
            'rawPath': '.local/earthdata-data/' + Path(urlparse(url).path).name, 'assets': [canonical_url(link) for link in links]}

def companion(record, url, kind):
    """Select a verified same-granule asset without changing its collection/version."""
    url=canonical_url(url)
    if url not in record.get('assets', [record['url']]):
        raise DownloadError('Companion is not among the granule verified NASA data links')
    return {**record, 'id':record['id']+':'+kind, 'url':url, 'kind':kind,
            'rawPath':'.local/earthdata-data/'+Path(urlparse(url).path).name}

class CMRClient:
    """Public NASA CMR discovery. Authentication is only used for the subsequent data download."""
    endpoint = 'https://cmr.earthdata.nasa.gov/search/granules.json'
    def search(self, *, short_name, version, bbox, start, end, count=1, collection_concept_id=None):
        if not 1 <= count <= 100:
            raise DownloadError('CMR result count must be between1 and100')
        if len(bbox) != 4 or not (-180 <= bbox[0] < bbox[2] <= 180 and -90 <= bbox[1] < bbox[3] <= 90):
            raise DownloadError('Invalid west,south,east,north bounding box')
        if dt.datetime.fromisoformat(start.replace('Z', '+00:00')) > dt.datetime.fromisoformat(end.replace('Z', '+00:00')):
            raise DownloadError('CMR start is after end')
        params = {'bounding_box': ','.join(map(str, bbox)), 'temporal': start + ',' + end,
                  'page_size': count, 'sort_key': '-start_date'}
        if collection_concept_id:
            params['collection_concept_id'] = collection_concept_id
        else:
            params.update(short_name=short_name, version=version)
        try:
            response = requests.get(self.endpoint, params=params, timeout=(10, 40))
            if response.status_code != 200:
                raise DownloadError('NASA CMR returned HTTP' + str(response.status_code))
            payload = response.json()
        except (requests.RequestException, ValueError):
            raise DownloadError('NASA CMR discovery failed') from None
        key = hashlib.sha256(urlencode(params).encode()).hexdigest()[:16]
        snapshot = ROOT / ('data/provenance/protected-cmr-' + key + '.json')
        atomic_json(snapshot, payload)
        result = []
        for item in payload.get('feed', {}).get('entry', []):
            augmented = dict(item, short_name=short_name, version=version)
            record = normalize_granule(augmented, site_id='salda', bbox=bbox)
            record['discovery'] = {'url': response.url, 'snapshot': snapshot.relative_to(ROOT).as_posix(),
                                   'sha256': sha256_file(snapshot), 'periodRequested': {'start': start, 'end': end}}
            result.append(record)
        return result

class Downloader:
    def __init__(self, *, offline=False, max_file_bytes=250*MIB, max_total_bytes=500*MIB,
                 manifest_path=None, token=None):
        self.offline = offline
        self.max_file_bytes = max_file_bytes
        self.max_total_bytes = max_total_bytes
        self.manifest_path = manifest_path or DEFAULT_MANIFEST
        self._token = token
        self._session = None
        self.used_bytes = 0
        if self.manifest_path.exists():
            self.manifest = json.loads(self.manifest_path.read_text(encoding='utf-8'))
        else:
            self.manifest = {'schemaVersion': 1, 'downloads': []}
    def close(self):
        if self._session:
            self._session.close()
        self._token = None
    def _get(self, url, headers):
        if self.offline:
            raise DownloadError('Offline mode cannot issue network requests')
        if not self._token:
            self._token = load_token()
        if self._session is None:
            self._session = session_for(self._token)
        try:
            return self._session.get(url, headers={'Authorization': 'Bearer ' + self._token,
                                     'User-Agent': 'TerraTwin bounded NASA data download/1.0', **headers},
                                     stream=True, timeout=(10, 60))
        except requests.RequestException:
            raise DownloadError('NASA download network request failed; credentials omitted from diagnostics') from None
    def _write_manifest(self, record):
        rows = [r for r in self.manifest['downloads'] if r['id'] != record['id']]
        rows.append(record)
        self.manifest.update(generatedAt=utc_now(), downloads=sorted(rows, key=lambda r:r['id']))
        atomic_json(self.manifest_path, self.manifest)
    def download(self, selected):
        selected = dict(selected)
        url = canonical_url(selected['url'])
        target = ROOT / selected['rawPath']
        allowed = (ROOT / '.local/earthdata-data').resolve()
        if not target.resolve().is_relative_to(allowed):
            raise DownloadError('Raw path escapes the local science-data directory')
        previous = next((r for r in self.manifest['downloads'] if r['id'] == selected['id']), None)
        if target.exists():
            if not previous or previous['url'] != url or target.stat().st_size != previous['bytes'] or sha256_file(target) != previous['sha256']:
                raise DownloadError('Existing science file failed manifest checksum/size verification')
            self.used_bytes += previous['bytes']
            if self.used_bytes > self.max_total_bytes:
                raise DownloadError('Selected files exceed configured total byte budget')
            return previous
        if self.offline:
            raise DownloadError('Offline science file is missing: ' + selected['shortName'])
        with self._get(url, {'Range': 'bytes=0-31'}) as probe:
            if probe.status_code not in (200, 206):
                raise DownloadError('NASA data probe returned HTTP' + str(probe.status_code))
            size = expected_size(probe.headers, probe.status_code)
            if size > self.max_file_bytes or self.used_bytes + size > self.max_total_bytes:
                raise DownloadError('NASA object exceeds configured download byte budget')
            prefix = probe.raw.read(32)
            if not science_file_prefix(prefix):
                raise DownloadError('NASA data response is not a supported science-file format')
            etag = probe.headers.get('ETag')
        target.parent.mkdir(parents=True, exist_ok=True)
        partial = target.with_suffix(target.suffix + '.part')
        partial_meta = partial.with_suffix(partial.suffix + '.json')
        if partial.exists():
            if not partial_meta.exists():
                raise DownloadError('Partial file has no provenance; refusing ambiguous resume')
            stored = json.loads(partial_meta.read_text())
            if stored != {'url': url, 'bytes': size, 'etag': etag}:
                raise DownloadError('NASA object metadata changed; refusing to resume old bytes')
        offset = partial.stat().st_size if partial.exists() else 0
        if offset > size:
            raise DownloadError('Partial file exceeds declared NASA object length')
        atomic_json(partial_meta, {'url': url, 'bytes': size, 'etag': etag})
        if offset < size:
            headers = {'Range': 'bytes=' + str(offset) + '-'}
            if offset and etag:
                headers['If-Range'] = etag
            try:
                with self._get(url, headers) as response:
                    if response.status_code not in (200, 206):
                        raise DownloadError('NASA download returned HTTP' + str(response.status_code))
                    if expected_size(response.headers, response.status_code) != size:
                        raise DownloadError('NASA object size changed during download')
                    if response.status_code == 206:
                        start = int(re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)', response.headers['Content-Range'])[1])
                        if start != offset:
                            raise DownloadError('NASA returned an unexpected resume position')
                    elif offset:
                        offset = 0  # server ignored range; restart safely rather than append a complete file
                    with partial.open('ab' if offset else 'wb') as stream:
                        written = offset
                        for chunk in response.iter_content(chunk_size=MIB):
                            if not chunk:
                                continue
                            if written + len(chunk) > size:
                                raise DownloadError('NASA response exceeds declared object length')
                            stream.write(chunk)
                            written += len(chunk)
            except requests.RequestException:
                raise DownloadError('NASA download interrupted; verified partial bytes retained for resume') from None
        if partial.stat().st_size != size:
            raise DownloadError('Incomplete NASA object; partial bytes retained for resume')
        with partial.open('rb') as stream:
            if not science_file_prefix(stream.read(32)):
                raise DownloadError('Downloaded object has an unexpected file signature')
        digest = sha256_file(partial)
        partial.replace(target)
        # Keep the tiny local resume record; it contains only canonical source metadata.
        record = {**selected, 'bytes': size, 'sha256': digest, 'retrievedAt': utc_now(),
                  'status': 'downloaded', 'distribution': 'Official NASA origin; authenticated HTTPS redirects may use NASA CDN',
                  'etag': etag, 'subset': False,
                  'note': 'Whole source granule downloaded. selection.bbox identifies intended analysis area, not a spatially subset file.'}
        self.used_bytes += size
        self._write_manifest(record)
        return record

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--products', nargs='+')
    parser.add_argument('--all-recorded', action='store_true', help='Replay every existing manifest asset, including quality companions; no new discovery')
    parser.add_argument('--max-total-mib', type=int, default=500)
    parser.add_argument('--start', help='Optional CMR observation start, ISO8601')
    parser.add_argument('--end', help='Optional CMR observation end, ISO8601')
    args = parser.parse_args(argv)
    if bool(args.start) != bool(args.end):
        parser.error('--start and --end must be supplied together')
    if args.all_recorded or args.offline and args.start:
        if not DEFAULT_MANIFEST.exists():
            raise DownloadError('Recorded download manifest is missing')
        selected=json.loads(DEFAULT_MANIFEST.read_text(encoding='utf-8'))['downloads']
        if args.products:
            selected=[r for r in selected if r['shortName'] in args.products]
        if args.start:
            start=dt.datetime.fromisoformat(args.start.replace('Z','+00:00'))
            end=dt.datetime.fromisoformat(args.end.replace('Z','+00:00'))
            selected=[r for r in selected if dt.datetime.fromisoformat(r['acquisitionPeriod']['start'].replace('Z','+00:00')) <= end and dt.datetime.fromisoformat(r['acquisitionPeriod']['end'].replace('Z','+00:00')) >= start]
        entries=[]
    else:
        registry = json.loads((ROOT/'data/source-registry.json').read_text(encoding='utf-8'))
        products=args.products or ['MOD13Q1','EMITL2BMIN','VNP46A2']
        entries = [r for r in registry['granule_access_checks'] if r['short_name'] in products]
        selected=[]
    for entry in entries:
        if args.start:
            selected.extend(CMRClient().search(short_name=entry['short_name'],version=entry['version'],bbox=entry['aoi_bbox'],
                            start=args.start,end=args.end,collection_concept_id=entry.get('collection_concept_id'),count=1))
        else:
            selected.append(normalize_granule(entry))
    if not selected:
        raise DownloadError('No matching NASA granules selected')
    downloader = Downloader(offline=args.offline,max_total_bytes=args.max_total_mib*MIB)
    try:
        for entry in selected:
            record = downloader.download(entry)
            print(json.dumps({'product':record['shortName'],'granule':record['granuleUr'],'bytes':record['bytes'],
                              'sha256':record['sha256'],'rawPath':record['rawPath']}),flush=True)
    finally:
        downloader.close()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
