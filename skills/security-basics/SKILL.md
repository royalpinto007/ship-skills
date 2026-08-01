---
name: security-basics
description: "When a repo is about to be public or the user wants baseline security. Triggers: 'security', 'SECURITY.md', 'dependabot', 'am I leaking secrets', 'security basics'. Adds a disclosure policy, dependency and secret scanning, and checks nothing sensitive is committed."
metadata:
  version: 1.0.0
---

# Security Basics

Baseline hygiene so a public repo does not embarrass you. Not a full audit, the essentials.

## Before you start

Read `.agents/ship.md`.

## Steps

1. **Check for committed secrets** (grep history for keys and tokens, scan with a tool). If found, rotate them and remove from history; a `.env` in git is a leak even if later deleted.
2. **Add `.env.example`** with placeholder keys and no real values; ensure `.env` is gitignored. See `env-and-config`.
3. **Add `SECURITY.md`** with how to report a vulnerability (an email or a private advisory) and a supported-versions line.
4. **Turn on scanning:** Dependabot or renovate for deps, secret scanning, and private vulnerability reporting on GitHub.
5. **Least privilege:** CI tokens and any bot use the minimum scope.

## Done when

No secrets in the repo or history, `.env.example` present, `SECURITY.md` exists, and dependency and secret scanning are on.
