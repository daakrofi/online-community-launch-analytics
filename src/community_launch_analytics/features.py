"""Feature engineering for launch-window online community analytics."""

from __future__ import annotations

import re

import pandas as pd

from .sentiment import score_sentiment, sentiment_label


HYPE_TERMS = {
    "ad",
    "advertising",
    "campaign",
    "marketing",
    "promise",
    "promised",
    "promises",
    "reveal",
    "showcase",
    "standards",
    "trailer",
}

HOPE_TERMS = {
    "future",
    "hope",
    "hopefully",
    "patch",
    "potential",
    "roadmap",
    "update",
    "wish",
}

DYSFUNCTION_TERMS = {
    "broken",
    "bug",
    "buggy",
    "crash",
    "crashing",
    "glitch",
    "issue",
    "issues",
    "lag",
    "missing",
    "problem",
    "problems",
    "stutter",
    "stutters",
    "unfinished",
    "unplayable",
}


def count_terms(text: str, terms: set[str]) -> int:
    """Count exact term matches in a block of text."""

    tokens = re.findall(r"[a-z']+", str(text).lower())
    return sum(token in terms for token in tokens)


def build_modeling_table(submissions: pd.DataFrame, comments: pd.DataFrame) -> pd.DataFrame:
    """Build one row per post with text, launch-window, and comment features."""

    posts = submissions.copy()
    comms = comments.copy()

    posts["post_sent_score"] = posts["fulltext"].map(score_sentiment)
    posts["post_sentiment"] = posts["post_sent_score"].map(sentiment_label)
    posts["is_dysfunction_post"] = posts["fulltext"].map(lambda text: count_terms(text, DYSFUNCTION_TERMS) > 0)
    posts["hype_count"] = posts["fulltext"].map(lambda text: count_terms(text, HYPE_TERMS))
    posts["hope_count"] = posts["fulltext"].map(lambda text: count_terms(text, HOPE_TERMS))
    posts["days_from_release"] = (posts["created_at"] - posts["release_date"]).dt.days
    posts["release_window"] = posts["days_from_release"].between(-30, 30).astype(int)
    posts["post_length"] = posts["fulltext"].str.split().map(len)

    comms["comment_sent_score"] = comms["body"].map(score_sentiment)
    comms["comment_sentiment"] = comms["comment_sent_score"].map(sentiment_label)

    comment_summary = (
        comms.groupby(["post_id", "comment_sentiment"])
        .size()
        .unstack(fill_value=0)
        .rename(columns=lambda value: f"{value}_comments")
    )

    for column in ["negative_comments", "neutral_comments", "positive_comments"]:
        if column not in comment_summary:
            comment_summary[column] = 0

    comment_summary["total_comments"] = comment_summary[
        ["negative_comments", "neutral_comments", "positive_comments"]
    ].sum(axis=1)
    comment_summary["oc_def"] = (
        comment_summary["positive_comments"] / comment_summary["total_comments"].replace(0, pd.NA)
    ).fillna(0)

    modeling = posts.merge(comment_summary.reset_index(), on="post_id", how="left").fillna(
        {
            "negative_comments": 0,
            "neutral_comments": 0,
            "positive_comments": 0,
            "total_comments": 0,
            "oc_def": 0,
        }
    )

    return modeling[
        [
            "post_id",
            "game",
            "created_at",
            "release_date",
            "days_from_release",
            "release_window",
            "post_sent_score",
            "post_sentiment",
            "is_dysfunction_post",
            "hype_count",
            "hope_count",
            "post_length",
            "negative_comments",
            "neutral_comments",
            "positive_comments",
            "total_comments",
            "oc_def",
        ]
    ]
