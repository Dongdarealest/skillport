---
name: csv-cleaner
description: Cleans a messy CSV file: trims whitespace, normalizes dates and numbers, drops exact duplicate rows and reports every change. Use when the user shares a spreadsheet or CSV export that needs tidying before analysis.
license: MIT
---

# CSV Cleaner

Clean the file with the bundled script, then report what changed. Never edit values by hand.

## Steps

1. Run `scripts/clean.py input.csv output.csv` from this skill folder.
2. Read the summary the script prints: rows in, rows out, duplicates dropped, columns normalized.
3. Spot check three changed rows against the original and show them to the user.
4. If a column cannot be normalized safely, leave it untouched and say why. See `references/field-notes.md` for the rules per column type.

## Output

The cleaned file, plus a short report: what changed, what was left alone, and anything that needs a human decision.
