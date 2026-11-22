# Examples

Four small, original skills that show what SkillPort converts. Each is a real, usable skill, not a fixture.

| Skill | Shows |
|---|---|
| [clear-writing](clear-writing/SKILL.md) | The basic shape: frontmatter plus a short body |
| [interface-craft](interface-craft/SKILL.md) | A long, trigger-rich description |
| [code-review](code-review/SKILL.md) | `allowed-tools`, which only some targets support, so SkillPort flags it in the manifest |
| [csv-cleaner](csv-cleaner/SKILL.md) | A skill with assets: the `scripts/` and `references/` folders are copied for Claude and Muse targets and listed in the manifest for the rest |

Convert any of them:

```bash
node src/skillport.mjs examples/csv-cleaner/SKILL.md dist
```
