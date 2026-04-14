---
name: academic-writing
description: Deep IMRAD writing guidance for ML/AI research papers. Covers narrative structure, section-specific writing with checklists, reviewer psychology, writing style principles, and experiment design. Use when drafting any paper section (abstract, introduction, methods, results, discussion), improving academic writing quality, or structuring research arguments. Triggers on keywords like write paper, draft section, improve writing, IMRAD, manuscript.
---

# Academic Writing Skill

Deep writing guidance for ML/AI research papers following the IMRAD structure. This skill covers narrative construction, section-by-section drafting, reviewer psychology, writing style principles, and experiment design.

---

## 1. The Narrative Principle

**The single most critical insight: your paper is a story with one clear contribution, not a collection of experiments.**

Every successful ML paper centers on what Neel Nanda calls "the narrative": a short, rigorous, evidence-based technical story with a takeaway readers care about. Andrej Karpathy reinforces this: a paper should have one main idea, executed well, with everything else in service of that idea.

### Three Pillars

These must be crystal clear by the end of the introduction:

| Pillar | Description | Test |
|--------|-------------|------|
| **The What** | 1-3 specific novel claims within a cohesive theme | Can you state each claim in one sentence? |
| **The Why** | Rigorous empirical evidence supporting each claim | Would a skeptic be convinced by your experiments? |
| **The So What** | Why readers should care about these claims | Does this connect to a recognized community problem? |

### The One-Sentence Test

> "If you cannot state your contribution in one sentence, you do not yet have a paper."

Before writing anything, formulate this sentence:

```
We [verb: show/prove/demonstrate/introduce] that [specific claim]
by [method/approach], achieving [concrete evidence].
```

Examples:
- "We demonstrate that sparse autoencoders can recover interpretable features in language models by training on residual stream activations, identifying 90% of known circuit components."
- "We prove that standard RLHF fine-tuning introduces systematic biases toward verbose outputs by measuring length-reward correlations across 5 model families."

### What Makes a Contribution

A contribution is NOT:
- "We apply X to Y" (application without insight)
- "We combine A and B" (combination without principle)
- "We achieve SOTA on benchmark Z" (numbers without understanding)

A contribution IS:
- A new understanding (why something works or fails)
- A new capability (something previously impossible)
- A new method with principled motivation (not just engineering)

**Credit**: Narrative principle from Neel Nanda; single-contribution focus from Andrej Karpathy.

---

## 2. Reviewer's Perspective Self-Check

**Write every sentence as if a skeptical reviewer is reading it. Because they are.**

### Five Core Questions

Before submission, verify your paper passes these tests:

1. **The 10-Minute Test**: Can a busy reviewer grasp your key points and logic chain within 10 minutes of skimming? If not, restructure.
2. **The Logic Chain**: Does the path from motivation to contribution hold without gaps? Every claim in the introduction must be supported later.
3. **The 3-Sentence Test**: Can you explain your main contribution in three sentences to a colleague? If you struggle, the paper lacks focus.
4. **The Experiment Validation**: Does every experiment serve the narrative? Each one should answer a specific question tied to your claims.
5. **The Consistency Check**: Is Abstract -> Introduction -> Methods -> Experiments logically consistent? No contradictions, no shifting goalposts.

### What Reviewers Actually Read

Understanding reviewer behavior should drive your time allocation:

| Section | % Who Read It | Implication |
|---------|---------------|-------------|
| Abstract | 100% | Must be flawless; this is your paper's advertisement |
| Introduction | 90%+ (often skimmed) | Front-load the contribution; do not bury the lede |
| Figures | Examined before methods | Figure 1 is your most important visual; make it self-contained |
| Methods | Only if still interested | Do not put your best ideas here and nowhere else |
| Appendix | Rarely read initially | Supplementary only; never hide critical information here |

### Conference Scoring

NeurIPS uses a 1-6 scale. Understanding it helps calibrate your writing:

| Score | Label | Meaning |
|-------|-------|---------|
| 6 | Strong Accept | Top 2-3% of submissions; clear, significant, well-executed |
| 5 | Accept | Solid contribution; well-written; minor issues only |
| 4 | Borderline Accept | Interesting but has weaknesses; writing quality often tips the balance |
| 3 | Borderline Reject | Some merit but insufficient evidence or unclear presentation |
| 2 | Reject | Significant flaws in method, experiments, or writing |
| 1 | Strong Reject | Fundamental problems; not suitable for venue |

**Most papers cluster at 3-4.** The difference between a 3 and a 4 is often writing quality, not research quality. Polish matters.

### Time Allocation Rule (from Neel Nanda)

Spend approximately **equal time** on each of these four areas:

1. The abstract
2. The introduction
3. The figures
4. Everything else combined

This feels counterintuitive but reflects how readers actually encounter your paper: title, then abstract, then introduction, then figures, then maybe the rest.

---

## 3. Presentation Hierarchy

**Figure > Table > Algorithm > Equation > Text**

Always choose the most intuitive representation for your content:

- **Figures** communicate faster than any other format. A well-designed architecture diagram or result plot conveys in seconds what paragraphs of text cannot.
- **Tables** organize quantitative comparisons efficiently. Use them for benchmarks, ablations, and hyperparameter summaries.
- **Algorithms** clarify complex multi-step procedures. Use pseudocode when the logic involves branching, looping, or non-obvious ordering.
- **Equations** formalize key relationships precisely. Use them for loss functions, optimization objectives, and novel mathematical contributions.
- **Text** provides context, motivation, and interpretation. It should explain the "why" behind figures, tables, and equations rather than redundantly describe what they already show.

**One picture is worth a thousand words.** If you can visualize a concept, visualize it first. Write text to explain what the visualization means, not to replace it.

**Figures and captions must be self-contained.** A reviewer should understand the core message by looking at figures and reading captions alone, without reading the main text.

---

## 4. Section-by-Section Writing Guide

### 4.1 Abstract

**The 5-Sentence Formula** (from Sebastian Farquhar, DeepMind):

| Sentence | Purpose | Starter |
|----------|---------|---------|
| 1 | What you achieved | "We introduce...", "We prove...", "We demonstrate..." |
| 2 | Why this is hard or important | "This is challenging because...", "Despite X, current methods..." |
| 3 | How you do it (include specialist keywords for discoverability) | "Our approach leverages...", "We propose a method that..." |
| 4 | What evidence you have | "Experiments on X show...", "We validate across..." |
| 5 | Your most remarkable number or result | "Achieving X% improvement...", "Reducing Y by a factor of..." |

**Rules**:
- Write the abstract LAST, after the full paper is complete
- Target 150-250 words (check venue requirements)
- Include at least one specific number for key results
- Delete generic openings like "Large language models have achieved remarkable success..."
- No undefined acronyms
- Must be self-contained: answering What? Why? How? Evidence?

**Template**: See `assets/abstract-template.md` for a structured format.

### 4.2 Introduction

**The Funnel Approach**: Start broad (why the area matters), narrow progressively (what has been done, what is missing), then present your specific contribution.

**Target**: Maximum 1.5 pages for conference papers. Methods must begin by page 2-3.

**Seven-Stage Structure**:

1. **Research Value** (1 paragraph): Why this problem matters. Use concrete scale, specific applications, or societal impact. Avoid cliches like "In recent years..." or "With the rapid development of..."

2. **Prior Work and Gaps** (1-2 paragraphs): Acknowledge mainstream approaches and their strengths. Then identify specific limitations. Be fair but clear: "While effective for X, these methods struggle with Y because Z."

3. **Motivation and Insight** (1 paragraph): Where does your key idea come from? What observation or insight drives your approach? **Include a concrete example here** -- an illustrative example in the introduction is extremely valuable.

4. **Proposed Method (Coarse)** (1 paragraph): High-level description of your approach. Explain the core idea and why it should work. Save technical details for the Methods section.

5. **Illustrative Example** (optional but powerful): A figure, diagram, or running example that makes the intuition tangible. This often becomes Figure 1.

6. **Proposed Method (Fine)** (1 paragraph): Slightly more detail on how the approach works. Still not full technical depth.

7. **Contributions List** (2-4 bullet points): Concrete, verifiable contributions. Each bullet should be specific: "We propose X, which achieves Y" not "We propose a new method."

**Contribution bullets should be 1-2 lines each in two-column format.** Three to four bullets is the sweet spot. More suggests lack of focus.

**Detailed guide**: See `references/introduction-guide.md` for 60+ common phrases and before/after examples.
**Checklist**: See `assets/introduction-checklist.md` for 35+ review checkpoints.

### 4.3 Related Work

**Organize methodologically, NOT paper-by-paper.**

| Approach | Example |
|----------|---------|
| **Good** | "One line of work uses assumption A [refs], whereas we use assumption B because..." |
| **Bad** | "Smith et al. did X. Jones et al. did Y. Lee et al. did Z." |

**Critical Analysis Framework**:

For each group of related work, address three questions:
1. What did they do? (1-2 sentences, objective summary)
2. How does it connect to your problem? (relationship)
3. What limitation or gap remains? (that your work addresses)

| Weak (just summarizing) | Strong (positioning critically) |
|-------------------------|-------------------------------|
| "Smith et al. (2022) propose a transformer model for classification." | "Smith et al. (2022) demonstrate transformers excel at classification. However, their approach requires large labeled datasets, limiting applicability to low-resource settings -- a gap our method addresses through..." |

**Scope Guidelines**:

| Paper Type | References | Deep Analysis |
|------------|-----------|---------------|
| Conference paper | 15-25 references | 3-5 key papers analyzed in depth |
| Workshop paper | 8-12 references | 2-3 key papers |
| Journal paper | 30-50+ references | 5-10 key papers |

**Cite generously.** Reviewers often authored papers in your area. Missing obvious citations signals unfamiliarity with the field.

### 4.4 Methods

**Standard Structure**:

```
3. Method
   3.1 Problem Formalization
   3.2 Overview / Framework (with architecture figure)
   3.3 Component Details
       3.3.1 First component
       3.3.2 Second component
   3.4 Training / Optimization
```

**Core Method vs. Implementation Details**:

| Put in Main Paper | Put in Appendix |
|-------------------|-----------------|
| Key algorithmic innovations | Hardware specifications |
| Novel architectural components | Random seeds |
| Loss functions and objectives | Full hyperparameter tables |
| Essential hyperparameters | Training curves |
| Design rationale | Minor implementation tricks |

**Rule of thumb**: If changing it would not change your scientific contribution, it is an implementation detail and belongs in the appendix.

**When to Use Pseudocode**:
- Complex multi-step procedures with branching or looping: YES
- Novel algorithms that are hard to describe in prose: YES
- Standard operations (SGD, backpropagation): NO
- Simple 2-3 sentence procedures: NO

**Mathematical Notation Conventions**:

| Type | Convention | Example |
|------|------------|---------|
| Scalars | Lowercase italic | x, y, alpha |
| Vectors | Lowercase bold | **x**, **h** |
| Matrices | Uppercase bold | **W**, **A** |
| Sets | Calligraphic | D, X |
| Functions | Roman/upright | softmax, ReLU |

Define ALL symbols before first use. Use consistent notation throughout the paper. Follow field conventions.

**Detailed guide**: See `references/methods-guide.md`.
**Checklist**: See `assets/methods-checklist.md`.

### 4.5 Experiments

**Principle: Every experiment answers exactly one question.**

| Question | Experiment Design |
|----------|-------------------|
| "Does it work?" | Main comparison against baselines |
| "Why does it work?" | Ablation studies |
| "When does it work?" | Breakdown by category, domain, or data size |
| "How robust is it?" | Sensitivity analysis, different hyperparameters |
| "What does it learn?" | Qualitative analysis, visualizations, case studies |

**Standard Structure**:

```
4. Experiments
   4.1 Experimental Setup (datasets, baselines, metrics, implementation)
   4.2 Main Results (primary comparison table)
   4.3 Analysis (ablations, case studies, sensitivity)
```

**Ablation Study Design**:
- Remove ONE component at a time
- Include base model (all novel components removed)
- Order rows by impact (largest performance drop first)
- Discuss which components matter most and why

**Statistical Significance**:
- Report mean +/- std from at least 3-5 runs with different random seeds
- For small improvements (<2%), statistical significance testing is mandatory
- Use paired t-test, bootstrap confidence intervals, or McNemar's test
- Format: "89.3 +/- 0.4% accuracy (mean +/- std over 5 runs)"

**Handling Negative Results**:

| Bad | Good |
|-----|------|
| "Our method does not work on Dataset-C." | "While our method shows lower accuracy on small datasets (<1K examples), it provides substantial gains on larger datasets, suggesting the approach benefits most from abundant training data." |

Reviewers respect honesty more than cherry-picked results. Present negative findings constructively: explain why they occur and what they reveal.

**Detailed guide**: See `references/results-guide.md`.
**Checklist**: See `assets/results-checklist.md`.

### 4.6 Discussion

**5-Step Framework**:

1. **Summarize Findings** (2-4 sentences): Restate key findings at a high level, without repeating the Results section verbatim. Connect to your original research questions.

2. **Relate to Literature** (2-3 paragraphs): Position findings within existing research. Note agreements ("consistent with Smith et al.") and divergences ("unlike Jones et al., we observe..."). Compare with 3-5 highly relevant studies.

3. **Discuss Unexpected Findings** (1 paragraph, if applicable): Address surprising results constructively. Offer plausible, evidence-based explanations. Frame them as learning opportunities, not failures.

4. **Broader Implications** (1-2 paragraphs): Elevate specific findings to general principles. Discuss theoretical contributions and practical applications. Answer "so what?" for both researchers and practitioners.

5. **Limitations** (1-2 paragraphs): Acknowledge 3-5 genuine methodological constraints. Frame each constructively and connect to future work. Maintain confidence in core contributions.

**Constructive Limitation Framing**:

| Self-defeating | Constructive |
|---------------|-------------|
| "Our method has many limitations and probably will not generalize." | "While our approach demonstrates strong performance on large-scale datasets, extending to low-resource settings through few-shot techniques is a natural and promising direction for future work." |

**Detailed guide**: See `references/discussion-guide.md` for 70+ common phrases and before/after examples.
**Checklist**: See `assets/discussion-checklist.md` for 49 checkpoint items.

### 4.7 Conclusion

**Structure**:

1. What we did (2-3 sentences): Summarize your approach and contribution
2. Key findings (2-3 sentences): Most important results
3. Significance (1-2 sentences): Why this matters
4. Limitations (1-2 sentences): Brief acknowledgment
5. Future work (2-3 sentences): Specific next steps

**Echo the Introduction**: The conclusion should connect back to the opening claim.

```
Introduction: "Current methods struggle with long sequences due to O(n^2) complexity."

Conclusion:  "We have presented EfficientAttn, which reduces attention complexity
              from O(n^2) to O(n log n). Experiments confirm this enables processing
              sequences 10x longer while maintaining competitive accuracy."
```

**What NOT to include**: New results, new methods, excessive detail, apologies, or hype. Be measured and precise.

**Length**: Half to one column for conference papers, half to one page for journal papers.

---

## 5. Writing Style Principles

### 5.1 Gopen and Swan's 7 Principles of Reader Expectations

These principles are based on how readers actually process scientific prose. Violating them forces readers to spend cognitive effort on sentence structure rather than content.

| # | Principle | Rule | Example |
|---|-----------|------|---------|
| 1 | **Subject-verb proximity** | Keep subject and verb close together | BAD: "The model, which was trained on ImageNet with data augmentation and learning rate warmup, achieves 92%." GOOD: "The model achieves 92% after training on ImageNet with data augmentation and warmup." |
| 2 | **Stress position** | Place the emphasis at the end of the sentence | BAD: "Accuracy improves by 15% when using attention." GOOD: "When using attention, accuracy improves by **15%**." |
| 3 | **Topic position** | Put context first, new information after | GOOD: "Given these constraints, we propose a lightweight alternative." |
| 4 | **Old before new** | Start with familiar information, then introduce unfamiliar | Link backward to what the reader already knows, then introduce new content. |
| 5 | **One unit, one function** | Each paragraph makes exactly one point | If a paragraph makes two points, split it into two paragraphs. |
| 6 | **Action in verb** | Use verbs, not nominalizations | BAD: "We performed an analysis of the results." GOOD: "We analyzed the results." |
| 7 | **Context before new** | Set the stage before presenting technical content | Explain the intuition before showing an equation. Describe what a figure shows before referencing it. |

### 5.2 Word Choice (Zachary Lipton)

- **Be specific**: Do not write "performance" when you mean "accuracy" or "latency." Say exactly what you mean.
- **Eliminate unnecessary hedging**: Drop "may" and "can" unless you are genuinely uncertain. "Our method improves accuracy" is stronger than "Our method may improve accuracy."
- **Avoid incremental vocabulary**: Replace weak verbs ("combine," "modify," "expand") with strong ones ("develop," "propose," "introduce") when introducing novel work.
- **Delete intensifiers**: Remove "very," "highly," "extremely," "significantly" (unless reporting statistical significance). "Provides tight approximation" is better than "provides very tight approximation."

### 5.3 Micro-Level Tips (Ethan Perez)

Small changes that accumulate into significantly clearer prose:

- **Minimize ambiguous pronouns**: "This shows..." is ambiguous. Write "This result shows..." or "This comparison shows..." instead.
- **Place verbs early in sentences**: Do not make readers wait through long subordinate clauses to find the main verb.
- **Delete filler words**: Remove "actually," "basically," "quite," "essentially," "a bit," "really," "just," "very" from every sentence. Then see if anything was lost. Usually nothing is.
- **One idea per sentence**: If a sentence contains "and" joining two independent ideas, consider splitting it.

### 5.4 Formal Style Conventions

**No contractions**:
- do not (not don't), cannot (not can't), it is (not it's), we have (not we've)

**Avoid possessives** (prefer "of" constructions in formal writing):
- "the performance of the model" (not "the model's performance")
- "the accuracy of the method" (not "the method's accuracy")

**Latin phrases** with proper punctuation:
- e.g., (with comma after)
- i.e., (with comma after)
- et al. (with period, no comma before in most styles)
- cf. (compare)

**Consistent terminology**: Choose one term for a concept and use it throughout. If your method is called "TransModel," do not alternate between "the model," "the system," "the architecture," and "our approach" when referring to the same thing.

### 5.5 Precision Over Brevity (Jacob Steinhardt)

- **State assumptions formally**: Before any theoretical claim, list all assumptions explicitly.
- **Provide intuition alongside rigor**: Do not force readers to choose between understanding the idea and understanding the proof. Offer both.
- **Different terms for different concepts**: If two things are different, use different words. If they are the same, use the same word. Ambiguity is the enemy of technical writing.

---

## 6. Manuscript Drafting Workflow

### Phase 1: Planning

- Define the one-sentence contribution
- Identify target venue and page limits
- Outline the argument structure
- Organize existing figures, tables, and experimental results
- List key related work to cite

### Phase 2: First Draft

Write sections in this order (not the order they appear in the paper):

1. **Methods** first (most straightforward: describe what you built)
2. **Experiments/Results** (describe what you observed)
3. **Introduction** (now that you know your results, write the story)
4. **Discussion** (interpret the results in context)
5. **Related Work** (position against literature)
6. **Conclusion** (summarize and look forward)
7. **Abstract** LAST (compress the entire paper into 150-250 words)

### Phase 3: Revision

- Verify the logic chain: does motivation lead naturally to method, and do experiments validate the claims?
- Check all cross-references: do contribution bullets match what is actually demonstrated?
- Eliminate redundancy: if the same point appears in three sections, consolidate
- Strengthen weak spots: vague claims, missing evidence, unsupported assertions

### Phase 4: Polishing

- Grammar and spelling check
- Consistent terminology throughout
- Proper citation formatting (citet for in-text, citep for parenthetical)
- Figure and table quality (vector graphics, readable fonts, self-contained captions)
- Reference list completeness
- Anonymity check for blind review (no names, no identifying URLs, no self-citations that reveal identity)

---

## 7. Bundled Resources

### References (Detailed Guides)

| File | When to Consult |
|------|-----------------|
| `references/writing-guidelines.md` | Quick reference card for all section writing guidelines |
| `references/introduction-guide.md` | When drafting or revising the Introduction; includes 60+ phrases and funnel approach |
| `references/methods-guide.md` | When drafting Methods; reproducibility focus, pseudocode guidance, notation conventions |
| `references/results-guide.md` | When drafting Results/Experiments; objective presentation, statistical reporting |
| `references/discussion-guide.md` | When drafting Discussion; 5-step framework with 70+ phrases and before/after examples |
| `references/academic-style.md` | When polishing language; hedging, formal tone, active vs passive, article usage |

### Assets (Checklists and Templates)

| File | When to Use |
|------|-------------|
| `assets/introduction-checklist.md` | Review after drafting Introduction (35+ checkpoints) |
| `assets/methods-checklist.md` | Review after drafting Methods (30+ checkpoints) |
| `assets/results-checklist.md` | Review after drafting Results (30+ checkpoints) |
| `assets/discussion-checklist.md` | Review after drafting Discussion (49 checkpoints) |
| `assets/manuscript-template.md` | Starting a new paper from scratch |
| `assets/abstract-template.md` | Structuring an abstract |

---

## 8. Integration with Other Skills

### Routing to Complementary Skills

- **`paper-writing`**: Use for full pipeline orchestration when managing an entire paper project from research repo to submission. That skill handles the workflow; this skill handles the writing craft.
- **`paperbanana-figures`**: Use when generating publication-quality figures, architecture diagrams, or result visualizations. Route there whenever a figure needs to be created or improved.
- **`latex-writing`**: Use for LaTeX formatting, template setup, citation management, and venue-specific compilation. Route there for any formatting or typesetting questions.

### When to Use This Skill vs. Others

| Task | Use This Skill | Use Other Skill |
|------|---------------|-----------------|
| "How should I structure my introduction?" | YES | -- |
| "Help me write the discussion section" | YES | -- |
| "Set up a NeurIPS template" | -- | latex-writing |
| "Create a figure showing my architecture" | -- | paperbanana-figures |
| "Manage the full paper writing pipeline" | -- | paper-writing |
| "Improve the clarity of my methods section" | YES | -- |
| "Fix my BibTeX citations" | -- | latex-writing |
