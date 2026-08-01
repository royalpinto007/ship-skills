---
name: set-up-ci
description: "When a repo has no CI or the user wants tests to run automatically. Triggers: 'set up CI', 'add GitHub Actions', 'run tests on PR', 'CI badge'. Adds a CI workflow that runs tests and lint on every push and PR, with a status badge."
metadata:
  version: 1.0.0
---

# Set Up CI

You make the tests run on every push and PR so "green" means something, and put a badge on the README so people can see it.

## Before you start

Read `.agents/ship.md` for the stack, package manager, and test command.

## Steps

1. **Add `.github/workflows/ci.yml`** (or the repo's CI provider): checkout, set up the runtime, install with locked deps, run lint then tests. Pin action versions.
2. **Keep it fast and honest:** cache deps, run on push and pull_request, fail on any test or lint failure.
3. **Add the status badge** to the top of the README so a visitor sees the build is green.
4. **Trigger a run** and confirm it passes. A red badge is worse than none.

## Done when

CI runs on push and PR, runs lint and tests, and the badge is live and green. Next: gate releases on it in `cut-a-release`.
