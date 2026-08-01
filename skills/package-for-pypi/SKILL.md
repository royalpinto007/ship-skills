---
name: package-for-pypi
description: "When a Python project should be publishable to PyPI. Triggers: 'publish to PyPI', 'make it a pip package', 'pyproject for publish', 'pipx-runnable'. Prepares pyproject.toml and metadata so the package builds, installs, and publishes cleanly."
metadata:
  version: 1.0.0
---

# Package for PyPI

You make a Python project a clean, installable package with a working entry point.

## Before you start

Read `.agents/ship.md`. Confirm the name is free on PyPI.

## Steps

1. **pyproject.toml:** `[project]` with name, version, description, readme, license, requires-python, dependencies, and `[project.scripts]` for a CLI entry point. Use a standard build backend (hatchling or setuptools).
2. **pipx-runnable:** the console script runs from a clean install (`pipx run <name>`, or `pip install` then the command).
3. **Build and check:** `python -m build`, then `twine check dist/*`. Fix any metadata warnings.
4. **Test the wheel** in a fresh venv before publishing.

## Done when

`python -m build` produces a wheel and sdist, `twine check` passes, and the entry point runs from a clean install. Then release via `cut-a-release`.
