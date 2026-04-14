# Methods Section Writing Guide

A reproducibility-focused guide for writing clear, complete Methods sections in ML/AI research papers.

---

## Overview

The Methods section is the technical heart of your paper. It must be detailed enough for reproduction while remaining clear and organized.

**Guiding Principle**: Reproducibility. Every design decision should be documented or cited. Ask yourself: "Could someone reimplement this from my description alone?"

**Typical Structure**:
```
3. Method
   3.1 Problem Formulation
   3.2 Overview / Framework (with figure)
   3.3 Component Details
       3.3.1 First component
       3.3.2 Second component
   3.4 Training / Optimization
   3.5 Implementation Details (optional, or in appendix)
```

---

## Problem Formulation

**Define all notation before first use.** Use standard notation from your field.

**Common Phrases**:

1. "Let X = {x_1, ..., x_n} denote..."
2. "We formulate the problem as follows..."
3. "Given [input], our goal is to [output]..."
4. "Formally, we define..."
5. "The task can be formulated as..."
6. "We aim to learn a function f: X -> Y that..."
7. "The objective is to minimize..."
8. "Under this formulation..."

**Good Example**:
> Let D = {(x_i, y_i)}_{i=1}^n denote our training dataset, where x_i in R^d represents input features and y_i in {1, ..., K} represents the class label. Given a new input x, our goal is to predict its label by learning a classifier f: R^d -> {1, ..., K} that minimizes the expected classification error.

**Bad Example**:
> We compute f(X) to get the output y using our model M.

The bad example uses undefined symbols (f, X, y, M) and provides no mathematical context.

---

## Overview / Framework

**Start with the bird's-eye view before diving into details.** Almost always accompanied by a figure.

**Common Phrases**:

1. "Figure X illustrates the overall architecture..."
2. "Our method consists of three main components:..."
3. "The framework operates in [number] stages:..."
4. "At a high level, the system..."
5. "The overall pipeline proceeds as follows:..."
6. "As shown in Figure X, the framework..."

**Before/After Example**:

*BEFORE (Too detailed upfront):*
> Our model uses 12 transformer layers with 768 hidden units each, dropout rate 0.1, and 12 attention heads per layer.

*AFTER (High-level first):*
> Figure 2 illustrates our framework, which consists of three stages: (1) encoding input text using a transformer-based encoder, (2) fusing multi-modal features through cross-attention, and (3) generating predictions via a classification head. We describe each component below.

---

## Describing Novel vs. Established Methods

| Method Type | How to Describe |
|-------------|-----------------|
| **Novel** (your contribution) | Full detail: equations, design rationale, pseudocode if complex |
| **Established** (prior work) | Brief description + citation: "We use multi-head attention (Vaswani et al., 2017)" |
| **Modified** (adapted from prior work) | Describe the modification and cite the original: "Following [X], we modify the attention mechanism by..." |

---

## When to Use Pseudocode

| Use Pseudocode | Do Not Use Pseudocode |
|----------------|----------------------|
| Complex multi-step procedures with branching | Standard operations (SGD, backpropagation) |
| Novel algorithms hard to describe in prose | Simple 2-3 sentence procedures |
| When math alone would be ambiguous | Well-known algorithms with existing citations |
| When the order of operations matters | When pseudocode would duplicate the text exactly |

**Pseudocode Best Practices**:
- Number lines if referenced in text
- Use meaningful variable names (not single letters in pseudocode)
- Specify Input and Output clearly
- Keep an appropriate abstraction level (not production code)

**Example**:
```
Algorithm 1: Meta-Learning Training Loop

Input:  Support sets D_s, query sets D_q, learning rates alpha, beta
Output: Trained model parameters theta

1: Initialize theta randomly
2: for each episode do
3:    Sample task T_i with support D_s^i and query D_q^i
4:    theta' <- theta
5:    for k inner steps do
6:       L_s <- loss on D_s^i with theta'
7:       theta' <- theta' - alpha * grad(L_s)
8:    end for
9:    L_q <- loss on D_q^i with theta'
10:   theta <- theta - beta * grad(L_q)
11: end for
12: return theta
```

---

## Mathematical Notation Conventions

| Element | Convention | LaTeX | Example |
|---------|------------|-------|---------|
| Scalars | Lowercase italic | `$x$, $\alpha$` | x, y, alpha |
| Vectors | Lowercase bold | `$\mathbf{h}$` | **h**, **x** |
| Matrices | Uppercase bold | `$\mathbf{W}$` | **W**, **H** |
| Sets | Calligraphic | `$\mathcal{D}$` | D, X |
| Number fields | Blackboard bold | `$\mathbb{R}$` | R, N |
| Functions | Roman/upright | `$\mathrm{softmax}$` | softmax, ReLU |

**Rules**:
- Define symbols on first use
- Use consistent notation throughout the entire paper
- Use `\ell` instead of `l` for loss (avoids confusion with 1)
- Multi-letter variable names in upright font: `\mathrm{proj}`, not italicized proj

---

## Training and Optimization

**Key Details to Specify**:

1. **Loss function** with equation
2. **Optimizer** (Adam, SGD, AdamW) with parameters (learning rate, betas, weight decay)
3. **Learning rate schedule** (warmup, decay, cosine annealing)
4. **Batch size** and number of training epochs or steps
5. **Regularization** (dropout rate, weight decay, gradient clipping)
6. **Initialization** strategy
7. **Convergence criteria**

**Common Phrases**:

1. "We train the model by minimizing..."
2. "The loss function is defined as..."
3. "We optimize using [optimizer] with learning rate..."
4. "Training proceeds for [N] epochs with batch size [B]..."
5. "We apply dropout (p = 0.1) to all layers..."
6. "Parameters are initialized using..."

---

## Core Method vs. Implementation Details

| Main Paper | Appendix |
|------------|----------|
| Key algorithmic innovations | Hardware specifications |
| Novel architectural components | Random seeds |
| Loss functions and objectives | Full hyperparameter search ranges |
| Essential hyperparameters | Training curves |
| Design rationale | Minor engineering details |

**Rule**: If changing it would not change your scientific contribution, it belongs in the appendix.

---

## Reproducibility Checklist

- [ ] Model architecture fully specified (layers, dimensions, activations)
- [ ] All hyperparameters listed or referenced in appendix
- [ ] Training procedure described (optimizer, schedule, epochs)
- [ ] Data splits clearly specified (train/validation/test proportions)
- [ ] Evaluation metrics defined precisely
- [ ] Baseline implementations explained (your own or others' code)
- [ ] Code availability statement included
- [ ] Random seeds mentioned (if results depend on initialization)
- [ ] Hardware described (if relevant for runtime comparisons)
- [ ] Software framework and version specified

---

## Method Figure Guidelines

- Show the overall architecture or pipeline as Figure 2 (or Figure 1 if it is your main contribution figure)
- Use consistent visual language (same colors and shapes for the same concepts)
- Include a legend if using non-obvious symbols
- Reference in text: "As shown in Figure 2, our framework consists of..."
- Make the figure self-contained: a reader should understand the high-level approach from the figure and caption alone

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Undefined symbols | Confuses readers, looks sloppy | Define all notation before first use |
| Insufficient detail | Cannot reproduce the work | Include all hyperparameters and design choices |
| Excessive detail in main text | Obscures key ideas | Move minor details to appendix |
| Missing citations for established methods | Appears to claim others' work | Cite standard techniques |
| Results in Methods | Wrong section | Save performance numbers for Results |
| No system figure | Hard to grasp architecture | Include at minimum one overview figure |
| Inconsistent notation | Creates confusion | Proofread all symbols for consistency |
