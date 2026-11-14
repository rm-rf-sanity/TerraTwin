import unittest
from analysis.surface import sample_values, ndvi_summary, builtup_summary, builtup_bounds, screening

class SurfaceTests(unittest.TestCase):
    def test_ndvi_zero_is_valid_and_fill_is_not(self):
        self.assertEqual(ndvi_summary([0.,0.])[0],0)
        with self.assertRaises(ValueError): ndvi_summary([.4,-9999.])
    def test_ndvi_remains_index_not_area_fraction(self):
        self.assertAlmostEqual(ndvi_summary([-.2,.6])[0],.2)
    def test_hbase_legend_is_not_water_or_percent(self):
        self.assertAlmostEqual(builtup_summary([200.,201.,202.])[0],2/3)
        with self.assertRaises(ValueError): builtup_summary([200.,255.])
        with self.assertRaises(ValueError): builtup_summary([0.,1.])
    def test_locked_scene_rejects_multiple_raster_samples(self):
        with self.assertRaises(ValueError): sample_values({'samples':[{'locationId':0,'value':'0.2'},{'locationId':0,'value':'0.4'}]},1)
    def test_missing_location_remains_missing(self):
        self.assertEqual(sample_values({'samples':[{'locationId':1,'value':'0'}]},2),[None,0.])
    def test_unknown_hbase_nodes_produce_bounds_not_zero_fill(self):
        result=builtup_bounds([201.,None,200.])
        self.assertAlmostEqual(result['lower'],1/3)
        self.assertAlmostEqual(result['upper'],2/3)
        self.assertEqual(result['unknownNodes'],1)
        self.assertLess(result['validFraction'],1)
    def test_screen_does_not_call_missing_data_verified(self):
        settings={'maximumBuiltUpSampleFraction':.5,'maximumNdvi':.6}
        self.assertFalse(screening({},settings)['complete'])
        self.assertEqual(screening({'ndvi':{'value':.8}},settings)['status'],'rejected')
        self.assertEqual(screening({'built_up_sample_fraction_lower_bound':{'value':.5}},settings)['status'],'rejected')

if __name__ == '__main__': unittest.main()
