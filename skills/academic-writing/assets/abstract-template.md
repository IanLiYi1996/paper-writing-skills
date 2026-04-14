# Abstract Template

Structured format for writing effective abstracts following the 5-sentence formula (Sebastian Farquhar).

---

## The 5-Sentence Formula

| # | Purpose | Starter Phrases |
|---|---------|-----------------|
| 1 | What you achieved | "We introduce...", "We prove...", "We demonstrate...", "We present..." |
| 2 | Why this is hard or important | "This is challenging because...", "Despite X, current methods...", "Existing approaches require..." |
| 3 | How you do it (with specialist keywords) | "Our approach leverages...", "We propose a method that...", "The key idea is to..." |
| 4 | What evidence you have | "Experiments on X show...", "We validate on...", "Across N benchmarks..." |
| 5 | Your most remarkable number | "Achieving X% improvement...", "Reducing Y by Z...", "Outperforming SOTA by..." |

---

## Template

```
[What you achieved]: We [introduce/demonstrate/prove] [method/finding],
a [type] that [key capability].

[Why hard/important]: [Problem or challenge] remains difficult because
[specific reason], limiting [practical consequence].

[How you do it]: Our approach [key technical idea], leveraging [technique]
to [mechanism]. [Optional: additional detail with specialist keywords.]

[Evidence]: Experiments on [datasets/benchmarks] demonstrate [key findings],
with [specific improvements] over [baselines].

[Remarkable number]: [Method name] achieves [specific metric] of [value],
representing a [X]% improvement over the strongest baseline while
[additional benefit, e.g., reducing compute by Y%].
```

---

## Rules

- Write the abstract LAST, after the full paper is complete
- Target 150-250 words (check venue requirements)
- Include at least one specific number
- No undefined acronyms or abbreviations
- Must be self-contained (understandable without reading the paper)
- Delete generic openings ("Large language models have achieved remarkable success...")
- Every sentence should earn its place; if a sentence adds nothing, cut it

---

## Example

> We introduce SparseAttn, a sparse attention mechanism that achieves
> competitive accuracy with 10x less computation than standard transformers.
> Processing long sequences remains challenging because self-attention
> scales quadratically with sequence length, making it impractical for
> documents exceeding 4K tokens. Our approach identifies and attends to
> only the most relevant tokens using a learned sparsity predictor,
> reducing attention complexity from O(n^2) to O(n sqrt(n)) while preserving
> information flow through auxiliary dense connections. Experiments on
> four long-document benchmarks (SCROLLS, LongBench, BookSum, and
> GovReport) demonstrate consistent improvements over efficient attention
> baselines including Longformer, BigBird, and Flash Attention. SparseAttn
> achieves 94.2% of full attention accuracy on SCROLLS while using only
> 8% of the FLOPs, enabling processing of 32K-token sequences on a
> single A100 GPU.

(138 words)
