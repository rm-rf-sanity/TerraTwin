/** Reproducible project verification. Uses cached NASA data; never requires credentials. */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const cwd = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const venvPython = path.join(cwd, '.venv', process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python');
const python = process.env.TERRATWIN_PYTHON || (existsSync(venvPython) ? venvPython : 'python');
const checks = [
  [python, ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py']],
  [process.execPath, ['--test', 'tests/frontend.test.cjs']],
  [process.execPath, ['scripts/build_content.mjs', '--check']],
  [python, ['-m', 'analysis.run', '--offline']],
  [process.execPath, ['scripts/check_project.mjs']],
  ...['site/data.js', 'site/app.js', 'site/analysis-ui.js'].map(file => [process.execPath, ['--check', file]])
];
if (process.argv.includes('--browser')) checks.push([process.execPath, ['scripts/verify_site.mjs']]);
for (const [command, args] of checks) {
  const result = spawnSync(command, args, { cwd, stdio: 'inherit', windowsHide: true });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status || 1);
}
console.log('All requested software and data-integrity checks passed. Scientific model validation remains explicitly inconclusive.');
