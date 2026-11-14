import os
import unittest
from unittest.mock import patch, MagicMock
import requests
from analysis.earthdata_access import protect, TokenSession, nasa_host, session_for, data_links, science_file_prefix, verify_token

class EarthdataAccessTests(unittest.TestCase):
    @unittest.skipUnless(os.name=='nt','Windows DPAPI test')
    def test_token_storage_is_encrypted_and_roundtrips(self):
        value=b'not-a-real-token-fixture-only'
        encrypted=protect(value)
        self.assertNotIn(value,encrypted)
        self.assertEqual(protect(encrypted,decrypt=True),value)
    def test_only_official_https_nasa_origins(self):
        self.assertTrue(nasa_host('https://data.lpdaac.earthdatacloud.nasa.gov/file'))
        self.assertFalse(nasa_host('https://nasa.gov.evil.example/file'))
        self.assertFalse(nasa_host('http://urs.earthdata.nasa.gov/file'))
    def test_cross_host_redirect_never_receives_bearer(self):
        for destination in ['https://example.s3.amazonaws.com/file?X-Amz-Signature=fixture','https://example.cloudfront.net/file','https://urs.earthdata.nasa.gov/oauth/authorize']:
            with TokenSession() as session:
                original=requests.Request('GET','https://data.lpdaac.earthdatacloud.nasa.gov/file',headers={'Authorization':'Bearer fixture'}).prepare()
                redirected=requests.Request('GET',destination,headers={'Authorization':'Bearer fixture'}).prepare()
                response=requests.Response();response.request=original
                session.rebuild_auth(redirected,response)
                self.assertNotIn('Authorization',redirected.headers)
    def test_same_host_redirect_keeps_authorization(self):
        with TokenSession() as session:
            original=requests.Request('GET','https://urs.earthdata.nasa.gov/a').prepare()
            redirected=requests.Request('GET','https://urs.earthdata.nasa.gov/b',headers={'Authorization':'Bearer fixture'}).prepare()
            response=requests.Response();response.request=original
            session.rebuild_auth(redirected,response)
            self.assertEqual(redirected.headers['Authorization'],'Bearer fixture')
    def test_http_downgrade_stopped(self):
        with TokenSession() as session:
            response=requests.Response();response.status_code=302;response.url='https://urs.earthdata.nasa.gov/a';response.headers['location']='http://example.com/file'
            with self.assertRaises(RuntimeError):session.get_redirect_target(response)
    def test_malformed_token_rejected(self):
        for value in ['', 'bad\r\nvalue', 'not-ascii-ş']:
            with self.assertRaises(RuntimeError):session_for(value)
    def test_science_probes_use_known_nasa_files(self):
        links=data_links()
        self.assertGreaterEqual(len(links),3)
        self.assertTrue(all(nasa_host(url) for _,url in links))
    def test_login_html_or_error_body_is_not_success(self):
        self.assertFalse(science_file_prefix(b'<html>Login</html>'))
        self.assertFalse(science_file_prefix(b'Forbidden'))
        self.assertTrue(science_file_prefix(b'\x89HDF\r\n\x1a\n1234'))
        self.assertTrue(science_file_prefix(b'\x0e\x03\x13\x01'))
    def test_tls_failure_is_distinct_and_never_logs_token(self):
        fake=MagicMock();fake.get.side_effect=requests.exceptions.SSLError('fixture')
        with patch('analysis.earthdata_access.session_for',return_value=fake),patch('analysis.earthdata_access.data_links',return_value=[('test','https://nasa.gov/file')]):
            report=verify_token('private-fixture')
        self.assertEqual(report['products'][0]['status'],'tls_verification_failed')
        self.assertNotIn('private-fixture',str(report))
    def test_http401_is_distinct_from_network_failure(self):
        fake=MagicMock();response=fake.get.return_value.__enter__.return_value
        response.status_code=401;response.url='https://urs.earthdata.nasa.gov/';response.history=[]
        with patch('analysis.earthdata_access.session_for',return_value=fake),patch('analysis.earthdata_access.data_links',return_value=[('test','https://nasa.gov/file')]):
            report=verify_token('private-fixture')
        self.assertEqual(report['products'][0]['status'],401)
        self.assertFalse(report['authenticated'])

if __name__=='__main__':unittest.main()
