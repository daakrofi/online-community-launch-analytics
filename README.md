# Online Community Launch Analytics

Portfolio project based on my Warwick Business School MRes thesis:

**Hype and Hope: A Study on Online Community Defensiveness Against Negative eWOM in the Wake of Product Launches**

This repo turns the thesis workflow into a public, recruiter-readable data science project. It demonstrates how public online community text can be cleaned, transformed into NLP features, linked to launch windows, and modeled as an interpretable community-level outcome.

## Project Question

When new products launch, why do some online communities respond defensively to negative word-of-mouth while others amplify it?

The original MRes study examined launch-period Reddit communities for video games and asked whether community-level **hype** and **hope** signals were associated with the proportion of positive comments under negative performance-dysfunction posts.

## What This Repo Shows

- Public text-data cleaning patterns for posts and comments
- Deleted/removed content filtering
- Launch-window feature engineering
- Lightweight sentiment scoring for posts and comments
- Hype/hope keyword feature construction
- Defensiveness metric construction
- Regression-ready modeling table generation
- Interpretable model-output reporting

## Data Policy

The full research dataset is not included here. Raw social-platform exports can be large and may contain user-generated text that deserves careful handling even when public.

This repo includes:

- small synthetic/anonymized sample files in `data/sample/`
- compact aggregate/model output files in `data/processed/`
- a data dictionary and methodology notes in `docs/`

No dataset larger than 5GB belongs in this repository. Large raw data should be stored outside GitHub and documented with access/reproduction notes.

## Repository Structure

```text
online-community-launch-analytics/
  data/
    sample/                # small synthetic/anonymized example inputs
    processed/             # compact model outputs and aggregate summaries
  docs/
    data_dictionary.md
    ethics_and_limitations.md
    methodology.md
  examples/
    run_sample_analysis.py
  reports/
    findings_summary.md
    figures/
  src/
    community_launch_analytics/
      cleaning.py
      features.py
      modeling.py
      sentiment.py
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/run_sample_analysis.py
```

The sample analysis writes:

- `data/processed/sample_modeling_table.csv`
- `data/processed/sample_coefficients.csv`
- `reports/figures/sample_defensiveness_by_game.png`
- `reports/figures/sample_hope_hype_scatter.png`

## Key Variables

- `OC_DEF`: proportion of positive comments under negative performance-dysfunction posts
- `HYPE`: frequency of hype-related terms in a rolling pre-post window
- `HOPE`: frequency of hope-related terms in a rolling pre-post window
- `RELEASE`: whether a post falls in the release window
- `POST_SENT`: sentiment score of the post
- `COMMS`: number of comments under a post

See `docs/data_dictionary.md` for the full public-facing variable map.

## Original Finding Direction

The thesis results suggested that hope-related community language had a positive association with community defensiveness, while hype-related language was more mixed and context-dependent. The public repo focuses on reproducible workflow structure rather than publishing raw platform data.

## Portfolio Links

- Portfolio website: <https://daakrofi.github.io/meet-daniel-akrofi/>
- GitHub profile: <https://github.com/daakrofi>
- Warwick profile: <https://www.wbs.ac.uk/about/person/1950442/>
