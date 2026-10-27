*made by clabhi*

# Motion Ad Director Pro

**A reference-aware production skill for premium motion-graphics advertisements.**

Motion Ad Director Pro helps Claude Code plan, implement, refine, and verify motion-design projects through a structured art-direction and quality-control workflow. It emphasizes coherent pacing, motivated transitions, readable typography, synchronized audio, reference analysis, and honest final verification.

> **Important:** A skill improves instructions and workflow; it does not upgrade the underlying model, guarantee flawless output, or replace unavailable rendering tools and human review.

## What it is designed to improve

- Reference breakdown into visual, motion, timing, and sound rules
- Clear creative brief, storyboard, and timestamped shot list
- Consistent typography, palette, spacing, depth, and lighting
- Smoother easing, transitions, scene continuity, and pacing
- Dialogue/music/SFX synchronization
- Project-aware implementation rather than assuming a particular software stack
- Render validation and a mandatory review → fix → re-render loop
- Honest PASS / FAIL / NOT VERIFIED reporting

## Repository structure

```text
motion-ad-director-pro/
├── SKILL.md
├── README.md
├── LICENSE
├── CHANGELOG.md
├── references/
│   ├── design-system.md
│   ├── production-pipeline.md
│   ├── quality-gates.md
│   └── scene-patterns.md
├── templates/
│   ├── creative-brief.md
│   └── shot-list.csv
└── scripts/
    └── validate_repo.py
```

## Supporting resources

- `references/design-system.md` — palette, typography, layout, materials, motion, transitions, and sound principles.
- `references/production-pipeline.md` — step-by-step workflow from environment check to final delivery.
- `references/quality-gates.md` — severity levels and PASS / FAIL / NOT VERIFIED checklists.
- `references/scene-patterns.md` — adaptable hook, UI reveal, feature, transformation, and CTA patterns.
- `templates/creative-brief.md` — reusable project brief.
- `templates/shot-list.csv` — starter shot list with timing and QA fields.
- `scripts/validate_repo.py` — lightweight structural validation script.

## Install for Claude Code

Claude Code skills are folders containing a `SKILL.md` file with YAML frontmatter. For a personal skill, place this folder at:

- macOS/Linux: `~/.claude/skills/motion-ad-director-pro/`
- Windows: `%USERPROFILE%\\.claude\\skills\\motion-ad-director-pro\\`

For a project-specific skill, place it at:

- `.claude/skills/motion-ad-director-pro/`

Copy the **entire folder**, not only `SKILL.md`, so the supporting references and templates remain available. Restart or refresh the Claude Code session if the skill does not appear. Skill discovery behavior may vary by Claude Code version; consult the current official documentation if installation differs.

## How to use

Ask for the task naturally, for example:

> Use Motion Ad Director Pro to create a 20-second product advertisement from the supplied reference video, logo, script, and audio. Analyze the references first, create a shot list, implement the best workflow supported by this project, render a preview, inspect it, fix detected problems, and verify the final export. Tell me honestly which checks could not be completed.

For an existing project:

> Audit this motion graphics project using Motion Ad Director Pro. Preserve my existing assets and structure. Find the biggest visual, timing, continuity, audio, and rendering issues; fix them in priority order; then render and verify the final output if the available environment supports it.

## Suggested buyer workflow

1. Install the skill folder.
2. Provide a reference video or representative screenshots.
3. Provide the product description, script/CTA, logo, brand assets, audio, duration, aspect ratio, and target platform.
4. Ask Claude to analyze the references before implementing.
5. Review the creative brief and shot list for major direction changes.
6. Ask Claude to render and inspect the result; provide feedback on any visible issues.
7. Verify the final export and keep the source project with it.

## Model compatibility

The skill is intended to be useful with supported Claude Code models, including Sonnet and Opus. It cannot turn Sonnet into Opus or promise identical output between models. Stronger models, available tools, project complexity, asset quality, and rendering environment all affect the result.

## Requirements

- Claude Code with skills support
- A project environment suitable for the desired output (the skill adapts to what is available)
- Reference media and assets supplied by the buyer
- A renderer/editor and relevant dependencies if a final video render is expected

This repository does not bundle third-party fonts, stock media, plugins, or proprietary assets. Check licenses for any assets used in a buyer's project.

## Quality and limitations

The skill asks Claude to validate output dimensions, duration, playback, text, transitions, and audio where tools allow. Some visual defects require actual playback or human judgment; some environments cannot render video at all. The skill requires those limitations to be disclosed instead of claiming an unverified result is flawless.

## Validation

Run:

```bash
python scripts/validate_repo.py
```

This checks the repository structure, frontmatter essentials, referenced support files, and template availability. It does **not** test a video render or prove visual quality.

## Commercial use

You may adapt this repository for your product workflow. Review the included license and any third-party asset licenses before redistribution. Do not promise buyers a guaranteed flawless result or a model capability upgrade. Sell the concrete workflow, reusable production standards, and verification process.

## Feedback

Useful improvement reports include the prompt used, model selected, operating environment, source project type, reference specs, render specs, the exact observed defect, and a short reproduction path. Do not include private keys, credentials, or confidential customer assets.
