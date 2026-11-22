import os, shutil, subprocess, sys
ROOT = os.path.expanduser("~/workspace/skillport")
CLI = os.path.join(ROOT, "src/skillport.mjs")
PACKS = {
    "human-touch-pack": ("Human Touch Pack", "Three skills that make anything your AI produces look human-made, not generated."),
    "design-pack": ("Design Pack", "Three skills that give your AI a designer's eye."),
    "writing-pack": ("Writing Pack", "Three skills that make your AI write like a person."),
    "coding-pack": ("Coding Pack", "Three skills that make your AI review, commit and document like a senior engineer."),
}
INSTALL = """## Install

Pick your AI, then follow its line. Every folder below is ready to use as-is.

- **Claude:** copy each folder in `for-claude/` into `~/.claude/skills/` (or your project's `.claude/skills/`).
- **Muse:** copy each folder in `for-muse/` into `~/workspace/custom-skills/`.
- **Cursor:** copy the files in `for-cursor/.cursor/rules/` into your project's `.cursor/rules/`.
- **Codex:** append the contents of `for-codex/AGENTS.md` to your project's `AGENTS.md`.
- **ChatGPT:** paste each file in `for-chatgpt/` into a custom GPT's instructions, or into project instructions.

## License

MIT. Use them, change them, ship them.
"""
for pack, (title, blurb) in PACKS.items():
    pdir = os.path.join(ROOT, "packs", pack)
    for d in ["for-claude", "for-muse", "for-cursor", "for-codex", "for-chatgpt"]:
        shutil.rmtree(os.path.join(pdir, d), ignore_errors=True)
    skills = sorted(os.listdir(os.path.join(pdir, "skills")))
    codex_sections = []
    for skill in skills:
        tmp = f"/tmp/pack-{pack}-{skill}"
        shutil.rmtree(tmp, ignore_errors=True)
        subprocess.run(["node", CLI, os.path.join(pdir, "skills", skill, "SKILL.md"), tmp], check=True, capture_output=True)
        shutil.copytree(os.path.join(tmp, "claude", skill), os.path.join(pdir, "for-claude", skill))
        shutil.copytree(os.path.join(tmp, "muse", skill), os.path.join(pdir, "for-muse", skill))
        os.makedirs(os.path.join(pdir, "for-cursor", ".cursor", "rules"), exist_ok=True)
        shutil.copy(os.path.join(tmp, "cursor", ".cursor", "rules", f"{skill}.mdc"), os.path.join(pdir, "for-cursor", ".cursor", "rules", f"{skill}.mdc"))
        codex_sections.append(open(os.path.join(tmp, "codex", "AGENTS.md")).read())
        os.makedirs(os.path.join(pdir, "for-chatgpt"), exist_ok=True)
        shutil.copy(os.path.join(tmp, "chatgpt", "instructions.txt"), os.path.join(pdir, "for-chatgpt", f"{skill}.txt"))
    os.makedirs(os.path.join(pdir, "for-codex"), exist_ok=True)
    open(os.path.join(pdir, "for-codex", "AGENTS.md"), "w").write("\n---\n\n".join(codex_sections))
    listing = "\n".join(f"- **{s}**" for s in skills)
    open(os.path.join(pdir, "README.md"), "w").write(f"# {title}\n\n{blurb}\n\n## Inside\n\n{listing}\n\n{INSTALL}")
    print(pack, "built:", skills)
print("PACKS BUILT")
