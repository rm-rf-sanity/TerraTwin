'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { featureValue, rankSites, scoreFor, csvCell, buildGeoJSON } = require('../site/analysis-ui.js');
const site = (id, value, status = 'partial') => ({ id, name: id, role: 'candidate', aoi: { type: 'Polygon', coordinates: [[[0, 0], [1, 0], [1, 1], [0, 0]]] }, scores: { mars: { missions: [{ score: value, coverage: .7, status }] } } });
test('missing values remain missing while measured zero is retained', () => {
  assert.equal(featureValue({ value: 0, status: 'measured' }), 0);
  assert.equal(featureValue({ value: 99, status: 'missing' }), null);
  assert.equal(featureValue({ value: null, status: 'derived' }), null);
  assert.equal(featureValue({ value: NaN, status: 'measured' }), null);
});
test('insufficient coverage never ranks above an eligible score', () => {
  const input = [site('insufficient', 99, 'insufficient'), site('low', 0), site('high', 80)];
  assert.deepEqual(rankSites(input, 'mars', 0).map((s) => s.id), ['high', 'low', 'insufficient']);
  assert.equal(input[0].id, 'insufficient');
  assert.equal(scoreFor(input[0], 'base', 0), null);
});
test('GeoJSON exports the selected comparison and does not disclose rejected scores', () => {
  const data = { sites: [site('a', 99, 'insufficient')], generatedAt: '2026-11-14' };
  assert.equal(buildGeoJSON(data, 'mars', 0).features[0].properties.score, null);
  const result = buildGeoJSON(data, 'mars', 0, () => ({ score: 20, coverage: 1, status: 'partial' }), 'terrain');
  assert.equal(result.features[0].properties.score, 20);
  assert.equal(result.features[0].properties.comparison, 'terrain');
  assert.equal(result.features[0].properties.body, 'earth');
});
test('CSV preserves empty missing fields and escapes spreadsheet formulas', () => {
  assert.equal(csvCell(null), '""');
  assert.equal(csvCell(-2.4), '"-2.4"');
  assert.equal(csvCell('=SUM(1,2)'), '"\'=SUM(1,2)"');
  assert.equal(csvCell('a"b'), '"a""b"');
});
