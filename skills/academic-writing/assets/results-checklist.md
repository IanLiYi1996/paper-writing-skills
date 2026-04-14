# Results Section Checklist

Use this checklist while drafting and revising your Results/Experiments section. For detailed guidance, see [results-guide.md](../references/results-guide.md).

---

## Experimental Setup

- [ ] All datasets described with citations, sizes, and splits
- [ ] Evaluation metrics defined precisely
- [ ] Baselines listed and justified (including current SOTA)
- [ ] Implementation details specified (or referenced in appendix)
- [ ] Hardware and software environment noted
- [ ] Number of runs and random seed strategy stated
- [ ] Hyperparameter tuning procedure described

---

## Main Results

- [ ] Primary comparison table included with all baselines
- [ ] Best results clearly marked (bold or underline)
- [ ] Error bars or confidence intervals reported (mean +/- std)
- [ ] Number of runs stated for averaged results
- [ ] All datasets and metrics reported (no cherry-picking)
- [ ] Results referenced in text with interpretation highlights
- [ ] Statistical significance tested for close comparisons

---

## Ablation Studies

- [ ] Each novel component ablated individually
- [ ] Full model and base model (all components removed) included
- [ ] Results ordered by impact (largest drop first)
- [ ] Clear discussion of which components matter most
- [ ] Ablation table is well-organized and easy to read

---

## Additional Analysis

- [ ] Sensitivity analysis for key hyperparameters (if applicable)
- [ ] Qualitative examples or case studies (if applicable)
- [ ] Error analysis or failure case discussion (if applicable)
- [ ] Efficiency comparison (runtime, memory) if relevant to claims
- [ ] Visualization of learned representations (if applicable)

---

## Tables and Figures

- [ ] Every table and figure referenced in text
- [ ] Captions are self-contained (understandable without main text)
- [ ] Tables use booktabs format (three horizontal lines, no vertical lines)
- [ ] Numbers aligned by decimal point
- [ ] Consistent precision across all numbers (e.g., one decimal place)
- [ ] Best results visually distinguished (bold)
- [ ] Figures are high-quality (vector graphics for plots)
- [ ] Figure text is readable at printed size

---

## Statistical Rigor

- [ ] Mean and standard deviation reported from multiple runs
- [ ] At least 3-5 runs with different random seeds
- [ ] Statistical significance tests for claims of improvement
- [ ] p-values reported for close comparisons
- [ ] Uncertainty measure clearly labeled (std vs. std error vs. CI)

---

## Objectivity

- [ ] Results presented factually without interpretation
- [ ] No causal language ("because," "due to") in pure Results
- [ ] Negative results reported honestly and constructively
- [ ] No cherry-picking of favorable metrics or datasets
- [ ] Differences described precisely ("3.2% higher" not "much better")

---

## Consistency

- [ ] Metric names consistent throughout section
- [ ] Number formatting consistent (same decimal places)
- [ ] Method names match those used in Methods section
- [ ] Dataset names consistent with Setup subsection
- [ ] Results support all claims made in Introduction

---

## Quick Self-Assessment

1. **Completeness**: Have I reported all metrics on all datasets?
2. **Fairness**: Are baseline comparisons fair (same data, same preprocessing)?
3. **Rigor**: Do I include error bars and significance tests?
4. **Clarity**: Can a reader understand the main findings from tables alone?
5. **Honesty**: Have I reported negative results constructively?
6. **Connection**: Does every experiment answer a specific question tied to my claims?
