# Methods Section Checklist

Use this checklist while drafting and revising your Methods section. For detailed guidance, see [methods-guide.md](../references/methods-guide.md).

---

## Problem Formulation

- [ ] All mathematical notation defined before first use
- [ ] Problem formally stated (input, output, objective)
- [ ] Used standard notation from the field when possible
- [ ] Notation is consistent throughout the entire paper
- [ ] Formulation is mathematically precise and unambiguous

---

## Overview / Framework

- [ ] Provided high-level architecture description before details
- [ ] Included system diagram or architecture figure
- [ ] Described information flow through the system
- [ ] Explained how components connect to each other
- [ ] Referenced the overview figure in text

---

## Component Details

- [ ] Each major component has its own subsection
- [ ] Novel components described in sufficient detail for reproduction
- [ ] Established techniques cited rather than re-derived
- [ ] Mathematical formulations provided where needed
- [ ] Algorithm pseudocode used for complex procedures
- [ ] Design choices and rationale explained
- [ ] Component interactions described clearly

---

## Training / Optimization

- [ ] Loss function(s) specified with equations
- [ ] Optimizer identified (Adam, SGD, AdamW, etc.)
- [ ] Learning rate specified
- [ ] Learning rate schedule described (warmup, decay, cosine)
- [ ] Batch size stated
- [ ] Number of training epochs or steps indicated
- [ ] Regularization techniques described (dropout, weight decay, etc.)
- [ ] Parameter initialization described
- [ ] Convergence criteria specified
- [ ] Gradient clipping or stabilization techniques noted (if used)

---

## Reproducibility Essentials

- [ ] Model architecture fully specified (layers, dimensions, activations)
- [ ] All key hyperparameters listed or referenced in appendix
- [ ] Dataset splits clearly defined (train/val/test proportions)
- [ ] Evaluation metrics defined precisely
- [ ] Random seeds mentioned (if results depend on initialization)
- [ ] Hardware specifications provided (if relevant for runtime)
- [ ] Software framework and version specified
- [ ] Code availability statement included

---

## Mathematical Notation

- [ ] Scalars in lowercase italic (x, alpha)
- [ ] Vectors in lowercase bold
- [ ] Matrices in uppercase bold
- [ ] Sets in calligraphic
- [ ] Functions in roman/upright font
- [ ] All symbols defined in order of appearance
- [ ] Using ell instead of l for loss (avoids confusion with 1)

---

## Figures and Algorithms

- [ ] Included system architecture figure
- [ ] Figure clearly shows component relationships
- [ ] Algorithm pseudocode provided for complex procedures (if applicable)
- [ ] Algorithm input/output clearly specified
- [ ] All figures and algorithms referenced in text
- [ ] Figures are self-contained (understandable from figure + caption)

---

## Citations

- [ ] Cited established techniques and methods used
- [ ] Cited datasets used
- [ ] Cited evaluation metrics (if non-standard)
- [ ] Cited baseline implementations
- [ ] Acknowledged prior work that your method builds on

---

## What NOT to Include

- [ ] No performance numbers (those belong in Results)
- [ ] No interpretation of outcomes (that belongs in Discussion)
- [ ] No minor implementation tricks (put in appendix)
- [ ] No subjective claims ("better," "more efficient") without evidence

---

## Quick Self-Assessment

1. **Reproducibility**: Could an expert in my field reproduce this work from my description?
2. **Clarity**: Is the architecture and methodology clear without unnecessary complexity?
3. **Completeness**: Have I specified all design choices and hyperparameters?
4. **Organization**: Does the structure flow logically from problem to solution?
5. **Precision**: Are mathematical formulations correct and unambiguous?
