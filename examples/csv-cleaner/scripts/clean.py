#!/usr/bin/env python3
"""Trim whitespace, drop exact duplicate rows, report the changes."""
import csv, sys

src, dst = sys.argv[1], sys.argv[2]
with open(src, newline="", encoding="utf-8") as f:
    rows = [[c.strip() for c in row] for row in csv.reader(f)]
seen, out = set(), []
for row in rows:
    key = tuple(row)
    if key not in seen:
        seen.add(key)
        out.append(row)
with open(dst, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
print(f"rows in: {len(rows)}  rows out: {len(out)}  duplicates dropped: {len(rows) - len(out)}")
