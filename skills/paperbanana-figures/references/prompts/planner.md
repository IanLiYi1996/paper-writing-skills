# Description Planner Prompt Template

Use this template during Step 4 of the pipeline. This is the most critical prompt -- the quality of the textual description directly determines the quality of the generated image.

---

## Instructions

Using the enriched context (Step 1), sharpened caption (Step 2), and selected reference diagrams (Step 3), generate a comprehensive textual description of the figure. The description must be precise enough that an image generation model can produce the figure, or a designer could recreate it manually.

## Input

- **Enriched context**: Structured output from Step 1.
- **Sharpened caption**: Output from Step 2.
- **Selected references**: IDs and style notes from Step 3.

## Output Format

### 1. Layout Specification

- **Direction**: Left-to-right / Top-to-bottom / Radial.
- **Grid**: Rows x Columns (e.g., "3 rows x 4 columns with the top row spanning full width").
- **Aspect ratio**: 16:9 / 4:3 / 1:1 with justification.
- **Total elements**: Count of all visual elements.

### 2. Visual Elements

For each element, specify:

```
Element: [Label]
  Shape: rounded-rectangle / cuboid / cylinder / diamond / ellipse / parallelogram
  Position: Row X, Column Y (or descriptive: "top-left", "center")
  Fill color: #HEXCODE (with semantic reason)
  Border: [color] [width]px [style: solid/dashed/none]
  Text: [Label text] [font-size]pt [font-weight]
  Size: [relative: small/medium/large] or [width x height in grid units]
```

### 3. Connections

For each connection, specify:

```
Connection: [Source] --> [Target]
  Line style: solid / dashed / dotted
  Line color: #HEXCODE
  Line width: [width]px
  Arrowhead: filled-triangle / open-triangle / none
  Routing: orthogonal / curved
  Label: [optional text] [font-size]pt
```

### 4. Grouping Boxes

For each visual group, specify:

```
Group: [Group Label]
  Members: [list of element labels]
  Background: #HEXCODE (very light pastel)
  Border: [color] [width]px [style: solid/dashed]
  Padding: [value]px
  Label position: top-left / top-center
```

### 5. Color Palette Summary

List all colors used and their semantic meaning:

```
#HEXCODE - [Semantic meaning] (used for: [elements])
```

### 6. Aspect Ratio and Dimensions

- Recommended aspect ratio with justification.
- Suggested minimum resolution.

---

## Example of a Good Description

```
Layout: Left-to-right, 1 row x 5 columns, 16:9 aspect ratio.

Element: "Input Text"
  Shape: parallelogram
  Position: Column 1
  Fill: #E8F5E9 (light green, represents input data)
  Border: #81C784 1px solid
  Text: "Input Text" 10pt regular
  Size: medium

Element: "Tokenizer"
  Shape: rounded-rectangle
  Position: Column 2
  Fill: #90A4AE (gray, frozen component)
  Border: #607D8B 1px solid
  Text: "Tokenizer" 10pt regular
  Size: medium

Element: "Encoder"
  Shape: rounded-rectangle
  Position: Column 3
  Fill: #4A90D9 (blue, trainable component)
  Border: #2171B5 1px solid
  Text: "Encoder" 10pt semibold
  Size: large

Connection: "Input Text" --> "Tokenizer"
  Line: solid #555555 1.5px
  Arrowhead: filled-triangle
  Routing: orthogonal

Connection: "Tokenizer" --> "Encoder"
  Line: solid #555555 1.5px
  Arrowhead: filled-triangle
  Routing: orthogonal
  Label: "token IDs" 8pt
```
