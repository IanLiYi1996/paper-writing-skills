# Academic Style Guide

Language conventions, formal tone, and stylistic rules for ML/AI research papers.

---

## Formal Language

### Contractions

Never use contractions in academic writing:

| Avoid | Use |
|-------|-----|
| don't | do not |
| it's | it is |
| can't | cannot |
| won't | will not |
| we've | we have |
| they're | they are |
| isn't | is not |
| aren't | are not |
| wouldn't | would not |
| couldn't | could not |

### Possessive Forms

In formal academic writing, prefer "of" constructions over possessives:

| Less Formal | More Formal |
|-------------|-------------|
| the model's performance | the performance of the model |
| the method's accuracy | the accuracy of the method |
| the paper's contribution | the contribution of this paper |
| the dataset's size | the size of the dataset |
| the network's output | the output of the network |

### Colloquialisms to Avoid

| Colloquial | Formal Alternative |
|------------|-------------------|
| a lot of | numerous, many, substantial |
| get | obtain, acquire, achieve |
| kind of | somewhat, rather |
| things | factors, aspects, elements |
| stuff | materials, components |
| pretty good | reasonably effective |
| figure out | determine, identify |
| deal with | address, handle |
| big | large, substantial, significant |
| show | demonstrate, illustrate, indicate |

---

## Hedging Language

### When to Hedge

Use hedging to avoid overclaiming. Hedge when:
- Results are suggestive but not definitive
- Generalizing beyond your exact experimental setting
- Drawing theoretical conclusions from empirical data
- Comparing with prior work

### Hedging Expressions

**Verbs**: suggest, indicate, imply, appear to, seem to, tend to

**Modal verbs**: may, might, could (in order of decreasing certainty)

**Adverbs**: possibly, probably, likely, generally, typically, often, somewhat, relatively

**Phrases**:
- "It is possible that..."
- "This suggests that..."
- "The results indicate that..."
- "Evidence suggests..."
- "One possible explanation is..."

### Certainty Expressions

Use for well-established facts or your own direct observations:

**Strong**: clearly, certainly, demonstrate, establish
**Moderate**: show, reveal, confirm, generally, typically
**Direct observation**: "We observe that...", "The data show that..."

### Calibrating Hedging

| Too strong | Appropriate | Too weak |
|-----------|-------------|----------|
| "This proves our method is optimal." | "The results suggest our method offers improvements in certain scenarios." | "It seems possible that perhaps our method might sometimes maybe improve things." |
| "We solve the problem." | "We address key challenges in [domain]." | "We attempt to somewhat address..." |
| "Our method is the best." | "Our method achieves competitive results." | "Our method might be somewhat useful." |

---

## Avoiding Absolute Statements

### Word Substitutions

| Absolute | Hedged Alternative |
|----------|-------------------|
| obvious | straightforward, clear |
| always | generally, typically, in most cases |
| never | rarely, seldom |
| prove | demonstrate, show, support |
| best | effective, promising, competitive |
| perfect | highly accurate, near-optimal |
| unique | distinctive, novel |
| impossible | challenging, infeasible under current constraints |
| solve | address, tackle, mitigate |
| eliminate | reduce, minimize |

### Phrase Substitutions

| Absolute | Hedged |
|----------|--------|
| "This is the first..." | "To the best of our knowledge, this is the first..." |
| "Our method outperforms all..." | "Our method shows competitive/superior performance on..." |
| "This problem is solved." | "This problem is addressed/mitigated." |
| "We achieve state-of-the-art." | "We achieve results competitive with state-of-the-art." |

---

## Active vs. Passive Voice

### When to Use Active Voice

Use for your own contributions and actions:
- "We propose a novel framework..."
- "We conduct experiments on three datasets..."
- "Our method achieves state-of-the-art results..."
- "We observe that..."

### When to Use Passive Voice

Use for general processes or when the agent is unimportant:
- "The data were collected from online sources..."
- "Experiments were conducted using standard protocols..."
- "The model was trained for 100 epochs..."
- "The loss function is defined as..."

### Consistency

Choose one style and maintain it within paragraphs. Most ML/AI papers prefer active voice for methodology descriptions and contribution claims.

---

## Article Usage (a / an / the)

### A vs. An

Based on **sound**, not spelling:

| Sound | Article | Examples |
|-------|---------|----------|
| Consonant sound | a | a model, a URL (/ju:/), a unified approach |
| Vowel sound | an | an LSTM (/el/), an F1 score (/ef/), an hour, an MLP (/em/) |

### The (Specific Reference)

Use "the" for specific, identifiable items:
- "The proposed method..."
- "The experimental results in Table 1..."
- "The model described in Section 3..."

### No Article (General Reference)

Use no article for general concepts:
- "Neural networks are powerful..."
- "Machine learning has advanced..."
- "Pre-training improves performance..."
- "Attention mechanisms enable..."

### Common Mistakes

| Wrong | Correct | Why |
|-------|---------|-----|
| "The neural networks are powerful." | "Neural networks are powerful." | General concept, not specific |
| "A proposed method achieves..." | "The proposed method achieves..." | Specific method, needs "the" |
| "We use a BERT model." | "We use the BERT model." or "We use BERT." | BERT is specific |

---

## Numbers and Units

### Spelling Out Numbers

- Spell out at sentence start: "Twenty participants were recruited..."
- Spell out small numbers (one through nine): "We conduct three experiments..."
- Use numerals for 10 and above: "We test on 15 datasets..."
- Use numerals with units: "5 GB," "100 epochs," "32 batch size"
- Use numerals for precise measurements: "3.5% improvement"

### Units and Formatting

- Space between number and unit: "100 ms" not "100ms"
- Use standard SI abbreviations: Hz, GB, ms, s
- Be consistent throughout the paper

---

## Latin Phrases

| Phrase | Meaning | Punctuation | Example |
|--------|---------|-------------|---------|
| e.g., | for example | comma after | "...tasks (e.g., classification, regression)" |
| i.e., | that is | comma after | "...the best model (i.e., the one with highest F1)" |
| et al. | and others | period after | "Smith et al. (2020)" |
| cf. | compare | no comma | "cf. the approach of Smith et al." |
| viz. | namely | period after | "...three metrics, viz. accuracy, F1, and BLEU" |
| vs. | versus | period after | "accuracy vs. efficiency" |

---

## Transition Phrases

### Adding Information
- Furthermore, Moreover, Additionally
- In addition, Besides, What is more
- Not only...but also

### Contrasting
- However, Nevertheless, Nonetheless
- In contrast, On the other hand
- Although, While, Whereas
- Despite, In spite of

### Cause and Effect
- Therefore, Thus, Hence, Consequently
- As a result, For this reason
- Due to, Because of, Owing to

### Exemplifying
- For example, For instance
- Specifically, In particular
- Such as, Including

### Summarizing
- In summary, To summarize
- In conclusion, Overall
- To conclude, In brief

### Sequencing
- First, Second, Third
- Initially, Subsequently, Finally
- First of all, Next, Lastly

---

## Sentence Structure Best Practices

### One Idea Per Sentence

**Poor**: "The model achieves high accuracy on the benchmark dataset, which was collected from multiple sources, and we also compare it with several baselines, finding that it outperforms them in most cases."

**Better**: "The model achieves high accuracy on the benchmark dataset. This dataset was collected from multiple sources. We compare our model with several baselines. Results show that our model outperforms them in most cases."

### Minimize Ambiguous Pronouns

**Ambiguous**: "We compare our model with BERT. It achieves better results."

**Clear**: "We compare our model with BERT. Our model achieves better results."

**Rule**: When using "this," "it," "they," or "these," always clarify the referent. "This result..." not just "This..."

### Subject-Verb Proximity

**Hard to read**: "The model, which was trained on ImageNet using data augmentation, mixed precision, and learning rate warmup over 90 epochs, achieves 92% accuracy."

**Easier**: "The model achieves 92% accuracy. It was trained on ImageNet for 90 epochs using data augmentation, mixed precision, and learning rate warmup."
