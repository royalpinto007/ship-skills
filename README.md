# Ship Skills

[![ci](https://github.com/royalpinto007/ship-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/royalpinto007/ship-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Agent Skills that make a repo shippable**, from "works on my machine" to something a stranger can trust, run, and that you can release. The build-side counterpart to [distro-skills](https://github.com/royalpinto007/distro-skills): ship it well, then distribute it.

Works with [Claude Code](https://claude.com/claude-code), OpenAI Codex, Cursor, Windsurf, and any agent that supports the [Agent Skills spec](https://agentskills.io).

## How they fit

`ship-context` runs first and writes `.agents/ship.md` (stack, package manager, test tooling, publish target) that every other skill reads. `ship-checklist` audits the repo against a shippable bar and sequences the rest.

## The skills

**Foundation**
- **ship-context**: detect the stack and record it in `.agents/ship.md`; every skill reads it.
- **ship-checklist**: audit the repo against a shippable bar and sequence the rest.

**Quality**
- **add-tests**: scaffold the right test runner and write first meaningful tests.
- **set-up-ci**: run tests and lint on every push and PR, with a green badge.
- **lint-and-format**: add the standard formatter and linter, applied and enforced.
- **security-basics**: a disclosure policy, dependency and secret scanning, no committed secrets.

**Package and release**
- **package-for-npm**: a clean, npx-runnable npm package.
- **package-for-pypi**: a clean, pipx-runnable PyPI package.
- **cut-a-release**: semver bump, tag, release notes, publish.
- **write-a-changelog**: a Keep a Changelog file kept current.

**Repo health**
- **repo-hygiene-pass**: LICENSE, CONTRIBUTING, code of conduct, templates, gitignore.
- **readme-that-converts**: a README first screen that says what, why, and how in ten seconds.
- **license-and-legal**: pick and add the right license and notices.
- **env-and-config**: document config, keep secrets out, fail loudly on missing vars.
- **one-command-run**: make it runnable in one command and verify the stranger path.

## Install

Copy the skill folders you want from `skills/` into your agent's skills directory (for Claude Code, `~/.claude/skills/`), or point your agent at this repo. Each skill is a self-contained folder with a `SKILL.md`.

## License

[MIT](LICENSE)
