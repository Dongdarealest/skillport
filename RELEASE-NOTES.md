# Release notes

## v0.2.9

The comparison is now one page in two executions everywhere, site included: the after panel on the website mirrors the before panel slot for slot, centered hero, pill buttons, three icon cards, with the craft carried by typography, palette, and copy.

## v0.2.8

The after panel earns its place now. The earlier version mistook empty for calm: the redesigned after is a proper editorial page, warm paper, a large serif headline with one gold stroke, and a numbered index instead of icon cards. Next to it, the before reads exactly like what it is, a template.

## v0.2.7

The comparison is honest now, and the site is leaner.

- The before and after demo is rebuilt as one page in two executions: the same Fieldnotes landing page, slot for slot, once as generic AI output and once with the Human Touch Pack loaded. Same nav, same headline slot, same feature row, only the craft differs.
- The share-card builder is removed from the site. It asked visitors to do work that earned them nothing.
- A Support section joins the README, and the funding file now points at the live Ko-fi page.

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

## v0.2.3 · 2026-11-22

The README, rebuilt the way the big projects do it.

- Full restructure after studying the leading skill projects: table of contents, a short "What is a skill?" explainer for newcomers, a "How it works" story, per-platform install sections with exact commands, a complete catalog of all twelve skills, updating instructions, a philosophy section, and a community section.
- A fill-in skill template in `template/` so anyone can author a skill in the house format.
- GitHub Discussions enabled for questions, ideas and before-and-after shares.

## v0.2.4 · 2026-11-22

An honest demo.

- The before/after comparison now uses one product on both sides: Fieldnotes, the same brief and the same sections, executed bare and then with the Human Touch Pack. Two different products proved nothing; one product, transformed, proves everything.
- The share-card generator was removed from the site. A card nobody asked for is not a feature.

## v0.2.5 · 2026-11-22

A README that looks designed, not typed.

- New masthead: a centered serif lockup over the harbor art replaces the plain title and banner, readable at any screen width.
- Badges restyled flat and dark to match the house palette, centered as one row.
- The contents list is gone; a single centered nav row does its job.
- The catalog is now tables, one per pack.

## v0.2.6 · 2026-11-22

- The Muse target is removed from the packs. Its package was a duplicate of the Claude one, and a store should not ship placeholders. The converter still supports the format for anyone who needs it.
- Designed masthead and social image updated to the four real targets: Claude, Cursor, Codex, ChatGPT.
