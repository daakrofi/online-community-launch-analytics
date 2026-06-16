# Ethics And Limitations

## Public Data Still Needs Care

The source context for this project is public online community discussion. Public availability does not remove the need to treat user-generated text carefully.

This repo therefore does not publish the raw research export or user-level identifiers.

## What Is Included

- Synthetic/anonymized example rows
- Compact model-output tables
- Public-facing documentation of the workflow
- Cleaned reusable code

## What Is Excluded

- Raw Reddit exports
- Usernames or durable user identifiers
- Full comment dumps
- Any large dataset intended for local analysis only
- Any credentials, API keys, or private paths

## Reproducibility Boundary

The repository is designed to show the analytical workflow and portfolio-quality implementation. It is not a full open-data replication package for the MRes thesis.

## Known Limitations

- The public sample is small and illustrative.
- The sample sentiment scorer is intentionally lightweight.
- Topic modeling is described but not run in the sample workflow because embedding/topic models are heavier and require additional setup.
- Platform APIs, data availability, and terms of service can change over time.
