"""Targeted ASTER GDEM V3/NUM sampler. Reads verified local NASA GeoTIFFs only.
Run with the analysis virtualenv: .venv\\Scripts\\python -m analysis.dem_v3
"""
from __future__ import annotations
import argparse
import collections
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sha256_file(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()

def num_class(value):
    """Categorical provenance; NUM is not a monotonically increasing quality score."""
    if value is None or not isinstance(value,(int,float)) or not math.isfinite(value) or int(value)!=value:
        return {'source':'unknown','count':None,'usable':False}
    value=int(value)
    if 0<=value<=50:return {'source':'ASTER_GDEM_V3','count':value if value else None,'usable':True}
    if 60<=value<=110:return {'source':'ASTER_GDEM_V2','count':value-60 if value>60 else None,'usable':True}
    if 131<=value<=184:return {'source':'PRISM','count':value-130,'usable':True}
    if 201<=value<=223:return {'source':'SRTM','count':value-200,'usable':True}
    sources={231:'SRTM_V3_INITIAL_V3_FILL',232:'SRTM_V2_INITIAL_V3_FILL',233:'SRTM_V2_V2_FILL',234:'SRTM_NGA_V2_FILL',241:'NED_V2_FILL',242:'NED_INITIAL_V3_FILL',243:'CDED_V2_FILL',244:'CDED_INITIAL_V3_FILL',245:'ALASKA_V2_FILL',246:'ALASKA_INITIAL_V3_FILL'}
    if value in sources:return {'source':sources[value],'count':None,'usable':True}
    if value==250:return {'source':'INTERPOLATION','count':None,'usable':False}
    return {'source':'unknown','count':None,'usable':False}

def verified_path(record,root=ROOT):
    directory=(root/'.local/earthdata-data').resolve()
    path=(root/record['rawPath']).resolve()
    if not path.is_relative_to(directory):raise ValueError('ASTER raw path escapes local science directory')
    if not path.is_file():raise ValueError('ASTER science file missing')
    if path.stat().st_size!=record['bytes'] or sha256_file(path)!=record['sha256']:
        raise ValueError('ASTER science file checksum/size mismatch')
    return path

def bilinear(dataset,x,y):
    """Affine coordinates describe pixel corners; interpolate around pixel centres."""
    from rasterio.windows import Window
    col,row=(~dataset.transform) @ (x,y)
    col-=.5;row-=.5
    c0=math.floor(col);r0=math.floor(row)
    fx=col-c0;fy=row-r0
    total=0.
    for dr,dc,weight in [(0,0,(1-fx)*(1-fy)),(0,1,fx*(1-fy)),(1,0,(1-fx)*fy),(1,1,fx*fy)]:
        if weight<1e-12:continue
        r=r0+dr;c=c0+dc
        if not(0<=r<dataset.height and 0<=c<dataset.width):return None
        cell=dataset.read(1,window=Window(c,r,1,1),masked=True)
        if bool(cell.mask.any()):return None
        value=float(cell[0,0])
        if not math.isfinite(value) or value==-9999 or not -20000<value<30000:return None
        total+=weight*value
    return total

def sample_pair(dem_path,num_path,points,minimum=.95):
    import rasterio
    from rasterio.windows import Window
    elevations=[];codes=[];source_counts=collections.Counter();rejections=collections.Counter();stack_counts=[]
    with rasterio.open(dem_path) as dem,rasterio.open(num_path) as num:
        if dem.crs is None or dem.crs.to_epsg()!=4326:raise ValueError('ASTER tile is not geographic WGS84')
        if dem.crs!=num.crs or dem.transform!=num.transform or dem.shape!=num.shape:raise ValueError('ASTER DEM/NUM grids do not match')
        if dem.count!=1 or num.count!=1:raise ValueError('ASTER DEM/NUM must each have one raster band')
        for lon,lat in points:
            row,col=num.index(lon,lat)
            if not(0<=row<num.height and 0<=col<num.width):
                elevations.append(None);codes.append(None);rejections['outside_tile']+=1;continue
            cell=num.read(1,window=Window(col,row,1,1),masked=False)
            code=int(cell[0,0])
            codes.append(code);category=num_class(code);source_counts[category['source']]+=1
            if category['count'] is not None:stack_counts.append(category['count'])
            if not category['usable']:
                elevations.append(None);rejections['interpolated_or_unknown_num']+=1;continue
            value=bilinear(dem,lon,lat)
            if value is None:rejections['void_or_incomplete_bilinear_support']+=1
            elevations.append(round(value,6) if value is not None else None)
        metadata={'crs':dem.crs.to_string(),'demShape':list(dem.shape),'transform':list(dem.transform)[:6],
                  'bounds':list(dem.bounds),'demNoData':dem.nodata,'numNoData':num.nodata,
                  'verticalReference':'EGM96 geoid','nativePostingArcSeconds':1}
    valid=sum(value is not None for value in elevations)/len(points) if points else 0
    quality={'validFraction':valid,'minimumValidFraction':minimum,'eligibleForOverride':valid>=minimum,
             'numCodes':codes,'numSourceCounts':dict(source_counts),'rejectionCounts':dict(rejections),
             'knownStackCountMin':min(stack_counts) if stack_counts else None,
             'knownStackCountMax':max(stack_counts) if stack_counts else None,
             'policy':'Nearest categorical NUM; interpolation250 and unknown codes withheld. Other source types retained as exploratory measurements; count0 means unspecified, not void. DEM bilinear samples reject any positively weighted void neighbour.',
             'warning':'500m sampling does not equalize DEM effective resolution, error, or vertical datums across planetary sources.',**metadata}
    return elevations,quality

def pairs_from_manifest(manifest):
    rows=[r for r in manifest.get('downloads',[]) if r.get('status')=='downloaded' and str(r.get('version')) in ('003','3')]
    by_url={r['url']:r for r in rows}
    return [(record,by_url[record['url'].replace('_dem.tif','_num.tif')]) for record in rows
            if record.get('shortName') in ('ASTGTM','ASTGTM_DEM','ASTGTM003') and record['url'].endswith('_dem.tif') and record['url'].replace('_dem.tif','_num.tif') in by_url]

def public_source(record):
    return {'id':record['id'],'provider':'NASA/METI; NASA LP DAAC official distribution','product':'ASTER GDEM V3 '+('NUM provenance' if record['url'].endswith('_num.tif') else 'elevation'),
            'version':'003','url':record['url'],'rawPath':record['rawPath'],'bytes':record['bytes'],'sha256':record['sha256'],
            'retrievedAt':record.get('retrievedAt'),'measurementPeriod':record.get('acquisitionPeriod'),
            'status':'available','distribution':record.get('distribution')}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',default='data/protected-manifest.json')
    parser.add_argument('--output',default='data/dem-v3-features.json')
    args=parser.parse_args(argv)
    manifest_path=ROOT/args.manifest
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    config=json.loads((ROOT/'data/project.json').read_text(encoding='utf-8'))
    from .run import sample_points
    pairs=pairs_from_manifest(manifest)
    if not pairs:raise RuntimeError('No complete verified ASTER V3 DEM+NUM pair in manifest')
    grids=[];sources={}
    for dem_record,num_record in pairs:
        dem_path=verified_path(dem_record);num_path=verified_path(num_record)
        import rasterio
        with rasterio.open(dem_path) as dataset:bounds=dataset.bounds
        for site in config['sites']:
            if site.get('body')!='earth' or not(bounds.left<=site['lon']<=bounds.right and bounds.bottom<=site['lat']<=bounds.top):continue
            size=config['experiment']['gridSize'];spacing=config['experiment']['spacingM']
            points=sample_points(site,size,spacing)
            elevations,quality=sample_pair(dem_path,num_path,points,config['experiment']['minimumValidFraction'])
            grids.append({'id':site['id'],'status':'available' if quality['eligibleForOverride'] else 'insufficient',
                          'terrainGrid':{'size':size,'spacingM':spacing,'coordinates':points,'elevations':elevations,
                                         'sourceId':dem_record['id'],'sourceIds':[dem_record['id'],num_record['id']],'quality':quality}})
            for record in (dem_record,num_record):sources[record['id']]=public_source(record)
    output={'schemaVersion':1,'generatedAt':dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),'status':'available' if any(s['status']=='available' for s in grids) else 'insufficient',
            'sites':grids,'sources':list(sources.values()),'processing':{'configSha256':sha256_file(ROOT/'data/project.json'),'manifestSha256':sha256_file(manifest_path),'codeSha256':sha256_file(Path(__file__)),'algorithm':'ASTERv3-bilinear-pixel-centres-num-nearest-v1'}}
    destination=ROOT/args.output;temporary=destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(output,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8');temporary.replace(destination)
    print(json.dumps({'output':args.output,'sites':len(grids),'available':sum(s['status']=='available' for s in grids),'sources':len(sources)}))
    return 0

if __name__=='__main__':raise SystemExit(main())
