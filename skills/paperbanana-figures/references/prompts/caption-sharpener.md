# Caption Sharpening Prompt Template

Use this template during Step 2 of the pipeline. Transform the user's vague or rough caption into a precise visual specification.

---

## Instructions

Given the user's draft caption and the enriched context from Step 1, generate a sharpened caption that serves as both a figure specification and a reader-facing description.

## Input

- **Draft caption**: The user's original caption (may be vague, e.g., "Our method").
- **Enriched context**: The structured output from Step 1.

## Output Format

### Sharpened Caption

Write the final caption in 2-4 sentences following this structure:

1. **Subject sentence**: "[Figure type] of [what it depicts]." Example: "Architecture overview of the dual-encoder retrieval-augmented generation pipeline."
2. **Component sentence**: "The system consists of [key components], connected by [relationship]." Example: "The frozen vision encoder (gray) produces patch embeddings that are projected into the language model's input space via a trainable adapter (blue)."
3. **Emphasis sentence** (optional): "The [novel component] enables [capability]." Example: "The cross-attention bridge (highlighted in orange) enables zero-shot transfer across modalities."
4. **Reading instruction** (optional): "Solid arrows indicate [X]; dashed arrows indicate [Y]." Example: "Solid arrows show the forward pass; dashed arrows show gradient flow during training."

### Visual Specification (Internal)

This part is not included in the final caption but guides the planner:

- **Subject**: Exactly what the figure depicts.
- **Scope**: What is included and what is excluded.
- **Emphasis**: What the reader should notice first.
- **Type**: Architecture / pipeline / comparison / flowchart / data-flow / other.
- **Complexity**: Simple (3-5 elements) / Medium (6-12 elements) / Complex (13+ elements).
