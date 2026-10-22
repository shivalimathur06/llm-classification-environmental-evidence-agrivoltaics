#!/usr/bin/env python3
"""Reproduce agreement metrics for the agrivoltaics evidence-classification pilot.
Uses only Python's standard library. Original human labels remain the primary reference.
"""
import csv, json
from collections import Counter
from pathlib import Path
LABELS = ["observed", "modelled", "proposed", "multiple", "unclear"]
HERE = Path(__file__).resolve().parent
with (HERE / "matched_labels_public.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 39, f"Expected 39 records, got {len(rows)}"
assert len({r["record_id"] for r in rows}) == len(rows), "Duplicate record IDs"
assert all(r["human_label"] in LABELS and r["claude_new_label"] in LABELS and r["new_run_adjudicated_reference_label"] in LABELS for r in rows)
def evaluate(reference_column):
    cm = {h: {c: 0 for c in LABELS} for h in LABELS}
    for r in rows: cm[r[reference_column]][r["claude_new_label"]] += 1
    n = len(rows); agree = sum(cm[l][l] for l in LABELS); po = agree/n
    rc = Counter(r[reference_column] for r in rows); cc = Counter(r["claude_new_label"] for r in rows)
    pe = sum((rc[l]/n)*(cc[l]/n) for l in LABELS)
    per_label = []
    for l in LABELS:
        tp=cm[l][l]; fp=sum(cm[h][l] for h in LABELS if h != l); fn=sum(cm[l][c] for c in LABELS if c != l)
        precision=tp/(tp+fp) if tp+fp else None
        recall=tp/(tp+fn) if tp+fn else None
        f1=2*precision*recall/(precision+recall) if precision is not None and recall is not None and precision+recall else (0.0 if precision == 0 and recall is not None else None)
        per_label.append({"label":l,"reference_support":rc[l],"claude_predicted":cc[l],"precision":precision,"recall":recall,"f1":f1})
    return {"reference_column":reference_column,"n":n,"agreement_count":agree,"agreement_rate":po,"expected_agreement":pe,"cohens_kappa":(po-pe)/(1-pe) if pe != 1 else None,"reference_counts":dict(rc),"claude_counts":dict(cc),"confusion_matrix":cm,"per_label_metrics":per_label,"disagreements":[{k:r[k] for k in ("batch_id","record_id","title",reference_column,"claude_new_label")} for r in rows if r[reference_column] != r["claude_new_label"]]}
result={"primary_original_human_reference":evaluate("human_label"),"secondary_provisional_adjudicated_reference":evaluate("new_run_adjudicated_reference_label")}
print(json.dumps(result, indent=2, ensure_ascii=False))
(HERE / "reproduced_metrics.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
