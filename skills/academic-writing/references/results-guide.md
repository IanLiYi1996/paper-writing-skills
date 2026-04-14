# Results Section Writing Guide

A guide to presenting experimental findings objectively and effectively in ML/AI research papers.

---

## Overview

The Results section presents your experimental findings objectively. It answers "What did you find?" without interpretation (interpretation belongs in Discussion or, for ML papers where Results and Discussion are combined, in clearly separated paragraphs).

**Guiding Principle**: Objectivity. Report what you observed and let the evidence speak.

**Standard Structure**:
```
4. Experiments
   4.1 Experimental Setup (datasets, baselines, metrics)
   4.2 Main Results (primary comparison)
   4.3 Ablation Studies (component analysis)
   4.4 Additional Analysis (sensitivity, case studies)
```

---

## Experimental Setup

Describe datasets, baselines, and evaluation metrics before presenting results.

**Common Phrases**:

1. "We evaluate our approach on [N] benchmark datasets..."
2. "We compare against [N] competitive baselines..."
3. "Performance is measured using [metric]..."
4. "We use the standard train/dev/test splits from..."
5. "Following prior work (Citation), we adopt [setup]..."
6. "We report results averaged over [N] runs with different random seeds..."
7. "All experiments are conducted on [hardware]..."
8. "Hyperparameters are tuned on the validation set..."

**Dataset Description Template**:
> [Dataset] (Citation): [Brief description]. Contains [size] examples for [task]. We use the standard train/dev/test split of [X/Y/Z].

**Baseline Selection**:

| Type | Purpose | Example |
|------|---------|---------|
| Classic | Historical context | SVM, Logistic Regression |
| Strong recent | Current SOTA comparison | BERT, GPT, recent domain methods |
| Ablated versions | Validate your components | Your method minus component X |
| Upper bound | Show ceiling | Human performance, oracle models |

**Avoid**: Only weak baselines, unfair comparisons (different data splits or preprocessing), or missing obvious competitors.

---

## Main Results

**Common Phrases**:

1. "Table X presents the main results on [dataset]..."
2. "As shown in Figure X, our method..."
3. "Our approach achieves [metric] of [value], outperforming..."
4. "Compared to the strongest baseline, we achieve a [N]% improvement..."
5. "Our method consistently outperforms baselines across all datasets..."
6. "The model achieves [metric] of [value] +/- [std]..."
7. "We observe that [finding]..."
8. "Results across all metrics are reported in Table X..."

**Before/After Example**:

*BEFORE (Interpretive, belongs in Discussion):*
> Table 1 shows that our method is much better than baselines because it uses better attention mechanisms.

*AFTER (Objective, factual):*
> Table 1 compares our method against five baselines across three datasets. Our approach achieves the highest F1 score on all datasets, with improvements ranging from 3.2% to 5.7% over the strongest baseline (p < 0.01).

---

## How to Describe Tables

Do NOT repeat the caption. Instead, interpret and highlight key observations:

| Bad | Good |
|-----|------|
| "Table 1 shows the accuracy of different methods. As shown, our method achieves 85.3% accuracy." | "Table 1 compares our method against baselines. Our method outperforms the strongest baseline by 3.2%, demonstrating the effectiveness of the proposed attention mechanism." |

**Patterns for referencing tables**:

- **Direct reference**: "Table X presents the results on [dataset]. Our method achieves..."
- **Comparative**: "As shown in Table X, our approach outperforms all baselines..."
- **Highlighting**: "Table X summarizes performance. Notably, we observe..."

---

## How to Describe Figures

**Common Phrases for Trends**:

1. "Figure X shows that performance increases with..."
2. "We observe a positive correlation between..."
3. "As [parameter] increases, [metric] decreases..."
4. "Performance plateaus at approximately..."
5. "There is a clear trade-off between [X] and [Y]..."
6. "The largest gains occur when..."
7. "Across all conditions, we consistently observe..."
8. "Results are relatively stable when [condition]..."

---

## Statistical Reporting Standards

**Always include uncertainty measures**:

```
Bad:  Our method achieves 89.3% accuracy.
Good: Our method achieves 89.3 +/- 0.4% accuracy (mean +/- std over 5 runs).
```

**When to report significance tests**:
- Small improvements (<2%): Mandatory
- Close results between methods: Report p-values
- Any claim of "significant improvement": Must be statistically validated

**Common approaches**:
- Standard deviation over 3-5 runs with different random seeds
- Bootstrap confidence intervals (95% CI)
- Paired t-test or Wilcoxon signed-rank test
- McNemar's test for classification accuracy comparisons

**Format**: Always specify what the uncertainty measure represents (standard deviation vs. standard error vs. confidence interval) and the number of runs.

---

## Ablation Studies

**Design**: Remove ONE component at a time to isolate contributions.

**Standard format**:

| Model | Accuracy | F1 |
|-------|----------|-----|
| Full model | 89.3 | 88.1 |
| w/o attention | 86.1 (-3.2) | 84.9 |
| w/o pre-training | 84.5 (-4.8) | 83.2 |
| Base only | 82.3 (-7.0) | 81.0 |

- Include the full model and base model (all components removed)
- Order rows by performance drop (largest drop = most important component)
- Discuss which components contribute most and why

---

## Presenting Negative Results

**Constructive framing**:

| Bad (dismissive) | Good (constructive) |
|-------------------|---------------------|
| "Our method does not work on Dataset-C." | "While our method shows lower accuracy on small datasets (<1K examples), it provides substantial gains on larger datasets, suggesting the approach benefits most from abundant training data." |
| "The results for this setting are poor." | "Performance degrades in the low-resource setting, indicating that [component] requires sufficient training examples to learn [pattern]. This boundary condition motivates future work on data-efficient variants." |

Reviewers respect honesty. Acknowledge negative results, explain them, and frame them as informative findings rather than failures.

---

## Results vs. Discussion

Keep these clearly separated:

| Results (report facts) | Discussion (interpret meaning) |
|------------------------|-------------------------------|
| "We achieve 89% accuracy" | "This demonstrates the effectiveness of our approach" |
| "Method A outperforms B by 5%" | "This is likely because A handles long sequences better" |
| "Ablating X reduces F1 by 3%" | "This confirms X's importance for capturing context" |
| "Performance drops with noise" | "This limitation suggests future robustness work" |

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| No error bars | Cannot assess reliability | Report mean +/- std over multiple runs |
| Cherry-picking results | Biased presentation undermines trust | Report all metrics and all datasets |
| Mixing results with interpretation | Confuses readers | Keep Results objective; save analysis for Discussion |
| Inconsistent formatting | Unprofessional appearance | Use same precision and format throughout |
| Missing significance tests | Close results may be noise | Report p-values for close comparisons |
| Weak baselines only | Inflates apparent contribution | Include current SOTA methods |
| No ablation studies | Cannot assess component contributions | Ablate each novel component |
