# Diagram Best Practices for Academic Papers

This document collects general principles for creating effective figures in academic ML/AI papers. These guidelines are venue-agnostic but calibrated for top-tier conferences (NeurIPS, ICML, ICLR, ACL, AAAI).

---

## Figure Size Requirements

### Single-Column Figures

- **Width**: 3.25 inches (8.25 cm) for NeurIPS/ICML; 3.3 inches for ACL.
- **Max height**: ~4 inches to leave room for the caption below.
- Use for: focused diagrams, single plots, ablation results.

### Double-Column (Full-Width) Figures

- **Width**: 6.875 inches (17.5 cm) for NeurIPS/ICML; 6.8 inches for ACL.
- **Max height**: ~5 inches for comfortable caption placement.
- Use for: Figure 1 overviews, multi-panel comparisons, wide pipelines.

### Design at Final Size

Always design your figure at the exact dimensions it will appear in the paper. Designing at 2x or 4x and scaling down leads to text that is too small, lines that are too thin, and inconsistent visual weight. If you use matplotlib, set `figsize` to the target dimensions.

---

## Font Size Guidelines

- **Minimum readable**: 7pt at final print size (any smaller is unacceptable).
- **Recommended range**: 8-11pt for labels and annotations.
- **Rule of thumb**: Figure text should be between the paper's body text size (10pt) and caption size (8-9pt).
- **Consistency**: All labels at the same hierarchical level must use the same font size. Do not make one box label 10pt and another 8pt.

---

## Color Usage

### Limit Your Palette

- Use a maximum of 6 distinct colors per figure.
- Each color must carry semantic meaning (e.g., blue = encoder, orange = decoder).
- Reuse colors consistently across all figures in the paper.

### Colorblind Safety

Approximately 8% of men and 0.5% of women have color vision deficiency. Your figures must be accessible:

- **Preferred palettes**: Okabe-Ito, Paul Tol, or ColorBrewer qualitative palettes.
- **Never rely on red-green distinction** alone. This is the most common deficiency.
- **Add redundant encoding**: Use different line styles (solid, dashed, dotted), marker shapes (circle, square, triangle), or fill patterns (solid, hatched, crosshatched) alongside color.

### Grayscale Readability

Some readers print in black and white. Ensure your figure remains interpretable:

- Lines must differ in style, not just color.
- Bar charts should use fill patterns or labeled callouts.
- Avoid using two colors that map to the same gray level (e.g., medium blue and medium red).

---

## Arrow and Connection Design

### Direction Consistency

- All arrows in a diagram should predominantly flow in one direction (left-to-right or top-to-bottom).
- Feedback loops and skip connections should be routed along the edges, not through the center.
- Avoid zigzag patterns where arrows reverse direction repeatedly.

### Arrow Semantics

- **Solid arrow**: Primary data flow or dependency.
- **Dashed arrow**: Optional, conditional, or gradient flow.
- **Dotted arrow**: Weak dependency or reference.
- **Thick arrow**: Emphasize a critical path.
- Label arrows only when the relationship is not obvious from context.

---

## Subfigure Organization

### When to Use Subfigures

- Comparing variants of the same method: (a) baseline, (b) with module X, (c) with module Y.
- Showing different views of the same system: (a) architecture, (b) training loop, (c) inference.
- Multi-panel results: (a) accuracy, (b) latency, (c) memory.

### Subfigure Labels

- Use (a), (b), (c) labels in the top-left corner of each panel.
- Labels should be bold, 9-10pt, in the same font as the rest of the figure.
- Reference in text as "Figure 3(a)" not "the left panel of Figure 3".

### Alignment

- All subfigures in a row should share the same height and y-axis scale (for plots).
- Vertical alignment of labels across panels.
- Consistent spacing between panels (typically 10-15pt).

---

## Caption Writing

### What Goes in the Caption

The caption describes **what the figure IS**. The body text describes **what it MEANS**.

A good caption has three parts:

1. **Statement**: One sentence describing what the figure shows. "Overview of our dual-encoder retrieval pipeline."
2. **Description**: One sentence identifying key components or reading instructions. "Blue modules are trainable; gray modules are frozen. Arrows indicate data flow direction."
3. **Takeaway** (for results figures): One sentence highlighting the main finding. "Our method (blue bars) outperforms all baselines across all three benchmarks."

### Caption Length

- Architecture figures: 2-4 sentences.
- Results figures: 2-3 sentences.
- Supplementary figures: 1-2 sentences.

### Self-Containment

A reader should be able to understand the figure by looking at it and reading the caption alone, without referring to the main text. Define any abbreviations or color codes in the caption.

---

## Format Guidelines

### Vector vs. Raster

| Content Type          | Recommended Format | Reason                           |
|-----------------------|-------------------|----------------------------------|
| Architecture diagrams | PDF               | Clean at any zoom level          |
| Line plots            | PDF               | Crisp lines and text             |
| Bar charts            | PDF               | Sharp edges                      |
| Photographs           | PNG (300 DPI)     | Raster content                   |
| Generated images      | PNG (300 DPI)     | Raster content from AI models    |
| Heatmaps              | PDF or PNG (300)  | Either works; PDF for sharp text |
| t-SNE / scatter plots | PDF               | Many small elements benefit from vector |

### File Naming Convention

```
figures/
  fig1-overview.pdf
  fig2-architecture.pdf
  fig3-main-results.pdf
  fig4-ablation.pdf
  fig5-qualitative.png
```

### LaTeX Integration

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig1-overview.pdf}
  \caption{Overview of our approach. Blue modules are trainable;
  gray modules are frozen. Arrows indicate data flow.}
  \label{fig:overview}
\end{figure}
```

Always use `\linewidth` (not `\textwidth`) for figures inside columns. Use `[t]` or `[!t]` placement for top-of-page positioning.
