import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const GUARD = join(HERE, '..', 'packs', 'guard-pack', 'skills', 'cws-rejection-guard', 'guard.mjs');
const FAILING = join(HERE, '..', 'packs', 'guard-pack', 'examples', 'failing-extension');
const PASSING = join(HERE, '..', 'packs', 'guard-pack', 'examples', 'passing-extension');
const DB = JSON.parse(readFileSync(join(HERE, '..', 'packs', 'guard-pack', 'skills', 'cws-rejection-guard', 'data', 'rejection-patterns.json'), 'utf8'));

test('pattern file: 30 patterns, unique ids, every pattern sourced and fixable', () => {
  assert.equal(DB.patterns.length, 30);
  const ids = new Set(DB.patterns.map((p) => p.id));
  assert.equal(ids.size, 30);
  for (const p of DB.patterns) {
    assert.ok(p.family && p.notification && p.policy && p.fix && p.source, p.id);
    assert.ok(['critical', 'high', 'medium'].includes(p.severity), p.id);
    assert.ok(Array.isArray(p.signals) && p.signals.length > 0, p.id);
  }
  assert.ok(DB.verified_on);
  assert.equal(typeof DB.stale_after_days, 'number');
});

test('failing sample: BLOCKED, exit 2, six findings with pattern ids', () => {
  const r = spawnSync('node', [GUARD, FAILING], { encoding: 'utf8' });
  assert.equal(r.status, 2);
  assert.match(r.stdout, /BLOCKED\. 2 critical, 4 high, 0 medium\./);
  for (const id of ['CWS-001', 'CWS-013', 'CWS-005', 'CWS-007', 'CWS-008', 'CWS-018']) {
    assert.ok(r.stdout.includes(id), 'missing finding ' + id);
  }
  assert.match(r.stdout, /What this scan cannot prove/);
});

test('passing sample: CLEAR, exit 0, with the honesty line', () => {
  const r = spawnSync('node', [GUARD, PASSING], { encoding: 'utf8' });
  assert.equal(r.status, 0);
  assert.match(r.stdout, /CLEAR\. 0 critical, 0 high, 0 medium\./);
  assert.match(r.stdout, /No mechanical findings\. That is not an approval\./);
});

test('json output parses and carries the verdict', () => {
  const r = spawnSync('node', [GUARD, '--json', PASSING], { encoding: 'utf8' });
  assert.equal(r.status, 0);
  const out = JSON.parse(r.stdout);
  assert.equal(out.verdict, 'CLEAR');
  assert.equal(out.findings.length, 0);
  assert.ok(out.manual_checks.length > 0);
});

test('no directory given: usage error, not a verdict', () => {
  const r = spawnSync('node', [GUARD], { encoding: 'utf8', cwd: '/' });
  assert.equal(r.status, 2);
  assert.match(r.stderr, /Usage: node guard\.mjs <extension-dir>/);
  assert.doesNotMatch(r.stdout, /BLOCKED|WARN|CLEAR/);
});
