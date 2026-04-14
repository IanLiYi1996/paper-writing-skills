#!/usr/bin/env python3
"""Generate publication-quality academic figures using Gemini or OpenAI image generation.

This script takes a textual description of an academic figure and generates
an image using either Google Gemini or OpenAI's image generation API.

Usage:
    python generate_figure.py --description "A left-to-right pipeline..." --output figure.png
    python generate_figure.py --description @description.txt --output figure.png --provider openai
"""

import argparse
import base64
import io
import os
import sys
from pathlib import Path


SYSTEM_PROMPT = (
    "You are an expert academic figure illustrator. Generate a clean, "
    "publication-quality diagram for a top-tier ML conference paper (NeurIPS, ICML, ICLR). "
    "Use soft pastel backgrounds (10-15% opacity), medium-saturation colors for active elements, "
    "rounded rectangles for processes, cuboids for tensors, cylinders for databases. "
    "Use sans-serif fonts for labels (Arial/Roboto), serif italics only for math. "
    "Maintain strict grid alignment and consistent spacing. "
    "The figure must be clean, professional, and print-ready at 300 DPI."
)


def read_description(description: str) -> str:
    """Read description from string or file (if prefixed with @)."""
    if description.startswith("@"):
        filepath = Path(description[1:])
        if not filepath.exists():
            print(f"Error: Description file not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        return filepath.read_text(encoding="utf-8").strip()
    return description.strip()


def generate_with_gemini(
    description: str,
    output_path: Path,
    aspect_ratio: str,
) -> Path:
    """Generate a figure using Google Gemini's image generation."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print(
            "Error: google-genai package not installed. "
            "Run: uv pip install google-genai",
            file=sys.stderr,
        )
        sys.exit(1)

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"Aspect ratio: {aspect_ratio}\n\n"
        f"Figure description:\n{description}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract the image from the response
    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None and part.inline_data.mime_type.startswith("image/"):
            image_data = part.inline_data.data
            from PIL import Image

            image = Image.open(io.BytesIO(image_data))
            output_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(str(output_path), format="PNG")
            image_saved = True
            break

    if not image_saved:
        print("Error: Gemini response did not contain an image.", file=sys.stderr)
        # Print any text response for debugging
        for part in response.candidates[0].content.parts:
            if part.text:
                print(f"Model response: {part.text}", file=sys.stderr)
        sys.exit(1)

    return output_path


def generate_with_openai(
    description: str,
    output_path: Path,
    aspect_ratio: str,
) -> Path:
    """Generate a figure using OpenAI's image generation API."""
    try:
        from openai import OpenAI
    except ImportError:
        print(
            "Error: openai package not installed. Run: uv pip install openai",
            file=sys.stderr,
        )
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    # Map aspect ratios to OpenAI's supported sizes
    size_map = {
        "1:1": "1024x1024",
        "16:9": "1536x1024",
        "9:16": "1024x1536",
        "4:3": "1536x1024",
        "3:4": "1024x1536",
    }
    size = size_map.get(aspect_ratio, "1536x1024")

    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"Figure description:\n{description}"
    )

    client = OpenAI(api_key=api_key)

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            n=1,
            size=size,
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        sys.exit(1)

    # Decode and save the image
    image_data = base64.b64decode(response.data[0].b64_json)
    from PIL import Image

    image = Image.open(io.BytesIO(image_data))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(str(output_path), format="PNG")

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate publication-quality academic figures via AI image generation.",
    )
    parser.add_argument(
        "--description",
        required=True,
        help="Figure description text, or @path/to/file.txt to read from file.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path (PNG format).",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "openai"],
        default="gemini",
        help="Image generation provider (default: gemini).",
    )
    parser.add_argument(
        "--aspect-ratio",
        default="16:9",
        choices=["16:9", "9:16", "4:3", "3:4", "1:1"],
        help="Aspect ratio of the output image (default: 16:9).",
    )

    args = parser.parse_args()

    description = read_description(args.description)
    output_path = Path(args.output)

    if not description:
        print("Error: Description is empty.", file=sys.stderr)
        sys.exit(1)

    print(f"Generating figure with {args.provider} (aspect ratio: {args.aspect_ratio})...")

    if args.provider == "gemini":
        result = generate_with_gemini(description, output_path, args.aspect_ratio)
    else:
        result = generate_with_openai(description, output_path, args.aspect_ratio)

    print(f"Figure saved to: {result}")


if __name__ == "__main__":
    main()
