# SkillPort

![SkillPort: a quiet port at night, a lighthouse beam over the water](assets/banner.png)

![Release](https://img.shields.io/badge/release-v0.2.2-C9A35F) ![License](https://img.shields.io/badge/license-MIT-C9A35F) ![Platforms](https://img.shields.io/badge/platforms-Claude%20%C2%B7%20Muse%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20ChatGPT-C9A35F) ![Skills](https://img.shields.io/badge/skills-12-C9A35F)

**Your AI is running bare. Give it skills.**

Everyone is talking about AI skills: the add-ons that turn a general chatbot into a designer, a writer, a reviewer. But each platform keeps its own format, so a skill written for one AI will not install on another, and most people give up at the folder full of YAML.

SkillPort fixes that. It is a store of ready-made skill packs that work on **Claude, Muse, Cursor, Codex and ChatGPT**. Pick a pack, pick your AI, install in about a minute. Every pack is also a single ZIP download inside its folder. Every pack ships pre-converted for all five platforms. No converting, no file surgery.

**Live demo:** https://dongdarealest.github.io/skillport/

Same AI. Same brief. The only difference is a skill pack.

![Before and after: a landing page made by a bare AI, then remade with SkillPort](assets/before-after.png)

## Packs

| Pack | What your AI learns | Inside |
|---|---|---|
| [Human Touch Pack](packs/human-touch-pack/) | **Flagship.** Output that looks human-made, not generated | human-voice, anti-slop-design, make-it-real |
| [Design Pack](packs/design-pack/) | A designer's eye | interface-craft, hero-section, color-system |
| [Writing Pack](packs/writing-pack/) | To write like a person | clear-writing, headline-hook, warm-email |
| [Coding Pack](packs/coding-pack/) | A senior engineer's habits | code-review, commit-craft, readme-craft |

## Install

One line in your terminal installs a whole pack. Swap the pack name and the last word for your AI:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/main/install.sh | bash -s -- human-touch-pack claude
```

Packs: `human-touch-pack`, `design-pack`, `writing-pack`, `coding-pack`. AIs: `claude`, `muse`, `cursor`, `codex`. On Windows, `install.ps1` in this repo does the same job in PowerShell.

**ChatGPT:** it has no skills folder, so download the pack ZIP from its page above and paste the files in `for-chatgpt/` into your custom GPT or project instructions.

**By hand:** every pack is also a ZIP download on its own page. Unzip it, open the folder for your AI, and copy its contents where that AI keeps its skills or rules. Each pack's README says exactly where, in one line per platform.

## For authors: the converter

Writing your own skill? The fastest way is the [live demo](https://dongdarealest.github.io/skillport/): paste a Claude-style `SKILL.md`, get all five packages back, nothing to install.

In the terminal instead:

```bash
node src/skillport.mjs your-skill/SKILL.md dist
```

It produces all five packages plus a `PORT.md` manifest. Differences that cannot travel, such as `allowed-tools`, are reported in the manifest, never silently dropped. Folder assets (scripts, references) are copied for Claude and Muse targets and listed for the rest. No dependencies, Node 18 or newer.

Four worked examples live in [`examples/`](examples/), including a data skill with scripts and references.

## Why

Skills are becoming the unit of reusable AI know-how, the way packages became the unit of reusable code. A skill locked to one vendor helps only that vendor's users. SkillPort treats the skill as the source of truth and each platform as a compile target, so a good skill can reach everyone.

## Contributing

New packs and new skills are the most welcome contributions. Keep each skill small, original and genuinely usable, and convert it for all five targets with the build script before opening a pull request. New platform targets are welcome too: open an issue with a real example of the platform's format.

## License

MIT
