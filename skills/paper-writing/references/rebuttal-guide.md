# Rebuttal Writing Guide

A structured guide for responding to reviewer feedback at ML/AI conferences. Rebuttals are your opportunity to correct misunderstandings, provide additional evidence, and improve your score.

---

## General Principles

1. **Respond to every point.** Skipping a concern signals you cannot address it. Even for minor comments, a brief acknowledgment ("We will fix the typo in Section 3.2") shows thoroughness.

2. **Be specific and evidence-based.** Replace vague promises with concrete actions and results. "We will add more experiments" is weak. "We ran Method X on Dataset Y, achieving 92.1% accuracy (see updated Table 3)" is strong.

3. **Provide new evidence when possible.** Additional experiments run during the rebuttal period are the most persuasive form of response. If you can run an experiment a reviewer asked for, do it.

4. **Keep the tone respectful and professional.** Never be defensive, dismissive, or sarcastic, even when you believe a reviewer is wrong. Assume good faith.

5. **Prioritize by impact.** Address the most serious concerns first. If a reviewer's main objection is weak baselines, lead with new baseline comparisons, not typo fixes.

6. **Be concise.** Reviewers read many rebuttals. A focused, well-structured response is more effective than a wall of text.

---

## Response Template

Use this structure for each reviewer comment:

```
> [R1-Q1] "The paper lacks comparison with Method X."

We thank Reviewer 1 for this suggestion. We have added a comparison
with Method X on all three benchmarks.

Results (averaged over 3 seeds):
| Method   | Dataset A | Dataset B | Dataset C |
|----------|-----------|-----------|-----------|
| Method X | 87.2±0.3  | 84.1±0.5  | 91.0±0.2  |
| Ours     | 89.5±0.4  | 86.3±0.3  | 92.1±0.3  |

Our method outperforms Method X by 2.3% on Dataset A and 2.2% on
Dataset B. We have updated Table 2 in the revised manuscript.
```

Key elements of a good response:
- **Acknowledge**: Thank the reviewer for the specific point
- **Address**: Directly answer the concern with evidence
- **Update**: State what changed in the manuscript (if applicable)

---

## Handling Common Reviewer Concerns

### 1. Misunderstandings

The reviewer misread or misunderstood part of your paper.

**Strategy**: Clarify politely without implying the reviewer was careless. The misunderstanding likely indicates unclear writing.

```
Good:
> "We apologize for the confusion in Section 3.2. To clarify,
> our method does not require paired training data. The
> formulation on page 4, Eq. (3), operates on unpaired samples.
> We have revised Section 3.2 to make this clearer."

Bad:
> "The reviewer misunderstood our method. As clearly stated
> in Section 3.2, we do not use paired data."
```

### 2. Requests for More Experiments

The reviewer wants additional baselines, datasets, or ablations.

**Strategy**: Run them if at all feasible during the rebuttal period. If not, explain why and commit to including them in the camera-ready version.

```
Good (experiment completed):
> "We have run the requested comparison with LoRA on all
> three datasets. Results in the table below show our method
> outperforms LoRA by 1.8% on average while using 30% fewer
> parameters. Updated in Table 4."

Good (experiment not feasible):
> "Training on the full ImageNet dataset requires ~200 GPU-hours,
> which exceeds our rebuttal compute budget. However, we have
> run the comparison on ImageNet-100 (a representative subset)
> and observe consistent improvements. We commit to including
> the full ImageNet results in the camera-ready version."

Bad:
> "We will add this experiment later."
```

### 3. Writing Quality Complaints

The reviewer finds the paper hard to follow or poorly written.

**Strategy**: Acknowledge the issue, describe specific improvements, and demonstrate the fix with a before/after example.

```
Good:
> "We appreciate this feedback and have significantly revised
> Section 4 for clarity. Specifically, we:
> - Restructured the method description into three clear
>   subsections (encoding, alignment, decoding)
> - Added Figure 3 to illustrate the data flow
> - Shortened the notation table and moved details to Appendix B
>
> Example revision (Section 4.1, paragraph 1):
> Before: [old text]
> After: [new text]"

Bad:
> "We will improve the writing."
```

### 4. Missing Related Work

The reviewer points out papers you did not cite.

**Strategy**: Add the citations, briefly discuss their relationship to your work, and thank the reviewer.

```
Good:
> "We thank the reviewer for pointing us to Chen et al. (2024)
> and Park et al. (2023). We have added both to Section 2:
>
> - Chen et al. (2024) address a similar problem but use
>   supervised contrastive learning, requiring labeled pairs.
>   Our approach is self-supervised.
> - Park et al. (2023) propose a complementary architecture
>   that could be combined with our method. We note this
>   as future work in Section 6."

Bad:
> "These papers are not directly related to our work."
```

### 5. Unfair Comparison Claims

The reviewer believes your experimental comparison is unfair.

**Strategy**: Provide evidence of fair protocol. If the comparison was indeed unfair, acknowledge it and provide corrected results.

```
Good:
> "We ensured fair comparison by:
> 1. Using the same training data for all methods
> 2. Matching compute budgets (all models trained for 100K steps
>    on 4 A100 GPUs)
> 3. Using the authors' official code with their recommended
>    hyperparameters
> 4. Reporting the best of 3 seeds for all methods
>
> We have added these details to Section 5.1 of the revised
> manuscript."
```

### 6. Novelty Concerns

The reviewer questions whether the contribution is sufficient.

**Strategy**: Clearly articulate what is new and why it matters. Highlight aspects the reviewer may have missed.

```
Good:
> "We appreciate this concern. While individual components
> (attention and MLP) are known, our contribution is the
> specific way they are combined: [one-sentence explanation].
> This combination is non-obvious because [reason], as
> demonstrated by:
> 1. No prior work has explored this combination (Table 1)
> 2. Naive combinations fail (ablation in Table 5, rows 3-4)
> 3. Our approach achieves a 15% improvement, suggesting the
>    combination captures something the individual parts miss"
```

---

## Examples of Good vs Bad Responses

### Example 1: Reviewer Questions Statistical Significance

```
Bad:
"Our improvements are significant."

Good:
"We report mean ± standard deviation over 5 seeds for all
experiments. On Dataset A, our improvement of 2.3% (89.5±0.4
vs 87.2±0.3) is statistically significant under a paired
t-test (p = 0.003). We have added significance indicators
to Table 2."
```

### Example 2: Reviewer Says Results Are Incremental

```
Bad:
"We respectfully disagree. Our 2% improvement is meaningful."

Good:
"While the overall accuracy improvement is 2%, we note that:
(a) this corresponds to a 15% reduction in error rate
(from 13% to 11%), (b) the improvement is consistent across
all 5 datasets (Table 2), and (c) our method additionally
reduces inference time by 40% (Table 3). We have emphasized
these aspects in the revised introduction."
```

---

## Venue-Specific Formatting

### NeurIPS
- **Platform**: OpenReview
- **Format**: Single response visible to all reviewers; character or page limit
- **Tips**: Address each reviewer with clear headers (e.g., "Response to Reviewer abc1"). Reviewers can update scores after the discussion period.

### ICML
- **Platform**: OpenReview
- **Format**: Author response with page/word limit
- **Tips**: Similar to NeurIPS. Focus on factual corrections and new evidence. Reviewers and ACs participate in discussion.

### ICLR
- **Platform**: OpenReview (public)
- **Format**: Public comments on each review; the community can also comment
- **Tips**: Responses are public. Be especially careful with tone. Other researchers may read your responses and form opinions about your work.

### ACL / EMNLP
- **Platform**: OpenReview or SoftConf
- **Format**: Structured response form, often per-reviewer; strict page limit
- **Tips**: Follow the form structure exactly. ACL often has a 1-page limit per reviewer, so be extremely concise.

---

## Timeline Management

Most venues give 5-7 days for rebuttals. Here is a recommended schedule:

| Day | Activity |
|-----|----------|
| Day 1 | Read all reviews carefully. Categorize each point (critical/important/minor). Identify experiments you can run. |
| Day 2-3 | Run additional experiments. These are your strongest evidence. |
| Day 4-5 | Draft responses for all reviewers. Have co-authors review. |
| Day 6 | Finalize responses. Polish wording. Check character/page limits. |
| Day 7 | Submit. Do a final read for tone and completeness. |

**Common mistakes in rebuttal timing**:
- Starting experiments too late -- begin Day 1
- Spending too long on minor points while neglecting critical ones
- Submitting without co-author review
- Exceeding the word/page limit (some systems truncate silently)

---

## Final Checklist

Before submitting your rebuttal:

- [ ] Every reviewer concern is addressed (even minor ones)
- [ ] Responses are specific with evidence, not vague promises
- [ ] Tone is respectful and professional throughout
- [ ] New experimental results are clearly presented with numbers
- [ ] References to specific sections, tables, and figures are included
- [ ] Co-authors have reviewed and approved the response
- [ ] Within the character/page limit for the venue
- [ ] No typos or formatting errors in the response
