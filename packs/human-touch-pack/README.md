# Human Touch Pack

Three skills that make anything your AI produces look human-made, not generated.

## Inside

- **anti-slop-design**: Designs interfaces and pages that do not look AI-generated: no purple gradient hero, no identical card grid, no default typeface at default sizes.
- **human-voice**: Rewrites AI-generated text so it reads like a specific person wrote it: no filler openings, no buzzwords, no identical sentence rhythm.
- **make-it-real**: Forces any AI output to be specific instead of generic: real numbers, named examples, concrete details and a stated point of view.

## Install

One line, in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/v0.3.8/install.sh -o /tmp/skillport-install.sh
echo "79e232f30c44364e16778000ec93fe80b199c66845bfbe55c606118786e0f9a3  /tmp/skillport-install.sh" | sha256sum -c -
bash /tmp/skillport-install.sh human-touch-pack claude
```

Swap the last word for your AI: `claude`, `cursor` or `codex`. On Windows, use `install.ps1` from the repo root the same way. For ChatGPT, download the ZIP above and paste the files in `for-chatgpt/` into your custom GPT or project instructions. Using Claude on the web instead? Zip any single skill folder inside `for-claude/` and upload it under Settings, Skills.

By hand instead? Open the folder for your AI (`for-claude`, `for-cursor`, `for-codex`, `for-chatgpt`) and copy its contents where your AI keeps its skills or rules. The pack README in the repo explains each target in one line.

## License

MIT. Use them, change them, ship them.
