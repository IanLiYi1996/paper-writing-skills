# Style Refinement Prompt Template

Use this template during Step 5 of the pipeline. Refine the planned description by checking compliance with the NeurIPS aesthetic guidelines defined in `references/style-guide.md`.

---

## Instructions

Review the description from Step 4 and apply corrections to ensure it conforms to the style guide. Check each category below. For any violation, specify the correction.

## Checklist

### 1. Color Compliance

- [ ] Background fills use 10-15% opacity pastels (hex codes from style guide).
- [ ] Active elements use medium-saturation colors, not pure primaries.
- [ ] Trainable components use warm tones (blue family: `#4A90D9`).
- [ ] Frozen components use cool/gray tones (`#7FB3D8`, `#90A4AE`).
- [ ] Novel contributions have a distinct emphasis color (`#FF8A65` coral).
- [ ] No more than 6 distinct hues in the entire figure.
- [ ] Text colors are `#333333` (primary) or `#666666` (secondary), never pure black.
- [ ] Color pairings follow the complementary scheme (blue/orange, green/purple, teal/coral).

### 2. Shape Conventions

- [ ] Processes and modules use rounded rectangles (5-10px corner radius).
- [ ] Tensors and data blobs use 3D cuboids.
- [ ] Databases and storage use cylinders.
- [ ] Decision points use diamonds.
- [ ] No generic rectangles with sharp corners (always round them).

### 3. Typography Consistency

- [ ] All labels use the same sans-serif font family.
- [ ] Mathematical notation uses serif italics.
- [ ] Same-level elements have the same font size.
- [ ] No font size below 7pt at final print size.
- [ ] Maximum 2 font families in the entire figure.

### 4. Layout Alignment

- [ ] All elements snap to a consistent grid.
- [ ] Horizontal centers of same-row elements are aligned.
- [ ] Vertical centers of same-column elements are aligned.
- [ ] Spacing between adjacent elements is consistent throughout.
- [ ] Flow direction is uniform (no backtracking without edge routing).
- [ ] At least 20% of canvas area is whitespace.

### 5. Arrow and Line Styles

- [ ] Architecture diagrams use orthogonal (elbow) routing.
- [ ] Forward-pass arrows are solid; gradient arrows are dashed.
- [ ] Arrow colors match the style guide conventions.
- [ ] No arrows cross through elements.
- [ ] Parallel arrows are evenly spaced.

### 6. Visual Weight Balance

- [ ] The novel contribution is the most visually prominent element.
- [ ] Supporting elements recede in size or saturation.
- [ ] The reader's eye is drawn to the key contribution first.
- [ ] No single element dominates excessively (unless it is the contribution).

## Output

Produce the refined description with all corrections applied. Mark each change with a brief note explaining the correction (e.g., "Changed fill from #FF0000 to #E07A5F per style guide"). If no corrections are needed for a category, note "Compliant" for that section.
