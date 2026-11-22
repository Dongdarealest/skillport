# Contributing

Thanks for helping make skills portable.

## Adding a target

1. Find a real instruction file from the platform you want to support.
2. Add a converter for it in `src/skillport.mjs`, following the existing targets.
3. Run the example below and check the output reads as a finished file, not a template.

```bash
node src/skillport.mjs examples/clear-writing/SKILL.md dist
```

## Ground rules

- Report what cannot be converted. Never drop a field silently.
- Keep the tool dependency-free.
- Every output must be usable as-is on its platform.
