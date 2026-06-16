"""Cleaning helpers for public online-community post and comment data."""

from __future__ import annotations

import re

import pandas as pd


REMOVED_PATTERN = re.compile(r"^\s*(\[deleted\]|\[removed\]|\[deleted by user\])\s*$", re.IGNORECASE)


def _is_valid_text(value: object) -> bool:
    if value is None or pd.isna(value):
        return False
    text = str(value).strip()
    return bool(text) and not REMOVED_PATTERN.match(text)


def clean_submissions(submissions: pd.DataFrame) -> pd.DataFrame:
    """Return cleaned submissions with a combined `fulltext` field.

    Expected input columns:
    - `post_id`
    - `game`
    - `created_at`
    - `title`
    - `selftext`
    - `release_date`
    """

    required = {"post_id", "game", "created_at", "title", "selftext", "release_date"}
    missing = required.difference(submissions.columns)
    if missing:
        raise ValueError(f"Missing submission columns: {sorted(missing)}")

    clean = submissions.copy()
    clean = clean[clean["title"].map(_is_valid_text)]
    clean = clean[clean["selftext"].map(_is_valid_text)]
    clean["created_at"] = pd.to_datetime(clean["created_at"], utc=True)
    clean["release_date"] = pd.to_datetime(clean["release_date"], utc=True)
    clean["fulltext"] = clean["title"].str.strip() + " " + clean["selftext"].str.strip()
    return clean.reset_index(drop=True)


def clean_comments(comments: pd.DataFrame) -> pd.DataFrame:
    """Return cleaned comments with valid body text and timestamps."""

    required = {"comment_id", "post_id", "created_at", "body"}
    missing = required.difference(comments.columns)
    if missing:
        raise ValueError(f"Missing comment columns: {sorted(missing)}")

    clean = comments.copy()
    clean = clean[clean["body"].map(_is_valid_text)]
    clean["created_at"] = pd.to_datetime(clean["created_at"], utc=True)
    return clean.reset_index(drop=True)
