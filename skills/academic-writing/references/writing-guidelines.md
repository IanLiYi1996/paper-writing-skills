# Academic Writing Guidelines: Quick Reference Card

A condensed reference for writing each section of an ML/AI research paper. For detailed guidance, see the section-specific guides.

---

## Section Navigation

| Section | Detailed Guide | Checklist |
|---------|---------------|-----------|
| Introduction | [introduction-guide.md](./introduction-guide.md) | [introduction-checklist.md](../assets/introduction-checklist.md) |
| Methods | [methods-guide.md](./methods-guide.md) | [methods-checklist.md](../assets/methods-checklist.md) |
| Results | [results-guide.md](./results-guide.md) | [results-checklist.md](../assets/results-checklist.md) |
| Discussion | [discussion-guide.md](./discussion-guide.md) | [discussion-checklist.md](../assets/discussion-checklist.md) |
| Style | [academic-style.md](./academic-style.md) | -- |

---

## Presentation Hierarchy

**Figure > Table > Algorithm > Equation > Text**

- Figures communicate fastest; use them for architecture, pipelines, and key results
- Tables organize quantitative comparisons efficiently
- Algorithms clarify complex multi-step procedures
- Equations formalize key mathematical relationships
- Text provides context, motivation, and interpretation

---

## Abstract (150-250 words)

**5-Sentence Formula** (Sebastian Farquhar):

1. What you achieved
2. Why this is hard or important
3. How you do it (with specialist keywords)
4. What evidence you have
5. Your most remarkable number

**Write last.** Include specific numbers. No undefined acronyms. Must be self-contained.

---

## Introduction (1-1.5 pages)

**Funnel Structure**:

1. **Research value**: Why this problem matters (1 paragraph)
2. **Prior work and gaps**: What has been done and what is missing (1-2 paragraphs)
3. **Motivation and insight**: Your key observation or inspiration (1 paragraph)
4. **Proposed method (coarse)**: High-level approach description (1 paragraph)
5. **Illustrative example**: Concrete example or Figure 1 (optional)
6. **Proposed method (fine)**: More detail on how it works (1 paragraph)
7. **Contributions list**: 2-4 concrete, verifiable bullet points

**Methods must start by page 2-3.**

---

## Related Work

**Organize by methodology, not paper-by-paper.**

For each group of related work:
1. What they did (brief summary)
2. How it connects to your problem
3. What gap remains (that you address)

| Paper Type | References | Deep Analysis |
|------------|-----------|---------------|
| Conference | 15-25 | 3-5 key papers |
| Workshop | 8-12 | 2-3 key papers |
| Journal | 30-50+ | 5-10 key papers |

---

## Methods

**Standard Structure**:
1. Problem Formalization (define input, output, objective)
2. Overview with architecture figure
3. Component details (one subsection each)
4. Training / Optimization

**Core method vs. implementation details**: If changing it would not change your scientific contribution, it is an implementation detail (put in appendix).

**Define all symbols before first use. Use consistent notation throughout.**

---

## Experiments

**Every experiment answers exactly one question.**

| Question | Design |
|----------|--------|
| Does it work? | Main comparison vs. baselines |
| Why does it work? | Ablation studies |
| When does it work? | Category/domain breakdown |
| How robust is it? | Sensitivity analysis |
| What does it learn? | Qualitative analysis |

**Always report**: mean +/- std over 3-5 runs. Error bars are mandatory.

**Ablation design**: Remove ONE component at a time. Include base model. Order by impact.

---

## Discussion

**5-Step Framework**:

1. **Summarize findings** (2-4 sentences, no verbatim repetition of Results)
2. **Relate to literature** (compare with 3-5 studies)
3. **Discuss unexpected findings** (if applicable)
4. **Broader implications** (theoretical and practical)
5. **Limitations** (3-5 genuine constraints, framed constructively)

---

## Conclusion

1. What we did (2-3 sentences)
2. Key findings (2-3 sentences)
3. Significance (1-2 sentences)
4. Limitations (1-2 sentences, brief)
5. Future work (2-3 sentences)

**Echo the introduction's opening claim.** Do not introduce new results.

---

## Writing Style Quick Rules

| Rule | Example |
|------|---------|
| No contractions | "do not" not "don't" |
| Subject-verb proximity | Keep them close; avoid long insertions |
| Stress position | Put emphasis at sentence end |
| Action in verbs | "We analyzed" not "We performed an analysis" |
| Minimize pronouns | "This result shows" not "This shows" |
| Be specific | "accuracy" or "latency" not "performance" |
| Delete filler words | Remove "actually," "basically," "very," "quite" |
| Consistent terminology | Pick one term per concept, use it everywhere |

---

## Reviewer Self-Check

Before submission, verify:

- [ ] 10-minute test: Key points graspable quickly?
- [ ] Logic chain: Motivation -> contribution holds?
- [ ] 3-sentence test: Can explain contribution in 3 sentences?
- [ ] Experiment validation: Each experiment supports a specific claim?
- [ ] Consistency: No contradictions between sections?

---

## Pre-Submission Checklist

### Content
- [ ] Abstract is self-contained with specific numbers
- [ ] Introduction clearly states 2-4 contributions
- [ ] Related work is methodologically organized and fair
- [ ] Methods enable reproduction
- [ ] All claims supported by evidence
- [ ] Limitations acknowledged constructively

### Format
- [ ] Within page limit
- [ ] Figures are high-quality vector graphics with self-contained captions
- [ ] Tables use booktabs formatting (three-line tables, no vertical rules)
- [ ] References complete and correctly formatted
- [ ] Anonymity maintained (blind review)

### Language
- [ ] No contractions
- [ ] Consistent terminology
- [ ] Appropriate hedging for uncertain claims
- [ ] Active voice for contributions, passive acceptable for procedures
