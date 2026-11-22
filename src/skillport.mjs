#!/usr/bin/env node
// SkillPort: write a skill once, run it on every AI agent.
// Converts a Claude-style SKILL.md into ready-to-use packages for
// Muse, Cursor, Codex (AGENTS.md) and ChatGPT (custom instructions).
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

export function parseSkill(source) {
  const fm = {};
  let body = source;
  const m = source.match(/^---\n([\s\S]*?)\n---\n?/);
  if (m) {
    body = source.slice(m[0].length);
    let currentKey = null;
    for (const line of m[1].split('\n')) {
      const kv = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
      if (kv && !line.startsWith(' ')) {
        currentKey = kv[1];
        fm[currentKey] = kv[2].trim();
      } else if (currentKey && line.trim()) {
        fm[currentKey] += ' ' + line.trim();
      }
    }
  }
  const name = (fm.name || 'my-skill').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  return { name, description: fm.description || '', license: fm.license || '', allowedTools: fm['allowed-tools'] || '', meta: fm, body: body.trim() };
}

const titleOf = (name) => name.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

export function convert(skill) {
  const { name, description, license, allowedTools, body } = skill;
  const warnings = [];
  if (allowedTools) warnings.push(`allowed-tools (${allowedTools}) only exists on Claude and Muse targets; other targets receive the instructions without tool gating.`);
  if (!description) warnings.push('No description found in frontmatter; targets that trigger on description will need one written by hand.');

  const claude = `---\nname: ${name}\ndescription: ${description}\n${license ? `license: ${license}\n` : ''}${allowedTools ? `allowed-tools: ${allowedTools}\n` : ''}---\n\n${body}\n`;

  const museSkill = body + '\n';
  const museYaml = `name: ${name}\ntitle: "${titleOf(name)}"\ndescription: "${description.replace(/"/g, '\\"')}"\ncategory: "Work and knowledge"\ninclude_in_prompt: false\n`;

  const cursor = `---\ndescription: ${description}\nglobs:\nalwaysApply: false\n---\n\n${body}\n`;

  const codex = `## Skill: ${titleOf(name)}\n\n> ${description}\n\n${body}\n`;

  const chatgpt = `${titleOf(name).toUpperCase()}\n\nWhen to use this skill: ${description}\n\n${body}\n`;

  return {
    files: {
      [`claude/${name}/SKILL.md`]: claude,
      [`muse/${name}/SKILL.md`]: museSkill,
      [`muse/${name}/skill.yaml`]: museYaml,
      [`cursor/.cursor/rules/${name}.mdc`]: cursor,
      [`codex/AGENTS.md`]: codex,
      [`chatgpt/instructions.txt`]: chatgpt,
    },
    warnings,
  };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [input, outDir = 'dist'] = process.argv.slice(2);
  if (!input) { console.error('Usage: node skillport.mjs <SKILL.md> [outDir]'); process.exit(1); }
  const skill = parseSkill(readFileSync(input, 'utf8'));
  const { files, warnings } = convert(skill);
  for (const [rel, content] of Object.entries(files)) {
    const dest = join(outDir, rel);
    mkdirSync(join(dest, '..'), { recursive: true });
    writeFileSync(dest, content);
    console.log('wrote', dest);
  }
  const manifest = { skill: skill.name, targets: Object.keys(files), warnings, convertedAt: new Date().toISOString() };
  writeFileSync(join(outDir, 'PORT.md'), `# SkillPort manifest\n\nSkill: ${skill.name}\nTargets: ${Object.keys(files).join(', ')}\n\nWarnings:\n${warnings.map(w => '- ' + w).join('\n') || '- none'}\n`);
  console.log('warnings:', warnings.length ? warnings.join(' | ') : 'none');
}
