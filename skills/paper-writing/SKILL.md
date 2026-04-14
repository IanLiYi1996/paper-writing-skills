---
name: paper-writing
description: End-to-end ML/AI paper writing orchestrator. Manages the full lifecycle from
  literature review to submission with quality gates between phases. Integrates figure
  generation, IMRAD writing, LaTeX formatting, and pre-submission validation. Includes
  bilingual Chinese/English writing tips and rebuttal guidance. Use when starting a new
  paper, planning paper structure, managing the writing pipeline, preparing for submission,
  or writing rebuttals. Triggers on write paper, new paper, prepare submission, paper
  pipeline, start writing, rebuttal.
---

# Paper Writing Orchestrator

## Overview

This skill orchestrates the end-to-end paper writing process for ML/AI conference submissions. It functions as a **project manager** that routes to specialized skills at each phase of the paper lifecycle, from initial literature review through final submission.

### What This Skill Provides

The orchestrator adds value beyond individual writing skills in four ways:

1. **Quality gates between phases** -- concrete checklists that prevent common mistakes like writing before crystallizing the contribution, or submitting without anonymity checks.
2. **ML reviewer psychology** -- understanding how reviewers actually read papers and what triggers rejection, so effort is allocated where it matters most.
3. **Bilingual Chinese/English writing tips** -- practical guidance for Chinese-speaking researchers writing in English, covering grammar patterns, LaTeX conventions, and common pitfalls.
4. **Rebuttal guidance** -- structured approach to responding to reviewer feedback with templates and venue-specific formatting.

### Companion Skills

This orchestrator works best when the following skills are also installed:

| Skill | Purpose |
|-------|---------|
| `academic-writing` | Section-level IMRAD writing guidance and checklists |
| `paperbanana-figures` | Methodology diagrams and Figure 1 generation |
| `latex-writing` | LaTeX formatting, templates, and compilation |
| `academic-research` | Literature search and paper analysis |
| `reference-management` | Citation management and BibTeX handling |
| `experiment-tracking` | Experiment logging and result organization |
| `data-visualization` | Publication-quality plots and charts |

When companion skills are not installed, the orchestrator provides inline guidance at each phase rather than routing. The pipeline still works, just with less specialized support.

---

## The 7-Phase Pipeline

Each phase has a clear goal, a set of actions, routing to specialized skills, and a quality gate that must pass before proceeding to the next phase. For detailed gate checklists, read `references/workflow-gates.md`.

### Phase 1: Literature Foundation (2-3 days)

**Goal**: Understand the landscape, identify the research gap, and frame your contribution relative to existing work.

**Actions**:
- Search for papers using arXiv, Semantic Scholar, Google Scholar, and connected databases
- Read and annotate the 10-20 most relevant papers (focus on the 3-5 closest competitors)
- Build an annotated bibliography with each paper's contribution, method, and limitation
- Identify the specific gap your work addresses
- Map the methodological lineage: what techniques does your approach build on?

**Route to**: `academic-research` skill for systematic search strategies, `reference-management` skill for bibliography management, arXiv MCP for paper retrieval.

**Gate 1 -- Literature Readiness**:
Before proceeding, you must be able to answer these three questions clearly:
1. What is the specific research gap your work fills?
2. Who are the 3-5 closest competing methods, and what are their limitations?
3. What makes your approach fundamentally different (not just incrementally better)?

If you cannot answer all three, you are not ready to write. Go back and read more.

---

### Phase 2: Contribution Crystallization (1 day)

**Goal**: Define the ONE core contribution in a single sentence.

**The Narrative Principle**: If you cannot state your contribution in one sentence, you do not yet have a paper. Every successful ML paper centers on a short, rigorous, evidence-based technical story with a takeaway that readers care about.

**Actions**:
- Write the one-sentence contribution using this template:
  > "We [verb: introduce/demonstrate/prove] [what] which [evidence/result] because [why it matters]."
- Verify the contribution is (a) novel, (b) significant, and (c) supported by your experiments
- Sketch the concept for Figure 1 -- this figure should convey the core idea at a glance
- Define the three pillars: **The What** (specific claims), **The Why** (evidence), **The So What** (why readers care)

**Examples of strong one-sentence contributions**:
- "We introduce sparse mixture-of-experts layers that reduce compute by 4x while matching dense model quality, enabling training of trillion-parameter models on commodity hardware."
- "We prove that standard fine-tuning modifies only a low-rank subspace of the weight matrix, motivating LoRA as a principled parameter-efficient alternative."

**Gate 2 -- Contribution Clarity**:
- One-sentence contribution written and approved by all co-authors
- Figure 1 concept sketched (does not need to be final)
- Three pillars (What/Why/So What) articulated
- Target venue selected (determines page limit, formatting, and required sections)

---

### Phase 3: Experiment Design and Execution (variable)

**Goal**: Design and run experiments that definitively support the claimed contribution.

**Actions**:
- Design experiments where each one answers a specific question:

| Question | Experiment Type |
|----------|-----------------|
| Does it work? | Main comparison against baselines |
| Why does it work? | Ablation studies |
| When does it work? | Analysis by category, dataset size, domain |
| How robust is it? | Sensitivity analysis, different seeds, hyperparameter sweeps |
| Is it practical? | Efficiency analysis (FLOPs, memory, wall-clock time) |

- Select baselines carefully: include SOTA methods, established classics, and simple baselines (a method that fails to beat a simple baseline loses all credibility)
- Run all experiments with 3-5 random seeds; report mean and standard deviation
- Document negative results honestly -- they strengthen the paper when framed constructively

**Route to**: `experiment-tracking` skill for logging and organizing results.

**Gate 3 -- Experiment Completeness**:
- All key experiments complete with 3-5 seeds each
- Results support the claimed contribution (if they do not, revisit Phase 2)
- Ablation studies done for every major component
- At least one efficiency/scalability measurement included
- Negative results documented with constructive framing

---

### Phase 4: IMRAD Writing (3-5 days)

**Goal**: Draft the complete manuscript following the IMRAD structure.

**Writing Order** (not the order sections appear in the paper):
1. **Methods** -- write first while details are fresh
2. **Results/Experiments** -- present evidence for each claim
3. **Introduction** -- now that you know the full story, write the setup
4. **Related Work** -- position against the literature
5. **Discussion/Conclusion** -- synthesize findings and limitations
6. **Abstract** -- write last, when you know exactly what the paper says

**Time Allocation** (from Neel Nanda): Spend approximately equal time on each of:
1. The abstract
2. The introduction
3. The figures
4. Everything else combined

This seems extreme, but reflects how reviewers actually read papers: title, abstract, introduction, figures, then maybe the rest.

**Route to**: `academic-writing` skill for section-specific guidance, templates, and checklists.

**Gate 4 -- Draft Completeness**:
- Complete draft with all sections present
- The "10-minute reviewer test": can a colleague who did not work on this project grasp the key contribution, approach, and results in 10 minutes of reading?
- Every experiment is explicitly connected to a claim ("This experiment tests whether...")
- No placeholder text or TODO markers remain in the main body

---

### Phase 5: Figure Generation (1-2 days)

**Goal**: Create all figures, with special attention to Figure 1.

**Why Figure 1 matters**: Many reviewers look at Figure 1 before reading any text. It must convey the core idea, approach, or most compelling result at a glance. A confusing Figure 1 can lose a reviewer before they reach your introduction.

**Typical ML paper figure sequence**:
- **Figure 1**: Overview/motivation -- the "elevator pitch" in visual form
- **Figure 2**: Architecture or method diagram -- detailed technical approach
- **Figure 3**: Main results -- comparison with baselines (table or plot)
- **Figure 4**: Ablation results -- what each component contributes
- **Figure 5**: Qualitative examples or case studies

**Figure requirements**:
- All figures must have **self-contained captions** -- a reader should understand the figure without reading the main text
- Use **vector format** (PDF) for all diagrams and plots; raster (PNG at 600 DPI) only for photographs
- Font sizes in figures must be legible when printed (between caption and body text size)
- Use no more than 6 colors; ensure readability in grayscale (8% of men have color vision deficiency)
- No titles inside figures -- the caption serves this purpose

**Route to**: `paperbanana-figures` skill for methodology diagrams, `data-visualization` skill for plots and charts.

**Gate 5 -- Figure Quality**:
- Figure 1 is compelling and self-explanatory
- All figures have complete, self-contained captions
- All diagrams in vector format (PDF)
- Color palette is consistent and colorblind-accessible
- No figures with unreadable text at print size

---

### Phase 6: LaTeX Production (1-2 days)

**Goal**: Format the paper in the target venue's LaTeX template.

**Actions**:
1. Copy the ENTIRE template directory (not just main.tex) to your project
2. Verify the template compiles as-is before making any changes
3. Replace content section by section, compiling after each change
4. Never modify .sty or .cls files -- these define the venue's format
5. Use the template's provided macros and commands

**Common LaTeX pitfalls**:
- Copying only main.tex without style files
- Adding packages that conflict with the template
- Exceeding the page limit after formatting
- Incorrect citation commands for the venue (\citet vs \citep vs \newcite)
- Missing non-breaking spaces before references (Figure~\ref{fig:x})

**Route to**: `latex-writing` skill for detailed LaTeX guidance, template management, and compilation workflows.

**Gate 6 -- LaTeX Quality**:
- Paper compiles cleanly without warnings
- Within the venue's page limit (references and appendix excluded)
- All figures, tables, and equations are referenced in the text
- Citation format matches venue requirements
- No overfull/underfull hbox warnings in critical areas

---

### Phase 7: Pre-Submission Validation (1 day)

**Goal**: Final systematic checks before clicking "Submit."

**Actions**:
- **Anonymity scan**: Search for author names, affiliations, institutional email addresses, file paths, and acknowledgments that reveal identity
- **Citation check**: Verify all \cite{} keys are defined in the .bib file; use consistent formatting; prefer published versions over arXiv preprints when available
- **Format check**: Confirm page count, required sections (abstract, introduction, conclusion, limitations for most venues), and checklist completion
- **Content check**: Verify title and abstract match the submission form; no TODO markers; all figures and tables referenced
- **File check**: Ensure all source files are included; no hidden metadata (.git folders, file paths)

**Route to**: Run the `/paper-check` command for automated validation.

**Gate 7 -- Submission Readiness**:
- All automated checks pass (anonymity, citations, formatting)
- Paper has been proofread by at least one co-author
- Supplementary materials are complete and properly referenced
- Submission form fields match the paper content
- Camera-ready checklist items addressed (if applicable)

For the complete gate checklists with yes/no checkpoints, read `references/workflow-gates.md`.

---

## ML Paper Writing Strategy

### Reviewer Psychology

Understanding how reviewers behave helps you allocate effort effectively.

**What reviewers actually read** (in order):

| Section | % Who Read It | Implication |
|---------|---------------|-------------|
| Title + Abstract | 100% | Must be perfect; first and often only impression |
| Introduction | 90%+ (often skimmed) | Front-load the contribution; do not bury the lede |
| Figures | Examined before methods | Figure 1 is your visual abstract |
| Methods | Only if interested after intro | Technical depth matters but clarity matters more |
| Experiments | Scanned for tables/numbers | Bold your best results; make tables self-explanatory |
| Appendix | Rarely | Supplementary details only |

**Scoring**: NeurIPS uses a 6-point scale: 1 (Strong Reject) through 6 (Strong Accept). Most accepted papers score 5-6 from at least one reviewer. Borderline papers (scores of 3-4) live or die by the meta-reviewer's reading of the discussion.

### Common Rejection Reasons and Mitigations

| # | Rejection Reason | Mitigation |
|---|-----------------|------------|
| 1 | **Unclear contribution** | Write the one-sentence contribution (Phase 2). If you struggle, the contribution may not exist yet. |
| 2 | **Weak baselines** | Include SOTA, classic methods, AND simple baselines. Unfair or outdated baselines undermine all results. |
| 3 | **Missing ablations** | Remove one component at a time. If you claim 3 contributions, show what happens without each one. |
| 4 | **Poor writing quality** | Follow the time allocation rule. Have a native speaker proofread. Use Grammarly as a first pass. |
| 5 | **Overclaiming** | Match claims to evidence exactly. Replace "significantly outperforms" with "outperforms by X% (p < 0.05)." |
| 6 | **Missing related work** | Check the last 6 months of arXiv. Cite generously -- reviewers may have authored relevant papers. |
| 7 | **Insufficient analysis** | Add error analysis, failure cases, and qualitative examples. Show you understand when your method fails. |
| 8 | **Reproducibility concerns** | Report all hyperparameters, seeds, compute requirements. Consider releasing code. |

### Ablation Study Design

A well-designed ablation study is often the difference between acceptance and rejection:

1. **Full model**: Your complete approach with all components
2. **Remove one component at a time**: Each row removes exactly one thing
3. **Base model**: Remove ALL proposed components (this is effectively a baseline)
4. **Order by impact**: Present the most impactful component first
5. **Report mean +/- std**: At least 3 seeds; format as "89.3 +/- 0.4"

### Baseline Selection Principles

- **SOTA**: The current best method on your benchmarks (check paperswithcode.com)
- **Classic**: Well-established methods that reviewers expect to see
- **Simple**: A trivially simple approach (e.g., linear probe, majority class, random)
- **Ablation baseline**: Your method minus all proposed components
- **Fairness**: Same compute budget, same data, same evaluation protocol

If your method cannot beat a simple baseline, do not submit. If it beats SOTA by a small margin, you need ablations and analysis to justify the contribution.

---

## Bilingual Writing Tips

This section summarizes the most common issues for Chinese-speaking researchers writing ML papers in English. For the complete guide in Chinese, read `references/chinese-writing-tips.md`.

### Common English Mistakes

| Pattern | Incorrect | Correct |
|---------|-----------|---------|
| Article omission (冠词遗漏) | "We propose method" | "We propose a method" |
| Article overuse | "The deep learning is powerful" | "Deep learning is powerful" |
| Singular/plural (单复数) | "Many method" | "Many methods" |
| Run-on sentences (长句) | One sentence spanning 4+ lines | Break into 2-3 sentences |
| Contractions (缩写) | "don't", "it's", "can't" | "do not", "it is", "cannot" |
| Possessives (所有格) | "method's performance" | "the performance of the method" |
| Absolute language (绝对化) | "always", "never", "obvious" | "generally", "rarely", "straightforward" |

### LaTeX Conventions

- **Non-breaking spaces**: Use `~` before all references: `Figure~\ref{fig:x}`, `Table~\ref{tab:x}`, `Section~\ref{sec:x}`, `Equation~\eqref{eq:x}`
- **Proper quotes**: Use ``` ``quoted text'' ``` (backticks + single quotes), never `"straight quotes"`
- **Citations**: Use `\citet{key}` when the author is the grammatical subject ("Smith et al. (2020) show..."), use `\citep{key}` for parenthetical references ("as shown in prior work (Smith et al., 2020)")
- **Tables**: Use `booktabs` package with `\toprule`, `\midrule`, `\bottomrule` -- never draw vertical lines
- **Latin abbreviations**: Always include the comma: `e.g.,` `i.e.,` (and note `et al.` ends with a period)

### Mathematical Notation Conventions

| Type | Convention | LaTeX |
|------|-----------|-------|
| Scalars (标量) | Lowercase italic | `$x$`, `$\ell$` |
| Vectors (向量) | Lowercase bold | `$\mathbf{x}$` or `$\boldsymbol{\theta}$` |
| Matrices (矩阵) | Uppercase bold | `$\mathbf{A}$`, `$\mathbf{W}$` |
| Sets (集合) | Calligraphic | `$\mathcal{D}$`, `$\mathcal{X}$` |
| Number fields (数域) | Blackboard bold | `$\mathbb{R}$`, `$\mathbb{E}$` |
| Multi-letter operators | Upright text | `$\textrm{softmax}(x)$`, not `$softmax(x)$` |

Use `\DeclareMathOperator{\softmax}{softmax}` for operators that appear frequently. Never leave multi-letter names in italic -- it makes each letter look like a separate variable.

For the complete Chinese writing tips guide, read `references/chinese-writing-tips.md`.

---

## Rebuttal Writing Guide

Rebuttals are your chance to address reviewer concerns and change scores. The typical rebuttal period is 5-7 days.

### Core Principles

1. **Respond to every point** -- even minor ones. Skipping a concern signals you cannot address it.
2. **Structure**: Acknowledge the concern, Address it directly, provide Evidence.
3. **Tone**: Open with gratitude: "We thank the reviewer for their insightful feedback." Remain respectful even when disagreeing.
4. **Be specific**: Replace "we will add more experiments" with "we ran experiment X on dataset Y, achieving Z% improvement (see updated Table 3)."
5. **Provide new evidence**: Additional experiments run during the rebuttal period are the strongest form of response.

### Response Template

For each reviewer comment:
```
> [R1-Q2] "The comparison with Method X is missing."

We thank Reviewer 1 for this suggestion. We have added a comparison
with Method X on all three benchmarks. Our method outperforms Method X
by 2.3% on Dataset A (Table 2, row 5) and 1.8% on Dataset B.
The updated results are included in the revised manuscript.
```

### Handling Common Reviewer Concerns

| Concern Type | Strategy |
|-------------|----------|
| Misunderstanding | Clarify politely: "We apologize for the confusion. To clarify, ..." |
| Request for more experiments | Run them if at all possible during the rebuttal period. If not feasible, explain why and commit to camera-ready. |
| Writing quality | Acknowledge and list specific improvements made |
| Missing related work | Add the citations, discuss the relationship, and thank the reviewer for the pointer |
| Unfair comparison claims | Provide evidence of fair experimental protocol (same compute, data, evaluation) |

### Venue-Specific Formatting

- **NeurIPS**: Direct author response via CMT/OpenReview; limited character count
- **ICML**: Author response form on OpenReview
- **ICLR**: Public comments on OpenReview; other reviewers and the public can see your response
- **ACL/EMNLP**: Response form via SoftConf/OpenReview; structured per-reviewer responses

For detailed rebuttal templates and examples, read `references/rebuttal-guide.md`.

---

## Skill Integration Map

This table shows which skill to route to at each pipeline phase, and what to do if that skill is not installed.

| Phase | Primary Skill(s) | Fallback (if not installed) |
|-------|------------------|-----------------------------|
| 1. Literature Foundation | `academic-research`, `reference-management` | Use web search, arXiv MCP server, Semantic Scholar API |
| 2. Contribution Crystallization | (orchestrator-native) | Follow the template and gates in this skill |
| 3. Experiment Design | `experiment-tracking` | Use MLflow, W&B, or manual tracking in CSV/JSON |
| 4. IMRAD Writing | `academic-writing` | Follow inline IMRAD guidance and section checklists |
| 5. Figure Generation | `paperbanana-figures`, `data-visualization` | Use `scientific-schematics` skill or matplotlib/seaborn |
| 6. LaTeX Production | `latex-writing` | Follow template instructions; compile with latexmk |
| 7. Pre-Submission Validation | `/paper-check` command | Run manual checklist from `references/workflow-gates.md` |

When routing to a skill, provide it with the context from the current phase: the contribution statement, experiment results, or draft text as appropriate. The orchestrator maintains the overall narrative thread while specialized skills handle the details.

---

## Quick Start

Tell the orchestrator where you are in the process, and it will route you to the right phase.

| Your Situation | Start Here |
|---------------|------------|
| "I want to start a new paper" | Phase 1 (Literature Foundation) -- build your understanding first |
| "I have results, help me write" | Phase 2 (Contribution Crystallization) -- define the one-sentence contribution before drafting |
| "I have a draft, help me improve it" | Jump to the relevant phase -- use the gate checklists to identify what needs work |
| "I need to format my paper" | Phase 6 (LaTeX Production) -- get the template set up and content migrated |
| "Help me prepare for submission" | Phase 7 (Pre-Submission Validation) -- run `/paper-check` and address findings |
| "I need to write a rebuttal" | Go directly to the Rebuttal Writing Guide section above |
| "I want to start a new project directory" | Read `assets/paper-project-template.md` for the recommended structure |

For any starting point, the orchestrator will assess what gates you have already passed and recommend the next action. When in doubt, start earlier in the pipeline -- it is faster to confirm a gate is passed than to discover later that it was not.
