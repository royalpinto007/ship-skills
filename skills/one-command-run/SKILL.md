---
name: one-command-run
description: "When trying a project takes too many steps. Triggers: 'one command to run', 'quickstart', 'cold start', 'make it easy to try', 'npx/pipx/docker run'. Makes the project runnable in one command and verifies the stranger path."
metadata:
  version: 1.0.0
---

# One-Command Run

The gap between interested and trying it is every extra step. You collapse it to one command and verify the cold path.

## Before you start

Read `.agents/ship.md`.

## Steps

1. **Pick the one command** for the stack: `npx <name>` for a Node CLI, `pipx run <name>` for Python, `docker run ...` for a service, or a `make dev` or single script for an app.
2. **Remove hidden prerequisites:** if it needs a key or a running service, either provide a zero-config default or mock, or make the first run work without them and tell the user what to set for more.
3. **Test the stranger path:** from a fresh clone or a clean environment (or a container), run only the README's quickstart. Fix anything that breaks or needs undocumented steps.
4. Put that exact command at the top of the README.

## Done when

A person who has never seen the repo can run it with one copy-pasted command from the README, on a clean environment.
