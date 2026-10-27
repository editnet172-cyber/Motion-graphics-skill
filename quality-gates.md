# Quality Gates and Defect Severity

Use these gates after the first render and again after final fixes. Every applicable item must be marked PASS, FAIL, or NOT VERIFIED.

## Severity scale

- **P0 — Delivery blocker:** no usable output, corrupted render, missing critical media, wrong aspect ratio, missing dialogue when required.
- **P1 — Major:** confusing story, unreadable key message, broken transition, obvious timing/audio mismatch, severe clipping or flicker.
- **P2 — Noticeable:** inconsistent shadow, uneven spacing, awkward settle, minor audio imbalance, distracting decorative element.
- **P3 — Polish:** subtle easing refinement, small noncritical alignment adjustment, optional detail.

Fix P0/P1 before spending time on P3.

## Gate 1: Brief and message

- [ ] First beat has a clear focal point and communicates the hook.
- [ ] Sequence supports the intended audience and product promise.
- [ ] CTA is accurate and readable.
- [ ] No unsupported claims have been added.
- [ ] Visuals are tailored to this product, not generic filler.

## Gate 2: Composition

- [ ] Main focal point is obvious at each beat.
- [ ] Negative space and margins are consistent.
- [ ] Safe areas match the target platform.
- [ ] UI cards, typography, and product elements do not collide accidentally.
- [ ] No unintended cropping or off-screen elements.

## Gate 3: Typography

- [ ] Spelling, grammar, punctuation, capitalization, and brand names checked.
- [ ] Text fits its containers.
- [ ] Line breaks and hierarchy are intentional.
- [ ] Small text remains readable at final size.
- [ ] No font substitution or glyph rendering problems.

## Gate 4: Motion and continuity

- [ ] No unintended jumps, flicker, jitter, teleporting, or one-frame flashes.
- [ ] Easing and settling are intentional.
- [ ] Object paths and screen direction make sense.
- [ ] Transitions are motivated or the cut is deliberately clean.
- [ ] Overlaps do not create visual collisions.
- [ ] No element exits before its message is readable.
- [ ] Final shot resolves and holds appropriately.

## Gate 5: Audio

- [ ] Correct supplied audio is used.
- [ ] Dialogue and key visual moments align.
- [ ] Dialogue is intelligible over music.
- [ ] No unintended clipping, duplicate audio, gaps, or drift.
- [ ] SFX have a clear visual cause.
- [ ] Audio tail is intentional.

## Gate 6: Technical export

- [ ] Output file exists and is non-empty.
- [ ] File decodes/plays in an available player or inspection tool.
- [ ] Dimensions and aspect ratio match the brief.
- [ ] Frame rate and duration are checked.
- [ ] Expected audio stream is present.
- [ ] No debug overlays, placeholders, broken assets, or unintended black frames.
- [ ] Output filename and destination are clear.

## Gate 7: Review evidence

Record:
- Tool/command used for each check
- What was actually inspected
- Defects found and fixes applied
- Remaining limitations

Do not mark a check PASS based only on intention. If a tool is missing or only a preview was checked, mark NOT VERIFIED and explain why.

## Example report

| Check | Status | Evidence / note |
|---|---|---|
| Output metadata | PASS | Dimensions, duration, and frame rate read from final export |
| Typography | PASS | Opening, scene boundaries, CTA inspected at output size |
| Full playback | NOT VERIFIED | No video playback tool available; sampled frames only |
| Audio peaks | NOT VERIFIED | No measurement tool available |
