---
name: add-tests
description: "When a repo has no tests or thin coverage and the user wants a real test setup. Triggers: 'add tests', 'set up testing', 'no tests', 'test coverage'. Scaffolds the right test runner for the stack and writes first meaningful tests."
metadata:
  version: 1.0.0
---

# Add Tests

Untested code is not shippable. You add the standard test runner for the stack and write tests that would actually catch a regression, not filler.

## Before you start

Read `.agents/ship.md` for language and existing tooling.

## Steps

1. **Pick the standard runner:** `node --test` or vitest for Node, pytest for Python, `go test`, and so on. Prefer zero or few dependencies.
2. **Test behaviour, not lines.** Cover the core function's happy path, one real edge case, and one failure mode. A test that only asserts "it does not throw" is close to useless.
3. **Make it one command:** `npm test` / `pytest` / `make test`, and it must pass locally.
4. **Add tests that would have caught a real bug** you can imagine in this code.

## Done when

`npm test` (or the stack equivalent) runs a handful of meaningful tests and passes. Note the count in the commit. Next: wire it into CI with `set-up-ci`.
