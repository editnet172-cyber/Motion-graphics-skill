# Design System Playbook

Use this reference to make a visual language coherent from frame to frame. The correct style is determined by the supplied brief and reference; the creamy premium system below is a starting point for projects with that direction.

## 1. Art-direction hierarchy

Decide these in order:
1. What must the viewer understand?
2. What is the one focal point for this beat?
3. What is the intended emotional tone?
4. Which visual treatment supports the message?
5. Which details can be removed?

If a decorative element competes with the message, simplify or remove it.

## 2. Palette tokens

Example restrained system; adjust to brand assets and reference:

| Token | Starting value | Role |
|---|---|---|
| `canvas-cream` | `#F6F4EF` | Primary background |
| `canvas-cool` | `#EEF0FA` | Secondary atmosphere |
| `ink` | `#171923` | Main typography |
| `muted-ink` | `#656979` | Supporting copy |
| `accent-blue` | `#3478F6` | Main action/focal accent |
| `accent-lavender` | `#B7B9F3` | Subtle depth |
| `surface` | `#FFFFFF` | Product/UI surfaces |
| `hairline` | `#E1E3EB` | Restrained separators |

Do not use every token in every scene. Keep one dominant background, one text color, and at most one or two accents unless the brand requires more.

## 3. Typography

- Establish a hierarchy: headline, supporting line, UI label, metadata.
- Choose a font actually installed or included with the project. Record the exact font and fallback.
- Use size, weight, spacing, and line breaks intentionally.
- Prefer short copy and comfortable line lengths.
- Avoid tiny interface text that only looks detailed at the working zoom.
- Verify punctuation, casing, product names, and CTA text.
- Keep text horizontal and crisp unless a deliberate typographic moment justifies otherwise.
- Test at final output resolution, not only in a large preview window.

## 4. Layout and spacing

- Define safe margins for each output aspect ratio.
- Use a grid or alignment anchors for repeated elements.
- Maintain consistent card edges, gaps, radii, and baselines.
- Give the hero element enough breathing room.
- Avoid symmetrical layouts by default if a clear asymmetrical composition creates stronger hierarchy.
- Keep the main message away from platform UI overlays and cropping zones.

## 5. Materials and lighting

- Matte: soft diffuse response, restrained specular.
- Glass: readable edge, subtle reflection, background visibility, no excessive bloom.
- Metal: controlled highlight direction and clear shape definition.
- Plastic: broad soft highlights and moderate contrast.
- Shadows: consistent direction, contact shadow near surfaces, softer shadow at greater distance.
- Depth: establish foreground/midground/background intentionally; avoid arbitrary floating.

Use one coherent light source logic. A card cannot cast a hard shadow in one shot and a soft shadow in the next without a motivated lighting change.

## 6. Motion vocabulary

Define a small family of durations and easing curves for the project. Example starting bands—not universal rules:

- Micro interaction: 120–220 ms
- UI reveal: 220–420 ms
- Product reveal: 450–900 ms
- Scene transition: 350–800 ms
- End-card hold: long enough to read and act

Use faster motion for small, low-mass UI responses; slower motion for hero objects and camera moves. These are reference ranges only; adapt to frame rate, duration, music, and style.

### Easing principles
- Ease-in: build momentum into an action.
- Ease-out: arrive and settle naturally.
- Ease-in-out: move between two states without a harsh start or stop.
- Overshoot: use sparingly for emphasis; settle must be intentional.
- Linear: use for constant-speed mechanical movement, scrolling, or data motion when appropriate.

Do not mix unrelated easing styles in adjacent elements unless the contrast is intentional.

## 7. Transition design

Choose transitions based on scene meaning:
- Match shape: an object or glyph becomes a shape in the next scene.
- Match position: a card exits where the next object enters.
- Typography transform: a key word becomes a UI element or product feature.
- Camera bridge: a controlled push/pan reveals the next composition.
- Light/color bridge: a restrained color or lighting change carries continuity.
- Cut on action: change scenes during a meaningful movement.

Use a simple cut when it is stronger than a transition. Do not add a transition just to demonstrate technical ability.

## 8. Sound identity

- Choose a restrained sound palette.
- Give each click/impact a visual cause.
- Preserve dialogue clarity.
- Avoid stacking multiple sounds on every movement.
- Let silence and negative space create contrast.
- Check the audio tail and final transition.
- Measure loudness and peaks if a suitable tool is available; otherwise, do not claim numeric compliance.

## 9. Anti-patterns

Remove or revise:
- Random floating geometry with no message function
- Constant zoom or constant motion
- Excessive neon/glow
- Excessive motion blur over text
- Unreadable microcopy
- Unmotivated rotations and bounce
- Inconsistent shadows and perspective
- UI cards that never settle
- Transition effects that hide poor scene planning
- Generic filler scenes that could advertise any product
