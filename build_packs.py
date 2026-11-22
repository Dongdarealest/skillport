import os, shutil, subprocess, sys
ROOT = os.path.expanduser("~/workspace/skillport")
CLI = os.path.join(ROOT, "src/skillport.mjs")
PACKS = {
    "human-touch-pack": ("Human Touch Pack", "Three skills that make anything your AI produces look human-made, not generated."),
    "design-pack": ("Design Pack", "Three skills that give your AI a designer's eye."),
    "writing-pack": ("Writing Pack", "Three skills that make your AI write like a person."),
    "coding-pack": ("Coding Pack", "Three skills that make your AI review, commit and document like a senior engineer."),
    "shipsafe-pack": ("ShipSafe Pack", "Three skills that keep other people's instructions from hurting your machine, your accounts or your work."),
}
INSTALL = """## Install

One line, in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/main/install.sh | bash -s -- {pack} claude
```

Swap the last word for your AI: `claude`, `cursor` or `codex`. On Windows, use `install.ps1` from the repo root the same way. For ChatGPT, download the ZIP above and paste the files in `for-chatgpt/` into your custom GPT or project instructions. Using Claude on the web instead? Zip any single skill folder inside `for-claude/` and upload it under Settings, Skills.

By hand instead? Open the folder for your AI (`for-claude`, `for-cursor`, `for-codex`, `for-chatgpt`) and copy its contents where your AI keeps its skills or rules. The pack README in the repo explains each target in one line.

## License

MIT. Use them, change them, ship them.
"""
for pack, (title, blurb) in PACKS.items():
    pdir = os.path.join(ROOT, "packs", pack)
    for d in ["for-claude", "for-cursor", "for-codex", "for-chatgpt"]:
        shutil.rmtree(os.path.join(pdir, d), ignore_errors=True)
    skills = sorted(os.listdir(os.path.join(pdir, "skills")))
    codex_sections = []
    for skill in skills:
        tmp = f"/tmp/pack-{pack}-{skill}"
        shutil.rmtree(tmp, ignore_errors=True)
        subprocess.run(["node", CLI, os.path.join(pdir, "skills", skill, "SKILL.md"), tmp], check=True, capture_output=True)
        shutil.copytree(os.path.join(tmp, "claude", skill), os.path.join(pdir, "for-claude", skill))
        os.makedirs(os.path.join(pdir, "for-cursor", ".cursor", "rules"), exist_ok=True)
        shutil.copy(os.path.join(tmp, "cursor", ".cursor", "rules", f"{skill}.mdc"), os.path.join(pdir, "for-cursor", ".cursor", "rules", f"{skill}.mdc"))
        codex_sections.append(open(os.path.join(tmp, "codex", "AGENTS.md")).read())
        os.makedirs(os.path.join(pdir, "for-chatgpt"), exist_ok=True)
        shutil.copy(os.path.join(tmp, "chatgpt", "instructions.txt"), os.path.join(pdir, "for-chatgpt", f"{skill}.txt"))
    os.makedirs(os.path.join(pdir, "for-codex"), exist_ok=True)
    open(os.path.join(pdir, "for-codex", "AGENTS.md"), "w").write("\n---\n\n".join(codex_sections))
    def desc_of(skill):
        txt = open(os.path.join(pdir, "skills", skill, "SKILL.md")).read()
        for line in txt.splitlines():
            if line.startswith("description:"):
                d = line[len("description:"):].strip()
                return d.split(". ")[0].rstrip(".") + "."
        return ""
    listing = "\n".join(f"- **{s}**: {desc_of(s)}" for s in skills)
    open(os.path.join(pdir, "README.md"), "w").write(f"# {title}\n\n{blurb}\n\n## Inside\n\n{listing}\n\n{INSTALL.format(pack=pack)}")
    print(pack, "built:", skills)
print("PACKS BUILT")
