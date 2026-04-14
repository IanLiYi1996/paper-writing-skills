#!/usr/bin/env python3
"""Generate publication-quality statistical plots using matplotlib.

This script reads structured data (JSON or CSV) and generates clean,
publication-ready plots with colorblind-safe palettes and academic styling.

Usage:
    python generate_plot.py --data results.json --intent "Compare methods" --output plot.pdf
    python generate_plot.py --data results.csv --intent "Show scaling trend" --output plot.png --style presentation
"""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Okabe-Ito colorblind-safe palette
OKABE_ITO = [
    "#0072B2",  # blue
    "#E69F00",  # orange
    "#009E73",  # green
    "#CC79A7",  # pink
    "#56B4E9",  # sky blue
    "#D55E00",  # vermilion
    "#F0E442",  # yellow
    "#000000",  # black
]

MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]
LINE_STYLES = ["-", "--", "-.", ":"]


def apply_publication_style(style: str = "paper"):
    """Apply clean publication styling to matplotlib."""
    base_params = {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "legend.frameon": False,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
    }
    if style == "presentation":
        base_params.update({
            "axes.labelsize": 14,
            "axes.titlesize": 16,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "axes.linewidth": 1.2,
        })
    plt.rcParams.update(base_params)


def load_data(data_path: Path) -> dict:
    """Load data from JSON or CSV file."""
    suffix = data_path.suffix.lower()
    if suffix == ".json":
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif suffix == ".csv":
        import pandas as pd
        df = pd.read_csv(data_path)
        return {"dataframe": df}
    else:
        print(f"Error: Unsupported data format '{suffix}'. Use .json or .csv.", file=sys.stderr)
        sys.exit(1)


def plot_grouped_bar(data: dict, output_path: Path):
    """Generate a grouped bar chart."""
    categories = data["categories"]
    series_list = data["series"]
    n_groups = len(categories)
    n_series = len(series_list)
    bar_width = 0.8 / n_series
    x = np.arange(n_groups)

    fig, ax = plt.subplots(figsize=(max(6, n_groups * 1.2), 4))

    for i, series in enumerate(series_list):
        offset = (i - n_series / 2 + 0.5) * bar_width
        bars = ax.bar(
            x + offset,
            series["values"],
            bar_width * 0.9,
            label=series["name"],
            color=OKABE_ITO[i % len(OKABE_ITO)],
            edgecolor="white",
            linewidth=0.5,
        )
        # Add error bars if available
        if "errors" in series:
            ax.errorbar(
                x + offset, series["values"], yerr=series["errors"],
                fmt="none", ecolor="gray", capsize=2, linewidth=0.8,
            )

    ax.set_xlabel(data.get("xlabel", ""))
    ax.set_ylabel(data.get("ylabel", ""))
    if data.get("title"):
        ax.set_title(data["title"])
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))

    save_figure(fig, output_path)


def plot_line(data: dict, output_path: Path):
    """Generate a line chart."""
    x_values = data.get("x", list(range(len(data["series"][0]["values"]))))

    fig, ax = plt.subplots(figsize=(6, 4))

    for i, series in enumerate(data["series"]):
        ax.plot(
            x_values,
            series["values"],
            label=series["name"],
            color=OKABE_ITO[i % len(OKABE_ITO)],
            marker=MARKERS[i % len(MARKERS)],
            linestyle=LINE_STYLES[i % len(LINE_STYLES)],
            linewidth=1.5,
            markersize=5,
        )
        if "errors" in series:
            ax.fill_between(
                x_values,
                np.array(series["values"]) - np.array(series["errors"]),
                np.array(series["values"]) + np.array(series["errors"]),
                alpha=0.15,
                color=OKABE_ITO[i % len(OKABE_ITO)],
            )

    ax.set_xlabel(data.get("xlabel", ""))
    ax.set_ylabel(data.get("ylabel", ""))
    if data.get("title"):
        ax.set_title(data["title"])
    ax.legend(loc="best")

    save_figure(fig, output_path)


def plot_heatmap(data: dict, output_path: Path):
    """Generate a heatmap."""
    matrix = np.array(data["matrix"])
    row_labels = data.get("row_labels", [str(i) for i in range(matrix.shape[0])])
    col_labels = data.get("col_labels", [str(i) for i in range(matrix.shape[1])])

    fig, ax = plt.subplots(figsize=(max(5, matrix.shape[1] * 0.8), max(4, matrix.shape[0] * 0.6)))

    im = ax.imshow(matrix, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(col_labels)))
    ax.set_yticks(range(len(row_labels)))
    ax.set_xticklabels(col_labels, rotation=45, ha="right")
    ax.set_yticklabels(row_labels)

    # Annotate cells
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            val = matrix[i, j]
            color = "white" if val > (matrix.max() + matrix.min()) / 2 else "black"
            ax.text(j, i, f"{val:.1f}", ha="center", va="center", color=color, fontsize=8)

    fig.colorbar(im, ax=ax, shrink=0.8)
    if data.get("title"):
        ax.set_title(data["title"])

    save_figure(fig, output_path)


def save_figure(fig, output_path: Path):
    """Save figure in the appropriate format."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    suffix = output_path.suffix.lower()
    if suffix == ".pdf":
        fig.savefig(str(output_path), format="pdf")
        print(f"Vector plot saved to: {output_path}")
    else:
        fig.savefig(str(output_path), format="png")
        print(f"Raster plot saved to: {output_path}")

    # Also save the other format as a companion file
    if suffix == ".pdf":
        png_path = output_path.with_suffix(".png")
        fig.savefig(str(png_path), format="png")
        print(f"Companion PNG saved to: {png_path}")
    elif suffix == ".png":
        pdf_path = output_path.with_suffix(".pdf")
        fig.savefig(str(pdf_path), format="pdf")
        print(f"Companion PDF saved to: {pdf_path}")

    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(
        description="Generate publication-quality statistical plots.",
    )
    parser.add_argument(
        "--data",
        required=True,
        help="Path to data file (JSON or CSV).",
    )
    parser.add_argument(
        "--intent",
        default="",
        help="Communicative intent: what the plot should convey.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path (PDF for vector, PNG for raster).",
    )
    parser.add_argument(
        "--style",
        choices=["paper", "presentation"],
        default="paper",
        help="Visual style (default: paper).",
    )

    args = parser.parse_args()

    data_path = Path(args.data)
    output_path = Path(args.output)

    if not data_path.exists():
        print(f"Error: Data file not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    apply_publication_style(args.style)
    data = load_data(data_path)

    # Determine plot type
    plot_type = data.get("type", "grouped_bar")
    print(f"Generating {plot_type} plot (intent: {args.intent or 'not specified'})...")

    plot_dispatch = {
        "grouped_bar": plot_grouped_bar,
        "bar": plot_grouped_bar,
        "line": plot_line,
        "heatmap": plot_heatmap,
    }

    plot_fn = plot_dispatch.get(plot_type)
    if plot_fn is None:
        print(
            f"Error: Unsupported plot type '{plot_type}'. "
            f"Supported types: {', '.join(plot_dispatch.keys())}",
            file=sys.stderr,
        )
        sys.exit(1)

    plot_fn(data, output_path)


if __name__ == "__main__":
    main()
