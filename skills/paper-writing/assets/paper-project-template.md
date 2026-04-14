# Paper Project Directory Template

Use this structure when starting a new paper project. Copy the venue's LaTeX template into the root directory first, then add the supporting directories.

```
my-paper/
├── main.tex              # Main LaTeX file (from venue template)
├── references.bib        # Bibliography (all BibTeX entries)
├── Makefile              # Build commands (latexmk -pdf main.tex)
├── figures/              # All figures (vector PDF preferred)
│   ├── fig1-overview.pdf       # Figure 1: method overview / visual pitch
│   ├── fig2-architecture.pdf   # Figure 2: detailed architecture
│   ├── fig3-results.pdf        # Figure 3: main results plot
│   ├── fig4-ablation.pdf       # Figure 4: ablation study
│   └── fig5-qualitative.pdf    # Figure 5: qualitative examples
├── tables/               # Table data sources
│   ├── main-results.csv        # Raw numbers for main results table
│   └── ablation-results.csv    # Raw numbers for ablation table
├── experiments/          # Experiment configs and results
│   ├── configs/                # Training/evaluation configurations
│   │   ├── baseline.yaml
│   │   └── proposed.yaml
│   └── results/                # Raw experiment outputs
│       ├── run-seed42/
│       ├── run-seed43/
│       └── run-seed44/
├── notes/                # Writing notes and planning documents
│   ├── outline.md              # Paper outline with section sketches
│   ├── contribution.md         # One-sentence contribution + three pillars
│   ├── annotated-bib.md        # Annotated bibliography from literature review
│   └── reviews/                # Reviewer feedback (after submission)
│       ├── round1-reviews.md
│       └── rebuttal-draft.md
└── submission/           # Final submission package
    ├── main.pdf                # Compiled paper
    ├── supplementary.pdf       # Supplementary materials
    └── checklist.pdf           # Completed paper checklist (if separate)
```

## Setup Instructions

1. Create the project directory and copy the venue template:
   ```bash
   mkdir -p my-paper && cd my-paper
   cp -r /path/to/venue-template/* .
   ```

2. Verify the template compiles before making any changes:
   ```bash
   latexmk -pdf main.tex
   ```

3. Create the supporting directories:
   ```bash
   mkdir -p figures tables experiments/configs experiments/results notes/reviews submission
   ```

4. Start with the `notes/` directory: write `contribution.md` (Phase 2) and `outline.md` (Phase 4) before writing LaTeX.

## Naming Conventions

- Figures: `fig{N}-{description}.pdf` (e.g., `fig1-overview.pdf`)
- Tables: `{description}-results.csv` (e.g., `main-results.csv`)
- Experiment runs: `run-seed{N}/` (e.g., `run-seed42/`)
- Use lowercase with hyphens, no spaces in filenames
