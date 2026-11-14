/** Canonical website content -> deterministic browser bundle. Run with --check in CI. */
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const input = path.join(root, 'data', 'content.json');
const output = path.join(root, 'site', 'data.js');
if (process.argv.includes('--import-existing')) {
  const context = { window: {} };
  vm.runInNewContext(await readFile(output, 'utf8'), context, { timeout: 3000 });
  if (!context.window.TT?.sites || !context.window.TT?.datasets) throw Error('Existing bundle has no TerraTwin content');
  await writeFile(input, JSON.stringify(context.window.TT, null, 2) + '\n');
}
const content = JSON.parse(await readFile(input, 'utf8'));
const unique = (rows, key) => new Set(rows.map(row => row[key])).size === rows.length;
if (!unique(content.sites, 'id')) throw Error('Duplicate site identifier');
if (!unique(content.datasets, 'n')) throw Error('Duplicate dataset name');
for (const site of content.sites) {
  if (!content.cats[site.cat]) throw Error(`Unknown category: ${site.id}`);
  if (!(site.lat >= -90 && site.lat <= 90 && site.lon >= -180 && site.lon <= 180)) throw Error(`Invalid coordinate: ${site.id}`);
  if (!Array.isArray(site.r) || site.r.length !== 3 || site.r.some(r => r !== null && ![1, 2, 3].includes(r))) throw Error(`Invalid qualitative rating: ${site.id}`);
  if (!site.src && !site.doc) throw Error(`Unattributed site: ${site.id}`);
}
for (const profile of Object.values(content.method)) for (const mission of profile.missions) {
  if (mission.w.length !== profile.criteria.length || mission.w.some(w => !Number.isFinite(w) || w < 0) || Math.abs(mission.w.reduce((a, b) => a + b, 0) - 1) > 1e-9) throw Error('Invalid mission weight vector');
}
const generated = '/* Generated from data/content.json by scripts/build_content.mjs. Edit the canonical JSON, then rebuild. */\n(function () {\n  window.TT = ' + JSON.stringify(content, null, 2) + ';\n})();\n';
if (process.argv.includes('--check')) {
  if (await readFile(output, 'utf8') !== generated) throw Error('site/data.js is stale; run node scripts/build_content.mjs');
} else await writeFile(output, generated);
console.log(`Content ${process.argv.includes('--check') ? 'verified' : 'generated'}: ${content.sites.length} sites, ${content.datasets.length} products; qualitative ratings remain explicitly separate from measured analysis.`);
