# Contributing

Issues and PRs welcome.

- Keep `SKILL.md` under ~500 lines / lean — move detail into `references/` instead of growing the main file.
- Don't add a specialist perspective, mode, or field "just in case" — every addition should fix a concrete failure seen in testing.
- If you change the council or research methodology, re-run the test scenarios described in `CHANGELOG.md` (or add new ones) and note the outcome in your PR description.
- No secrets, API keys, or personal data in commits.

## Repository naming: do not change casually

The repository is `decision` and its default branch is `council` on purpose. GitHub names the folder inside Code → Download ZIP `<repository>-<branch>`, so this pair yields exactly `decision-council/`, the skill's required folder name. Renaming the repository or the default branch changes that folder name and breaks one-click installs (verified by experiment on 2026-09-18). If you must rename either, re-download the ZIP afterwards and check its root folder.

`.gitattributes` uses `export-ignore` so that ZIP contains only the installable skill files. If you add a repo-only file (not part of the skill), add it there too.
