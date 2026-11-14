"""Local Earthdata token setup and bounded authenticated access verification.
Secrets remain in memory or Windows user-protected DPAPI storage, never in outputs.
"""
from __future__ import annotations
import argparse
import ctypes
from ctypes import wintypes
import datetime as dt
import json
import os
from pathlib import Path
import threading
import requests
from urllib.parse import urljoin
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / '.local'
TOKEN_FILE = PRIVATE / 'earthdata-token.bin'
STATUS_FILE = PRIVATE / 'earthdata-status.json'

class DataBlob(ctypes.Structure):
    _fields_ = [('cbData', wintypes.DWORD), ('pbData', ctypes.POINTER(ctypes.c_ubyte))]

def protect(data: bytes, decrypt=False) -> bytes:
    if os.name != 'nt':
        raise RuntimeError('Persistent token storage requires Windows DPAPI')
    buffer = ctypes.create_string_buffer(data)
    input_blob = DataBlob(len(data), ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte)))
    output_blob = DataBlob()
    crypt = ctypes.WinDLL('crypt32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.LocalFree.argtypes = [ctypes.c_void_p]
    kernel.LocalFree.restype = ctypes.c_void_p
    if decrypt:
        function = crypt.CryptUnprotectData
        function.argtypes = [ctypes.POINTER(DataBlob), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(DataBlob)]
        ok = function(ctypes.byref(input_blob), None, None, None, None, 1, ctypes.byref(output_blob))
    else:
        function = crypt.CryptProtectData
        function.argtypes = [ctypes.POINTER(DataBlob), wintypes.LPCWSTR, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(DataBlob)]
        ok = function(ctypes.byref(input_blob), 'TerraTwin Earthdata access', None, None, None, 1, ctypes.byref(output_blob))
    if not ok:
        raise RuntimeError('Windows could not protect/unprotect the local token')
    try:
        return ctypes.string_at(output_blob.pbData, output_blob.cbData)
    finally:
        kernel.LocalFree(output_blob.pbData)

def load_token():
    token = os.environ.get('EARTHDATA_TOKEN')
    if token:
        return token.strip()
    if TOKEN_FILE.exists():
        return protect(TOKEN_FILE.read_bytes(), decrypt=True).decode('utf-8')
    raise RuntimeError('Earthdata access is not configured; run python -m analysis.earthdata_access --setup')

def nasa_host(url):
    parsed = urlparse(url)
    host = (parsed.hostname or '').lower()
    return parsed.scheme == 'https' and (host == 'nasa.gov' or host.endswith('.nasa.gov'))

class TokenSession(requests.Session):
    """Follow NASA's requests.Session pattern; never forward credentials across hosts."""
    def get_redirect_target(self, response):
        target = super().get_redirect_target(response)
        if target and urlparse(urljoin(response.url, target)).scheme != 'https':
            raise RuntimeError('Insecure redirect stopped')
        return target

    def rebuild_auth(self, prepared_request, response):
        before = urlparse(response.request.url)
        after = urlparse(prepared_request.url)
        # Avoid re-applying credentials from unrelated local .netrc entries.
        if (before.hostname, before.port) != (after.hostname, after.port):
            prepared_request.headers.pop('Authorization', None)


def session_for(token):
    if not token or any(c in token for c in '\r\n') or not token.isascii():
        raise RuntimeError('Access token is empty or malformed')
    return TokenSession()


def science_file_prefix(prefix):
    return prefix.startswith((b'\x0e\x03\x13\x01', b'\x89HDF\r\n\x1a\n', b'CDF\x01', b'CDF\x02', b'II*\x00', b'MM\x00*'))


def data_links():
    registry = json.loads((ROOT / 'data/source-registry.json').read_text(encoding='utf-8'))
    records = []
    for entry in registry.get('granule_access_checks', []):
        links = [link for link in entry.get('data_links', []) if link.get('rel', '').endswith('/data#') and nasa_host(link.get('href', ''))]
        if links:
            records.append((entry['short_name'], links[0]['href']))
    return records

def verify_token(token):
    session = session_for(token)
    results = []
    try:
        for product, url in data_links():
            try:
                with session.get(url, headers={'Authorization': 'Bearer ' + token, 'Range': 'bytes=0-31',
                                 'User-Agent': 'TerraTwin Earthdata access verification/1.1'}, stream=True, timeout=(10, 30)) as response:
                    prefix = response.raw.read(32) if response.status_code in (200, 206) else b''
                    accessible = response.status_code in (200, 206) and science_file_prefix(prefix)
                    results.append({'product': product, 'status': response.status_code if accessible or response.status_code not in (200, 206) else 'unexpected_file_content',
                                    'accessible': accessible, 'checkedBytes': len(prefix),
                                    'finalHost': urlparse(response.url).hostname,
                                    'redirectHosts': [urlparse(r.url).hostname for r in response.history]})
            except requests.exceptions.SSLError:
                results.append({'product': product, 'status': 'tls_verification_failed', 'accessible': False})
            except requests.exceptions.ConnectTimeout:
                results.append({'product': product, 'status': 'connection_timeout', 'accessible': False})
            except requests.exceptions.ReadTimeout:
                results.append({'product': product, 'status': 'read_timeout', 'accessible': False})
            except requests.exceptions.TooManyRedirects:
                results.append({'product': product, 'status': 'redirect_loop', 'accessible': False})
            except requests.exceptions.ConnectionError:
                results.append({'product': product, 'status': 'connection_failed', 'accessible': False})
            except (requests.exceptions.RequestException, RuntimeError, OSError):
                results.append({'product': product, 'status': 'request_failed', 'accessible': False})
    finally:
        session.close()
    if not results:
        raise RuntimeError('No verified NASA download endpoints are configured')
    return {'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),
            'authenticated': any(r['accessible'] for r in results), 'products': results}


def save_status(status):
    PRIVATE.mkdir(exist_ok=True)
    temporary = STATUS_FILE.with_suffix('.tmp')
    temporary.write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
    temporary.replace(STATUS_FILE)

def setup_gui():
    import tkinter as tk
    from tkinter import ttk, messagebox
    import webbrowser
    window = tk.Tk()
    window.title('TerraTwin — NASA Earthdata bağlantısı')
    window.geometry('740x440')
    window.minsize(600, 360)
    frame = ttk.Frame(window, padding=24)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='NASA Earthdata erişimini bağla', font=('Segoe UI', 16, 'bold')).pack(anchor='w', pady=(0, 14))
    ttk.Label(frame, text='1. NASA profilinde Generate Token → Generate Token yolunu izle.\n2. Show Token ile anahtarı kopyala ve aşağıdaki gizli alana yapıştır.\n3. Bağlantıyı test et. Anahtar yalnızca bu Windows hesabında şifreli saklanır.', wraplength=680, justify='left').pack(anchor='w')
    ttk.Button(frame, text='NASA profilini aç', command=lambda: webbrowser.open('https://urs.earthdata.nasa.gov/profile')).pack(anchor='w', pady=12)
    value = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=value, show='•', width=75)
    entry.pack(fill='x', pady=6)
    status = tk.StringVar(value='Anahtarı bu pencereye gir; sohbete göndermene gerek yok.')
    ttk.Label(frame, textvariable=status, wraplength=680).pack(anchor='w', pady=12)
    def finished(report, token):
        if report['authenticated']:
            PRIVATE.mkdir(exist_ok=True)
            encrypted = protect(token.encode('utf-8'))
            temporary = TOKEN_FILE.with_suffix('.tmp')
            temporary.write_bytes(encrypted)
            temporary.replace(TOKEN_FILE)
            save_status(report)
            value.set('')
            status.set('Bağlantı doğrulandı. Anahtar Windows tarafından şifrelendi; pencereyi kapatabilirsin.')
            messagebox.showinfo('NASA bağlantısı hazır', 'En az bir korumalı NASA dosyasına erişim doğrulandı.\nSohbete “bağlantı hazır” yazabilirsin.')
            button.config(state='disabled')
        else:
            save_status(report)
            labels = {401: 'NASA anahtarı kabul etmedi', 403: 'yetki/izin reddi', 404: 'dosya bulunamadı', 'tls_verification_failed': 'TLS sertifika doğrulama hatası', 'connection_timeout': 'bağlantı zaman aşımı', 'read_timeout': 'sunucu yanıt zaman aşımı', 'redirect_loop': 'yönlendirme döngüsü', 'connection_failed': 'ağ bağlantısı kurulamadı', 'request_failed': 'istek/yönlendirme hatası', 'unexpected_file_content': 'beklenen bilim dosyası dönmedi'}
            summary = ', '.join(f"{r['product']}: {labels.get(r['status'], r['status'])}" for r in report['products'])
            status.set('Erişim doğrulanamadı; anahtar kaydedilmedi. ' + summary)
            button.config(state='normal')
    def run():
        token = value.get().strip()
        if not token:
            status.set('Önce NASA erişim anahtarını gir.')
            return
        button.config(state='disabled')
        status.set('Korumalı NASA dosyalarına erişim test ediliyor…')
        def worker():
            try:
                report = verify_token(token)
                window.after(0, lambda: finished(report, token))
            except Exception:
                window.after(0, lambda: (status.set('Bağlantı kurulamadı; anahtar kaydedilmedi.'), button.config(state='normal')))
        threading.Thread(target=worker, daemon=True).start()
    button = ttk.Button(frame, text='Bağlantıyı test et ve şifreli kaydet', command=run)
    button.pack(anchor='w')
    entry.focus_set()
    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.setup:
        setup_gui()
        return 0
    if args.check:
        report = verify_token(load_token())
        save_status(report)
        print(json.dumps(report))
        return 0 if report['authenticated'] else 1
    parser.print_help()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
