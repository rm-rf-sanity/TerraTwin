"""Synthetic fixtures are unit tests only and never used as published science data."""
import unittest
import numpy as np
from analysis.protected_features import summarize_ndvi, summarize_ntl, summarize_minerals, parse_grid, grid_window, polygon_mask

class NdviTests(unittest.TestCase):
    def test_c61_divisor_not_metadata_multiplier(self):
        result=summarize_ndvi(np.array([[5000]],np.int16),np.array([[2048]],np.uint16),np.array([[0]],np.int8),np.array([[True]]),.95)
        self.assertEqual(result['value'],.5)
        self.assertEqual(result['unit'],'NDVI')
    def test_water_is_not_low_vegetation_land(self):
        result=summarize_ndvi(np.array([[5000,0]]),np.array([[2048,4096]],np.uint16),np.zeros((1,2)),np.ones((1,2),bool),.95)
        self.assertEqual(result['value'],.5)
        self.assertEqual(result['totalPixels'],2)
        self.assertEqual(result['eligibleLandPixels'],1)
        self.assertEqual(result['validFraction'],1)
    def test_cloud_adjacent_shadow_and_snow_are_rejected(self):
        for flag in [1<<8,1<<10,1<<14,1<<15]:
            result=summarize_ndvi(np.array([[5000]]),np.array([[2048|flag]],np.uint16),np.array([[0]]),np.array([[True]]),.95)
            self.assertIsNone(result['value'])
    def test_insufficient_coverage_keeps_diagnostic_mean_separate(self):
        qa=np.full((1,10),2048,np.uint16);qa[0,-1]|=1<<8
        result=summarize_ndvi(np.full((1,10),5000),qa,np.zeros((1,10)),np.ones((1,10),bool),.95)
        self.assertIsNone(result['value'])
        self.assertEqual(result['qualityValidSubsetMean'],.5)
        self.assertEqual(result['validPixels'],9)
    def test_fill_value_is_never_zero(self):
        result=summarize_ndvi(np.array([[-3000]]),np.array([[2048]],np.uint16),np.array([[0]]),np.array([[True]]))
        self.assertIsNone(result['value'])
        self.assertEqual(result['validPixels'],0)

class NightLightTests(unittest.TestCase):
    def fixture(self,raw=8.,cloud=48,mandatory=0,snow=0):
        return summarize_ntl(np.array([[raw]]),np.array([[mandatory]]),np.array([[cloud]],np.uint16),np.array([[snow]]),np.array([[True]]),.95)
    def test_v2_float_radiance_not_v1_scale(self):
        self.assertEqual(self.fixture()['value'],8)
    def test_flags_override_mandatory_good(self):
        for flag in [1,1<<8,1<<9,1<<10,1<<12,1<<13]:
            self.assertIsNone(self.fixture(cloud=48|flag)['value'])
        self.assertIsNone(self.fixture(snow=1)['value'])
    def test_fill_and_poor_quality_are_missing(self):
        self.assertIsNone(self.fixture(raw=-999.9)['value'])
        self.assertIsNone(self.fixture(mandatory=5)['value'])
    def test_measured_zero_radiance_is_valid(self):
        self.assertEqual(self.fixture(raw=0)['value'],0)

class GeometryTests(unittest.TestCase):
    def test_projection_does_not_treat_modis_metres_as_degrees(self):
        metadata='XDim=4800\nYDim=4800\nUpperLeftPointMtrs=(2223901,4447802)\nLowerRightMtrs=(3335851,3335851)\nProjection=GCTP_SNSOID\nProjParams=(6371007.181,0,0)'
        result=parse_grid(metadata)
        self.assertEqual(result['projection'],'GCTP_SNSOID')
        self.assertGreater(result['ul'][0],2000000)
    def test_unknown_projection_is_not_guessed(self):
        metadata='XDim=2\nYDim=2\nUpperLeftPointMtrs=(0,2)\nLowerRightMtrs=(2,0)\nProjection=OTHER'
        with self.assertRaises(ValueError):parse_grid(metadata)
    def test_crop_uses_pixel_centres_and_exact_polygon(self):
        grid={'ul':[0,4],'lr':[4,0],'width':4,'height':4}
        window,inside=grid_window(grid,[[1,1],[3,1],[3,3],[1,3],[1,1]])
        self.assertEqual(window,{'row':1,'col':1,'rows':2,'cols':2})
        self.assertEqual(int(inside.sum()),4)
        self.assertIsNone(grid_window(grid,[[5,5],[6,5],[6,6],[5,6],[5,5]]))

class MineralContextTests(unittest.TestCase):
    def test_quality_mask_excludes_spectral_matches(self):
        raw={'group_1_mineral_id':np.array([[2,2]]),'group_2_mineral_id':np.array([[0,0]]),'group_1_band_depth':np.array([[.2,.2]]),'group_2_band_depth':np.array([[0.,0.]]),'mask_cloud':np.array([[0,1]])}
        result=summarize_minerals(raw,np.ones((1,2),bool),{1:'record1',2:'carbonate_record'},True)
        self.assertEqual(result['validPixels'],1)
        self.assertEqual(result['classes'][0]['count'],1)
        self.assertEqual(result['status'],'context_only')
        self.assertNotIn('mineral_match',result)
    def test_zero_library_id_is_not_a_confirmed_mineral(self):
        raw={f'group_{group}_{name}':np.array([[0]]) for group in [1,2] for name in ['mineral_id','band_depth']}
        result=summarize_minerals(raw,np.ones((1,1),bool),{1:'record1'})
        self.assertEqual(result['classes'],[])
        self.assertEqual(result['validPixels'],0)

if __name__=='__main__':unittest.main()
