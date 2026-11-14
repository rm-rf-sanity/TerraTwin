"""Unit fixtures below are synthetic and are NEVER used for published results."""
import datetime as dt
import hashlib
import json
import math
import struct
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from analysis import run

class ScoringTests(unittest.TestCase):
 def test_missing_values_are_not_zero(self):
  components=[{'weight':.6,'value':.8},{'weight':.4,'value':None}]
  result=run.aggregate(components,.6)
  self.assertEqual(result['score'],80)
  self.assertEqual(result['coverage'],.6)
  self.assertEqual(result['status'],'partial')
 def test_coverage_blocks_sparse_score(self):
  result=run.aggregate([{'weight':.59,'value':1},{'weight':.41,'value':None}],.6)
  self.assertIsNone(result['score'])
  self.assertEqual(result['status'],'insufficient')
 def test_invalid_weights_or_scores_rejected(self):
  for components in [[{'weight':-1,'value':.5}], [{'weight':1,'value':1.2}], [{'weight':0,'value':1}]]:
   with self.assertRaises(ValueError):run.aggregate(components)
 def test_gaussian_and_tolerance(self):
  self.assertEqual(run.gaussian(4,4,2),1)
  self.assertAlmostEqual(run.gaussian(6,4,2),math.exp(-.5))
  self.assertIsNone(run.gaussian(None,4,2))
  self.assertIsNone(run.gaussian(4,4,0))
 def test_sensitivity_changes_weights_not_data(self):
  original=[{'weight':.5,'value':1},{'weight':.5,'value':0}]
  result=run.sensitivity(original,.6)
  self.assertLess(result['min'],50);self.assertGreater(result['max'],50)
  self.assertEqual(original[0]['weight'],.5)

class TerrainTests(unittest.TestCase):
 def test_flat_surface_is_not_missing(self):
  features,slopes,fraction=run.terrain_features([0.]*25,5,500)
  self.assertEqual(features['slope_p50_deg'],0)
  self.assertEqual(features['roughness_m'],0)
  self.assertEqual(features['landable_fraction'],1)
  self.assertEqual(fraction,1)
 def test_known_planar_slope_uses_physical_metres(self):
  elevations=[c*500*math.tan(math.radians(10)) for r in range(7) for c in range(7)]
  features,_,_=run.terrain_features(elevations,7,500)
  self.assertAlmostEqual(features['slope_p50_deg'],10,places=7)
  self.assertAlmostEqual(features['roughness_m'],0,places=7)
 def test_voids_block_unreliable_neighbourhoods(self):
  grid=[10.]*25;grid[12]=None
  with self.assertRaises(ValueError):run.terrain_features(grid,5,500,.95)
 def test_earth_binary_voids_masked_before_statistics(self):
  class Fake:
   def fetch(self,*args,**kwargs):return struct.pack('<25h',*([-9999]*25)),{'id':'test'}
  elevations,_,_=run.read_earth_dem(Fake(),{'id':'test','lat':37.,'lon':30.},{'gridSize':5,'spacingM':500})
  self.assertTrue(all(v is None for v in elevations))
  with self.assertRaises(ValueError):run.terrain_features(elevations,5,500)
 def test_missing_sample_count_rejected(self):
  with self.assertRaises(ValueError):run.terrain_features([0.]*24,5,500)
 def test_geodesic_square_is_body_specific(self):
  earth=run.destination(0,0,500,0,'earth');mars=run.destination(0,0,500,0,'mars')
  self.assertGreater(mars[0],earth[0])
  self.assertAlmostEqual(math.radians(mars[0])*run.RADII['mars'],500,places=5)

class ClimateTests(unittest.TestCase):
 def payload(self,year=2025):
  start=dt.date(year,1,1);end=dt.date(year,12,31)
  dates=[(start+dt.timedelta(days=i)).strftime('%Y%m%d') for i in range((end-start).days+1)]
  params={key:{day:value for day in dates} for key,value in [('T2M',5.),('T2M_MAX',10.),('T2M_MIN',-2.),('PRECTOTCORR',1.)]}
  return {'header':{'start':f'{year}0101','end':f'{year}1231','fill_value':-999},'properties':{'parameter':params}}
 def test_daily_rain_summed_not_averaged(self):
  values,count=run.climate_features(self.payload())
  self.assertEqual(values['precipitation_annual_mm'],365)
  self.assertEqual(values['temperature_range_c'],12)
  self.assertEqual(values['frost_days'],365)
  self.assertEqual(count,365)
 def test_leap_year_has_366_days(self):
  values,count=run.climate_features(self.payload(2024))
  self.assertEqual(count,366);self.assertEqual(values['precipitation_annual_mm'],366)
 def test_fill_precipitation_cannot_be_silently_extrapolated(self):
  payload=self.payload();payload['properties']['parameter']['PRECTOTCORR']['20250101']=-999
  with self.assertRaises(ValueError):run.climate_features(payload)
 def test_missing_date_and_negative_rain_rejected(self):
  payload=self.payload();del payload['properties']['parameter']['T2M']['20250101']
  with self.assertRaises(ValueError):run.climate_features(payload)
  payload=self.payload();payload['properties']['parameter']['PRECTOTCORR']['20250101']=-1
  with self.assertRaises(ValueError):run.climate_features(payload)
 def test_boolean_and_nan_are_not_measurements(self):
  self.assertFalse(run.valid(True));self.assertFalse(run.valid(float('nan')));self.assertTrue(run.valid(0))

class ProvenanceTests(unittest.TestCase):
 def test_official_domain_is_enforced(self):
  self.assertTrue(run.trusted_url('https://trek.nasa.gov/moon'))
  self.assertFalse(run.trusted_url('https://nasa.gov.evil.example/file'))
  with self.assertRaises(ValueError):run.Cache().fetch('x','https://example.com/data','not NASA')
 def test_offline_missing_is_fatal(self):
  with tempfile.TemporaryDirectory() as directory,patch.object(run,'ROOT',Path(directory)):
   with self.assertRaises(run.CacheIntegrityError):run.Cache(offline=True).fetch('x','https://power.larc.nasa.gov/test','test')
 def test_checksum_tampering_is_fatal_even_when_online(self):
  url='https://power.larc.nasa.gov/test';key=hashlib.sha256(url.encode()+b'\n').hexdigest()[:24]
  with tempfile.TemporaryDirectory() as directory,patch.object(run,'ROOT',Path(directory)):
   folder=Path(directory)/'data/cache';folder.mkdir(parents=True)
   (folder/(key+'.json')).write_bytes(b'{"modified":true}')
   (folder/(key+'.meta.json')).write_text(json.dumps({'sha256':'incorrect'}))
   with self.assertRaises(run.CacheIntegrityError):run.Cache().fetch('x',url,'test')

if __name__=='__main__':unittest.main()
