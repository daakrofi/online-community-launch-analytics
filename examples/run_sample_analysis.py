"""Run the public sample analysis workflow."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from community_launch_analytics.cleaning import clean_comments, clean_submissions
from community_launch_analytics.features import build_modeling_table
from community_launch_analytics.modeling import fit_linear_model


def main() -> None:
    submissions = pd.read_csv(ROOT / "data" / "sample" / "submissions_sample.csv")
    comments = pd.read_csv(ROOT / "data" / "sample" / "comments_sample.csv")

    clean_posts = clean_submissions(submissions)
    clean_comms = clean_comments(comments)
    modeling_table = build_modeling_table(clean_posts, clean_comms)
    coefficients = fit_linear_model(modeling_table)

    processed_dir = ROOT / "data" / "processed"
    figures_dir = ROOT / "reports" / "figures"
    processed_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    modeling_table.to_csv(processed_dir / "sample_modeling_table.csv", index=False)
    coefficients.to_csv(processed_dir / "sample_coefficients.csv", index=False)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 5.8))
    sns.barplot(data=modeling_table, x="game", y="oc_def", hue="release_window", errorbar=None)
    plt.title("Sample Defensiveness Metric by Game")
    plt.xlabel("Game")
    plt.ylabel("Positive comment share under dysfunction posts")
    plt.xticks(rotation=18, ha="right")
    plt.legend(title="Release window", loc="upper right")
    plt.tight_layout()
    plt.savefig(figures_dir / "sample_defensiveness_by_game.png", dpi=160)
    plt.close()

    plt.figure(figsize=(10, 5.8))
    sns.scatterplot(
        data=modeling_table,
        x="hope_count",
        y="hype_count",
        size="oc_def",
        hue="game",
        sizes=(80, 420),
        legend="brief",
    )
    plt.title("Sample Hope/Hype Signals and Defensiveness")
    plt.xlabel("Hope term count")
    plt.ylabel("Hype term count")
    plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0, loc="upper left", title="Game / OC_DEF")
    plt.tight_layout()
    plt.savefig(figures_dir / "sample_hope_hype_scatter.png", dpi=160)
    plt.close()

    print("Wrote sample modeling outputs:")
    print(f"- {processed_dir / 'sample_modeling_table.csv'}")
    print(f"- {processed_dir / 'sample_coefficients.csv'}")
    print(f"- {figures_dir / 'sample_defensiveness_by_game.png'}")
    print(f"- {figures_dir / 'sample_hope_hype_scatter.png'}")


if __name__ == "__main__":
    main()
