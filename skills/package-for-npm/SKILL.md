---
name: package-for-npm
description: "When a Node project should be publishable to npm. Triggers: 'publish to npm', 'make it an npm package', 'npx-runnable', 'package.json for publish'. Prepares package.json and metadata so the package installs, runs, and publishes cleanly."
metadata:
  version: 1.0.0
---

# Package for npm

You make a Node project a clean, installable package that runs with one command.

## Before you start

Read `.agents/ship.md`. Confirm the name is free (`npm view <name>`); if taken, scope it (`@user/name`).

## Steps

1. **package.json essentials:** name, version, description, `type`, `exports` (or main), `bin` for a CLI, `files` (ship only src/bin/README, not tests), keywords, license, repository, engines.
2. **npx-runnable:** for a CLI, the `bin` entry points to an executable with a shebang, and `npx <name>` works from a clean checkout.
3. **Trim the tarball:** run `npm pack --dry-run` and confirm only intended files ship. No node_modules, no secrets, no fixtures.
4. **Publish dry-run:** `npm publish --dry-run`. Fix warnings. Publish with `--access public` for a scoped package.

## Done when

`npm pack --dry-run` shows a lean file list, `npx <name>` works, and a dry-run publish is clean. Then release via `cut-a-release`.
