---
name: write-a-changelog
description: "When a repo has no changelog or an outdated one. Triggers: 'add a changelog', 'CHANGELOG.md', 'keep a changelog', 'release notes'. Adds a Keep a Changelog file and keeps an Unreleased section current."
metadata:
  version: 1.0.0
---

# Write a Changelog

A changelog tells users what changed and whether to upgrade. You add one in the standard format and keep it honest.

## Before you start

Read `.agents/ship.md`.

## Steps

1. **Use Keep a Changelog format:** a top `## [Unreleased]`, then released versions newest-first, each with `Added / Changed / Fixed / Removed` as needed.
2. **Seed from git history** if starting fresh, but write for humans: group by what a user cares about, not raw commits.
3. **Keep Unreleased current** as you work, so cutting a release is just renaming the section to the version and date.
4. Link versions to their diff or compare URLs.

## Done when

`CHANGELOG.md` exists in Keep a Changelog format with an Unreleased section, and `cut-a-release` can turn it into release notes.
