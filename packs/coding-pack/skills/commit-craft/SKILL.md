---
name: commit-craft
description: Writes commit messages and pull request descriptions that explain why a change exists, not only what it does. Use when the user is committing work, opening a pull request, or cleaning up a branch before review.
license: MIT
---

# Commit Craft

The diff already says what changed. The message exists to say why, and what to watch for.

## Rules

1. Subject line: imperative, under 60 characters, no period. "Fix login timeout", not "Fixed some stuff".
2. Body: the reason for the change, the alternatives considered when they matter, and anything risky.
3. One concern per commit. If the message needs the word "and" twice, split the commit.
4. Name the test that proves it works, or say plainly that there is none.
5. Never write "WIP", "fix", or "updates" as a whole message. Future readers include you in six months.

## Output

The subject line, then the body in short paragraphs. For a pull request, add a section on how a reviewer can verify the change.
