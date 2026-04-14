# Workflow Quality Gates

Detailed checklists for the 7-phase paper writing pipeline. Each gate must be passed before proceeding to the next phase. A single "No" on a critical item means you are not ready to advance.

---

## Gate 1: Literature Readiness

Complete this checklist after Phase 1 (Literature Foundation).

- [ ] Research gap identified and articulated in 1-2 sentences
- [ ] 3-5 closest competing methods listed with their key limitations
- [ ] Novelty claim articulated: what does your approach do that no prior work does?
- [ ] Annotated bibliography of 10-20 relevant papers complete
- [ ] Methodological lineage mapped: what techniques does your approach build on?
- [ ] Recent work checked: arXiv papers from the last 6 months reviewed
- [ ] Target venue identified (determines page limit, required sections, formatting)

**Advancement criteria**: You can clearly explain to a colleague (1) what gap exists, (2) who the competitors are and why they fall short, and (3) what your approach will do differently.

---

## Gate 2: Contribution Clarity

Complete this checklist after Phase 2 (Contribution Crystallization).

- [ ] One-sentence contribution written using the template: "We [verb] [what] which [evidence] because [why it matters]"
- [ ] All co-authors agree on the contribution framing
- [ ] The three pillars defined: The What (specific claims), The Why (evidence), The So What (why readers care)
- [ ] Figure 1 concept sketched (rough layout of the visual pitch)
- [ ] Contribution is novel: no existing paper makes the same claim
- [ ] Contribution is testable: you can design experiments to support or refute it
- [ ] Paper title drafted (can be revised later, but having a working title focuses thinking)

**Advancement criteria**: The one-sentence contribution is clear enough that a reviewer reading only that sentence would understand what the paper offers.

---

## Gate 3: Experiment Completeness

Complete this checklist after Phase 3 (Experiment Design and Execution).

- [ ] Main comparison experiments complete: your method vs. SOTA, classic, and simple baselines
- [ ] All experiments run with 3-5 random seeds; mean and standard deviation computed
- [ ] Results support the claimed contribution (if not, revisit Gate 2)
- [ ] Ablation studies complete: each proposed component removed individually
- [ ] At least one efficiency measurement included (FLOPs, memory, wall-clock time)
- [ ] Negative results documented with constructive framing
- [ ] Baselines are fair: same compute, data, and evaluation protocol for all methods
- [ ] Statistical significance tested for small improvements (< 2%)

**Advancement criteria**: The experimental evidence is strong enough to convince a skeptical reviewer that the contribution is real and meaningful.

---

## Gate 4: Draft Completeness

Complete this checklist after Phase 4 (IMRAD Writing).

- [ ] All sections present: Abstract, Introduction, Related Work, Methods, Experiments, Conclusion
- [ ] The "10-minute reviewer test" passed: a colleague who did not work on this project grasps the key contribution, approach, and results in 10 minutes
- [ ] Every experiment explicitly connected to a claim: "This experiment tests whether..."
- [ ] Introduction contains 2-4 bullet-point contributions
- [ ] Methods section starts by page 2-3
- [ ] Limitations section written (required by NeurIPS, ICML, ACL)
- [ ] No placeholder text, TODO markers, or incomplete sentences in the main body
- [ ] Abstract follows the 5-sentence formula and includes at least one key number

**Advancement criteria**: The draft is a complete, coherent document that could be read end-to-end by a reviewer without encountering gaps or confusion.

---

## Gate 5: Figure Quality

Complete this checklist after Phase 5 (Figure Generation).

- [ ] Figure 1 conveys the core idea without requiring the main text
- [ ] All figures have complete, self-contained captions
- [ ] All diagrams and plots are in vector format (PDF); only photographs use raster (PNG at 600 DPI)
- [ ] Font sizes in all figures are legible at print size (between caption and body text size)
- [ ] Color palette uses no more than 6 colors
- [ ] Figures are readable in grayscale (different line styles, markers, or patterns used)
- [ ] No titles inside figures (the caption serves this purpose)
- [ ] All figures are referenced in the text: "as shown in Figure X"

**Advancement criteria**: A reader could understand the paper's approach and key results by looking only at the figures and their captions.

---

## Gate 6: LaTeX Quality

Complete this checklist after Phase 6 (LaTeX Production).

- [ ] Paper compiles cleanly without errors
- [ ] No overfull hbox warnings in critical areas (title, abstract, main body)
- [ ] Within the venue's page limit (references and appendix excluded)
- [ ] All figures, tables, and equations referenced in text with correct labels
- [ ] Citation format matches venue requirements (\citet/\citep or \newcite/\cite)
- [ ] Non-breaking spaces (~) used before all \ref{}, \eqref{}, and \cite{} commands
- [ ] English quotes use backtick notation (``...''), not straight quotes
- [ ] Style files (.sty, .cls) are unmodified from the venue template
- [ ] Tables use booktabs (toprule/midrule/bottomrule) with no vertical lines

**Advancement criteria**: The PDF looks professionally formatted and indistinguishable from other papers at the target venue.

---

## Gate 7: Submission Readiness

Complete this checklist after Phase 7 (Pre-Submission Validation).

### Anonymity
- [ ] No author names in the paper body, headers, or footers
- [ ] No institutional affiliations visible
- [ ] No institutional email addresses
- [ ] No file paths that reveal identity (e.g., /home/username/)
- [ ] Self-citations use third person ("Zhang et al. (2023) show..." not "In our previous work...")
- [ ] Acknowledgments section removed or hidden for blind review

### Citations
- [ ] All \cite{} keys defined in the .bib file (no undefined reference warnings)
- [ ] No unused BibTeX entries generating warnings
- [ ] Conference names formatted consistently (all abbreviated or all full)
- [ ] Published versions cited over arXiv preprints where available
- [ ] All references include year, venue, and page numbers where applicable

### Formatting
- [ ] Page count within venue limits
- [ ] All required sections present (abstract, introduction, conclusion, limitations, checklist)
- [ ] Paper checklist completed (NeurIPS, ICML, ICLR all require this)
- [ ] Supplementary materials properly referenced in the main paper

### Content
- [ ] Title and abstract match the submission system fields
- [ ] No TODO, FIXME, or placeholder text anywhere in the document
- [ ] All figures and tables referenced in the text
- [ ] Keywords and subject areas selected in the submission form

### Files
- [ ] All source files included (main.tex, .bib, figures, .sty)
- [ ] No hidden metadata or .git directories in the submission package
- [ ] PDF renders correctly when opened in a standard viewer
- [ ] Supplementary PDF (if any) compiles and is complete

**Advancement criteria**: The paper is ready to submit. All automated checks pass, and a co-author has done a final read-through.
