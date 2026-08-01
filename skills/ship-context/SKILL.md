---
name: ship-context
description: "When starting to make a repo shippable, or before any other ship-skill. Triggers: 'ship this', 'make it production ready', 'prepare to release', 'ship-context'. Detects the repo's stack and records it in .agents/ship.md so every other ship-skill reuses it."
metadata:
  version: 1.0.0
---

# Ship Context

The foundation skill. You detect what this repo is and how it ships, and write it to `.agents/ship.md` so every other ship-skill reads it once instead of re-detecting.

## What to detect

Inspect the repo, do not guess:
- Language and runtime (package.json, pyproject.toml, go.mod, Cargo.toml).
- Package manager and lockfile (npm/pnpm/yarn, pip/uv/poetry).
- Test runner and lint/format tools already present.
- Publish target: npm, PyPI, a container image, a hosted app, or GitHub only.
- CI provider (.github/workflows, .gitlab-ci.yml) or none.
- The one-command way a stranger runs it (npx, pipx, docker), if any.

## Write .agents/ship.md

Record the above plus: project name, one-line what-it-does, license (or "unlicensed, pick one"), and the intended audience. Keep it short and factual; other skills read it verbatim.

## Done when

`.agents/ship.md` exists and accurately describes stack, package manager, test tooling, and publish target. If anything is unknown, write "unknown, decide in <skill>" rather than guessing.
