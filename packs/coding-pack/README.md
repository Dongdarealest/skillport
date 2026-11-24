# Coding Pack

Three skills that make your AI review, commit and document like a senior engineer.

## Inside

- **code-review**: Reviews a diff or a pull request for correctness first and style last.
- **commit-craft**: Writes commit messages and pull request descriptions that explain why a change exists, not only what it does.
- **readme-craft**: Writes or rewrites a project README so a stranger understands what the project is, why it exists and how to run it within one screen.

## Install

One line, in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/v0.3.8/install.sh -o /tmp/skillport-install.sh
echo "79e232f30c44364e16778000ec93fe80b199c66845bfbe55c606118786e0f9a3  /tmp/skillport-install.sh" | sha256sum -c -
bash /tmp/skillport-install.sh coding-pack claude
```

Swap the last word for your AI: `claude`, `cursor` or `codex`. On Windows, use `install.ps1` from the repo root the same way. For ChatGPT, download the ZIP above and paste the files in `for-chatgpt/` into your custom GPT or project instructions. Using Claude on the web instead? Zip any single skill folder inside `for-claude/` and upload it under Settings, Skills.

By hand instead? Open the folder for your AI (`for-claude`, `for-cursor`, `for-codex`, `for-chatgpt`) and copy its contents where your AI keeps its skills or rules. The pack README in the repo explains each target in one line.

## License

MIT. Use them, change them, ship them.
