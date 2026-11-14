"""Merge audited protected-product extractions into the public pilot.
This module reads numeric checkpoints, never Earthdata credentials.
"""
import hashlib
import json
import math
from pathlib import Path

ALLOWED_FEATURES = {'ndvi_mean', 'night_lights'}

def load_bundle(root, name, processor):
    path = root / 'data' / name
    if not path.exists():
        return None
    result = json.loads(path.read_text(encoding='utf-8-sig'))
    if result.get('schemaVersion') != 1 or not isinstance(result.get('sites'), list):
        raise ValueError('Unsupported protected-product checkpoint schema')
    processing = result.get('processing', {})
    expected = hashlib.sha256((root / 'data/project.json').read_bytes()).hexdigest()
    if processing.get('configSha256') != expected:
        raise ValueError('Protected-product extraction has stale AOIs/configuration; rebuild it')
    actual = hashlib.sha256((root / processor).read_bytes()).hexdigest()
    recorded = processing.get('parserSha256', processing.get('codeSha256'))
    if recorded != actual:
        raise ValueError('Protected-product extraction has stale processor code; rebuild it')
    return result

def merge_site(site, extracted, source_ids):
    if extracted.get('id') != site['id']:
        raise ValueError('Protected-product site identifier mismatch')
    for name, feature in extracted.get('features', {}).items():
        if name not in ALLOWED_FEATURES:
            continue
        value = feature.get('value')
        if value is None:
            site['features'][name].update(feature, value=None, status='missing')
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('Invalid protected-product measurement')
        if name == 'ndvi_mean' and not -0.2 <= value <= 1:
            raise ValueError('NDVI outside the MOD13Q1 physical range')
        if name == 'night_lights' and value < 0:
            raise ValueError('Negative physical night radiance')
        if feature.get('sourceId') not in source_ids:
            raise ValueError('Unattributed protected-product measurement')
        site['features'][name].update(feature)
    if extracted.get('mineral_summary'):
        site['mineralSummary'] = extracted['mineral_summary']
    if extracted.get('missing'):
        site['missing'].extend(extracted['missing'])
    return site

def environmental_proxies(features, scales):
    ndvi = features.get('ndvi_mean', {}).get('value')
    lights = features.get('night_lights', {}).get('value')
    ceiling, radiation_scale = scales['ndviBareGroundCeiling'], scales['nightLightsRadiance']
    if ceiling <= 0 or radiation_scale <= 0:
        raise ValueError('Positive environmental proxy scales are required')
    bare = max(0., min(1., 1. - ndvi / ceiling)) if ndvi is not None else None
    isolation = math.exp(-lights / radiation_scale) if lights is not None else None
    return bare, isolation


def source_records(root, bundle, checkpoint):
    """Canonical origins plus original hashes; public extraction is the replay checkpoint."""
    from urllib.parse import urlparse
    extraction_hash = hashlib.sha256((root / 'data' / checkpoint).read_bytes()).hexdigest()
    records = []
    for original in bundle.get('sources', []):
        source = dict(original)
        host = (urlparse(source.get('url', '')).hostname or '').lower()
        if not (host == 'nasa.gov' or host.endswith('.nasa.gov')):
            raise ValueError('Protected measurement lacks an official NASA origin')
        raw_path = source.get('rawPath', source.get('cachePath'))
        if not raw_path:
            raise ValueError('Protected granule has no original file reference')
        resolved = (root / raw_path).resolve()
        if not resolved.is_relative_to((root / '.local/earthdata-data').resolve()):
            raise ValueError('Protected science path escapes the science cache')
        source.update(kind='protected-granule', cachePath=raw_path, status='available',
                      extractionPath='data/' + checkpoint, extractionSha256=extraction_hash)
        records.append(source)
    return records
