---
name: lint-and-format
description: "When a repo has inconsistent style or no linter or formatter. Triggers: 'add linting', 'set up prettier/eslint/ruff', 'format the code', 'style config'. Adds the standard linter and formatter for the stack with config and a check."
metadata:
  version: 1.0.0
---

# Lint and Format

Consistent code reads as cared-for. You add the stack's standard formatter and linter, apply them once, and wire a check.

## Before you start

Read `.agents/ship.md`.

## Steps

1. **Add the standard tools:** Prettier + ESLint for JS/TS, Ruff (or Black + Ruff) for Python, gofmt + golangci-lint for Go. Start from the recommended config, do not invent a bespoke one.
2. **Apply once** across the repo in a single "style: format" commit, so real changes are not buried in reformatting later.
3. **Add a check:** a `lint` script and a CI step (or a pre-commit hook) that fails on violations.
4. Keep rules pragmatic. A linter everyone disables is worse than a lean one that stays on.

## Done when

`npm run lint` (or equivalent) passes, formatting is applied repo-wide in its own commit, and CI or a hook enforces it.
