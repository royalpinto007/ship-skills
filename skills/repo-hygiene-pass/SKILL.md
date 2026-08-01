---
name: repo-hygiene-pass
description: "When a repo is missing the standard github-ready files. Triggers: 'repo hygiene', 'add contributing/license/templates', 'make it github-ready', 'issue and PR templates'. Adds LICENSE, CONTRIBUTING, code of conduct, issue and PR templates, gitignore, and editorconfig."
metadata:
  version: 1.0.0
---

# Repo Hygiene Pass

You add the files that make a repo read as maintained, not a dump. One pass, the full github-ready set.

## Before you start

Read `.agents/ship.md`.

## The set

- **LICENSE** (see `license-and-legal`) so people know they can use it.
- **CONTRIBUTING.md:** how to set up, test, and open a PR for this specific repo.
- **CODE_OF_CONDUCT.md:** the Contributor Covenant, with a real contact.
- **.github/ISSUE_TEMPLATE** and **PULL_REQUEST_TEMPLATE.md:** short, so reports are useful.
- **.gitignore** for the stack (no node_modules, build output, or secrets tracked), and **.editorconfig** for consistent whitespace.
- **README** links to CONTRIBUTING and shows how to run tests.

## Rules

Tailor each to the repo, do not paste generic boilerplate. A CONTRIBUTING that says "run npm test" for a Python repo signals the opposite of care.

## Done when

All the files above exist, are repo-specific, and are linked from the README where relevant.
