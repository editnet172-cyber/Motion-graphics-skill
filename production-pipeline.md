# Production Pipeline

A practical workflow from brief to verified deliverable.

## Stage 0 — Environment check

Identify the existing project, available tools, package manager, renderer, and output path. Read project documentation and inspect scripts before installing or changing anything. Do not assume a particular framework.

Record:
- Project type and entry point
- Relevant dependencies and versions
- Existing render/build commands
- Available video/audio inspection tools
- Asset locations and missing dependencies
- Safe test command and expected output

Never install a large dependency or rewrite the project structure without a clear reason.

## Stage 1 — Asset inventory

Create a manifest with asset name, type, dimensions/duration, intended role, and status. Check:
- Image transparency and dimensions
- Video frame rate, duration, and aspect ratio
- Audio duration and channels
- Font availability
- File paths and capitalization
- Whether an asset is licensed/authorized for this use

Preserve originals. Work on copies when edits may be destructive.

## Stage 2 — Reference map

Sample the full reference at regular intervals and at scene changes. Note:
- Message
- Composition and focal point
- Motion path and easing impression
- Transition in/out
- Audio cue
- Text hold/readability
- Distinctive style traits

Do not infer exact frame timing from sparse samples; mark estimates as approximate.

## Stage 3 — Brief and storyboard

Create `templates/creative-brief.md` from the project facts. Produce a shot list using `templates/shot-list.csv` or an equivalent structured table. Make sure total shot durations plus overlaps produce the requested final duration.

Each shot should be independently understandable but contribute to the larger story.

## Stage 4 — Animatic / greybox

Before high polish, build a simple version with:
- Correct scene order
- Rough durations
- Main typography
- Main product/UI elements
- Transition timing
- Audio cues

Review this stage for narrative clarity and pacing. Fix structural problems before expensive polish.

## Stage 5 — Visual build

Implement the selected design system with reusable tokens and components. Keep timing centralized. Avoid duplicating nearly identical code or scattering magic numbers. Use real assets and legible copy.

## Stage 6 — Motion and sound

Add:
- Intentional easing and settles
- Choreographed stagger
- Motivated scene bridges
- Depth and lighting consistency
- Audio cues aligned to meaningful visual beats
- Appropriate dialogue/music balance

Review at actual playback speed; static frames cannot reveal jitter, awkward timing, or a bad transition.

## Stage 7 — Diagnostic render

Render a short section or lower-resolution preview. Check:
- Build/render errors
- Font fallback
- Missing assets
- Frame rate and output dimensions
- Text layout
- Audio sync
- Transition continuity

Do not proceed to a long final render while obvious issues remain.

## Stage 8 — Final render and review

Render the final output. Inspect:
- Metadata: duration, dimensions, frame rate, codec/container
- Beginning, ending, all scene boundaries, transition midpoints, and complex motion
- Audio start/end, dialogue sync, peaks/clipping where measurable
- Full playback if tools permit

If only sampled frames were inspected, say so. A frame montage is not equivalent to full playback.

## Stage 9 — Fix and verify

Rank issues by severity:
1. Broken export or missing media
2. Message/story clarity
3. Timing and continuity
4. Text readability and layout
5. Audio quality/synchronization
6. Minor aesthetic polish

Fix the most consequential issue first. Re-render the affected section, then re-render the final export if required. Re-run checks after changes.

## Stage 10 — Delivery

Deliver:
- Final video path
- Source project path
- Actual export specs
- Completed checks
- Unverified checks or limitations

Use plain language and never label an unverified result “perfect.”
