import unittest
from analysis.protected_integration import merge_site, environmental_proxies

class ProtectedIntegrationTests(unittest.TestCase):
 def site(self):return {'id':'test','features':{'ndvi_mean':{'value':None,'status':'missing'},'night_lights':{'value':None,'status':'missing'},'mineral_match':{'value':None,'status':'missing'}},'missing':[]}
 def test_ndvi_is_not_a_vegetation_fraction_or_mineral_match(self):
  site=self.site();merge_site(site,{'id':'test','features':{'ndvi_mean':{'value':.3,'sourceId':'source','status':'derived'},'mineral_match':{'value':1,'sourceId':'source'}}},{'source'})
  self.assertEqual(site['features']['ndvi_mean']['value'],.3)
  self.assertIsNone(site['features']['mineral_match']['value'])
 def test_invalid_or_unattributed_measurements_rejected(self):
  for feature in [{'value':True,'sourceId':'source'},{'value':float('nan'),'sourceId':'source'},{'value':.3,'sourceId':'unknown'}]:
   with self.assertRaises(ValueError):merge_site(self.site(),{'id':'test','features':{'ndvi_mean':feature}},{'source'})
 def test_missing_is_not_zero(self):
  site=self.site();merge_site(site,{'id':'test','features':{'ndvi_mean':{'value':None,'status':'outside'}}},set())
  self.assertIsNone(site['features']['ndvi_mean']['value']);self.assertEqual(site['features']['ndvi_mean']['status'],'missing')
 def test_directional_proxy_scales_are_explicit(self):
  scales={'ndviBareGroundCeiling':.6,'nightLightsRadiance':5}
  bare,isolated=environmental_proxies({'ndvi_mean':{'value':.3},'night_lights':{'value':0}},scales)
  self.assertAlmostEqual(bare,.5);self.assertEqual(isolated,1)
  self.assertEqual(environmental_proxies({},scales),(None,None))

if __name__=='__main__':unittest.main()
