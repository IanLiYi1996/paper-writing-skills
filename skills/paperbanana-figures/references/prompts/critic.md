# Visual Critique Prompt Template

Use this template during Step 7 of the pipeline. Evaluate the generated image on four dimensions and determine whether to accept or revise.

---

## Instructions

Examine the generated image using your vision capability. For each dimension, provide a score (1-5), a brief justification, and specific issues if the score is below 3.

## Evaluation Rubric

### Dimension 1: Faithfulness (Does it match the source?)

| Score | Criteria |
|-------|----------|
| 5     | Every component and connection from the methodology is present and correctly represented. No fabricated elements. |
| 4     | All major components present. Minor omissions (e.g., a secondary arrow label is missing). |
| 3     | Core structure is correct but 1-2 components are misrepresented or missing. |
| 2     | Several components are wrong, missing, or the overall structure diverges from the description. |
| 1     | The figure bears little resemblance to the described methodology. |

### Dimension 2: Conciseness (Is it focused?)

| Score | Criteria |
|-------|----------|
| 5     | Every visual element serves a purpose. No decorative clutter. Perfect information density. |
| 4     | Minimal clutter. One or two elements could be simplified or removed. |
| 3     | Some unnecessary elements present, but the core message is clear. |
| 2     | Significant clutter that distracts from the main message. |
| 1     | Overwhelmingly cluttered. The key message is lost in visual noise. |

### Dimension 3: Readability (Is it clear at a glance?)

| Score | Criteria |
|-------|----------|
| 5     | An ML researcher can understand the full pipeline in under 10 seconds. All text is legible. Flow direction is immediately obvious. |
| 4     | Understandable within 15 seconds. Minor readability issues (e.g., one label is slightly small). |
| 3     | Requires 20-30 seconds to parse. Some labels are hard to read or the flow direction is ambiguous. |
| 2     | Confusing layout. Multiple readings needed. Text is too small or overlapping. |
| 1     | Cannot determine what the figure represents without external explanation. |

### Dimension 4: Aesthetics (Does it follow NeurIPS style?)

| Score | Criteria |
|-------|----------|
| 5     | Fully compliant with the style guide. Colors, shapes, typography, and layout are all correct. Professional appearance. |
| 4     | Mostly compliant. One minor style deviation (e.g., slightly saturated colors). |
| 3     | Acceptable appearance but with 2-3 style deviations (e.g., mixed arrow styles, inconsistent spacing). |
| 2     | Noticeable style problems (e.g., PowerPoint-like shadows, clashing colors, poor alignment). |
| 1     | Unprofessional appearance. Major violations of academic figure conventions. |

## Output Format

```
## Critique Report

### Faithfulness: [X]/5
[Justification in 1-2 sentences]
Issues: [List specific problems, or "None"]

### Conciseness: [X]/5
[Justification in 1-2 sentences]
Issues: [List specific problems, or "None"]

### Readability: [X]/5
[Justification in 1-2 sentences]
Issues: [List specific problems, or "None"]

### Aesthetics: [X]/5
[Justification in 1-2 sentences]
Issues: [List specific problems, or "None"]

### Verdict: [PASS / REVISE]

### Revision Suggestions (if REVISE):
1. [Specific actionable change]
2. [Specific actionable change]
3. [Specific actionable change]
```

## Decision Logic

- **PASS**: All four dimensions score 3 or above. Deliver the figure to the user.
- **REVISE**: Any dimension scores below 3. Apply the revision suggestions and regenerate from Step 6.
- **After 3 iterations**: Deliver the best version with a note listing remaining imperfections.
