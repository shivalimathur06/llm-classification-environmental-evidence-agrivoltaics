# Results and interpretation

## Primary comparison

- Records evaluated: **39**
- Exact agreement with original human labels: **34/39 (87.2%)**
- Nominal Cohen's kappa: **0.820**
- Disagreements: **5**

The primary comparison uses the original human labels as the working reference. These labels were assigned before the LLM labels were viewed, but they are not an independently verified gold standard. The sample is small and purposively selected, so these metrics describe this pilot only and do not establish generalisable accuracy.

## Five disagreements

The disagreements were reviewed against the working annotation rules using abstracts only. This was a provisional project-level review, not expert or full-text validation. Original labels remain unchanged in the dataset.

| Batch | Original human label | LLM label | Provisional reviewed label |
|---|---|---|---|
| B08 | observed | unclear | unclear |
| B17 | proposed | unclear | proposed |
| B25 | proposed | unclear | proposed |
| B36 | proposed | unclear | proposed |
| B37 | observed | unclear | unclear |

The reviewed cases suggest the LLM tended to choose `unclear` when abstracts described literature mapping, design frameworks, or potential co-benefits without clearly reporting environmental outcomes. The review also highlighted a distinction the annotation rules need to make explicit: a review that synthesises environmental outcome findings is different from one that mainly counts or categorises studies.

## Secondary comparison after provisional review

After assigning provisional reviewed labels to the five disagreement cases, the LLM labels agree with the reviewed reference on **36/39 (92.3%)**, with nominal Cohen's kappa **0.894**. This is a secondary, post-review figure. It must not replace the primary result because some labels were reconsidered after inspecting the same disagreement cases and the reviewed labels are still provisional.

## Limitations

- Only 39 selected abstracts were evaluated; the sample was purposive rather than random.
- Judgements are based on abstracts, not full texts. Some abstracts may omit details needed for classification.
- Human labels are working annotations, not an independently established gold standard.
- Provisional disagreement review is not independent expert validation.
- The original human labels contain no `unclear` examples, so model performance for this category cannot be meaningfully assessed against the primary reference.
- The B01–B39 mapping to source records was checked using supporting phrases and source abstracts; the public dataset retains record IDs and titles but excludes publisher abstracts and copied supporting phrases.

## Reproducibility

Run `python evaluate_pilot.py` using Python 3. The script verifies the number of records, unique record IDs and valid labels, then recalculates both primary and secondary comparisons.
