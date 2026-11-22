# ShipSafe Pack

Three skills that keep other people's instructions from hurting your machine, your accounts or your work.

## Inside

- **backup-before-change**: Makes a restore point of your skills, configs and dotfiles before an AI agent edits them, and rolls back cleanly when an edit goes wrong.
- **secrets-out**: Scrubs credentials, tokens, personal data and private paths out of text and files before they are pasted into an AI chat, committed to a repo or sent to anyone.
- **vet-before-install**: Vets a third-party skill or prompt pack before it goes anywhere near your AI: an automated audit first, then the human checks that catch what scanners miss.

## Install

One line, in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/main/install.sh | bash -s -- shipsafe-pack claude
```

Swap the last word for your AI: `claude`, `cursor` or `codex`. On Windows, use `install.ps1` from the repo root the same way. For ChatGPT, download the ZIP above and paste the files in `for-chatgpt/` into your custom GPT or project instructions. Using Claude on the web instead? Zip any single skill folder inside `for-claude/` and upload it under Settings, Skills.

By hand instead? Open the folder for your AI (`for-claude`, `for-cursor`, `for-codex`, `for-chatgpt`) and copy its contents where your AI keeps its skills or rules. The pack README in the repo explains each target in one line.

## License

MIT. Use them, change them, ship them.
