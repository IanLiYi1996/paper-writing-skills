---
name: paperbanana-figures
description: Generate publication-quality academic figures using a multi-agent pipeline inspired by PaperBanana. Creates methodology diagrams, architecture diagrams, and statistical plots with iterative refinement. Self-contained with built-in image generation scripts. Use when creating Figure 1, methodology diagrams, architecture diagrams, statistical plots, or any publication figure for ML/AI papers. Also triggers on draw figure, generate diagram, paper illustration, make plot.
---

# PaperBanana Figures: Publication-Quality Academic Figure Generation

## Overview

This skill implements a 7-step figure generation pipeline inspired by PaperBanana, a framework for automated academic illustration. It is fully self-contained: Claude executes the planning, critique, and refinement steps, while built-in Python scripts handle image generation via Gemini or OpenAI APIs.

Two figure types are supported:

1. **Methodology / Architecture Diagrams** -- Generated via text-to-image models (Gemini or OpenAI). Suitable for Figure 1 overviews, architecture diagrams, pipeline illustrations, and conceptual figures.
2. **Statistical Plots** -- Generated via matplotlib. Suitable for bar charts, line plots, ablation studies, and quantitative comparisons.

The pipeline enforces NeurIPS-grade aesthetics throughout: soft pastels, clean typography, colorblind-safe palettes, and consistent visual language. Every figure goes through at least one critique-and-revise cycle before delivery.

**Prerequisites**: A `GOOGLE_API_KEY` (for Gemini, recommended) or `OPENAI_API_KEY` must be set. Install dependencies with `uv pip install -r scripts/requirements.txt` from this skill's directory.

---

## The 7-Step Pipeline

Follow these steps sequentially for every figure request. Do not skip steps. Each step builds on the output of the previous one.

### Step 1: Context Enrichment

Read the user's methodology text (paper section, abstract, or verbal description) and restructure it into a diagram-ready format.

Read the prompt template at `references/prompts/context-enricher.md` in this skill's directory. Apply it to the user's input. Your output should be a structured document with:

- **Key Components**: Each module, model, or process as a named entity with a one-line description.
- **Data Flows**: Explicit source-to-destination connections (e.g., "Encoder output --> Attention layer").
- **Logical Groupings**: Which components belong together (e.g., "Training Pipeline", "Inference Module").
- **Inputs / Outputs**: System boundaries -- what enters and what leaves the diagram.
- **Key Innovations**: What to visually emphasize (the novel contribution).

If the user provides only a vague request ("draw a figure for my method"), ask for the relevant paper section or at minimum a 3-sentence description of the approach.

### Step 2: Caption Sharpening

Transform the user's rough caption into a precise visual specification. A vague caption like "Our method" must become something like "Overview of the dual-encoder retrieval-augmented generation pipeline with frozen vision encoder and trainable language adapter."

Read the prompt template at `references/prompts/caption-sharpener.md`. Your sharpened caption should specify:

- **Subject**: Exactly what the figure depicts.
- **Scope**: What is included and what is deliberately excluded.
- **Emphasis**: What the reader should notice first (the key contribution).
- **Type**: The diagram category (architecture, pipeline, comparison, ablation, etc.).

The sharpened caption becomes the figure's actual caption. It must be self-contained: a reader should understand the figure without reading the main text.

### Step 3: Reference Selection

Select 2-3 relevant reference diagrams from the bundled examples to guide the visual planning.

Read `assets/reference-diagrams/index.json` in this skill's directory. Each entry has: id, category, caption, style_notes, image_path, and aspect_ratio. Match references by:

1. **Domain alignment**: If the paper is about agents, prefer agent-system references; if about transformers, prefer transformer-architecture references.
2. **Structural similarity**: Match the complexity level -- a simple 3-block pipeline should not reference a 20-component architecture.
3. **Style compatibility**: Prefer references whose style_notes align with the desired aesthetic.

Record the selected reference IDs and explain why each was chosen. If reference images are available at the image_path locations, use the Read tool to examine them visually.

### Step 4: Description Planning

Generate a detailed textual description of the figure. This is the most critical step -- the description directly determines the quality of the generated image.

Read the prompt template at `references/prompts/planner.md`. Using the enriched context (Step 1), sharpened caption (Step 2), and selected references (Step 3), produce a description that specifies:

- **Layout**: Direction (left-to-right, top-to-bottom) and grid structure (rows x columns).
- **Visual Elements**: For each element: shape (rounded rectangle, cuboid, cylinder, ellipse, diamond), label text, approximate position, fill color (hex code), border style, and relative size.
- **Connections**: For each arrow/line: source element, target element, line style (solid, dashed, dotted), arrowhead style, color, and optional label.
- **Grouping Boxes**: Which elements are grouped together, group label, background color (very light pastel).
- **Aspect Ratio**: Recommended ratio (16:9 for wide pipelines, 4:3 for architectures, 1:1 for focused diagrams).
- **Color Palette**: List all colors used with their semantic meaning (e.g., "#4A90D9 = trainable components").

The description must be precise enough that someone could recreate the figure from text alone.

### Step 5: Style Refinement

Refine the description by applying the NeurIPS aesthetic guidelines.

Read `references/style-guide.md` and `references/prompts/stylist.md` in this skill's directory. Check and correct:

- **Color Compliance**: Backgrounds at 10-15% opacity pastels. Active elements at medium saturation. No pure red, green, or blue. Warm tones for trainable, cool for frozen.
- **Shape Conventions**: Rounded rectangles (5-10px radius) for processes. 3D cuboids for tensors/data. Cylinders for databases/storage. Diamonds for decision points.
- **Typography**: Sans-serif (Arial, Roboto, Helvetica) for all labels. Serif with italics for mathematical notation only. Font size consistent across same-level elements.
- **Layout Alignment**: All elements on a grid. Consistent spacing. Flow direction is uniform (no backtracking arrows). Adequate whitespace (at least 20% of canvas).
- **Visual Weight Balance**: Important elements are larger or more saturated. Secondary elements recede. The eye is drawn to the key contribution first.

Output the refined description with all corrections applied.

### Step 6: Image Generation

Execute the appropriate generation script.

**For methodology/architecture diagrams:**

```bash
uv run python3 scripts/generate_figure.py \
  --description "THE_REFINED_DESCRIPTION" \
  --output output/figure.png \
  --provider gemini \
  --aspect-ratio 16:9
```

If the description is long, write it to a temporary file and pass `--description @path/to/description.txt`.

**For statistical plots:**

```bash
uv run python3 scripts/generate_plot.py \
  --data path/to/data.json \
  --intent "Show that method A outperforms baselines on all metrics" \
  --output output/plot.pdf \
  --style paper
```

After generation, use the Read tool to visually inspect the output image.

### Step 7: Visual Critique

Examine the generated image using your vision capability. Read `references/prompts/critic.md` for the evaluation rubric. Score the image on four dimensions:

| Dimension      | Question                                                        | Score |
|----------------|-----------------------------------------------------------------|-------|
| Faithfulness   | Does the figure accurately represent the source methodology?    | 1-5   |
| Conciseness    | Is the figure focused without unnecessary visual clutter?       | 1-5   |
| Readability    | Can the figure be understood at a glance by an ML researcher?   | 1-5   |
| Aesthetics     | Does the figure follow NeurIPS style guidelines?                | 1-5   |

**Verdict:**
- **PASS**: All dimensions score 3 or above. Deliver the figure.
- **REVISE**: Any dimension scores below 3. List specific issues, revise the description, and repeat from Step 6.

Recommend 2-3 iterations for important figures (especially Figure 1). After the third iteration, deliver the best version with a note on remaining imperfections.

---

## Figure Strategy for ML Papers

### The Canonical Figure Set

A well-structured ML paper typically includes 5-7 figures. Plan the full set before generating any individual figure:

| Figure | Purpose                    | Typical Type              | Priority |
|--------|----------------------------|---------------------------|----------|
| Fig 1  | High-level method overview | Architecture diagram      | Critical |
| Fig 2  | Detailed architecture      | Component diagram         | High     |
| Fig 3  | Main results               | Bar chart / table         | High     |
| Fig 4  | Ablation studies           | Grouped bar / line chart  | Medium   |
| Fig 5  | Qualitative examples       | Grid of images / cases    | Medium   |
| Fig 6  | Analysis / visualization   | Heatmap / t-SNE / curves  | Low      |

### Figure 1 Is Special

Figure 1 is the most important figure in the paper. Many reviewers look at it before reading the abstract. It must:

- Communicate the entire approach in one glance.
- Be understandable without reading the paper.
- Highlight the key novelty visually (larger size, distinct color, annotation).
- Be visually appealing -- this sets the tone for the entire paper.
- Have a self-contained caption of 3-5 sentences.

Allocate at least 3 critique iterations to Figure 1.

### Self-Contained Captions

Every caption should answer: "What does this figure show?" The body text answers: "What does this figure mean?" A good caption includes:

1. One sentence stating what the figure depicts.
2. One sentence describing the key components or axes.
3. One sentence highlighting the main takeaway (for results figures).

### Accessibility Requirements

- **Colorblind-safe**: Use Okabe-Ito or Paul Tol palettes. Never rely on red-green distinctions.
- **Grayscale readability**: Use line styles (solid, dashed, dotted), markers (circle, square, triangle), and hatching patterns in addition to color.
- **Font size**: All text in figures must be between body text size and caption size. A common mistake is using text that is too small after the figure is scaled to column width.
- **Vector graphics**: Use PDF for diagrams and line plots (infinite zoom, small file size). Use high-DPI PNG (300+ DPI) only for raster content (photos, generated images).

### Size Constraints

- Single column: 3.25 inches wide (ACL, NeurIPS one-column figures).
- Double column: 6.875 inches wide (NeurIPS full-width figures).
- Maximum height: 9 inches (leave room for caption).
- Plan your figure for its final display size -- do not design at 4x and hope it scales.

---

## Using Reference Diagrams

The `assets/reference-diagrams/` directory contains a curated index of reference diagram metadata. These serve as visual anchors during the planning step.

### How References Are Used

During Step 3 (Reference Selection), match the paper's domain and diagram type against the index entries. Selected references inform:

- **Layout patterns**: Whether to use left-to-right flow, top-to-bottom hierarchy, or radial arrangement.
- **Component density**: How many elements fit comfortably at a given aspect ratio.
- **Color usage**: Which palette and saturation levels work for similar content.
- **Grouping strategies**: How to visually cluster related components.

### Index Structure

Each entry in `assets/reference-diagrams/index.json` contains:

- `id`: Unique identifier for the reference.
- `category`: One of: agent, transformer, training-pipeline, rag, diffusion, multi-modal, reinforcement-learning, graph-neural-network.
- `caption`: Descriptive caption of what the reference shows.
- `style_notes`: Brief notes on layout, palette, and distinguishing visual features.
- `image_path`: Relative path to the reference image (when available).
- `aspect_ratio`: The aspect ratio of the reference image.

When reference images are not yet available, use the caption and style_notes to guide planning textually.

---

## Statistical Plot Generation

For quantitative figures (results, ablations, comparisons), use `scripts/generate_plot.py` instead of the text-to-image pipeline.

### Input Format

Provide data as JSON with this structure:

```json
{
  "type": "grouped_bar",
  "title": "Performance Comparison on Three Benchmarks",
  "xlabel": "Benchmark",
  "ylabel": "Accuracy (%)",
  "categories": ["MMLU", "HumanEval", "GSM8K"],
  "series": [
    {"name": "Ours", "values": [85.2, 72.1, 91.3]},
    {"name": "Baseline A", "values": [80.1, 65.4, 87.2]},
    {"name": "Baseline B", "values": [78.5, 60.2, 83.1]}
  ]
}
```

### Communicative Intent

Always specify what the plot should communicate. The intent drives design choices:

- "Show that our method outperforms all baselines" --> emphasize the winning bars.
- "Show diminishing returns with scale" --> use a line plot with clear inflection point.
- "Show component contributions via ablation" --> use a stacked or grouped bar with clear labeling.

### Publication Style

The generated plots follow these conventions:

- No top or right spines (clean look).
- No gridlines by default (add only if they aid reading).
- Colorblind-safe palette (Okabe-Ito by default).
- Consistent fonts matching the paper body.
- Legend outside the plot area when possible.
- Error bars when data variance is available.

---

## Iteration and Refinement

### When to Iterate

- **Figure 1**: Always iterate at least 2-3 times.
- **Results plots**: Usually 1-2 iterations (layout adjustments).
- **Supplementary figures**: 1 iteration is often sufficient.

### Common Issues and Fixes

| Issue                     | Symptom                              | Fix                                                |
|---------------------------|--------------------------------------|-----------------------------------------------------|
| Too cluttered             | Elements overlap or crowd            | Reduce component count, increase whitespace         |
| Misaligned elements       | Uneven spacing, crooked arrows       | Enforce strict grid, use orthogonal paths           |
| Wrong emphasis            | Novel contribution does not stand out| Use larger size, distinct color, or annotation      |
| Inconsistent style        | Mixed fonts, random colors           | Re-apply style guide from Step 5                    |
| Illegible text            | Labels too small after scaling       | Increase font size, reduce label count              |
| Missing flow direction    | Reader does not know where to start  | Add explicit input/output markers, unify arrow flow |

### When to Stop

Stop iterating when all four critique dimensions score 3 or above, OR after 3 iterations (deliver the best version). Document any remaining issues for the user to address manually.

---

## Environment Setup

### API Keys

Set one of the following environment variables:

- `GOOGLE_API_KEY` -- For Gemini image generation (recommended, default provider).
- `OPENAI_API_KEY` -- For OpenAI image generation (gpt-image-1).

### Dependencies

From this skill's directory, install Python dependencies:

```bash
uv pip install -r scripts/requirements.txt
```

Required packages: `google-genai`, `openai`, `Pillow`, `matplotlib`, `pandas`.

### Output Directory

Generated figures are saved to the path specified by `--output`. Create the output directory beforehand if it does not exist. Recommended convention: `figures/` in the paper's project root.
