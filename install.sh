#!/usr/bin/env bash
# SkillPort one-line installer.
# Usage: install.sh <pack> <ai>
#   pack: human-touch-pack | design-pack | writing-pack | coding-pack
#   ai:   claude | muse | cursor | codex | chatgpt
set -euo pipefail
PACK="${1:?Usage: install.sh <pack> <ai>}"
AI="${2:?Usage: install.sh <pack> <ai>}"
BASE="https://github.com/Dongdarealest/skillport/raw/main/packs/$PACK"
TMP="$(mktemp -d)"
echo "Downloading $PACK..."
curl -fsSL "$BASE/$PACK.zip" -o "$TMP/pack.zip"
unzip -q "$TMP/pack.zip" -d "$TMP/x"
SRC="$TMP/x/$PACK/for-$AI"
[ -d "$SRC" ] || { echo "Unknown AI target: $AI (use claude, muse, cursor, codex or chatgpt)"; exit 1; }
case "$AI" in
  claude)
    DEST="$HOME/.claude/skills"; mkdir -p "$DEST"; cp -R "$SRC"/* "$DEST"/
    echo "Done. $PACK is installed for Claude in $DEST" ;;
  muse)
    DEST="$HOME/workspace/custom-skills"; mkdir -p "$DEST"; cp -R "$SRC"/* "$DEST"/
    echo "Done. $PACK is installed for Muse in $DEST" ;;
  cursor)
    DEST="$PWD/.cursor/rules"; mkdir -p "$DEST"; cp "$SRC/.cursor/rules"/*.mdc "$DEST"/
    echo "Done. $PACK rules are in $DEST" ;;
  codex)
    touch "$PWD/AGENTS.md"; printf "\n" >> "$PWD/AGENTS.md"; cat "$SRC/AGENTS.md" >> "$PWD/AGENTS.md"
    echo "Done. $PACK was added to $PWD/AGENTS.md" ;;
  chatgpt)
    echo "ChatGPT installs by pasting. Open these files and paste each one into your custom GPT or project instructions:"
    ls "$SRC" ;;
esac
