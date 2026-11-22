# Release notes

## v0.1.0 · 2026-11-22

The store opens.

- Three ready-made packs, nine original skills: Design Pack, Writing Pack, Coding Pack.
- Every pack pre-converted for Claude, Muse, Cursor, Codex and ChatGPT, with per-platform install instructions.
- The converter for authors: one Claude-style `SKILL.md` compiles to all five platforms, with a manifest that reports anything that cannot travel.
- Folder assets (scripts, references) are copied for Claude and Muse targets and listed in the manifest for the rest.
- Test suite for the converter: `node --test test/convert.test.mjs`.
