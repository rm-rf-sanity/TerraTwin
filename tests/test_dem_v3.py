import importlib.util
import json
import tempfile
from pathlib import Path
import unittest
from analysis.dem_v3 import num_class,verified_path,sha256_file,pairs_from_manifest

RASTERIO_AVAILABLE=importlib.util.find_spec('rasterio') is not None

class NumTests(unittest.TestCase):
    def test_count_zero_is_unspecified_not_void(self):
        self.assertTrue(num_class(0)['usable']);self.assertIsNone(num_class(0)['count'])
    def test_num_is_source_coding_not_simple_count(self):
        self.assertEqual(num_class(71),{'source':'ASTER_GDEM_V2','count':11,'usable':True})
        self.assertEqual(num_class(139)['count'],9)
        self.assertEqual(num_class(204)['count'],4)
        self.assertFalse(num_class(250)['usable']);self.assertFalse(num_class(255)['usable'])
        self.assertEqual(num_class(245)['source'],'ALASKA_V2_FILL')
    def test_checksum_and_path_guard(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);folder=root/'.local/earthdata-data';folder.mkdir(parents=True)
            path=folder/'fixture.tif';path.write_bytes(b'fixture')
            record={'rawPath':path.relative_to(root).as_posix(),'bytes':7,'sha256':sha256_file(path)}
            self.assertEqual(verified_path(record,root),path)
            path.write_bytes(b'changed')
            with self.assertRaises(ValueError):verified_path(record,root)
            with self.assertRaises(ValueError):verified_path({'rawPath':'../outside','bytes':0,'sha256':''},root)
    def test_manifest_requires_both_exact_assets(self):
        record={'status':'downloaded','shortName':'ASTGTM','version':'003','url':'https://data.lpdaac.earthdatacloud.nasa.gov/tile_dem.tif'}
        self.assertEqual(pairs_from_manifest({'downloads':[record]}),[])
        num={**record,'url':record['url'].replace('_dem','_num')}
        self.assertEqual(len(pairs_from_manifest({'downloads':[record,num]})),1)

@unittest.skipUnless(RASTERIO_AVAILABLE,'rasterio installed in analysis virtualenv')
class RasterTests(unittest.TestCase):
    def make_pair(self,directory,dem_values,num_values=None):
        import numpy as np,rasterio
        from rasterio.transform import from_origin
        array=np.asarray(dem_values,dtype='int16');num=np.full(array.shape,4,dtype='uint8') if num_values is None else np.asarray(num_values,dtype='uint8')
        paths=[]
        for filename,values,nodata in [('dem.tif',array,-9999),('num.tif',num,255)]:
            path=Path(directory)/filename
            with rasterio.open(path,'w',driver='GTiff',height=values.shape[0],width=values.shape[1],count=1,dtype=values.dtype,crs='EPSG:4326',transform=from_origin(0,3,1,1),nodata=nodata) as dataset:dataset.write(values,1)
            paths.append(path)
        return paths
    def test_bilinear_uses_pixel_centres_and_zero_is_valid(self):
        from analysis.dem_v3 import sample_pair
        with tempfile.TemporaryDirectory() as directory:
            paths=self.make_pair(directory,[[0,10,20],[100,110,120],[200,210,220]])
            elevations,quality=sample_pair(*paths,[[1,2],[.5,2.5]])
            self.assertEqual(elevations,[55,0]);self.assertEqual(quality['validFraction'],1)
    def test_positive_weight_void_blocks_but_zero_weight_void_does_not(self):
        from analysis.dem_v3 import sample_pair
        with tempfile.TemporaryDirectory() as directory:
            paths=self.make_pair(directory,[[0,-9999,20],[100,110,120],[200,210,220]])
            elevations,_=sample_pair(*paths,[[1,2],[.5,2.5]])
            self.assertEqual(elevations,[None,0])
    def test_absent_nodata_metadata_does_not_break_scalar_mask(self):
        import rasterio
        from analysis.dem_v3 import sample_pair
        with tempfile.TemporaryDirectory() as directory:
            paths=self.make_pair(directory,[[0,-9999,20],[100,110,120],[200,210,220]])
            with rasterio.open(paths[0],'r+') as dataset:dataset.nodata=None
            elevations,_=sample_pair(*paths,[[.5,2.5],[1,2]])
            self.assertEqual(elevations,[0,None])
    def test_num_nearest_keeps_classes_discrete_and_withholds_interpolation(self):
        from analysis.dem_v3 import sample_pair
        with tempfile.TemporaryDirectory() as directory:
            paths=self.make_pair(directory,[[0,10,20],[100,110,120],[200,210,220]],[[0,250,4],[4,4,4],[4,4,4]])
            elevations,quality=sample_pair(*paths,[[.5,2.5],[1.5,2.5]])
            self.assertEqual(elevations,[0,None]);self.assertFalse(quality['eligibleForOverride'])
            self.assertEqual(quality['numCodes'],[0,250])
    def test_outside_tiles_never_extrapolate(self):
        from analysis.dem_v3 import sample_pair
        with tempfile.TemporaryDirectory() as directory:
            paths=self.make_pair(directory,[[0,10,20],[100,110,120],[200,210,220]])
            elevations,_=sample_pair(*paths,[[-1,2]])
            self.assertEqual(elevations,[None])

if __name__=='__main__':unittest.main()
