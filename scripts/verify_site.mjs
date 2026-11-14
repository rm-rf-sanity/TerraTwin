/** Browser integration check using an installed Chromium and Node >=22. No npm dependencies. */
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, writeFile, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import assert from 'node:assert/strict';

const url = process.env.TERRATWIN_URL || 'http://127.0.0.1:5173/';
const browser = process.env.CHROME_PATH || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const profile = await mkdtemp(path.join(tmpdir(), 'terratwin-browser-'));
const artifacts = process.env.TERRATWIN_ARTIFACTS || path.join(profile, 'artifacts');
await mkdir(artifacts, { recursive: true });
const proc = spawn(browser, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'], { windowsHide: true, stdio: 'ignore' });
let ws;
const pending = new Map();
let nextId = 0;
const runtimeErrors = [];
const failedResponses = [];
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
async function until(fn, timeout = 20000) {
  const started = Date.now();
  while (Date.now() - started < timeout) { try { const value = await fn(); if (value) return value; } catch {} await sleep(150); }
  throw Error('Timed out waiting for browser condition');
}
function send(method, params = {}) {
  const id = ++nextId;
  return new Promise((resolve, reject) => { const timer = setTimeout(() => { pending.delete(id); reject(Error(`CDP timeout: ${method}`)); }, 20000); pending.set(id, { resolve, reject, timer }); ws.send(JSON.stringify({ id, method, params })); });
}
async function evaluate(expression) {
  const response = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (response.exceptionDetails) throw Error(JSON.stringify(response.exceptionDetails));
  return response.result.value;
}
async function click(selector) { assert(await evaluate(`!!document.querySelector(${JSON.stringify(selector)})`), `Missing control ${selector}`); await evaluate(`document.querySelector(${JSON.stringify(selector)}).click()`); }
try {
  const port = await until(async () => (await readFile(path.join(profile, 'DevToolsActivePort'), 'utf8')).split('\n')[0]);
  const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
  ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { ws.addEventListener('open', resolve, { once: true }); ws.addEventListener('error', reject, { once: true }); });
  ws.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id) { const p = pending.get(message.id); if (p) { clearTimeout(p.timer); pending.delete(message.id); if (message.error) p.reject(Error(message.error.message)); else p.resolve(message.result); } }
    if (message.method === 'Runtime.exceptionThrown') runtimeErrors.push(message.params.exceptionDetails.text + ' ' + (message.params.exceptionDetails.exception?.description || ''));
    if (message.method === 'Network.responseReceived' && message.params.response.status >= 400) failedResponses.push({ url: message.params.response.url, status: message.params.response.status });
  });
  await send('Page.enable'); await send('Runtime.enable'); await send('Network.enable');
  await send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: artifacts });
  await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await send('Page.navigate', { url });
  await until(() => evaluate(`document.readyState === 'complete' && !!document.querySelector('#site-card h3')`));
  assert.equal(await evaluate(`!!document.querySelector('#durum')`), false, 'Removed section must stay removed');
  await click('[data-lang="tr"]');
  await click('#site-list [data-id="salda"]');
  assert.match(await evaluate(`document.querySelector('#site-card h3').textContent`), /Salda/);
  await click('#profile-seg [data-p="mars"]');
  await click('#cat-legend [data-cat="hypo"]');
  assert.equal(await evaluate(`document.querySelector('#site-list [data-id="nemrut"]').classList.contains('off')`), true);
  await click('#cat-legend [data-cat="hypo"]');
  await click('#body-seg [data-b="mars"]');
  assert.equal(await evaluate(`document.querySelectorAll('#catalog tbody tr').length`), 7);
  await click('[data-lang="en"]');
  assert.equal(await evaluate(`document.documentElement.lang`), 'en');
  assert.match(await evaluate(`document.querySelector('#site-card h3').textContent`), /Salda/);
  await click('#m-profile [data-k="mars"]');
  await click('#m-missions [data-i="1"]');
  await click('[data-lang="tr"]');
  await sleep(500);
  const analysis = await evaluate(`fetch('site/analysis-results.json').then(async r => ({status:r.status, data:r.ok ? await r.json() : null}))`);
  assert.equal(analysis.status, 200, 'Analysis export must be served');
  assert(analysis.data && typeof analysis.data === 'object', 'Analysis export must be JSON');

  await until(() => evaluate(`document.querySelector('#analysis-panel')?.dataset.status === 'loaded'`));
  assert(analysis.data.sites.length > 0, 'A genuine completed data run must contain sites');
  assert.equal(await evaluate(`document.querySelectorAll('#analysis-ranking button').length`), analysis.data.sites.length);
  await evaluate(`document.querySelector('#analysis-target').value = 'jezero'; document.querySelector('#analysis-target').dispatchEvent(new Event('change', {bubbles:true}))`);
  assert.equal(await evaluate(`document.querySelector('#m-profile [data-k="mars"]').getAttribute('aria-pressed')`), 'true');
  await click('#analysis-ranking [data-analysis-id="control-istanbul"]');
  assert.match(await evaluate(`document.querySelector('#analysis-detail').textContent`), /2010/);
  assert.match(await evaluate(`document.querySelector('#analysis-detail').textContent`), /Dışlandı/);
  await evaluate(`document.querySelector('#analysis-mode').value = 'terrain'; document.querySelector('#analysis-mode').dispatchEvent(new Event('change', {bubbles:true}))`);
  await click('#analysis-ranking button');
  assert(await evaluate(`!!document.querySelector('#analysis-detail h4')`));
  await evaluate(`document.querySelector('#analysis-layer').value = 'slope_p50_deg'; document.querySelector('#analysis-layer').dispatchEvent(new Event('change', {bubbles:true}))`);
  if (await evaluate(`!!window.d3 && !!document.querySelector('#map .markers')`)) assert.equal(await evaluate(`document.querySelectorAll('#map .analysis-sample').length`), analysis.data.sites.length);
  await click('#analysis-json');
  const exportedJSON = JSON.parse(await until(() => readFile(path.join(artifacts, 'terratwin-analysis.json'), 'utf8')));
  assert.equal(exportedJSON.generatedAt, analysis.data.generatedAt);
  await click('#analysis-csv');
  const exportedCSV = await until(() => readFile(path.join(artifacts, 'terratwin-analysis.csv'), 'utf8'));
  assert.equal(exportedCSV.trim().split('\r\n').length, analysis.data.sites.length + 1);
  await click('#analysis-geojson');
  const exportedGeoJSON = JSON.parse(await until(() => readFile(path.join(artifacts, 'terratwin-earth-aois.geojson'), 'utf8')));
  assert.equal(exportedGeoJSON.features.length, analysis.data.sites.length);
  assert(exportedGeoJSON.features.every(f => f.properties.body === 'earth'));
  await evaluate(`document.querySelector('#analysis-panel').scrollIntoView({block:'start',behavior:'instant'})`);
  await sleep(300);
  const analysisDesktop = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  await writeFile(path.join(artifacts, 'analysis-desktop.png'), Buffer.from(analysisDesktop.data, 'base64'));
  await evaluate('scrollTo(0,0)');

  const desktop = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  await writeFile(path.join(artifacts, 'desktop.png'), Buffer.from(desktop.data, 'base64'));
  await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
  await sleep(300);
  assert(await evaluate(`document.documentElement.scrollWidth <= innerWidth + 1`), 'Mobile page must not overflow horizontally');
  await evaluate(`document.querySelector('#analysis-panel').scrollIntoView({block:'start',behavior:'instant'})`);
  await sleep(300);
  const mobile = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  await writeFile(path.join(artifacts, 'mobile.png'), Buffer.from(mobile.data, 'base64'));
  await send('Network.setBlockedURLs', { urls: ['*://cdnjs.cloudflare.com/*', '*://fonts.googleapis.com/*', '*://fonts.gstatic.com/*', '*://cdn.jsdelivr.net/*'] });
  await send('Page.navigate', { url });
  await until(() => evaluate(`document.querySelector('#analysis-panel')?.dataset.status === 'loaded' && !!document.querySelector('#site-card h3')`));
  assert.equal(await evaluate(`document.querySelectorAll('#analysis-ranking button').length`), analysis.data.sites.length, 'Analysis remains usable without external presentation libraries');
  assert(await evaluate(`!!document.querySelector('#map-offline') && !document.querySelector('#map-offline').hidden`));
  assert.deepEqual(runtimeErrors, [], 'No uncaught JavaScript errors');
  assert.deepEqual(failedResponses.filter(r => r.url.startsWith(url)), [], 'No failed local assets');
  console.log(JSON.stringify({ passed: true, url, artifacts, analysisKeys: Object.keys(analysis.data), failedExternalResponses: failedResponses.filter(r => !r.url.startsWith(url)), browserChecks: 'language, atlas selection, category filter, marker profile, catalog filter, method controls, analysis JSON, desktop/mobile layout, runtime errors' }, null, 2));
} finally {
  for (const p of pending.values()) { clearTimeout(p.timer); p.reject(Error('Browser closed')); }
  ws?.close();
  proc.kill();
}
