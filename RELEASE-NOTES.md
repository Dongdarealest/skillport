# Release notes

## v0.1.0 · 2026-11-22

The store opens.

- Three ready-made packs, nine original skills: Design Pack, Writing Pack, Coding Pack.
- Every pack pre-converted for Claude, Muse, Cursor, Codex and ChatGPT, with per-platform install instructions.
- The converter for authors: one Claude-style `SKILL.md` compiles to all five platforms, with a manifest that reports anything that cannot travel.
- Folder assets (scripts, references) are copied for Claude and Muse targets and listed in the manifest for the rest.
- Test suite for the converter: `node --test test/convert.test.mjs`.

## v0.2.0 · 2026-11-22

The flagship arrives.

- Human Touch Pack: human-voice, anti-slop-design and make-it-real. Skills that strip the generated smell out of text, interfaces and ideas.
- Before and after demo at the top of the README and the site: the same landing page brief, made by a bare AI and then with a SkillPort pack.
- Four packs, twelve skills, all pre-converted for Claude, Muse, Cursor, Codex and ChatGPT.

## v0.2.2 · 2026-11-22

Presence and proof, improved.

- A cinematic banner now opens the README: the SkillPort lighthouse, and the line "Your AI is running bare. Give it skills."
- The after side of the demo was rebuilt around a real product window, so the difference reads at a glance.
- Every pack is a one-click ZIP download from its own page, and pack pages now describe each skill in one line.
- One-line install: a small installer script downloads a pack and places every skill in the right folder for Claude, Muse, Cursor or Codex.
- The converter is a proper Node package (package.json, bin entry), and a CI workflow runs the tests and verifies every pack ships all five targets on every push.
