---
name: cut-a-release
description: "When the user wants to ship a version. Triggers: 'cut a release', 'publish a version', 'tag a release', 'release it'. Bumps the version with semver, tags, writes release notes, and publishes to the registry."
metadata:
  version: 1.0.0
---

# Cut a Release

You turn the current state into a real, versioned release people can install.

## Before you start

Read `.agents/ship.md`. CI must be green and the changelog current (`write-a-changelog`).

## Steps

1. **Choose the version by semver:** patch for fixes, minor for backward-compatible features, major for breaking changes. From 0.x, breaking changes bump the minor.
2. **Bump + tag:** update the version in package.json or pyproject, commit "release: vX.Y.Z", tag `vX.Y.Z`.
3. **Release notes:** from the changelog's unreleased section, write a short GitHub release: the headline change, then bullets. Link the diff.
4. **Publish:** to npm or PyPI (see the package skills) and push the tag. For GitHub-only, the tag and release are the release.
5. **Verify:** install the published version fresh and confirm it runs.

## Done when

A `vX.Y.Z` tag and GitHub release exist, the package is live on the registry (if any), and a clean install of that version works.
