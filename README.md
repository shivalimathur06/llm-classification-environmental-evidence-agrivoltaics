# LLM Classification of Environmental Evidence in Agrivoltaics Research

An independent, exploratory pilot comparing an LLM's classification of environmental evidence in agrivoltaics research with manually assigned reference labels. This is a personal learning project; it is not affiliated with or endorsed by the Stockholm Environment Institute (SEI).

## Research question

Can an LLM distinguish observed, modelled, and proposed environmental outcomes in agrivoltaics research, while recognising cases that involve multiple evidence types or remain unclear?

## What I did

- Screened titles and abstracts for environmental themes, including pollinators, biodiversity, soil, habitat, ecosystem services, and vegetation.
- Manually selected 39 abstracts to cover different evidence types and challenging cases. The sample was purposive, not random.
- Defined five labels: `observed`, `modelled`, `proposed`, `multiple`, and `unclear`.
- Assigned my own labels before viewing the LLM's labels.
- Compared the LLM classifications with the original human labels using Python and the standard library.
- Reviewed five disagreements against the annotation rules and recorded a separate, provisional interpretation.

## Main result

The LLM labels matched the original human labels for **34 of 39 records (87.2%)**. This is exact agreement on a small, selected pilot sample, not a general accuracy estimate or a validated result. The original human labels are working annotations, not an independently verified gold standard.

A separate provisional review of the five disagreements yields 36/39 agreement (92.3%) against the reviewed reference labels. This secondary figure is post-review and must not be treated as independent validation or substituted for the primary result.

## Reproduce the metrics

Requires Python 3; no third-party packages are needed. From this folder, run:

```bash
python evaluate_pilot.py
```

The script checks the 39 records and label values, calculates exact agreement and nominal Cohen's kappa, produces confusion matrices and per-label metrics, and writes `reproduced_metrics.json`.

## Files

- `matched_labels_public.csv` — record metadata, original labels, LLM labels, and provisional review notes. Publisher abstracts and copied supporting phrases are intentionally excluded.
- `evaluate_pilot.py` — reproducible metric calculations.
- `results_summary.md` — interpretation, disagreement review, and limitations.
- `reproduced_metrics.json` — generated metric output after running the script.

## Limitations

- Only 39 purposively selected abstracts were evaluated; the results may not generalise to other samples, topics, or prompts.
- Classification was based on abstracts, not full texts.
- The human labels are a working reference set and were not independently reviewed by a second researcher.
- The disagreement review is provisional and based on abstracts only.
- No original human examples were labelled `unclear`, so performance for that category cannot be meaningfully assessed against the original reference labels.
- LLM confidence values, where supplied in the source run, are self-reported and are not calibrated probabilities.

This repository documents a transparent learning exercise, not a full systematic review, validated classifier, or novel classification method.
