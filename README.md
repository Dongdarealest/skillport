# SkillPort

**Write a skill once. Run it on every AI.**

AI skills are fragmenting. A skill written for Claude does not run on Muse, Cursor, Codex or ChatGPT, because every platform invented its own file layout. SkillPort converts one Claude-style `SKILL.md` into ready-to-use packages for all of them, in one pass.

**Live demo:** https://dongdarealest.github.io/skillport/ — paste a `SKILL.md`, get all five packages in your browser. Nothing is uploaded; conversion runs entirely on your machine.

## What it does

| Source | Output |
|---|---|
| Claude `SKILL.md` | Claude `SKILL.md`, normalized |
| | Muse `SKILL.md` + `skill.yaml` |
| | Cursor `.cursor/rules/<name>.mdc` |
| | Codex `AGENTS.md` section |
| | ChatGPT `instructions.txt` |

Differences that cannot travel are reported, not silently dropped. For example, `allowed-tools` only exists on some platforms, so SkillPort flags it in the manifest instead of pretending it converted.

## Quick start

```bash
node src/skillport.mjs examples/clear-writing/SKILL.md dist
```

This writes the five converted packages into `dist/`, plus a `PORT.md` manifest listing every file produced and every warning.

No dependencies. Node 18 or newer.

## Why

Skills are becoming the unit of reusable AI know-how, the way packages became the unit of reusable code. But a skill locked to one vendor helps only that vendor's users. SkillPort treats the skill as the source of truth and each platform as a compile target, so authors can publish once and reach everyone.

## Status

Early prototype. The converter handles frontmatter (`name`, `description`, `license`, `allowed-tools`) and the markdown body. Folder assets such as scripts and references are copied for Claude and Muse targets and listed in the manifest for the rest.

## Contributing

Issues and pull requests are welcome. The most useful contributions are new targets: if your agent platform reads instructions from a file, open an issue with a real example of its format.

## License

MIT
