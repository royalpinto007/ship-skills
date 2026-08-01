---
name: env-and-config
description: "When a project needs configuration or risks leaking secrets. Triggers: 'env variables', 'config', '.env.example', 'keep secrets out', 'twelve-factor'. Documents config, adds an env example, and keeps real secrets out of the repo."
metadata:
  version: 1.0.0
---

# Env and Config

You make configuration explicit and keep secrets out, so the app runs the same for everyone and leaks nothing.

## Before you start

Read `.agents/ship.md`.

## Steps

1. **List every config value** the app reads (keys, URLs, flags). Config belongs in the environment, not hardcoded.
2. **Add `.env.example`** with every variable and a placeholder value, and make sure `.env` is gitignored. Never commit real values.
3. **Fail loudly:** on startup, if a required variable is missing, error with a clear message naming the variable, do not run half-configured.
4. **Document** each variable in the README (what it is, required or optional, default).
5. Separate build-time from run-time config where relevant (public vs secret).

## Done when

`.env.example` covers every variable, `.env` is ignored, the app errors clearly on missing required config, and the README documents each one.
