# Introduction Section Writing Guide

A comprehensive guide to writing compelling Introduction sections for ML/AI research papers, with the funnel approach, 60+ common phrases, and before/after examples.

---

## Overview

The Introduction is your paper's opening argument. It must hook readers, establish context, identify gaps, and clearly articulate your contribution. A strong Introduction answers four questions:

1. **Why should I care?** (Broad importance)
2. **What has been done?** (Existing work)
3. **What is missing?** (Research gap)
4. **What do you do about it?** (Your contribution)

**Typical Length**: 1-1.5 pages for conference papers, 2-4 pages for journals.

**Critical Rule**: Methods must begin by page 2-3. Do not let the Introduction run long.

---

## The Funnel Approach

Start broad and narrow progressively to your specific contribution:

```
+---------------------------------------------+
|   BROAD CONTEXT: Why this area matters       |
+---------------------------------------------+
|     PRIOR WORK: What has been done           |
+---------------------------------------------+
|   RESEARCH GAP: What is missing or wrong     |
+---------------------------------------------+
|  YOUR APPROACH: What you propose             |
+---------------------------------------------+
| CONTRIBUTIONS: Specific achievements         |
+---------------------------------------------+
```

---

## Stage 1: Opening Context

**Purpose**: Hook the reader by establishing why this research area matters. Start broad enough to engage diverse readers, then narrow toward your specific problem.

**Common Phrases** (12 expressions):

1. "[Research area] has become increasingly important due to..."
2. "Understanding [phenomenon] is critical for..."
3. "Recent advances in [field] have enabled..."
4. "[Application domain] relies heavily on..."
5. "The ability to [task] has far-reaching implications for..."
6. "One of the fundamental challenges in [field] is..."
7. "With the rapid growth of [technology/data], there is an urgent need for..."
8. "[Phenomenon] plays a crucial role in..."
9. "Effective [task] is essential for..."
10. "The proliferation of [X] has created both opportunities and challenges..."
11. "[Task] remains a central problem in..."
12. "As [field] continues to evolve, [challenge] becomes increasingly important..."

**Opening Hook Patterns**:

- **Scale/Impact**: "Recommendation systems now serve over 2 billion users daily..."
- **Challenge**: "One of the fundamental challenges in interpretability is..."
- **Recent Development**: "Recent advances in chain-of-thought prompting have enabled complex reasoning, but..."
- **Concrete Example**: "Consider the challenge of diagnosing rare diseases from medical images..."

**Before/After Example**:

*BEFORE (Generic, weak hook):*
> In recent years, machine learning has become very popular. Many researchers are studying this area. It has many applications.

*AFTER (Specific, compelling):*
> Machine learning models now power systems that affect billions of users daily -- from personalized recommendations to medical diagnosis. However, these models typically require massive labeled datasets, limiting their applicability in specialized domains where data is scarce or expensive to annotate.

---

## Stage 2: Prior Work and Current State

**Purpose**: Demonstrate knowledge of the field. Acknowledge existing approaches fairly, then set up the transition to limitations.

**Common Phrases** (12 expressions):

1. "Several approaches have been proposed to address this challenge..."
2. "Prior work has primarily focused on..."
3. "Traditional methods rely on..."
4. "Recent advances leverage [technique] to improve..."
5. "A common approach is to..."
6. "Existing research has demonstrated that..."
7. "State-of-the-art methods typically employ..."
8. "One line of work explores..."
9. "Previous studies have shown that..."
10. "The dominant paradigm involves..."
11. "Researchers have proposed various techniques, including..."
12. "Building on classical [method], recent work has..."

**Before/After Example**:

*BEFORE (Dismissive):*
> Many people have worked on this problem before, but their methods do not work very well.

*AFTER (Fair, specific):*
> Several approaches have been proposed to address low-resource translation. Transfer learning from high-resource languages has shown promise (Smith et al., 2020; Johnson et al., 2021), while unsupervised methods exploit monolingual data (Brown et al., 2019). These approaches have significantly advanced the field, achieving competitive results on standard benchmarks.

---

## Stage 3: Research Gap Identification

**Purpose**: Identify what is missing, limited, or problematic. This is the pivot from "what exists" to "what you do." Make the gap clear and compelling.

**Common Phrases** (12 expressions):

1. "However, these approaches face limitations when..."
2. "Despite this progress, a key challenge remains..."
3. "Existing methods typically require [constraint], which limits..."
4. "While effective in [context], these techniques struggle with..."
5. "A significant gap exists in understanding..."
6. "Less attention has been paid to..."
7. "Current approaches do not adequately address..."
8. "One limitation of existing work is that..."
9. "These methods, however, assume [assumption], which may not hold when..."
10. "An open question is whether..."
11. "Previous work has not explored..."
12. "It remains unclear how to..."

**Before/After Example**:

*BEFORE (Vague):*
> But existing methods have some problems.

*AFTER (Specific, motivated):*
> However, these approaches face a critical limitation: they require large amounts of parallel data for each language pair, which is prohibitively expensive for most of the world's 7,000+ languages. Furthermore, transfer learning assumes linguistic similarity between source and target, limiting effectiveness for typologically distant languages.

---

## Stage 4: Proposed Approach Overview

**Purpose**: Provide a high-level description of your solution. Give readers the intuition before technical details (which belong in Methods).

**Common Phrases** (12 expressions):

1. "To address these limitations, we propose..."
2. "Our key insight is that..."
3. "In this work, we present..."
4. "We introduce [name], a novel approach that..."
5. "Our method builds on the observation that..."
6. "Motivated by [insight], we develop..."
7. "The central idea behind our approach is..."
8. "We tackle this challenge by..."
9. "Our work is based on the hypothesis that..."
10. "We leverage [technique] to overcome..."
11. "This paper presents a new framework for..."
12. "Our approach differs from prior work in that..."

**Before/After Example**:

*BEFORE (Too technical, no intuition):*
> We use a transformer architecture with 12 layers and 768 hidden dimensions, trained with cross-entropy loss and Adam optimizer.

*AFTER (Intuitive, high-level):*
> To address these challenges, we propose a meta-learning framework that learns to adapt quickly from minimal parallel examples. Our key insight is that many linguistic phenomena exhibit similar structural patterns across languages. By explicitly modeling these shared regularities, our approach enables rapid adaptation with as few as 100 parallel sentences.

---

## Stage 5: Contributions List

**Purpose**: Clearly and concisely list specific contributions. This is often the most-read part of the Introduction.

**Common Phrases** (8 expressions):

1. "Our main contributions are:"
2. "This paper makes the following contributions:"
3. "We make three key contributions:"
4. "The contributions of this work are:"
5. "In summary, our contributions are threefold:"
6. "We advance the state of the art through:"
7. "We make both methodological and empirical contributions:"
8. "The key contributions of this paper include:"

**Contribution Types**:

| Type | Format |
|------|--------|
| Methodological | "We propose [X], a novel [type] that [key feature]..." |
| Theoretical | "We provide [analysis/proof] showing that..." |
| Empirical | "We conduct extensive experiments demonstrating that..." |
| Resource | "We release [dataset/code], enabling..." |
| Analysis | "We provide insights into [phenomenon] by analyzing..." |

**Before/After Example**:

*BEFORE (Vague):*
> We propose a better method. Our experiments show good results. We provide analysis.

*AFTER (Concrete):*
> Our main contributions are:
> - We propose **MetaTranslate**, a meta-learning framework that achieves competitive translation quality with 100x less parallel data.
> - We introduce a **structural transfer mechanism** that models cross-lingual syntactic patterns.
> - Through experiments on 25 low-resource languages spanning 8 families, we demonstrate 15-30% BLEU improvements over transfer learning baselines.
> - We release our code, models, and a benchmark of 100-sentence parallel corpora for 50 endangered languages.

---

## Stage 6: Paper Organization (Optional)

Usually omitted in conference papers due to page limits. Include only for complex or non-standard paper structures.

**Common Phrases**:

1. "The rest of this paper is organized as follows:"
2. "Section X describes..., Section Y presents..., and Section Z concludes."

---

## Transition Phrases Between Stages

| Transition | Phrases |
|-----------|---------|
| Context -> Prior Work | "Several approaches have been proposed...", "Researchers have explored various techniques..." |
| Prior Work -> Gap | "However, these approaches face limitations when...", "Despite this progress, a key challenge remains..." |
| Gap -> Approach | "To address these limitations, we propose...", "Motivated by this gap, we develop..." |
| Approach -> Contributions | "Our main contributions are:", "Specifically, we contribute:" |

---

## Common Mistakes and Solutions

| Mistake | Problem | Solution |
|---------|---------|----------|
| Starting too narrow | Non-specialists lose interest | Begin with broader context |
| Dismissing prior work | Appears arrogant; offends reviewers | Acknowledge contributions first |
| Vague contributions | Cannot verify claims | Be specific: methods, numbers, resources |
| Missing gap | Unclear why work is needed | Explicitly state what is missing |
| Too much detail | Buries the lead | Save technical details for Methods |
| No hook | Fails to engage | Start with compelling motivation |
| Overclaiming | Triggers skepticism | Be precise about scope |
| Opening with cliche | "In recent years..." is tired | Use specific facts or examples |

---

## Balancing Confidence

| Too weak | Just right | Too strong |
|----------|-----------|------------|
| "We try to somewhat improve..." | "We propose [X], which achieves..." | "We completely solve... for the first time ever..." |
| "We attempt to address..." | "We demonstrate that..." | "Our method is the best..." |

---

## Checklist

For a detailed review checklist, see [introduction-checklist.md](../assets/introduction-checklist.md).
