# Methodology

This repo demonstrates the public version of an MRes research workflow for analyzing product-launch discourse in online communities.

## 1. Collect

The original study used public Reddit product-community posts and comments around video game launches. The analysis window covered pre-launch and post-launch periods, with a specific focus on launch-adjacent negative word-of-mouth.

This public repo does not include the raw research export. It includes small synthetic/anonymized sample files that preserve the workflow shape without publishing raw user text.

## 2. Clean

Cleaning rules include:

- remove missing text
- remove `[deleted]`, `[removed]`, and equivalent placeholders
- standardize timestamps
- combine title and post body into a single text field
- join comments to focal posts

## 3. Identify Performance-Dysfunction Posts

The thesis workflow used guided topic modeling and text extraction to identify posts about product performance dysfunction, including bugs, crashes, glitches, missing features, frame-rate problems, and unfinished systems.

The public sample uses a small keyword set to keep the example runnable without large embedding models.

## 4. Score Sentiment

The original workflow used VADER-style sentiment analysis. The public sample uses a small built-in lexicon so the example can run without downloads.

In a full reproduction, this step should be replaced with a validated sentiment model, error analysis, and sensitivity checks.

## 5. Engineer Hype And Hope Features

Hype-related terms capture attention to promotion, promises, trailers, standards, marketing, and firm/media expectations.

Hope-related terms capture future-oriented optimism, patches, potential, updates, roadmaps, and desired improvements.

## 6. Construct Defensiveness

The core dependent variable is:

```text
OC_DEF = positive comments under negative performance-dysfunction posts / all comments under those posts
```

This captures when a community response softens or counters negative product discourse.

## 7. Model

The thesis used regression models with controls for release window, critical reception, user reception, sequel/franchise status, community size/activity, post sentiment, post length, media, upvotes, and comment volume.

The sample runner fits a lightweight linear model on the sample data to demonstrate the modeling-table shape.
