# Findings Summary

This summary translates the MRes findings into a portfolio-readable form.

## Research Question

The project asked whether hype and hope signals in online product communities help explain why some communities respond defensively to negative word-of-mouth during product launches.

## Main Outcome

The core outcome was **online community defensiveness**, measured as the proportion of positive comments under negative performance-dysfunction posts.

## Directional Findings

- Hope-related language showed a positive association with community defensiveness in the thesis model.
- The hope relationship was not purely linear; model outputs suggested diminishing or curved effects at higher levels.
- Hype-related language was more mixed and context-dependent.
- Release-window status alone was not the strongest explanatory signal once text and community controls were included.
- User and critic reception moderated parts of the relationship between expectation language and defensiveness.

## Example Model Output

The compact coefficient table in `data/processed/final_model_regression_results.csv` includes thesis-derived final-model coefficients.

Selected coefficients:

| Variable | Coefficient | Interpretation |
|---|---:|---|
| `hope_freq_30days_std` | 0.0622 | Higher hope-language frequency was associated with higher defensiveness. |
| `hope_freq_30days_sq_log` | -0.0288 | The hope relationship showed curvature/diminishing effects. |
| `hype_freq_30days_std` | -0.0453 | Hype language had a negative main association in the final specification. |
| `user_recpt_positive_True[T.True]` | 0.0528 | Positive user reception was associated with higher defensiveness. |
| `critic_recpt_positive_True[T.True]` | 0.0346 | Positive critic reception was associated with higher defensiveness. |

## Portfolio Takeaway

The project demonstrates a full applied analytics pattern:

1. collect messy public text data
2. clean and structure it
3. extract NLP features
4. operationalize a behavioral outcome
5. build interpretable models
6. translate model results into product/community insight
