"""Small modeling helpers for the public sample workflow."""

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "hype_count",
    "hope_count",
    "release_window",
    "post_sent_score",
    "post_length",
    "total_comments",
]


def fit_linear_model(modeling_table: pd.DataFrame) -> pd.DataFrame:
    """Fit an interpretable linear model and return coefficient rows."""

    data = modeling_table[modeling_table["is_dysfunction_post"]].copy()
    if len(data) < 3:
        raise ValueError("Need at least three dysfunction posts to fit the sample model.")

    x = data[FEATURE_COLUMNS].astype(float)
    y = data["oc_def"].astype(float)

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    model = LinearRegression()
    model.fit(x_scaled, y)

    return pd.DataFrame(
        {
            "variable": FEATURE_COLUMNS,
            "coefficient": model.coef_,
            "interpretation": [
                "Community attention to promotion/expectations language",
                "Community evocation of future-oriented hope language",
                "Whether the post falls within the launch window",
                "Sentiment score of the negative/dysfunction post",
                "Word length of the original post",
                "Number of comments received by the post",
            ],
        }
    ).sort_values("coefficient", ascending=False)
