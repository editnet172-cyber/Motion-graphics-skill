#!/usr/bin/env python3
"""Lightweight structural checks for the Motion Ad Director Pro repository.

This validates repository structure and documentation references only.
It does not validate Claude Code runtime discovery or the visual quality of a video.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
WARNINGS = []

def require(condition, message):
    if not condition:
        ERRORS.append(message)

skill_path = ROOT / "SKILL.md"
readme_path = ROOT / "README.md"
require(skill_path.is_file(), "Missing SKILL.md")
require(readme_path.is_file(), "Missing README.md")

if skill_path.exists():
    content = skill_path.read_text(encoding="utf-8")
    require(content.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    blocks = re.findall(r"\A---\n(.*?)\n---\n", content, flags=re.S)
    require(bool(blocks), "Could not parse opening YAML frontmatter block")
    if blocks:
        frontmatter = blocks[0]
        require(bool(re.search(r"(?m)^name:\s*[a-z0-9-]+\s*$", frontmatter)),
                "Frontmatter needs a lowercase hyphenated name")
        require(bool(re.search(r"(?m)^description:\s*.+$", frontmatter)),
                "Frontmatter needs a non-empty description")
    for heading in [
        "Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5",
        "Phase 6", "Phase 7", "Phase 8", "Phase 9", "Phase 10",
        "Definition of done"
    ]:
        require(heading.lower() in content.lower(), f"SKILL.md missing section: {heading}")

required_files = [
    "references/design-system.md",
    "references/production-pipeline.md",
    "references/quality-gates.md",
    "references/scene-patterns.md",
    "templates/creative-brief.md",
    "templates/shot-list.csv",
    "scripts/validate_repo.py",
    "LICENSE",
    "CHANGELOG.md",
]
for rel in required_files:
    require((ROOT / rel).is_file(), f"Missing required file: {rel}")

if readme_path.exists():
    readme = readme_path.read_text(encoding="utf-8")
    for rel in required_files:
        if rel not in readme and rel not in ("scripts/validate_repo.py",):
            WARNINGS.append(f"README does not mention {rel}")

if ERRORS:
    print("FAIL")
    for item in ERRORS:
        print(f" - {item}")
    sys.exit(1)

print("PASS: required repository structure and SKILL.md frontmatter found.")
print("NOTE: this is a structural check, not a video-render or visual-quality test.")
for item in WARNINGS:
    print(f"WARNING: {item}")
