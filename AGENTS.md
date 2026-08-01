# Ship Skills, agent guide

These are Agent Skills for **shipping** a repo: getting it from "works locally" to trustworthy,
installable, and released. The build-side counterpart to distro-skills (which handles distribution
after you ship).

Run `ship-context` first on any repo; it writes `.agents/ship.md` (stack, package manager, test
tooling, publish target) that every other skill reads. Then `ship-checklist` audits the repo and
tells you which skills to run, in order.

Principle every skill inherits: a stranger should be able to trust it, run it in one command, and
see it is maintained. Never ship secrets, never overclaim in the README, and make "green" mean
the tests actually ran.
