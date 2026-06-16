# Data Dictionary

Public-facing variable dictionary adapted from the MRes thesis.

| Label | Description / Operationalization | Source |
|---|---|---|
| `OC_DEF` | Online community defensiveness: proportion of positive comments under negative-sentiment performance dysfunction posts. | Text mining |
| `HYPE` | Community attention to firm/media promotion material, measured as frequency of hype-related words in a rolling pre-post window. | Text mining |
| `HOPE` | Community evocations of hope, measured as frequency of hope-related words in a rolling pre-post window. | Text mining |
| `STUDIO` | Reputation perceptions of the game studio. | External reputation sources |
| `CRITR` | Critical reception of the game upon release. | Metacritic |
| `USERR` | Consumer/player reception of the game upon release. | Metacritic |
| `RELEASE` | Whether the post falls within the release window, defined as 30 days before through 30 days after release. | Feature engineered |
| `SEQUEL` | Whether the game is a direct sequel. | Desk research |
| `FRANCHISE` | Whether the game belongs to a franchise. | Desk research |
| `SIZE` | Community size at launch. | Community metadata |
| `WAIT` | Time from community activation or product announcement to release. | Feature engineered |
| `ACTIVITY` | Number of posts made in the 24 hours before a focal post. | Platform metadata |
| `POST_LE` | Word length of the focal post. | Text mining |
| `POST_SENT` | Sentiment score of the focal post. | Text mining |
| `MEDIA` | Whether the post includes image/video media. | Platform metadata |
| `UPVOTE` | Upvote ratio or score of the post. | Platform metadata |
| `COMMS` | Number of comments received by the post. | Platform metadata |

## Sample Data Columns

`data/sample/submissions_sample.csv`

- `post_id`: anonymized post identifier
- `game`: product/community label
- `created_at`: post timestamp
- `release_date`: product release date
- `title`: synthetic/anonymized post title
- `selftext`: synthetic/anonymized post body

`data/sample/comments_sample.csv`

- `comment_id`: anonymized comment identifier
- `post_id`: post identifier used for joining to submissions
- `created_at`: comment timestamp
- `body`: synthetic/anonymized comment text
