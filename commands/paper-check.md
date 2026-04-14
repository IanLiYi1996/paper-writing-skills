---
allowed-tools: Bash(grep:*), Bash(find:*), Read, Grep, Glob
description: Pre-submission paper validation - checks anonymity, formatting, citations, and completeness
---

# Paper Pre-Submission Validation

Run this command on a paper project directory to check for common submission issues. Scan the LaTeX source files and report findings as a checklist.

## How to Run

The user should provide the path to their paper directory, or you should detect it from the current working directory. Look for `.tex` files and `.bib` files to identify the paper root.

## Checks to Perform

### 1. Anonymity Scan

Search all `.tex` files for potential anonymity violations:

- **Author names**: Look for common patterns like `\author{`, names in comments, or hardcoded author strings
- **Affiliations**: Search for university/company names, department names
- **Email addresses**: Search for `@` patterns that look like institutional emails (e.g., `@university.edu`, `@company.com`)
- **File paths**: Search for `/home/`, `/Users/`, `C:\Users\`, or any path containing what looks like a username
- **Acknowledgments**: Check if `\section{Acknowledgments}` or `\section*{Acknowledgments}` exists and is not commented out
- **Self-references**: Look for patterns like "our previous work", "our earlier", "we previously" that break blind review

Report each finding with the file name, line number, and the matching text.

### 2. Citation Consistency

- **Undefined citations**: Extract all `\cite{...}`, `\citet{...}`, `\citep{...}` keys from `.tex` files. Then extract all BibTeX entry keys from `.bib` files. Report any cite keys that are not defined in the bibliography.
- **Unused entries**: Report BibTeX keys that exist in `.bib` but are never cited (these generate warnings but are not critical).
- **Format consistency**: Check if citation commands are consistent (mixing `\cite` and `\citep` in venues that use natbib may indicate errors).
- **arXiv vs published**: In `.bib` files, look for entries with `journal = {arXiv}` or `eprinttype = {arXiv}` and flag them as candidates for replacement with published versions.

### 3. Figure and Table References

- **Unreferenced figures**: Find all `\label{fig:...}` definitions and check that each has a corresponding `\ref{fig:...}` or `Figure~\ref{fig:...}` in the text.
- **Unreferenced tables**: Find all `\label{tab:...}` definitions and check for corresponding `\ref{tab:...}`.
- **Missing labels**: Find `\begin{figure}` and `\begin{table}` environments that do not contain a `\label{}`.
- **Broken references**: Look for `??` in the compiled PDF or `\ref{...}` patterns where the label is not defined.

### 4. Page Count

- If a compiled PDF exists, report the page count.
- Compare against common venue limits: NeurIPS (9 pages), ICML (8 pages), ICLR (9 pages), ACL (8 pages long / 4 pages short), AAAI (7 pages).
- If the venue is detectable from the `.sty` file name, use the specific limit.

### 5. Required Sections

Check for the presence of these sections in the `.tex` files:

- [ ] Abstract (`\begin{abstract}` or `\abstract`)
- [ ] Introduction (`\section{Introduction}`)
- [ ] Conclusion (`\section{Conclusion}` or `\section{Conclusions}`)
- [ ] Limitations (`\section{Limitations}` -- required by NeurIPS, ICML, ACL)
- [ ] References / Bibliography (`\bibliography{` or `\begin{thebibliography}`)

### 6. LaTeX Quality

- **Compilation warnings**: If `main.log` exists, scan for `Warning` lines, especially overfull hbox, undefined references, and multiply defined labels.
- **Non-breaking spaces**: Check for missing `~` before `\ref{`, `\eqref{`, and `\cite{` commands (e.g., `Figure \ref` instead of `Figure~\ref`).
- **Quote style**: Look for straight quotes `"..."` that should be ``` ``...'' ```.
- **TODO markers**: Search for `TODO`, `FIXME`, `XXX`, `HACK` in all `.tex` files.

## Output Format

Present results as a structured checklist:

```
## Paper Pre-Submission Check Results

### Anonymity
- [x] No author names found in paper body
- [ ] ISSUE: Email address found in main.tex:42 -- john@university.edu
- [ ] ISSUE: File path found in appendix.tex:15 -- /home/jsmith/experiments/

### Citations
- [x] All 47 citation keys defined in references.bib
- [ ] WARNING: 3 BibTeX entries never cited (smith2020, jones2021, chen2019)
- [ ] WARNING: 5 entries appear to be arXiv preprints that may have published versions

### Figures & Tables
- [x] All 5 figures referenced in text
- [ ] ISSUE: Table tab:ablation2 defined but never referenced

### Page Count
- [x] 8 pages (within ICML limit of 8)

### Required Sections
- [x] Abstract present
- [x] Introduction present
- [x] Conclusion present
- [ ] ISSUE: Limitations section not found (required by most venues)

### LaTeX Quality
- [ ] WARNING: 3 overfull hbox warnings in main.log
- [ ] ISSUE: 12 instances of missing non-breaking space before \ref
- [x] No TODO/FIXME markers found
- [ ] WARNING: 2 instances of straight quotes found
```

Mark passing checks with [x] and issues with [ ] ISSUE or [ ] WARNING. Summarize the total count at the end: "X issues found, Y warnings."
