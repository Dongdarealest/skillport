# Guard Pack

Two skills that catch a Chrome Web Store rejection before the reviewer does.

## Inside

- **cws-appeal-draft**: Drafts a Chrome Web Store rejection appeal from the rejection email and the extension's evidence, in the three-part shape that wins appeals: acknowledgment, explanation, evidence.
- **cws-rejection-guard**: Audits a Chrome extension against the Chrome Web Store rejection patterns before submission, using Google's own notification IDs, and returns a verdict: BLOCKED, WARN or CLEAR.

## Install

One line, in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillport/v0.3.8/install.sh -o /tmp/skillport-install.sh
echo "79e232f30c44364e16778000ec93fe80b199c66845bfbe55c606118786e0f9a3  /tmp/skillport-install.sh" | sha256sum -c -
bash /tmp/skillport-install.sh guard-pack claude
```

Swap the last word for your AI: `claude`, `cursor` or `codex`. On Windows, use `install.ps1` from the repo root the same way. For ChatGPT, download the ZIP above and paste the files in `for-chatgpt/` into your custom GPT or project instructions. Using Claude on the web instead? Zip any single skill folder inside `for-claude/` and upload it under Settings, Skills.

By hand instead? Open the folder for your AI (`for-claude`, `for-cursor`, `for-codex`, `for-chatgpt`) and copy its contents where your AI keeps its skills or rules. The pack README in the repo explains each target in one line.

## License

MIT. Use them, change them, ship them.
