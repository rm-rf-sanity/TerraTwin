/** Cross-file, provenance and arithmetic integration checks. No network needed. */
import { readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const bytes = name => readFile(path.join(root, name));
const json = async name => JSON.parse((await bytes(name)).toString('utf8').replace(/^\uFEFF/, ''));
const hash = value => createHash('sha256').update(value).digest('hex');
const content = await json('data/content.json');
const project = await json('data/project.json');
const output = await json('site/analysis-results.json');
assert.deepEqual(project.profiles, content.method, 'Website and analysis mission definitions must agree');
assert.deepEqual(output.profiles, project.profiles, 'Analysis output has stale mission definitions');
assert.equal(output.processing.configSha256, hash(await bytes('data/project.json')), 'Recompute analysis after config changes');
assert.equal(output.processing.codeSha256, hash(await bytes('analysis/run.py')), 'Recompute analysis after algorithm changes');
assert.equal(output.processing.contentSha256, hash(await bytes('data/content.json')), 'Recompute analysis after canonical content changes');
for (const [name, expected] of Object.entries(output.processing.algorithmFiles || {})) assert.equal(hash(await bytes(name)), expected, `Changed analysis module: ${name}`);
const registry = await json('data/source-registry.json');
for (const evidence of [...(registry.evidence_snapshots || []), ...(registry.surface_probe_snapshot_status || []), ...(registry.granule_access_checks || [])]) if (evidence.snapshot && evidence.sha256) assert.equal(hash(await bytes(evidence.snapshot)), evidence.sha256, `Changed source evidence: ${evidence.snapshot}`);
assert.equal(output.sites.length, project.sites.length);
assert.equal(output.targets.length, project.targets.length);
const officialHost = url => { const host = new URL(url).hostname; return host === 'nasa.gov' || host.endsWith('.nasa.gov') || host === 'modis.ornl.gov'; };
const sourceMap = new Map(output.sources.map(s => [s.id, s]));
for (const source of output.sources) {
  if (source.status === 'derived') continue;
  assert(officialHost(source.url), `Unexpected science distributor ${source.url}`);
  assert.match(source.sha256, /^[a-f0-9]{64}$/);
  if (source.kind === 'protected-granule') {
    assert.equal(hash(await bytes(source.extractionPath)), source.extractionSha256, `Changed protected checkpoint: ${source.id}`);
    if (source.evidencePath) assert.equal(hash(await bytes(source.evidencePath)), source.evidenceSha256, `Changed AOI raw/QA evidence: ${source.id}`);
    assert(source.cachePath.replaceAll('\\', '/').startsWith('.local/earthdata-data/'), 'Protected science path must stay outside credentials');
    if (existsSync(path.join(root, source.cachePath))) assert.equal(hash(await bytes(source.cachePath)), source.sha256, `Changed protected granule: ${source.id}`);
  } else assert.equal(hash(await bytes(source.cachePath)), source.sha256, `Changed raw response: ${source.id}`);
}
function compare(result, minimum, label) {
  const total = result.components.reduce((n, c) => n + c.weight, 0);
  const available = result.components.filter(c => Number.isFinite(c.value));
  const covered = available.reduce((n, c) => n + c.weight, 0);
  assert(total > 0 && result.components.every(c => c.weight >= 0), `${label}: invalid weights`);
  assert(Math.abs(result.coverage - covered / total) < 1e-5, `${label}: coverage mismatch`);
  assert(available.every(c => c.value >= 0 && c.value <= 1), `${label}: component range`);
  if (result.score !== null) {
    assert(covered / total + 1e-9 >= minimum, `${label}: score below coverage gate`);
    const expected = 100 * available.reduce((n, c) => n + c.weight * c.value, 0) / covered;
    assert(Math.abs(result.score - expected) < .0011, `${label}: score arithmetic mismatch`);
  }
}
for (const configured of project.sites) {
  const canonical = content.sites.find(s => s.id === configured.id);
  if (!canonical) { assert.equal(configured.role, 'negative_control'); continue; }
  assert.equal(configured.lat, canonical.lat, `Stale latitude: ${configured.id}`);
  assert.equal(configured.lon, canonical.lon, `Stale longitude: ${configured.id}`);
  assert.equal(configured.sourceCategory, canonical.cat, `Stale source category: ${configured.id}`);
  assert.equal(configured.referenceSource, canonical.src?.[1] || canonical.doc, `Stale citation: ${configured.id}`);
}
for (const area of [...output.sites, ...output.targets]) {
  assert(area.aoi.type === 'Polygon');
  const ring = area.aoi.coordinates[0];
  assert.deepEqual(ring[0], ring.at(-1), `AOI ring not closed: ${area.id}`);
  for (const [lon, lat] of ring) assert(lon >= -180 && lon <= 180 && lat >= -90 && lat <= 90);
  for (const feature of Object.values(area.features)) {
    if (feature.value === null) { assert.equal(feature.status, 'missing'); continue; }
    assert(Number.isFinite(feature.value), `Non-numeric feature: ${area.id}`);
    assert(sourceMap.has(feature.sourceId), `Unattributed feature: ${area.id}`);
    for (const id of feature.sourceIds || []) assert(sourceMap.has(id), `Missing batch provenance: ${id}`);
  }
  for (const result of Object.values(area.terrainPilot?.targets || {})) compare(result, 1, `${area.id}/terrain`);
  for (const profile of Object.values(area.scores || {})) for (const mission of profile.missions) compare(mission, output.experiment.minimumCoverage, `${area.id}/${mission.id}`);
  if (area.surfaceScreening?.status === 'rejected') for (const profile of Object.values(area.scores || {})) for (const mission of profile.missions) { assert.equal(mission.score, null, 'Screened sites cannot publish a mission score'); assert.equal(mission.status, 'excluded'); }
  if (area.surfaceSamples) { const b = area.surfaceSamples.bounds; assert(b.lower >= 0 && b.upper <= 1 && b.lower <= b.upper); assert.equal(b.builtUpNodes + b.unknownNodes <= b.requestedNodes, true); assert(Math.abs(b.lower - b.builtUpNodes / b.requestedNodes) < 1e-9); }
}
assert(!String(await bytes('index.html')).includes('id="durum"'), 'Removed status section must remain removed');
assert.equal(output.validation.status, 'inconclusive', 'Incomplete scientific validation must remain explicit');
console.log(JSON.stringify({ passed: true, sites: output.sites.length, targets: output.targets.length, verifiedRawResponses: output.sources.filter(s => s.status !== 'derived').length, checks: 'canonical content, exact config/code hashes, primary distributors, cached response hashes, source attribution, AOI geometry, score arithmetic, coverage gates, explicit validation status' }, null, 2));
