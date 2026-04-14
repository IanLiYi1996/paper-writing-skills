# Context Enrichment Prompt Template

Use this template during Step 1 of the pipeline. Read the user's methodology text and restructure it into a diagram-ready format.

---

## Instructions

Given the following methodology text from the paper, extract and organize the information into the structured format below. Be exhaustive -- capture every component and connection mentioned, even implicitly.

## Input

```
[Paste the methodology section, abstract, or verbal description here]
```

## Output Format

### Key Components

List every distinct module, model, process, or data structure. For each:

- **Name**: Short label suitable for a diagram box (2-4 words).
- **Type**: One of: model, module, process, data, loss, metric, external-service.
- **Description**: One sentence explaining what it does.
- **Trainable**: Yes / No / N/A.

### Data Flows

List every connection between components. For each:

- **Source**: Component name.
- **Target**: Component name.
- **What flows**: Description of the data or signal (e.g., "hidden states", "gradient", "query embeddings").
- **Directionality**: Forward / Backward / Bidirectional.

### Logical Groupings

Identify which components belong together and should be visually grouped:

- **Group name**: A descriptive label for the cluster.
- **Members**: List of component names.
- **Rationale**: Why they are grouped (e.g., "all part of the encoder stack").

### Inputs and Outputs

- **System inputs**: What enters the system from outside (e.g., "raw text", "image patches").
- **System outputs**: What the system produces (e.g., "class probabilities", "generated text").
- **Intermediate outputs**: Key intermediate representations worth showing.

### Key Innovations

List 1-3 novel contributions that should be visually emphasized in the diagram:

- **Innovation**: Short description.
- **Which components**: The components involved.
- **Suggested emphasis**: How to highlight it (e.g., "distinct color", "larger box", "annotation arrow").
