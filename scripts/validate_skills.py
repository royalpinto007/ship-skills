#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md, the same bar `set-up-ci` asks for.

Each skill must have YAML frontmatter with a name, a description, and a
metadata.version, the name must match its folder, and a body must follow.
Exits non-zero on any problem so CI fails loudly.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
problems = []

folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
if not folders:
    problems.append("no skill folders found under skills/")

for folder in folders:
    md = folder / "SKILL.md"
    if not md.exists():
        problems.append(f"{folder.name}: missing SKILL.md")
        continue
    text = md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        problems.append(f"{folder.name}: no YAML frontmatter block")
        continue
    fm, body = m.group(1), m.group(2)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    ver = re.search(r"^\s*version:\s*(.+)$", fm, re.M)
    if not name:
        problems.append(f"{folder.name}: frontmatter missing 'name'")
    elif name.group(1).strip() != folder.name:
        problems.append(
            f"{folder.name}: name '{name.group(1).strip()}' does not match folder"
        )
    if not desc:
        problems.append(f"{folder.name}: frontmatter missing 'description'")
    if not ver:
        problems.append(f"{folder.name}: frontmatter missing 'metadata.version'")
    if len(body.strip()) < 80:
        problems.append(f"{folder.name}: body looks empty or too short")

if problems:
    print("SKILL validation failed:")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)

print(f"OK: {len(folders)} skills valid.")
