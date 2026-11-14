"""TerraTwin NASA-only pilot. Run python -m analysis.run [--offline] [--refresh].
No credentials, third-party terrain or synthetic measurements are used.
"""
from __future__ import annotations
import argparse, calendar, concurrent.futures, datetime as dt, hashlib, json, math, statistics, struct, threading, time
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from . import surface
from .protected_integration import load_bundle, merge_site, environmental_proxies, source_records

ROOT = Path(__file__).resolve().parents[1]
L = lambda tr,en: {"tr":tr,"en":en}
FEATURES = {
 'temperature_mean_c':('°C',L('Ortalama 2 m hava sıcaklığı','Mean 2 m air temperature')),
 'precipitation_annual_mm':('mm/year',L('Yıllık düzeltilmiş yağış','Annual corrected precipitation')),
 'temperature_range_c':('°C',L('Ortalama günlük hava sıcaklığı aralığı','Mean daily air-temperature range')),
 'frost_days':('days',L('Minimum hava sıcaklığı 0 °C altındaki günler','Days with minimum air temperature below 0 °C')),
 'slope_p50_deg':('°',L('500 m örnekleme: medyan eğim','500 m sampling: median slope')),
 'relief_m':('m',L('10 km alanda %95–%5 yükseklik farkı','95th–5th percentile elevation range in 10 km area')),
 'roughness_m':('m',L('Yerel komşuluk yükseklik kalıntısı RMS','RMS local-neighbourhood elevation residual')),
 'landable_fraction':('fraction',L('Örnek düğümlerinde eğim <5° oranı','Fraction of sample nodes with slope <5°')),
 'vegetation_fraction':('fraction',L('Bitki örtüsü alan oranı (NDVI değildir)','Vegetation area fraction (not NDVI)')),
 'ndvi_mean':('index',L('Kaliteli kara piksellerinde MODIS NDVI','MODIS NDVI over quality-screened land pixels')),
 'built_up_sample_fraction_lower_bound':('fraction',L('2010 yapılaşma/yol örnekleri: doğrulanmış alt sınır','2010 built-up/road samples: confirmed lower bound')),
 'built_up_sample_fraction_upper_bound':('fraction',L('2010 yapılaşma/yol örnekleri: olası üst sınır','2010 built-up/road samples: possible upper bound')),
 'mineral_match':('index',L('Mineral eşleşmesi','Mineral match')),
 'ice_evidence':('index',L('Buz kanıtı','Ice evidence')),
 'night_lights':('radiance',L('Gece ışıkları','Night lights')),
 'polar_day_hours':('hours',L('Geometrik yaz gündönümü gün uzunluğu','Geometric summer-solstice day length')),
}
def now(): return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
def dump(path, obj):
 path.parent.mkdir(parents=True,exist_ok=True)
 temporary=path.with_suffix(path.suffix+'.tmp')
 temporary.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
 temporary.replace(path)
def finite(value): return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)
def valid(value, fill=-999): return finite(value) and value != fill

def trusted_url(url):
 host=(urlparse(url).hostname or '').lower()
 return host=='nasa.gov' or host.endswith('.nasa.gov')

class CacheIntegrityError(RuntimeError): pass

class Cache:
 def __init__(self, offline=False, refresh=False):
  self.offline,self.refresh=offline,refresh; self.sources={}; self.lock=threading.Lock()
 def fetch(self, source_id, url, product, *, post=None, binary=False, version=None, measurement_period=None):
  if not trusted_url(url): raise ValueError('Only official nasa.gov distribution hosts are allowed')
  body=urlencode(post).encode() if post else None
  key=hashlib.sha256(url.encode()+b'\n'+(body or b'')).hexdigest()[:24]
  path=ROOT/'data/cache'/(key+('.bin' if binary else '.json')); meta_path=ROOT/'data/cache'/(key+'.meta.json')
  data=None; meta=None
  if path.exists() and meta_path.exists() and not self.refresh:
   data=path.read_bytes(); meta=json.loads(meta_path.read_text(encoding='utf-8'))
   if hashlib.sha256(data).hexdigest()!=meta['sha256']: raise CacheIntegrityError('Cache checksum mismatch: '+str(path))
  elif self.offline:
   raise CacheIntegrityError('Offline cache missing: '+source_id)
  else:
   error=None
   for attempt in range(3):
    try:
     req=Request(url,data=body,headers={'User-Agent':'TerraTwin NASA research pilot/1.0','Accept':'*/*'})
     with urlopen(req,timeout=60) as response:
      if not trusted_url(response.geturl()): raise ValueError('Refusing redirect outside NASA')
      data=response.read()
      content_type=response.headers.get('Content-Type','')
     if not binary:
      parsed=json.loads(data)
      if 'error' in parsed or 'messages' in parsed and not parsed.get('properties'):
       raise ValueError('NASA API returned error: '+str(parsed)[:300])
     elif content_type.startswith('text/') or b'ServiceException' in data[:1000]:
      raise ValueError('WMS did not return binary elevation data')
     meta={'id':source_id,'url':url,'method':'POST' if body else 'GET','requestBody':body.decode() if body else None,
      'provider':'NASA','product':product,'version':version,'measurementPeriod':measurement_period,
      'retrievedAt':now(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
      'cachePath':path.relative_to(ROOT).as_posix(),'status':'available','contentType':content_type}
     path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data); dump(meta_path,meta)
     break
    except Exception as exc:
     error=exc
     if attempt<2:time.sleep(1+attempt)
   else: raise RuntimeError(str(error))
  record={**meta,'id':source_id}
  with self.lock:self.sources[source_id]=record
  return data if binary else json.loads(data),record

RADII={'earth':6371008.8,'moon':1737400.,'mars':3396190.}
def destination(lat,lon,x,y,body='earth'):
 distance=math.hypot(x,y)/RADII[body]
 if not distance:return [lon,lat]
 bearing=math.atan2(x,y); phi=math.radians(lat); lam=math.radians(lon)
 phi2=math.asin(math.sin(phi)*math.cos(distance)+math.cos(phi)*math.sin(distance)*math.cos(bearing))
 lam2=lam+math.atan2(math.sin(bearing)*math.sin(distance)*math.cos(phi),math.cos(distance)-math.sin(phi)*math.sin(phi2))
 return [((math.degrees(lam2)+180)%360)-180,math.degrees(phi2)]
def area(site,extent):
 h=extent/2; ring=[destination(site['lat'],site['lon'],x,y,site.get('body','earth')) for x,y in [(-h,-h),(h,-h),(h,h),(-h,h),(-h,-h)]]
 return {'type':'Polygon','coordinates':[ring]}
def sample_points(site,size,spacing):
 h=(size-1)/2
 return [destination(site['lat'],site['lon'],(c-h)*spacing,(h-r)*spacing,site.get('body','earth')) for r in range(size) for c in range(size)]
def pct(values,quantile):
 seq=sorted(values); position=(len(seq)-1)*quantile; i=int(position); frac=position-i
 return seq[i]*(1-frac)+seq[min(i+1,len(seq)-1)]*frac

def terrain_features(elevations,size,spacing,min_fraction=.95):
 if len(elevations)!=size*size:raise ValueError('Elevation sample count does not match grid')
 values=[v for v in elevations if finite(v) and -20000<v<30000]
 if len(values)/len(elevations)<min_fraction:raise ValueError('Insufficient valid elevation coverage')
 slopes=[]; residuals=[]; slope_grid=[None]*len(elevations)
 for r in range(1,size-1):
  for c in range(1,size-1):
   k=r*size+c; neighbourhood=[elevations[(r+dy)*size+c+dx] for dy in [-1,0,1] for dx in [-1,0,1]]
   if not all(finite(v) and -20000<v<30000 for v in neighbourhood):continue
   gx=(elevations[k+1]-elevations[k-1])/(2*spacing);gy=(elevations[k-size]-elevations[k+size])/(2*spacing)
   slope=math.degrees(math.atan(math.hypot(gx,gy)));slopes.append(slope);slope_grid[k]=slope
   residuals.append(elevations[k]-statistics.mean(neighbourhood))
 if len(slopes)<(size-2)**2*min_fraction:raise ValueError('Insufficient valid gradient neighbourhoods')
 return {'slope_p50_deg':statistics.median(slopes),'relief_m':pct(values,.95)-pct(values,.05),
  'roughness_m':math.sqrt(statistics.mean(v*v for v in residuals)),
  'landable_fraction':sum(s<5 for s in slopes)/len(slopes)},slope_grid,len(values)/len(elevations)

def read_earth_dem(cache,site,experiment):
 n=experiment['gridSize'];spacing=experiment['spacingM']; lat=site['lat'];lon=site['lon']
 if abs(lat)>82.8:raise ValueError('ASTER v2 NASA WorldWind cache excludes this latitude')
 dy=math.degrees(spacing/RADII['earth']);dx=dy/math.cos(math.radians(lat));h=n/2
 bounds=[lon-h*dx,lat-h*dy,lon+h*dx,lat+h*dy]
 q={'service':'WMS','version':'1.1.1','request':'GetMap','layers':'aster_v2','styles':'','srs':'EPSG:4326',
  'bbox':','.join(f'{v:.9f}' for v in bounds),'width':n,'height':n,'format':'application/bil16'}
 url='https://worldwind26.arc.nasa.gov/elev?'+urlencode(q)
 data,meta=cache.fetch('dem-'+site['id'],url,'NASA WorldWind ASTER GDEM v2 elevation cache',binary=True,version='ASTER GDEM v2; WorldWind cache layer aster_v2',measurement_period='Historical ASTER GDEM v2 observations; not 2025 terrain measurements')
 if len(data)!=n*n*2:raise ValueError('BIL16 response length mismatch')
 elevations=[None if v in (-32768,-32767,-9999) else v for v in struct.unpack('<'+str(n*n)+'h',data)]
 # WMS1.1.1 pixel centres correspond to a latitude/longitude grid, top row north.
 points=[[lon+(c-(n-1)/2)*dx,lat+((n-1)/2-r)*dy] for r in range(n) for c in range(n)]
 return elevations,points,meta

def read_planet_dem(cache,site,experiment,provider):
 n=experiment['gridSize'];points=sample_points(site,n,experiment['spacingM'])
 metadata,_=cache.fetch('service-'+site['body'],provider+'?f=json','NASA Trek elevation service metadata',version='Live service metadata')
 sr=metadata['spatialReference'];sr={'wkid':sr['wkid']} if sr.get('wkid') else {'wkt':sr['wkt']}
 # Query batches keep POST bodies bounded; locationId indexes each input batch.
 elevations=[];records=[]
 for batchno,start in enumerate(range(0,len(points),40)):
  batch=points[start:start+40]
  geometry={'points':batch,'spatialReference':sr}
  query={'f':'json','geometry':json.dumps(geometry,separators=(',',':')),'geometryType':'esriGeometryMultipoint','returnFirstValueOnly':'true','interpolation':'RSP_BilinearInterpolation'}
  response,meta=cache.fetch('dem-'+site['id']+'-'+str(batchno),provider+'/getSamples?'+urlencode(query),'NASA Trek '+('LRO LOLA global DEM' if site['body']=='moon' else 'MGS MOLA merged DEM'),
   version=provider.split('/')[-2],measurement_period='Historical mission-derived DEM; service retrieval date is not observation date')
  found={s['locationId']:s for s in response.get('samples',[])}
  for i in range(len(batch)):
   val=found.get(i,{}).get('value')
   try:val=float(val)
   except (ValueError,TypeError):val=None
   elevations.append(val if finite(val) and -20000<val<30000 else None)
  records.append(meta)
 return elevations,points,records

def missing_features():
 return {k:{'value':None,'unit':v[0],'name':v[1],'status':'missing','sourceId':None} for k,v in FEATURES.items()}
def measured(features,key,value,source_id,**extra):
 features[key].update(value=round(value,6),status='derived',sourceId=source_id,**extra)

def climate_features(payload,minimum=.95):
 header=payload.get('header',{}); params=payload.get('properties',{}).get('parameter',{})
 fill=header.get('fill_value',-999);start=dt.datetime.strptime(header['start'],'%Y%m%d').date();end=dt.datetime.strptime(header['end'],'%Y%m%d').date()
 expected=(end-start).days+1;dates=[(start+dt.timedelta(days=i)).strftime('%Y%m%d') for i in range(expected)]
 series={}
 for key in ['T2M','T2M_MAX','T2M_MIN','PRECTOTCORR']:
  vals=params.get(key,{})
  if any(day not in vals for day in dates):raise ValueError('Incomplete calendar in '+key)
  good=[vals[day] for day in dates if valid(vals[day],fill)]
  if len(good)/expected<minimum:raise ValueError('Insufficient valid daily observations in '+key)
  series[key]=good
 precip=series['PRECTOTCORR']
 if any(v<0 for v in precip):raise ValueError('Negative precipitation rejected')
 if len(precip)!=expected:raise ValueError('Annual precipitation requires every daily observation; no silent extrapolation')
 ranges=[params['T2M_MAX'][d]-params['T2M_MIN'][d] for d in dates if valid(params['T2M_MAX'][d],fill) and valid(params['T2M_MIN'][d],fill)]
 if any(v<0 for v in ranges):raise ValueError('Inverted daily temperatures rejected')
 return {'temperature_mean_c':statistics.mean(series['T2M']),'precipitation_annual_mm':sum(precip),
  'temperature_range_c':statistics.mean(ranges),'frost_days':sum(v<0 for v in series['T2M_MIN'])},expected

def fetch_climate(cache,site,exp):
 period=exp['period'];q={'parameters':'T2M,T2M_MAX,T2M_MIN,PRECTOTCORR','community':'AG','longitude':site['lon'],'latitude':site['lat'],
 'start':period['start'].replace('-',''),'end':period['end'].replace('-',''),'format':'JSON','time-standard':'UTC'}
 data,meta=cache.fetch('power-'+site['id'],'https://power.larc.nasa.gov/api/temporal/daily/point?'+urlencode(q),'NASA POWER daily meteorological data',measurement_period=period)
 if data['parameters']['T2M']['units']!='C' or data['parameters']['PRECTOTCORR']['units']!='mm/day':raise ValueError('Unexpected NASA POWER units')
 values,count=climate_features(data,exp['minimumValidFraction'])
 meta['version']=data['header'].get('api',{}).get('version');meta['upstreamSources']=data['header'].get('sources');meta['expectedDays']=count
 cache.sources[meta['id']]=meta
 return values,meta

def gaussian(x,target,sigma):
 if not all(finite(v) for v in [x,target,sigma]) or sigma<=0:return None
 return math.exp(-((x-target)**2)/(2*sigma*sigma))
def aggregate(components,minimum=.6):
 total=sum(c['weight'] for c in components)
 if total<=0:raise ValueError('Positive total weight required')
 if any(c['weight']<0 for c in components):raise ValueError('Negative weights are invalid')
 available=[c for c in components if c.get('value') is not None and finite(c['value'])]
 if any(not 0<=c['value']<=1 for c in available):raise ValueError('Criterion scores must be in [0,1]')
 covered=sum(c['weight'] for c in available);coverage=covered/total
 score=100*sum(c['weight']*c['value'] for c in available)/covered if covered and coverage+1e-9>=minimum else None
 return {'score':round(score,3) if score is not None else None,'coverage':round(coverage,6),
 'status':('complete' if coverage>=1-1e-9 else 'partial') if score is not None else 'insufficient'}
def sensitivity(components,minimum,fraction=.2):
 scores=[]
 for index in range(len(components)):
  for direction in [-1,1]:
   varied=[dict(c) for c in components];varied[index]['weight']*=1+direction*fraction
   result=aggregate(varied,minimum)
   if result['score'] is not None:scores.append(result['score'])
 return {'min':min(scores) if scores else None,'max':max(scores) if scores else None,'weightPerturbation':fraction,
 'method':'One weight at a time ±20%, all weights renormalized; data uncertainty not represented'}

def target_comparison(site,target,config):
 features=site['features'];target_features=target['features'];components=[]
 for key,sigma in config['scoring']['sigma'].items():
  value=gaussian(features[key]['value'],target_features[key]['value'],sigma)
  components.append({'id':key,'name':FEATURES[key][1],'weight':1/3,'value':value,
   'contribution':round(value/3,6) if value is not None else None,'status':'available' if value is not None else 'missing',
   'sourceId':features[key]['sourceId'],'targetSourceId':target_features[key]['sourceId'],'sigma':sigma,'rawValue':features[key]['value'],'targetValue':target_features[key]['value'],'unit':FEATURES[key][0]})
 result=aggregate(components,1.)
 return {**result,'targetId':target['id'],'components':components,'sensitivity':sensitivity(components,1.),
 'interpretation':'Experimental terrain-only similarity at 500 m sampling; no mineral, vegetation, ice, safety or access screening'}

def daylight(lat):
 val=-math.tan(math.radians(abs(lat)))*math.tan(math.radians(23.44))
 return 24. if val<=-1 else 0. if val>=1 else 24*math.acos(val)/math.pi

def full_profile(site,target,profile,config):
 f=site['features'];get=lambda key:f[key]['value'];terrain=target_comparison(site,target,config)
 tc={c['id']:c['value'] for c in terrain['components']}
 bare,isolation=environmental_proxies(f,config['scoring']['proxyScales'])
 cold=max(0,min(1,(10-get('temperature_mean_c'))/40)) if get('temperature_mean_c') is not None else None
 dry=math.exp(-get('precipitation_annual_mm')/250) if get('precipitation_annual_mm') is not None else None
 # Directional cold/aridity/daylight are declared experimental operational proxies, NOT planetary climate equivalence.
 if profile=='base':
  vals=[(get('polar_day_hours')/24 if get('polar_day_hours') is not None else None),cold,None,tc['relief_m'],tc['slope_p50_deg'],bare,isolation]
  source_ids=['earth-geometry',f['temperature_mean_c']['sourceId'],None,f['relief_m']['sourceId'],f['slope_p50_deg']['sourceId'],f['ndvi_mean']['sourceId'],f['night_lights']['sourceId']]
 else:
  vals=[dry,None,(terrain['score']/100 if terrain['score'] is not None else None),None,bare,cold,None]
  source_ids=[f['precipitation_annual_mm']['sourceId'],None,f['relief_m']['sourceId'],None,f['ndvi_mean']['sourceId'],f['temperature_mean_c']['sourceId'],None]
 definition=config['profiles'][profile];missions=[]
 ids={'base':['base_operations','prospecting','rover','power','geology'],'mars':['life_detection','rover','crewed_base','geology']}[profile]
 for i,mission in enumerate(definition['missions']):
  components=[{'id':c['code'],'name':c['name'],'weight':mission['w'][j],'value':vals[j],
   'contribution':round(mission['w'][j]*vals[j],6) if vals[j] is not None else None,'status':'available' if vals[j] is not None else 'missing','sourceId':source_ids[j]}
   for j,c in enumerate(definition['criteria'])]
  result=aggregate(components,config['experiment']['minimumCoverage'])
  if not site.get('eligible',True) or site.get('surfaceScreening',{}).get('status')=='rejected':result.update(score=None,status='excluded')
  missions.append({'id':ids[i],'name':mission['name'],**result,'components':components,'sensitivity':sensitivity(components,config['experiment']['minimumCoverage'])})
 return {'targetId':target['id'],'missions':missions,'interpretation':'Experimental mixed operational screening; partial scores are not total Moon/Mars equivalence'}

def process_site(cache,site,config,target=False):
 exp=config['experiment'];out={**site,'aoi':area(site,exp['aoiSizeM']),'features':missing_features(),'missing':[],'status':'partial'}
 if site['body']=='earth':
  try:
   values,meta=fetch_climate(cache,site,exp)
   for key,value in values.items():measured(out['features'],key,value,meta['id'],measurementPeriod=exp['period'],resolution='Regional MERRA-2/POWER grid; not AOI-average microclimate')
  except CacheIntegrityError:raise
  except Exception as exc:out['missing'].append({'provider':'NASA POWER','reason':str(exc)})
  measured(out['features'],'polar_day_hours',daylight(site['lat']),'earth-geometry',description='Geometric Earth summer-solstice day length at latitude; ignores terrain horizon/refraction and is not lunar illumination')
 try:
  if site['body']=='earth':elevations,points,meta=read_earth_dem(cache,site,exp);source_id=meta['id'];source_ids=[source_id]
  else:
   elevations,points,records=read_planet_dem(cache,site,exp,config['providers'][site['body']+'Dem']);source_id=records[0]['id'];source_ids=[m['id'] for m in records]
  values,slopes,valid_fraction=terrain_features(elevations,exp['gridSize'],exp['spacingM'],exp['minimumValidFraction'])
  for key,value in values.items():measured(out['features'],key,value,source_id,spacingM=exp['spacingM'],validFraction=valid_fraction,sourceIds=source_ids)
  out['grid']={'size':exp['gridSize'],'spacingM':exp['spacingM'],'coordinates':points,'elevations':elevations,'slopes':slopes,'sourceId':source_id,'sourceIds':source_ids}
 except CacheIntegrityError:raise
 except Exception as exc:out['missing'].append({'provider':'NASA DEM','reason':str(exc)})
 if site['body']=='earth':
  try:
   points=sample_points(site,5,2500)
   values,meta=surface.query_samples(cache,'hbase-'+site['id'],surface.HBASE,points,
    'NASA HBASE global built-up and settlement extent','HBASE v1; GLS2010 Landsat','2010 target year; not current land-use mapping')
   bounds=surface.builtup_bounds(values)
   out['surfaceSamples']={'coordinates':points,'hbaseClasses':values,'bounds':bounds,'sourceId':meta['id']}
   if bounds['validFraction']>0:
    measured(out['features'],'built_up_sample_fraction_lower_bound',bounds['lower'],meta['id'],validFraction=bounds['validFraction'],unknownNodes=bounds['unknownNodes'],interpretation='Lower bound over25 fixed sample nodes; NOT a measured area fraction. Unknown nodes are not known non-urban nodes.')
    measured(out['features'],'built_up_sample_fraction_upper_bound',bounds['upper'],meta['id'],validFraction=bounds['validFraction'],unknownNodes=bounds['unknownNodes'],interpretation='Upper bound over25 fixed sample nodes; unknown nodes remain possible built-up nodes.')
  except CacheIntegrityError:raise
  except Exception as exc:out['missing'].append({'provider':'NASA HBASE','reason':str(exc)})
  out['surfaceScreening']=surface.screening(out['features'],config['surfaceScreening'])
  out['surfaceScreening']['thresholds']=config['surfaceScreening']
  out['surfaceScreening']['description']=L('2010 yapılaşma/yol örnekleri seçili eşiğe göre incelendi. Eksik örnekler alt ve üst sınır arasında bırakılır. NDVI doğrulanamadığından bitki örtüsü elemesi tamamlanmadı.','2010 built-up/road samples screened with configured thresholds. Unknown samples remain between lower and upper bounds. Vegetation screening remains incomplete because dated NDVI could not be verified.')
 t=out['features']['temperature_mean_c']['value'];p=out['features']['precipitation_annual_mm']['value']
 out['environmentalScreen']={'aridity':round(100*math.exp(-p/250),3) if p is not None else None,'cold':round(100*max(0,min(1,(10-t)/40)),3) if t is not None else None,
 'interpretation':'Earth-only directional indices with analyst-selected scales: aridity=100 exp(-annual_mm/250), cold=100 clamp((10-temperature_C)/40). Not planetary similarity.'}
 return out

def validate(sites,targets):
 checks=[]
 for target in targets:
  scored=[s for s in sites if s.get('eligible',True) and s['terrainPilot']['targets'][target['id']]['score'] is not None]
  refs=[s['terrainPilot']['targets'][target['id']]['score'] for s in scored if s['role']=='reference']
  controls=[s['terrainPilot']['targets'][target['id']]['score'] for s in scored if s['role']=='negative_control']
  status='inconclusive';message='Insufficient reference/control coverage'
  if refs and controls:
   passed=statistics.median(refs)>statistics.median(controls);status='passed' if passed else 'failed'
   message='Predeclared check: median reference terrain score must exceed median negative-control terrain score. No thresholds tuned after seeing results.'
  checks.append({'id':'reference-v-control-'+target['id'],'targetId':target['id'],'status':status,'message':message,'referenceScores':refs,'controlScores':controls,
   'referenceMedian':statistics.median(refs) if refs else None,'controlMedian':statistics.median(controls) if controls else None})
  if scored:
   ordered=sorted(scored,key=lambda s:s['terrainPilot']['targets'][target['id']]['score'],reverse=True);n=max(1,math.ceil(len(ordered)*.1))
   offenders=[s['id'] for s in ordered[:n] if s['role']=='negative_control']
   checks.append({'id':'negative-top-decile-'+target['id'],'status':'failed' if offenders else 'passed','offenders':offenders,
    'message':'Terrain-only check; no vegetation/city mask is available, so passing does not establish ecological filtering.'})
 urban=[s for s in sites if s['id']=='control_istanbul' or 'istanbul' in s['id'].lower()]
 checks.append({'id':'historical-urban-screen','status':'passed' if urban and all(s.get('surfaceScreening',{}).get('status')=='rejected' for s in urban) else 'inconclusive','message':L('Kent kontrolünün 2010 NASA HBASE örneklerine dayanan operasyonel elemesi; güncel yerleşim doğrulaması değildir.','Urban control screening based on2010 NASA HBASE samples; not validation of present-day settlement.'),'rejected':[s['id'] for s in sites if s.get('surfaceScreening',{}).get('status')=='rejected']})
 checks.append({'id':'full-profile-coverage','status':'inconclusive','message':'Mineral matching, ground ice and target thermal measurements remain missing; NDVI/night-light measurements are quality- and footprint-limited. Full scientific model validation cannot pass.'})
 return {'status':'inconclusive','checks':checks,'conclusion':L('Pilot arazi karşılaştırması sınandı; tam analog uygunluğu doğrulanmadı. Başarısız kontroller sonuçlarda korunur.','Pilot terrain comparison tested; full analog suitability is not validated. Failed controls are retained.'),
 'design':'Named analogs and diagnostic controls; Manaus/Konya urban labels corrected and separate intended forest/agriculture windows added during source review. No held-out field truth. Sigma and weights are uncalibrated. This is diagnostic validation, not predictive certification.'}

def main(argv=None):
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--offline',action='store_true');parser.add_argument('--refresh',action='store_true');parser.add_argument('--workers',type=int,default=3)
 args=parser.parse_args(argv);config=json.loads((ROOT/'data/project.json').read_text(encoding='utf-8'));cache=Cache(args.offline,args.refresh)
 protected=load_bundle(ROOT,'protected-features.json','analysis/protected_features.py')
 dem_v3=load_bundle(ROOT,'dem-v3-features.json','analysis/dem_v3.py')
 targets=[process_site(cache,t,config,True) for t in config['targets']]
 with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,4))) as pool:
  sites=list(pool.map(lambda s:process_site(cache,s,config),config['sites']))
 for bundle,checkpoint in [(protected,'protected-features.json'),(dem_v3,'dem-v3-features.json')]:
  if bundle:
   for record in source_records(ROOT,bundle,checkpoint):cache.sources[record['id']]=record
 if protected:
  extracted={s['id']:s for s in protected['sites']}
  for s in sites:
   if s['id'] in extracted:merge_site(s,extracted[s['id']],set(cache.sources))
 if dem_v3:
  updated={s['id']:s for s in dem_v3['sites']}
  for s in sites:
   candidate=updated.get(s['id'],{}).get('terrainGrid')
   if not candidate:continue
   s['demV3Quality']=candidate['quality']
   if not candidate['quality'].get('eligibleForOverride'):continue
   if candidate['size']!=config['experiment']['gridSize'] or candidate['spacingM']!=config['experiment']['spacingM']:
    raise ValueError('ASTERv3 checkpoint uses a different physical sample grid')
   values,slopes,fraction=terrain_features(candidate['elevations'],candidate['size'],candidate['spacingM'],config['experiment']['minimumValidFraction'])
   for key,value in values.items():measured(s['features'],key,value,candidate['sourceId'],sourceIds=candidate['sourceIds'],validFraction=fraction,spacingM=candidate['spacingM'],productVersion='ASTGTM.003')
   s['grid']={**candidate,'slopes':slopes};s['terrainSourceVersion']='ASTGTM.003'
 for s in sites:
  s['surfaceScreening']=surface.screening(s['features'],config['surfaceScreening'])
  s['surfaceScreening']['thresholds']=config['surfaceScreening']
  s['surfaceScreening']['description']=L('Yerleşim 2010 HBASE örneklerinden, bitki göstergesi varsa tarihli ve kalite kontrollü MODIS NDVI’dan incelenir. NDVI yoksa bitki elemesi eksik kalır; güncel arazi kullanımının tamamı doğrulanmaz.','Settlement uses2010 HBASE samples; vegetation uses dated quality-screened MODIS NDVI where available. Missing NDVI leaves vegetation screening incomplete; current land use is not fully validated.')
 for s in sites:
  s['terrainPilot']={'targets':{t['id']:target_comparison(s,t,config) for t in targets}}
  s['scores']={t['profile']:full_profile(s,t,t['profile'],config) for t in targets}
  if all(s['features'][k]['value'] is not None for k in config['scoring']['sigma']):s['status']='terrain_available'
 if not all(t['features']['slope_p50_deg']['value'] is not None for t in targets):
  raise RuntimeError('Planetary target DEM unavailable; previous published results preserved')
 if not any(s['features']['slope_p50_deg']['value'] is not None for s in sites):
  raise RuntimeError('No Earth terrain available; previous published results preserved')
 for t in targets:
  t['status']='available' if t['features']['slope_p50_deg']['value'] is not None else 'unavailable'
 cache.sources['earth-geometry']={'id':'earth-geometry','provider':'TerraTwin derived geometry','product':'Earth latitude-based summer-solstice daylight','version':'algorithm-v1','status':'derived','url':'https://science.nasa.gov/earth/facts/','measurementPeriod':None,'retrievedAt':None,'sha256':None}
 limitations=[L('NDVI ve gece ışığı yalnızca dosya kapsamı ve kalite yeterliyse kullanılır. EMIT mineral gözlemi, Mars mineral eşleşmesi değildir; buz ve hedef termal verileri eksik kaldığından tam analog uygunluğu doğrulanamaz.','NDVI and night radiance are used only with adequate footprint and quality. EMIT mineral observations are not Mars mineral matching; missing ice and target thermal measurements prevent full analog validation.'),
 L('Yerleşim elemesi 2010 NASA HBASE sınıflamasında 25 örnek noktaya dayanır; gerçek alan oranı veya güncel yerleşim haritası değildir. Eksik noktalar alt/üst sınırlarla korunur.','Settlement screening uses25 sample nodes from2010 NASA HBASE classification; not an area fraction or current settlement map. Missing nodes remain represented by lower/upper bounds.'),
 L('NASA WorldWind, ASTER GDEM v2 önbelleği sunar; katalogdaki v3 değildir ve 2026 arazi ölçümü sayılmaz.','NASA WorldWind serves an ASTER GDEM v2 cache, not catalogue v3 and not a 2026 terrain survey.'),
 L('500 m düğüm aralığı fiziksel ölçeği eşler; kaynak etkin çözünürlüğünü, DEM hatasını veya bütün frekans içeriğini eşitlemez.','500 m node spacing matches physical sampling scale; it does not equalize effective resolution, DEM error or full frequency content.'),
 L('POWER 2025 verileri 2 m hava sıcaklığı ve bölgesel yağıştır; yüzey sıcaklığı, donmuş zemin veya göl kıyısı mikroiklimi değildir.','POWER 2025 values are regional precipitation and 2 m air temperature, not land-surface temperature, permafrost or shoreline microclimate.'),
 L('Alan sınırları, toleranslar ve ağırlıklar analist seçimidir; NASA onayı veya iniş güvenliği anlamına gelmez.','AOIs, tolerances and weights are analyst choices; no NASA endorsement or landing-safety assessment is implied.')]
 results={'schemaVersion':1,'generatedAt':now(),'status':'partial','experiment':config['experiment'],'targets':targets,'sites':sites,'profiles':config['profiles'],'methods':config['profiles'],
 'protectedData':{'loaded':protected is not None,'demV3Loaded':dem_v3 is not None,'ndviSites':sum(s['features']['ndvi_mean']['value'] is not None for s in sites),'nightLightSites':sum(s['features']['night_lights']['value'] is not None for s in sites),'demV3Sites':sum(s.get('terrainSourceVersion')=='ASTGTM.003' for s in sites)},
 'sources':sorted(cache.sources.values(),key=lambda source:source['id']),'validation':validate(sites,targets),'limitations':limitations,
 'processing':{'configSha256':hashlib.sha256((ROOT/'data/project.json').read_bytes()).hexdigest(),'codeSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'offline':args.offline,'algorithmVersion':'pilot-v3-protected','algorithmFiles':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['analysis/run.py','analysis/surface.py','analysis/protected_integration.py']},'contentSha256':hashlib.sha256((ROOT/'data/content.json').read_bytes()).hexdigest() if (ROOT/'data/content.json').exists() else None}}
 dump(ROOT/'site/analysis-results.json',results)
 features=[]
 for s in targets+sites:
  features.append({'type':'Feature','geometry':s['aoi'],'properties':{'id':s['id'],'name':s['name'],'body':s['body'],'role':s.get('role','target')}})
 dump(ROOT/'data/analysis-areas.geojson',{'type':'FeatureCollection','features':features})
 dump(ROOT/'data/provenance.json',{'generatedAt':results['generatedAt'],'sources':results['sources'],'processing':results['processing']})
 measured_sites=sum(s['features']['slope_p50_deg']['value'] is not None for s in sites)
 print(json.dumps({'sites':len(sites),'terrainAvailable':measured_sites,'targetsAvailable':sum(t['status']=='available' for t in targets),'sources':len(results['sources']),'validation':results['validation']['status'],'output':'site/analysis-results.json'}))
 return 0
if __name__=='__main__':raise SystemExit(main())
