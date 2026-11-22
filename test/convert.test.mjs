import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { parseSkill, convert, listAssets } from '../src/skillport.mjs';

const sample = readFileSync(new URL('../examples/clear-writing/SKILL.md', import.meta.url), 'utf8');

test('parses frontmatter and body', () => {
  const s = parseSkill(sample);
  assert.equal(s.name, 'clear-writing');
  assert.match(s.description, /read like a person/);
  assert.match(s.body, /# Clear Writing/);
});

test('converts to all five targets', () => {
  const { files } = convert(parseSkill(sample));
  const keys = Object.keys(files);
  assert.equal(keys.length, 6);
  assert.ok(files['muse/clear-writing/skill.yaml'].includes('include_in_prompt: false'));
  assert.ok(files['cursor/.cursor/rules/clear-writing.mdc'].includes('alwaysApply: false'));
  assert.ok(files['codex/AGENTS.md'].startsWith('## Skill: Clear Writing'));
  assert.ok(files['chatgpt/instructions.txt'].includes('When to use this skill:'));
});

test('warns about allowed-tools instead of dropping it', () => {
  const { warnings } = convert(parseSkill(sample));
  assert.ok(warnings.some(w => w.includes('allowed-tools')));
});

test('lists folder assets and skips SKILL.md itself', () => {
  const dir = new URL('../examples/csv-cleaner/', import.meta.url).pathname;
  const assets = listAssets(dir);
  assert.ok(assets.includes('scripts/clean.py'));
  assert.ok(assets.includes('references/field-notes.md'));
  assert.ok(!assets.includes('SKILL.md'));
});
