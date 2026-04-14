# Paper Writing Skills

Claude Code plugin for end-to-end academic paper writing. Three specialized skills covering the full lifecycle from literature review to submission, with self-contained figure generation inspired by [PaperBanana](https://github.com/IanLiYi1996/paperbanana).

## Skills

### `paper-writing` — Orchestrator

Manages the 7-phase paper writing pipeline with quality gates:

1. **Literature Foundation** — survey the field, identify the gap
2. **Contribution Crystallization** — define the one-sentence contribution
3. **Experiment Design** — design experiments that support the claim
4. **IMRAD Writing** — draft the manuscript section by section
5. **Figure Generation** — create publication-quality figures
6. **LaTeX Production** — format for the target venue
7. **Pre-Submission Validation** — anonymity, citations, formatting checks

Also includes ML reviewer psychology, bilingual Chinese/English writing tips, and rebuttal guidance.

### `academic-writing` — IMRAD Deep Guidance

Section-specific writing guidance with checklists:

- **The Narrative Principle** — your paper is a story with one clear contribution
- **5-Sentence Abstract Formula** (Farquhar) — structured abstract writing
- **Section Guides** — Introduction (funnel approach, 60+ phrases), Methods (reproducibility), Results (objective presentation), Discussion (5-step framework, 70+ phrases)
- **Writing Style** — Gopen & Swan's 7 principles, Lipton's word choice, Perez's micro-tips
- **Checklists** — 35+ checkpoints per section (Introduction, Methods, Results, Discussion)

### `paperbanana-figures` — Self-Contained Figure Generation

Generates publication-quality academic figures using a multi-agent pipeline:

1. **Context Enrichment** — structure methodology text into diagram-ready format
2. **Caption Sharpening** — transform vague captions into visual specs
3. **Reference Selection** — pick from bundled curated examples
4. **Description Planning** — generate detailed visual descriptions via in-context learning
5. **Style Refinement** — apply NeurIPS "Soft Tech & Scientific Pastels" aesthetics
6. **Image Generation** — built-in scripts calling Gemini or OpenAI APIs
7. **Visual Critique** — evaluate and iterate using Claude's vision

Includes 8 curated reference diagrams, NeurIPS style guide, and matplotlib plot generation.

## Installation

### Claude Code Plugin

```bash
# Add as marketplace
claude plugin marketplace add IanLiYi1996/paper-writing-skills

# Install
claude plugin install paper-writing-skills
```

### From GitHub

```bash
# Clone to your plugins directory
git clone https://github.com/IanLiYi1996/paper-writing-skills.git \
  ~/.claude/plugins/marketplaces/paper-writing-skills
```

## Setup

### For Figure Generation

The `paperbanana-figures` skill needs an image generation API key:

```bash
# Option 1: Google Gemini (recommended, free tier available)
export GOOGLE_API_KEY="your-key"

# Option 2: OpenAI
export OPENAI_API_KEY="your-key"
```

Install Python dependencies:

```bash
cd skills/paperbanana-figures
uv pip install -r scripts/requirements.txt
```

## Quick Start

| You want to... | Say this |
|----------------|----------|
| Start a new paper from scratch | "Help me write a NeurIPS paper" |
| Draft a specific section | "Help me write the introduction for my paper on X" |
| Generate a methodology figure | "Create a Figure 1 showing my method architecture" |
| Improve existing writing | "Review my methods section for clarity" |
| Prepare for submission | "Run pre-submission checks on my paper" |
| Write a rebuttal | "Help me write a rebuttal for these reviews" |

## Compatibility

Works standalone, but integrates with these skills when available:

| Skill | Integration |
|-------|-------------|
| `academic-research` | Literature survey in Phase 1 |
| `reference-management` | Bibliography management |
| `experiment-tracking` | Experiment design in Phase 3 |
| `latex-writing` | LaTeX formatting in Phase 6 |
| `data-visualization` | Statistical plots |
| `20-ml-paper-writing` | ML writing philosophy and conference templates |

## Repository Structure

```
paper-writing-skills/
├── .claude-plugin/marketplace.json
├── skills/
│   ├── paper-writing/          # Orchestrator (~413 lines)
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── chinese-writing-tips.md
│   │   │   ├── rebuttal-guide.md
│   │   │   └── workflow-gates.md
│   │   └── assets/
│   ├── paperbanana-figures/    # Figure generation (~311 lines)
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── generate_figure.py
│   │   │   └── generate_plot.py
│   │   ├── references/
│   │   │   ├── style-guide.md
│   │   │   ├── diagram-best-practices.md
│   │   │   └── prompts/
│   │   └── assets/reference-diagrams/
│   └── academic-writing/       # IMRAD guidance (~493 lines)
│       ├── SKILL.md
│       ├── references/         # 6 section-specific guides
│       └── assets/             # 6 checklists + templates
└── commands/
    └── paper-check.md          # Pre-submission validation
```

## License

MIT
