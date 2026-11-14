"""NASA GIS surface proxies. NDVI is an index, never a vegetation-area fraction.
HBASE is a historical 2010 classification, not a current settlement map.
"""
import json
import math
import statistics
from urllib.parse import urlencode

PACE = 'https://gis.earthdata.nasa.gov/portal/rest/services/GESDISC/PACE_OCI_L3M_LANDVI/ImageServer'
HBASE = 'https://gis.earthdata.nasa.gov/portal/rest/services/ulandsat/ulandsat_hbase_v1/ImageServer'

def sample_values(payload, count):
    """Reject duplicate/absent locations rather than silently accepting another raster."""
    found = {}
    for sample in payload.get('samples', []):
        index = sample.get('locationId')
        if not isinstance(index, int) or not 0 <= index < count:
            raise ValueError('Unexpected sample location index')
        if index in found:
            raise ValueError('Multiple rasters returned for a supposedly locked scene')
        try:
            value = float(sample.get('value'))
        except (TypeError, ValueError):
            value = None
        found[index] = value if value is not None and math.isfinite(value) else None
    return [found.get(i) for i in range(count)]

def ndvi_summary(values, minimum=.95):
    valid = [v for v in values if v is not None and -1 <= v <= 1]
    if not values or len(valid) / len(values) < minimum:
        raise ValueError('Insufficient valid NDVI samples; clouds/voids are not zero')
    return statistics.mean(valid), len(valid) / len(values)

def builtup_summary(values, minimum=.95):
    # Official NASA HBASE legend:200=NOT HBASE,201=HBASE,202=Road,255=NoData/cloud/shadow.
    valid = [v for v in values if v in (200, 201, 202)]
    if not values or len(valid) / len(values) < minimum:
        raise ValueError('Insufficient valid HBASE classes; unknown classes are missing')
    return sum(v in (201, 202) for v in valid) / len(valid), len(valid) / len(values)

def builtup_bounds(values):
    """Bounds over fixed sample nodes; missing nodes never become known non-urban nodes."""
    if not values:
        raise ValueError('No HBASE samples requested')
    valid = [v for v in values if v in (200, 201, 202)]
    built = sum(v in (201, 202) for v in valid)
    unknown = len(values) - len(valid)
    return {'lower': built / len(values), 'upper': (built + unknown) / len(values),
            'validFraction': len(valid) / len(values), 'builtUpNodes': built, 'unknownNodes': unknown,
            'requestedNodes': len(values)}

def query_samples(cache, source_id, endpoint, points, product, version, period, raster_id=None):
    params = {'f': 'json', 'geometry': json.dumps({'points': points, 'spatialReference': {'wkid': 4326}}, separators=(',', ':')),
              'geometryType': 'esriGeometryMultipoint', 'returnFirstValueOnly': 'true',
              'renderingRule': json.dumps({'rasterFunction': 'None'}, separators=(',', ':'))}
    if raster_id is not None:
        params['mosaicRule'] = json.dumps({'mosaicMethod': 'esriMosaicLockRaster', 'lockRasterIds': [raster_id], 'mosaicOperation': 'MT_FIRST'}, separators=(',', ':'))
    payload, record = cache.fetch(source_id, endpoint + '/getSamples?' + urlencode(params), product,
                                  version=version, measurement_period=period)
    if raster_id is not None and any(sample.get('rasterId') != raster_id for sample in payload.get('samples', [])):
        raise ValueError('NDVI service did not return the locked acquisition scene')
    return sample_values(payload, len(points)), record

def ndvi_scene(cache, config):
    """Resolve one explicitly dated8-day scene from NASA metadata; no default/latest mosaic."""
    where = "stdtime >= timestamp '2025-06-18 00:00:00' AND stdtime < timestamp '2025-06-26 00:00:00'"
    params = {'f': 'json', 'where': where, 'outFields': 'objectid,name,variable,stdtime', 'returnGeometry': 'false', 'resultRecordCount': 20}
    payload, record = cache.fetch('pace-scene-catalog', PACE + '/query?' + urlencode(params),
                                  'NASA PACE OCI NDVI scene catalogue', version='V3_1', measurement_period='2025-06-18 to 2025-06-25')
    rows = [f['attributes'] for f in payload.get('features', []) if f.get('attributes', {}).get('variable') == 'ndvi']
    if len(rows) != 1:
        raise ValueError('Expected exactly one named June2025 NDVI scene')
    row = rows[0]
    if '20250618_20250625' not in row['name']:
        raise ValueError('Unexpected PACE scene acquisition interval')
    return {**row, 'sourceId': record['id'], 'period': '2025-06-18 to 2025-06-25'}

def screening(features, settings):
    reasons = []
    built = features.get('built_up_sample_fraction_lower_bound', {}).get('value')
    ndvi = features.get('ndvi_mean', features.get('ndvi', {})).get('value')
    if built is not None and built >= settings['maximumBuiltUpSampleFraction']:
        reasons.append('Confirmed lower bound of historical2010 built-up/road sample fraction reaches the experimental screening threshold')
    if ndvi is not None and ndvi > settings['maximumNdvi']:
        reasons.append('June2025 NDVI snapshot exceeds the experimental bare-ground screening threshold')
    return {'status': 'rejected' if reasons else 'not_rejected', 'reasons': reasons,
            'complete': built is not None and ndvi is not None,
            'interpretation': 'Experimental surface screen only; historical settlement and one NDVI snapshot cannot establish current land use, year-round vegetation, protected status or safe access.'}
