import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from analysis import protected_download as module

PAYLOAD=b'\x89HDF\r\n\x1a\n'+b'NASA-test-fixture-only'*8
URL='https://data.lpdaac.earthdatacloud.nasa.gov/test/file.nc'

class FakeResponse:
 def __init__(self,data=PAYLOAD,status=206,start=0,total=None):
  self.status_code=status;self.raw=io.BytesIO(data);self.data=data
  self.headers={'Content-Length':str(len(data)),'ETag':'fixture-etag'}
  if status==206:self.headers['Content-Range']=f'bytes {start}-{start+len(data)-1}/{total or len(PAYLOAD)}'
 def __enter__(self):return self
 def __exit__(self,*args):pass
 def iter_content(self,chunk_size):yield self.data

class DownloaderTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
  self.override=patch.object(module,'ROOT',self.root);self.override.start()
  self.record={'id':'test:one','shortName':'test','granuleUr':'one','url':URL,'rawPath':'.local/earthdata-data/file.nc'}
 def tearDown(self):self.override.stop();self.temp.cleanup()
 def downloader(self,**kw):return module.Downloader(manifest_path=self.root/'manifest.json',token='fixture',**kw)
 def responses(self,downloader,response=None):
  return patch.object(downloader,'_get',side_effect=[FakeResponse(PAYLOAD[:32],start=0),response or FakeResponse()])
 def partial(self,length):
  file=self.root/(self.record['rawPath']+'.part');file.parent.mkdir(parents=True,exist_ok=True);file.write_bytes(PAYLOAD[:length])
  module.atomic_json(file.with_suffix(file.suffix+'.json'),{'url':URL,'bytes':len(PAYLOAD),'etag':'fixture-etag'})
  return file
 def test_complete_download_records_exact_bytes_hash_and_canonical_url(self):
  d=self.downloader()
  with self.responses(d):result=d.download(self.record)
  self.assertEqual(result['bytes'],len(PAYLOAD));self.assertEqual(result['sha256'],hashlib.sha256(PAYLOAD).hexdigest())
  self.assertEqual((self.root/result['rawPath']).read_bytes(),PAYLOAD)
  self.assertFalse(result['subset']);self.assertEqual(result['url'],URL)
  self.assertNotIn('fixture',json.dumps(d.manifest).replace('fixture-etag',''))
 def test_offline_verified_cache_needs_no_credentials_or_network(self):
  d=self.downloader()
  with self.responses(d):d.download(self.record)
  with patch.object(module,'load_token',side_effect=AssertionError('no credentials should be read')):
   result=self.downloader(offline=True).download(self.record)
  self.assertEqual(result['bytes'],len(PAYLOAD))
 def test_tampered_file_fails_even_offline(self):
  d=self.downloader()
  with self.responses(d):d.download(self.record)
  (self.root/self.record['rawPath']).write_bytes(b'x'*len(PAYLOAD))
  with self.assertRaises(module.DownloadError):self.downloader(offline=True).download(self.record)
 def test_offline_missing_file_fails(self):
  with self.assertRaises(module.DownloadError):self.downloader(offline=True).download(self.record)
 def test_budget_is_checked_before_full_download(self):
  d=self.downloader(max_file_bytes=len(PAYLOAD)-1)
  with patch.object(d,'_get',return_value=FakeResponse(PAYLOAD[:32])) as get:
   with self.assertRaises(module.DownloadError):d.download(self.record)
  self.assertEqual(get.call_count,1)
 def test_resume_appends_only_returned_matching_range(self):
  self.partial(40);d=self.downloader()
  with self.responses(d,FakeResponse(PAYLOAD[40:],start=40)) as get:result=d.download(self.record)
  self.assertEqual((self.root/result['rawPath']).read_bytes(),PAYLOAD)
  self.assertEqual(get.call_args_list[1].args[1]['Range'],'bytes=40-')
 def test_ignored_range_restarts_instead_of_duplicate_append(self):
  self.partial(40);d=self.downloader()
  with self.responses(d,FakeResponse(PAYLOAD,status=200)):result=d.download(self.record)
  self.assertEqual((self.root/result['rawPath']).read_bytes(),PAYLOAD)
 def test_interrupted_download_preserves_partial_for_a_later_resume(self):
  class Interrupted(FakeResponse):
   def iter_content(self,chunk_size):
    yield PAYLOAD[:40]
    raise module.requests.ConnectionError('fixture without real URL')
  d=self.downloader()
  with self.responses(d,Interrupted()):
   with self.assertRaises(module.DownloadError):d.download(self.record)
  partial=self.root/(self.record['rawPath']+'.part')
  self.assertEqual(partial.read_bytes(),PAYLOAD[:40])
  with self.responses(d,FakeResponse(PAYLOAD[40:],start=40)):result=d.download(self.record)
  self.assertEqual((self.root/result['rawPath']).read_bytes(),PAYLOAD)
 def test_server_cannot_stream_more_than_declared_object_size(self):
  class Oversized(FakeResponse):
   def iter_content(self,chunk_size):yield PAYLOAD+b'overflow'
  d=self.downloader()
  with self.responses(d,Oversized()):
   with self.assertRaises(module.DownloadError):d.download(self.record)
  self.assertFalse((self.root/self.record['rawPath']).exists())
 def test_changed_etag_prevents_resuming_incompatible_object(self):
  partial=self.partial(40)
  metadata=json.loads(partial.with_suffix(partial.suffix+'.json').read_text());metadata['etag']='old-object'
  module.atomic_json(partial.with_suffix(partial.suffix+'.json'),metadata)
  d=self.downloader()
  with patch.object(d,'_get',return_value=FakeResponse(PAYLOAD[:32])):
   with self.assertRaises(module.DownloadError):d.download(self.record)
 def test_wrong_resume_position_rejected(self):
  self.partial(40);d=self.downloader()
  with self.responses(d,FakeResponse(PAYLOAD[30:],start=30)):
   with self.assertRaises(module.DownloadError):d.download(self.record)
 def test_invalid_magic_never_becomes_science_file(self):
  d=self.downloader()
  with patch.object(d,'_get',return_value=FakeResponse(b'<html>Login</html>')):
   with self.assertRaises(module.DownloadError):d.download(self.record)
 def test_output_path_cannot_escape_private_science_directory(self):
  with self.assertRaises(module.DownloadError):self.downloader().download(dict(self.record,rawPath='../outside.nc'))
 def test_unbounded_probe_is_rejected(self):
  with self.assertRaises(module.DownloadError):module.expected_size({},200)
 def test_non_nasa_initial_url_and_query_parameters_rejected(self):
  for url in ['https://example.com/file.nc',URL+'?token=not-real','http://nasa.gov/file.nc']:
   with self.assertRaises(module.DownloadError):module.canonical_url(url)
 def test_companion_must_be_in_verified_granule_links(self):
  with self.assertRaises(module.DownloadError):module.companion(self.record,'https://nasa.gov/guessed.nc','mask')
 def test_normalizer_ignores_search_and_metadata_links(self):
  entry={'short_name':'test','version':'1','granule_ur':'one','links':[{'href':'https://search.earthdata.nasa.gov/search?granule=one','rel':'http://esipfed.org/ns/fedsearch/1.1/data#'},{'href':URL,'rel':'http://esipfed.org/ns/fedsearch/1.1/data#'}]}
  result=module.normalize_granule(entry)
  self.assertEqual(result['assets'],[URL])

if __name__=='__main__':unittest.main()
