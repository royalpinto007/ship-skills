---
name: license-and-legal
description: "When a repo has no license or unclear terms. Triggers: 'add a license', 'which license', 'license and legal', 'can people use this'. Helps pick and add the right license plus any third-party notices."
metadata:
  version: 1.0.0
---

# License and Legal

Code with no license is all-rights-reserved by default, nobody can legally use it. You fix that deliberately.

## Before you start

Read `.agents/ship.md` and ask the user's intent: maximum adoption, or copyleft.

## Steps

1. **Pick by intent:** MIT or Apache-2.0 for permissive (Apache adds a patent grant), GPL or AGPL for copyleft, CC0 for public domain (docs, lists). If unsure and the goal is adoption, MIT is the safe default.
2. **Add `LICENSE`** with the correct year and author, and set the `license` field in package metadata to match.
3. **Third-party:** if you vendored or heavily adapted others' code, keep their notices and add a NOTICE or credits section.
4. State the license in the README.

## Done when

A `LICENSE` file exists, the package metadata matches, and any third-party obligations are honoured.
