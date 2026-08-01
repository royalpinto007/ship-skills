---
name: ship-checklist
description: "When the user wants to know what is left before a repo is shippable, or wants the ship sequence. Triggers: 'is this ready to ship', 'ship checklist', 'what is missing before release'. Audits the repo against a shippable bar and sequences the other ship-skills."
metadata:
  version: 1.0.0
---

# Ship Checklist

You turn "it works on my machine" into "a stranger can trust and run it." Audit, then sequence.

## Before you start

Read `.agents/ship.md` (run `ship-context` first if it is missing).

## The bar (audit each, honestly)

- **Runs cold:** a stranger installs and runs it from the README in under 5 minutes. -> `one-command-run`
- **Tested + CI green:** there are tests and CI runs them on every push. -> `add-tests`, `set-up-ci`
- **Clean:** lint and format are set up and passing. -> `lint-and-format`
- **Documented:** the README says what, why, and how in the first screen. -> `readme-that-converts`
- **Licensed + github-ready:** LICENSE, CONTRIBUTING, code of conduct, templates. -> `repo-hygiene-pass`, `license-and-legal`
- **Safe:** no secrets committed, config documented, basic scanning on. -> `env-and-config`, `security-basics`
- **Releasable:** versioned, changelog, a real release. -> `cut-a-release`, `write-a-changelog`, `package-for-npm`/`package-for-pypi`

## Output

A short checklist with each item marked done or missing, and the ordered list of ship-skills to run to close the gaps. Do not fix everything at once; propose the sequence and start at the top.
