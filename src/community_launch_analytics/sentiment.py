"""Small sentiment utility used for the public sample workflow.

The thesis workflow used VADER-style sentiment scoring. This lightweight scorer keeps
the sample repo runnable without external lexicon downloads.
"""

from __future__ import annotations

import re

POSITIVE_TERMS = {
    "amazing",
    "better",
    "excited",
    "fix",
    "fixed",
    "fun",
    "great",
    "hope",
    "improved",
    "love",
    "promising",
    "stable",
    "support",
}

NEGATIVE_TERMS = {
    "bad",
    "broken",
    "bug",
    "buggy",
    "crash",
    "crashes",
    "disappointed",
    "glitch",
    "issue",
    "lag",
    "missing",
    "problem",
    "refund",
    "stutter",
    "unfinished",
    "unplayable",
}


def tokenize(text: str) -> list[str]:
    """Tokenize text into lowercase word terms."""

    return re.findall(r"[a-z']+", str(text).lower())


def score_sentiment(text: str) -> float:
    """Return a simple sentiment score in roughly the -1 to 1 range."""

    tokens = tokenize(text)
    if not tokens:
        return 0.0

    positive = sum(token in POSITIVE_TERMS for token in tokens)
    negative = sum(token in NEGATIVE_TERMS for token in tokens)
    return (positive - negative) / max(1, positive + negative)


def sentiment_label(score: float, threshold: float = 0.05) -> str:
    """Map a numeric score to negative, neutral, or positive."""

    if score > threshold:
        return "positive"
    if score < -threshold:
        return "negative"
    return "neutral"
