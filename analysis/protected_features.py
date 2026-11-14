"""Extract quality-screened, geolocated NASA protected-product AOI evidence.
Run with the optional scientific environment. No authentication is read here.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import re
from contextlib import ExitStack
import numpy as np
from .run import area

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def parse_grid(structure):
    """Parse actual HDF-EOS metadata; never infer sinusoidal pixels as lat/lon."""
    if isinstance(structure, bytes):
        structure = structure.decode('ascii').rstrip('\x00')
    def integer(name):
        match = re.search(r'\b' + name + r'\s*=\s*(\d+)', structure)
        if not match:
            raise ValueError('Missing grid dimension: ' + name)
        return int(match.group(1))
    def pair(name):
        match = re.search(r'\b' + name + r'\s*=\s*\(([^)]+)\)', structure)
        if not match:
            raise ValueError('Missing grid corner: ' + name)
        result = [float(x.strip()) for x in match.group(1).split(',')]
        if len(result) != 2:
            raise ValueError('Invalid grid corner')
        return result
    projection = re.search(r'\bProjection\s*=\s*([A-Za-z0-9_]+)', structure)
    if not projection:
        raise ValueError('Missing projection')
    result = {'width': integer('XDim'), 'height': integer('YDim'), 'ul': pair('UpperLeftPointMtrs'), 'lr': pair('LowerRightMtrs'), 'projection': projection.group(1)}
    if 'SNSOID' in result['projection']:
        parameters = re.search(r'ProjParams\s*=\s*\(([^)]+)\)', structure)
        if not parameters:
            raise ValueError('Missing sinusoidal sphere parameters')
        radius = float(parameters.group(1).split(',')[0])
        if not 6300000 < radius < 6400000:
            raise ValueError('Unexpected sinusoidal Earth radius')
        result['radiusM'] = radius
    elif result['projection'] in ('GCTP_GEO', 'HE5_GCTP_GEO'):
        # HDF-EOS geographic whole-degree corners use packed DMS (degrees *1e6 here).
        if any(abs(x) > 360 for x in result['ul'] + result['lr']):
            result['ul'] = [x / 1e6 for x in result['ul']]
            result['lr'] = [x / 1e6 for x in result['lr']]
        if any(abs(x) > 180 for x in (result['ul'][0], result['lr'][0])):
            raise ValueError('Invalid geographic longitude')
    else:
        raise ValueError('Unsupported source projection: ' + result['projection'])
    if result['width'] < 1 or result['height'] < 1 or result['ul'][0] >= result['lr'][0] or result['ul'][1] <= result['lr'][1]:
        raise ValueError('Invalid source grid extent')
    return result


def polygon_mask(xs, ys, ring):
    """Pixel-coordinate point-in-polygon mask, preserving the actual AOI footprint."""
    xs, ys = np.broadcast_arrays(xs, ys)
    inside = np.zeros(xs.shape, dtype=bool)
    for a, b in zip(ring[:-1], ring[1:]):
        crossing = (a[1] > ys) != (b[1] > ys)
        if a[1] != b[1]:
            boundary = (b[0] - a[0]) * (ys - a[1]) / (b[1] - a[1]) + a[0]
            inside ^= crossing & (xs < boundary)
    return inside


def grid_window(grid, ring):
    xmin, ymax = grid['ul']; xmax, ymin = grid['lr']
    x0, x1 = min(p[0] for p in ring), max(p[0] for p in ring)
    y0, y1 = min(p[1] for p in ring), max(p[1] for p in ring)
    if x1 <= xmin or x0 >= xmax or y1 <= ymin or y0 >= ymax:
        return None
    dx = (xmax - xmin) / grid['width']; dy = (ymax - ymin) / grid['height']
    c0 = max(0, math.floor((x0 - xmin) / dx)); c1 = min(grid['width'], math.ceil((x1 - xmin) / dx))
    r0 = max(0, math.floor((ymax - y1) / dy)); r1 = min(grid['height'], math.ceil((ymax - y0) / dy))
    if c0 >= c1 or r0 >= r1:
        return None
    xs = xmin + (np.arange(c0, c1) + .5) * dx
    ys = ymax - (np.arange(r0, r1) + .5) * dy
    return {'row': r0, 'col': c0, 'rows': r1-r0, 'cols': c1-c0}, polygon_mask(xs[None, :], ys[:, None], ring)


def base_summary(values, accepted, inside, minimum, eligible=None):
    total = int(np.count_nonzero(inside)); valid = int(np.count_nonzero(accepted & inside))
    eligible_pixels = int(np.count_nonzero(inside & eligible)) if eligible is not None else total
    fraction = valid / eligible_pixels if eligible_pixels else 0.
    value = float(np.mean(values[accepted & inside], dtype=np.float64)) if valid and fraction >= minimum else None
    return {'value': round(value, 8) if value is not None else None, 'status': 'derived' if value is not None else 'missing',
            'validPixels': valid, 'totalPixels': total, 'eligibleLandPixels': eligible_pixels, 'coverageDenominator': 'eligible_land_pixels' if eligible is not None else 'geometric_AOI_pixels', 'geometricValidFraction': round(valid/total,8) if total else 0., 'validFraction': round(fraction, 8),
            'reason': None if value is not None else 'insufficient_quality_valid_land_pixels', 'minimumValidFraction': minimum, 'qualityValidSubsetMean': round(float(np.mean(values[accepted & inside],dtype=np.float64)),8) if valid else None, 'subsetInterpretation': 'Diagnostic mean of accepted samples only; NEVER a score input when value is null.'}


def summarize_ndvi(raw, quality, reliability, inside, minimum=.5):
    raw = np.asarray(raw); qa = np.asarray(quality, dtype=np.uint16); reliability = np.asarray(reliability)
    inside = np.asarray(inside, dtype=bool)
    if raw.shape != qa.shape or raw.shape != reliability.shape or raw.shape != inside.shape:
        raise ValueError('MODIS NDVI/QA/reliability/AOI shapes differ')
    land = ((qa >> 11) & 7) == 1
    accepted = ((raw >= -2000) & (raw <= 10000) & (raw != -3000) & (qa != 65535) & (reliability == 0) &
                ((qa & 3) == 0) & (((qa >> 2) & 15) <= 2) & (((qa >> 6) & 3) != 3) &
                ((qa & (1 << 8)) == 0) & ((qa & (1 << 10)) == 0) & ((qa & (1 << 14)) == 0) & ((qa & (1 << 15)) == 0) & land)
    # C6.1 HDF scale_factor=10000 is a divisor, not a multiplier.
    result = base_summary(raw.astype(np.float64) / 10000., accepted, inside, minimum, land)
    result.update(unit='NDVI', nativeResolution='250 m nominal, MODIS sinusoidal; 16-day composite',
                  quality={'policy': 'Pixel reliability0; MODLAND00; usefulness<=2; non-high aerosol; no adjacent/mixed cloud/snow/shadow; land-only',
                           'landPixels': int(np.count_nonzero(inside & land)), 'fillPixels': int(np.count_nonzero(inside & (raw == -3000)))},
                  interpretation='Mean of quality-valid land NDVI pixels in this single16-day composite; not vegetation-area fraction or annual land-use classification.')
    return result


def summarize_ntl(raw, mandatory, cloud, snow, inside, minimum=.5):
    raw = np.asarray(raw, dtype=np.float64); mandatory = np.asarray(mandatory); qa = np.asarray(cloud, dtype=np.uint16); snow = np.asarray(snow); inside = np.asarray(inside, dtype=bool)
    if not all(x.shape == raw.shape for x in (mandatory, qa, snow, inside)):
        raise ValueError('VIIRS radiance/quality/AOI shapes differ')
    land = ((qa >> 1) & 7) <= 1
    accepted = (np.isfinite(raw) & (raw >= 0) & (mandatory == 0) & (qa != 65535) & ((qa & 1) == 0) & land &
                (((qa >> 4) & 3) == 3) & (((qa >> 6) & 3) == 0) & ((qa & (1 << 8)) == 0) & ((qa & (1 << 9)) == 0) &
                ((qa & (1 << 10)) == 0) & ((qa & (1 << 12)) == 0) & ((qa & (1 << 13)) == 0) & (snow == 0))
    result = base_summary(raw, accepted, inside, minimum, land)
    result.update(unit='nW cm^-2 sr^-1', nativeResolution='15 arc-second geographic grid (~500 m nominal)',
                  quality={'policy': 'V2 float radiance unchanged; mandatory0; night; high cloud-mask quality; confidently clear; land-only; no shadow/cirrus/snow/aurora/eclipse',
                           'landPixels': int(np.count_nonzero(inside & land)), 'nonnegativePixels': int(np.count_nonzero(inside & np.isfinite(raw) & (raw >= 0)))},
                  interpretation='Direct quality-valid, non-gap-filled daily VNP46A2v2 radiance; not an annual night-light average. Float V2 radiance is NOT multiplied by0.1.')
    return result


def summarize_minerals(raw, inside, names, quality_available=False, uncertainty_available=False):
    inside = np.asarray(inside, dtype=bool); total = int(inside.sum()); classes = []
    detected = np.zeros(inside.shape, dtype=bool)
    quality_valid = inside.copy()
    if quality_available:
        for key,value in raw.items():
            if key.startswith('mask_'):
                quality_valid &= np.asarray(value)==0
    for group in (1, 2):
        ids = np.asarray(raw[f'group_{group}_mineral_id']); depths = np.asarray(raw[f'group_{group}_band_depth'], dtype=np.float64)
        valid = quality_valid & (ids > 0) & (ids <= max(names)) & np.isfinite(depths) & (depths > 0)
        uncertainty = np.asarray(raw.get(f'group_{group}_band_depth_unc',np.full(ids.shape,np.nan)),dtype=np.float64)
        fit = np.asarray(raw.get(f'group_{group}_fit',np.full(ids.shape,np.nan)),dtype=np.float64)
        if uncertainty_available:
            valid &= np.isfinite(uncertainty) & (uncertainty>=0) & np.isfinite(fit) & (fit>=0)
        detected |= valid
        unique, counts = np.unique(ids[valid], return_counts=True)
        for mineral_id, count in zip(unique.tolist(), counts.tolist()):
            selected=valid & (ids==mineral_id)
            classes.append({'group': group, 'id': mineral_id, 'name': names.get(mineral_id, 'unmapped_library_record'), 'count': count, 'meanBandDepth':round(float(np.mean(depths[selected])),8), 'meanBandDepthUncertainty':round(float(np.mean(uncertainty[selected])),8) if uncertainty_available else None, 'meanFit':round(float(np.mean(fit[selected])),8) if uncertainty_available else None})
    return {'status': 'context_only', 'classes': sorted(classes, key=lambda x: (-x['count'], x['group'], x['id'])),
            'validPixels': int(detected.sum()), 'totalPixels': total,
            'quality': {'cloudMaskApplied': quality_available, 'uncertaintyApplied': uncertainty_available, 'qualityEligiblePixels':int(quality_valid.sum()), 'policy': 'Positive spectral-library ID/depth; matchedV002 cloud/cirrus/water/spacecraft/dilated/aggregate/SpecTfcloud flags0 when available; finite nonnegative uncertainty/fit when available. No arbitrary uncertainty detection threshold or cross-planet mineral match.'},
            'nativeResolution': '60 m nominal native EMIT swath with per-pixel location arrays',
            'interpretation': 'NASA spectral-library match IDs, not mineral abundance, confirmed field mineralogy, life evidence or a numerical Earth–Mars mineral match.'}


def clean_array(array):
    data = np.asarray(array)
    if np.issubdtype(data.dtype, np.floating):
        return [float(x) if np.isfinite(x) else None for x in data.ravel()]
    return data.ravel().tolist()


def evidence_record(kind, site, source, window, inside, raw, extra=None):
    result = {'schemaVersion': 1, 'kind': kind, 'siteId': site['id'], 'source': source, 'window': window,
              'shape': list(inside.shape), 'insideAOI': inside.ravel().tolist(),
              'raw': {name: clean_array(data) for name, data in raw.items()}}
    if extra:
        result.update(extra)
    return result


def modis_evidence(record, sites, extent):
    from pyhdf.SD import SD, SDC
    from pyproj import CRS, Transformer
    handle = SD(str(ROOT / record['rawPath']), SDC.READ)
    try:
        grid = parse_grid(handle.attributes()['StructMetadata.0'])
        if grid['projection'] != 'GCTP_SNSOID':
            raise ValueError('MOD13Q1 expected sinusoidal source grid')
        layers = {'ndvi': handle.select('250m 16 days NDVI'), 'vi_quality': handle.select('250m 16 days VI Quality'), 'reliability': handle.select('250m 16 days pixel reliability')}
        attributes = layers['ndvi'].attributes()
        if attributes.get('units') != 'NDVI' or float(attributes.get('scale_factor')) != 10000. or int(attributes.get('_FillValue')) != -3000:
            raise ValueError('Unexpected MOD13Q1 C6.1 scale/units/fill metadata')
        source_crs = CRS.from_proj4(f"+proj=sinu +R={grid['radiusM']} +units=m +no_defs")
        project = Transformer.from_crs('EPSG:4326', source_crs, always_xy=True)
        for site in sites:
            geographic = area(site, extent)['coordinates'][0]
            ring = [list(project.transform(lon, lat)) for lon, lat in geographic]
            selection = grid_window(grid, ring)
            if not selection:
                continue
            window, inside = selection
            if not inside.any():
                continue
            start = (window['row'], window['col']); count = (window['rows'], window['cols'])
            raw = {name: layer.get(start=start, count=count) for name, layer in layers.items()}
            yield evidence_record('ndvi', site, record, window, inside, raw, {'grid': grid, 'scaleRule': 'raw/10000'})
    finally:
        handle.end()


def ntl_evidence(record, sites, extent):
    import h5py
    with h5py.File(ROOT / record['rawPath'], 'r') as handle:
        group = handle['HDFEOS/GRIDS/VIIRS_Grid_DNB_2d/Data Fields']
        layer = group['DNB_BRDF-Corrected_NTL']
        if not np.issubdtype(layer.dtype, np.floating) or float(np.asarray(layer.attrs['scale_factor']).ravel()[0]) != 1.:
            raise ValueError('VNP46A2v2 radiance must be float with scale1')
        latitude = group['lat'][:]; longitude = group['lon'][:]
        if latitude.ndim != 1 or longitude.ndim != 1 or layer.shape != (len(latitude), len(longitude)):
            raise ValueError('Unexpected VIIRS coordinate vectors')
        for site in sites:
            ring = area(site, extent)['coordinates'][0]
            xmin, xmax = min(x for x,y in ring), max(x for x,y in ring); ymin, ymax = min(y for x,y in ring), max(y for x,y in ring)
            rows = np.flatnonzero((latitude >= ymin) & (latitude <= ymax)); cols = np.flatnonzero((longitude >= xmin) & (longitude <= xmax))
            if not len(rows) or not len(cols):
                continue
            r0,r1 = int(rows[0]),int(rows[-1])+1; c0,c1 = int(cols[0]),int(cols[-1])+1
            inside = polygon_mask(longitude[c0:c1][None,:], latitude[r0:r1][:,None], ring)
            if not inside.any():
                continue
            raw = {name: group[field][r0:r1,c0:c1] for name,field in [('radiance','DNB_BRDF-Corrected_NTL'),('mandatory','Mandatory_Quality_Flag'),('cloud','QF_Cloud_Mask'),('snow','Snow_Flag')]}
            yield evidence_record('night_lights',site,record,{'row':r0,'col':c0,'rows':r1-r0,'cols':c1-c0},inside,raw,
                                  {'coordinates':{'lat':latitude[r0:r1].tolist(),'lon':longitude[c0:c1].tolist()},'scaleRule':'physicalFloatUnchanged'})


def mineral_evidence(record, sites, extent):
    import netCDF4
    manifest=json.loads((ROOT/'data/protected-manifest.json').read_text(encoding='utf-8'))
    acquisition=re.search(r'\d{8}T\d{6}',record['granuleUr']).group()
    companions=[r for r in manifest['downloads'] if r.get('status')=='downloaded' and r['version']==record['version'] and acquisition in r.get('rawPath','') and ('MINUNCERT' in r.get('rawPath','') or r['shortName']=='EMITL2AMASK')]
    with ExitStack() as stack:
        handle=stack.enter_context(netCDF4.Dataset(ROOT/record['rawPath']));handle.set_auto_maskandscale(False)
        if str(handle.getncattr('product_version'))!='V002':raise ValueError('Expected EMIT mineralV002')
        latitude=handle['location/lat'][:];longitude=handle['location/lon'][:]
        names={int(k):str(v) for k,v in zip(handle['mineral_metadata/index'][:],handle['mineral_metadata/name'][:])}
        companion_handles=[]
        for companion in companions:
            if digest(ROOT/companion['rawPath'])!=companion['sha256']:raise ValueError('EMIT companion checksum mismatch')
            other=stack.enter_context(netCDF4.Dataset(ROOT/companion['rawPath']));other.set_auto_maskandscale(False)
            if str(other.getncattr('product_version'))!='V002' or str(other.getncattr('time_coverage_start'))[:19]!=str(handle.getncattr('time_coverage_start'))[:19]:raise ValueError('EMIT companion version/acquisition mismatch')
            if other['location/lat'].shape!=latitude.shape:raise ValueError('EMIT companion grid shape mismatch')
            companion_handles.append(other)
        for site in sites:
            ring=area(site,extent)['coordinates'][0]
            xmin,xmax=min(x for x,y in ring),max(x for x,y in ring);ymin,ymax=min(y for x,y in ring),max(y for x,y in ring)
            intersects=(longitude>=xmin)&(longitude<=xmax)&(latitude>=ymin)&(latitude<=ymax)
            rows,cols=np.where(intersects)
            if not len(rows):continue
            r0,r1,c0,c1=int(rows.min()),int(rows.max())+1,int(cols.min()),int(cols.max())+1
            inside=polygon_mask(longitude[r0:r1,c0:c1],latitude[r0:r1,c0:c1],ring)
            raw={name:handle[name][r0:r1,c0:c1] for name in ['group_1_mineral_id','group_2_mineral_id','group_1_band_depth','group_2_band_depth']}
            quality_available=False;uncertainty_available=False;alignment=[]
            for other in companion_handles:
                delta_lat=np.asarray(other['location/lat'][r0:r1,c0:c1])-latitude[r0:r1,c0:c1]
                delta_lon=np.asarray(other['location/lon'][r0:r1,c0:c1])-longitude[r0:r1,c0:c1]
                displacement=np.hypot(delta_lat*111195.,delta_lon*111195.*np.cos(np.radians(latitude[r0:r1,c0:c1])))
                if not np.all(np.isfinite(displacement)) or float(displacement.max())>30.:raise ValueError('EMIT companion geolocation shift exceeds half a nominal60m pixel')
                alignment.append({'file':other.filepath().split('\\')[-1],'method':'Same acquisition detector indices; geolocation shift bounded below half a nominal60m pixel','maximumShiftM':round(float(displacement.max()),6)})
                if 'mask' in other.variables:
                    bands=[str(x) for x in other['sensor_band_parameters/mask_bands'][:]]
                    for band in ['Cloud Flag','Cirrus Flag','Water Flag','Spacecraft Flag','Dilated Cloud Flag','Aggregate Flag','SpecTf-Cloud Flag']:
                        if band not in bands:raise ValueError('Required EMIT quality flag absent')
                        raw['mask_'+re.sub('[^a-z0-9]+','_',band.lower())]=other['mask'][r0:r1,c0:c1,bands.index(band)]
                    quality_available=True
                if 'group_1_band_depth_unc' in other.variables:
                    for group in [1,2]:
                        for suffix in ['band_depth_unc','fit']:
                            name=f'group_{group}_{suffix}';raw[name]=other[name][r0:r1,c0:c1]
                    uncertainty_available=True
            yield evidence_record('minerals',site,record,{'row':r0,'col':c0,'rows':r1-r0,'cols':c1-c0},inside,raw,{'mineralNames':names,'qualityAvailable':quality_available,'uncertaintyAvailable':uncertainty_available,'companionSources':companions,'companionAlignment':alignment,'coordinates':{'lat':clean_array(latitude[r0:r1,c0:c1]),'lon':clean_array(longitude[r0:r1,c0:c1])}})


def evidence_summary(evidence, minimum):
    shape = evidence['shape']; inside = np.array(evidence['insideAOI'],dtype=bool).reshape(shape)
    raw = {key:np.asarray(value).reshape(shape) for key,value in evidence['raw'].items()}
    if evidence['kind'] == 'ndvi':
        return summarize_ndvi(raw['ndvi'],raw['vi_quality'],raw['reliability'],inside,minimum)
    if evidence['kind'] == 'night_lights':
        return summarize_ntl(raw['radiance'],raw['mandatory'],raw['cloud'],raw['snow'],inside,minimum)
    if evidence['kind'] == 'minerals':
        result=summarize_minerals(raw,inside,{int(k):v for k,v in evidence['mineralNames'].items()},evidence.get('qualityAvailable',False),evidence.get('uncertaintyAvailable',False))
        result['quality']['companionAlignment']=evidence.get('companionAlignment',[])
        return result
    raise ValueError('Unknown evidence type')


def build(manifest_path, output_path, evidence_only=False, evidence_dir=None):
    config_path = ROOT / 'data/project.json'; config = json.loads(config_path.read_text(encoding='utf-8'))
    manifest = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    minimum = config.get('protectedData',{}).get('minimumValidFraction',config['experiment']['minimumValidFraction'])
    evidence_dir = Path(evidence_dir or ROOT/'data/protected-evidence')
    site_map = {site['id']:{'id':site['id'],'features':{},'mineral_summary':{'status':'missing','classes':[],'reason':'outside_downloaded_footprints_or_not_processed'}} for site in config['sites']}
    sources = []; evidence_index = []; errors = []
    if evidence_only:
        evidence_paths = []
        existing = json.loads(Path(output_path).read_text(encoding='utf-8'))
        if existing.get('processing',{}).get('configSha256')!=digest(config_path):raise ValueError('AOI configuration changed; regenerate evidence from raw files')
        for entry in existing.get('evidence',[]):
            path = ROOT / entry['path']
            if digest(path) != entry['sha256']:
                raise ValueError('AOI evidence checksum mismatch')
            evidence_paths.append(path)
        iterator = ((json.loads(path.read_text(encoding='utf-8')),path) for path in evidence_paths)
    else:
        def records():
            readers = {'MOD13Q1':modis_evidence,'VNP46A2':ntl_evidence,'EMITL2BMIN':mineral_evidence}
            for record in manifest.get('downloads',[]):
                if 'MINUNCERT' in record.get('rawPath',''):continue
                if record.get('status')!='downloaded' or record['shortName'] not in readers:
                    continue
                raw_path = ROOT / record['rawPath']
                if digest(raw_path) != record['sha256']:
                    raise ValueError('Downloaded raw file checksum mismatch')
                try:
                    for evidence in readers[record['shortName']](record,config['sites'],config['experiment']['aoiSizeM']):
                        filename = re.sub(r'[^A-Za-z0-9_.-]','_',f"{record['shortName']}-{record['granuleUr']}-{evidence['siteId']}.json")
                        path = evidence_dir / filename
                        dump(path,evidence)
                        yield evidence,path
                except Exception as exc:
                    errors.append({'product':record['shortName'],'granuleUr':record['granuleUr'],'reason':str(exc)})
        iterator = records()
    for evidence,path in iterator:
        site_id = evidence['siteId']
        if site_id not in site_map:
            continue
        record = evidence['source']; source_id = 'protected-'+evidence['kind']+'-'+site_id+'-'+record['sha256'][:12]
        summary = evidence_summary(evidence,minimum)
        summary.update(sourceId=source_id,measurementPeriod=record['acquisitionPeriod'],evidencePath=path.relative_to(ROOT).as_posix())
        if evidence['kind']=='minerals':
            site_map[site_id]['mineral_summary'] = summary
        else:
            key = 'ndvi_mean' if evidence['kind']=='ndvi' else 'night_lights'
            previous=site_map[site_id]['features'].get(key)
            if previous is None or (summary.get('value') is not None and (previous.get('value') is None or record['acquisitionPeriod']['start']>previous['measurementPeriod']['start'])) or (previous.get('value') is None and summary['validPixels']>previous['validPixels']):
                site_map[site_id]['features'][key] = summary
        evidence_hash=digest(path)
        sources.append({'id':source_id,'url':record['url'],'sha256':record['sha256'],'bytes':record['bytes'],'cachePath':record['rawPath'],
                        'kind':'protected-granule','evidencePath':path.relative_to(ROOT).as_posix(),'evidenceSha256':evidence_hash,
                        'product':record['shortName']+' '+record['granuleUr'],'version':record['version'],'measurementPeriod':record['acquisitionPeriod'],
                        'retrievedAt':record['retrievedAt'],'provider':'NASA Earthdata / official DAAC','status':'available'})
        evidence_index.append({'path':path.relative_to(ROOT).as_posix(),'sha256':evidence_hash,'sourceId':source_id,'siteId':site_id,'kind':evidence['kind']})
        if evidence.get('companionSources'):
            summary['sourceIds']=[source_id]
            for companion in evidence['companionSources']:
                companion_id='protected-companion-'+site_id+'-'+companion['sha256'][:12]
                summary['sourceIds'].append(companion_id)
                sources.append({'id':companion_id,'url':companion['url'],'sha256':companion['sha256'],'bytes':companion['bytes'],'cachePath':companion['rawPath'],'kind':'protected-granule','evidencePath':path.relative_to(ROOT).as_posix(),'evidenceSha256':evidence_hash,'product':companion['shortName']+' '+Path(companion['rawPath']).name,'version':companion['version'],'measurementPeriod':companion['acquisitionPeriod'],'retrievedAt':companion['retrievedAt'],'provider':'NASA Earthdata / official DAAC','status':'available'})

    for site in site_map.values():
        for key,unit in [('ndvi_mean','NDVI'),('night_lights','nW cm^-2 sr^-1')]:
            site['features'].setdefault(key,{'value':None,'unit':unit,'status':'missing','sourceId':None,'reason':'outside_downloaded_footprints_or_not_processed'})
    result={'schemaVersion':1,'generatedAt':dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),'sites':list(site_map.values()),'sources':sources,'evidence':evidence_index,'errors':errors,
            'processing':{'parserSha256':digest(Path(__file__)),'configSha256':digest(config_path),'minimumValidFraction':minimum,'evidenceOnly':evidence_only},
            'limitations':['Only downloaded footprints and actual acquisition periods are represented; not global product coverage or an annual composite.',
                           'NDVI is not a vegetation-area fraction. VIIRS V2 radiance uses its physical float scale, not the V1 0.1 multiplier.',
                           'EMIT mineral-library matches remain contextual even with matched masks/uncertainty; no validated field mineralogy or Earth–Mars matching score is computed.']}
    dump(output_path,result)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=ROOT/'data/protected-manifest.json')
    parser.add_argument('--output',type=Path,default=ROOT/'data/protected-features.json')
    parser.add_argument('--evidence-only',action='store_true')
    args=parser.parse_args(); result=build(args.manifest,args.output,args.evidence_only)
    print(json.dumps({'sites':len(result['sites']),'ndviAvailable':sum(s['features']['ndvi_mean']['value'] is not None for s in result['sites']),
                      'nightLightsAvailable':sum(s['features']['night_lights']['value'] is not None for s in result['sites']),
                      'mineralContexts':sum(s['mineral_summary']['status']=='context_only' for s in result['sites']),'evidence':len(result['evidence']),'errors':result['errors']}))

if __name__=='__main__':main()
