## Skill: Code Review

> Reviews a diff or a pull request for correctness first and style last. Use when the user asks for a code review, a second pair of eyes on a change, or a pre-merge check.

# Code Review

Read the whole diff before commenting on any line.

## What to look for, in order

1. Correctness: does the change do what its description claims? Check the edge cases the author did not mention.
2. Data safety: migrations, deletions and writes that cannot be undone get a second look and a rollback note.
3. Tests: every behavior change needs a test that would fail without it.
4. Clarity: names and structure a new reader can follow without the author in the room.
5. Style: only what the linter cannot catch. Never block a merge on taste.

## Output

Verdict first: approve, approve with notes, or request changes. Then findings grouped by the order above, each with file, line and a concrete fix.

---

## Skill: Commit Craft

> Writes commit messages and pull request descriptions that explain why a change exists, not only what it does. Use when the user is committing work, opening a pull request, or cleaning up a branch before review.

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

---

## Skill: Readme Craft

> Writes or rewrites a project README so a stranger understands what the project is, why it exists and how to run it within one screen. Use when the user is launching a repo, open sourcing a tool, or fixing a README nobody reads.

# README Craft

A README is a landing page for people who arrive skeptical and busy.

## Structure

1. Name and one line: what it is, in the words a user would search for.
2. One screenshot, demo link or example output, above the fold. Proof before promises.
3. Why it exists: the problem, in two lines, and what is different about this answer.
4. Quick start: the shortest path from clone to running, copy-pasteable, tested.
5. Examples of real use, not a feature list.
6. Contributing and license, one line each, at the end.

## Rules

- Cut every badge that does not help a decision.
- If a section has not changed in a year, it is probably wrong. Date or delete volatile claims.
- Write for the second reader: the one deciding whether to trust this project with their time.

## Output

The full README in that structure, ready to commit.
