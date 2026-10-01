"""Evidence-first ML evaluation, calibration and abstention utilities.

This module evaluates model outputs; it does not claim scientific validity for any
domain. Accuracy is computed only against explicit labelled evaluation records.
"""
from __future__ import annotations
from collections import defaultdict
import hashlib, json
from math import isfinite
from typing import Any, Iterable

VERSION = "supreme-eval-v1"

def _clip(x: Any) -> float:
    try: value = float(x)
    except (TypeError, ValueError): return 0.0
    if not isfinite(value): return 0.0
    return max(0.0, min(1.0, value))

def _binary_metrics(rows: list[dict[str, Any]], threshold: float) -> dict[str, Any]:
    valid = []
    for row in rows:
        if row.get("label") not in (0, 1): continue
        valid.append((int(row["label"]), _clip(row.get("probability"))))
    if not valid:
        return {"status":"NO_LABELLED_DATA","count":0,"coverage":0.0,"abstentions":0}
    decisions=[]; abstentions=0; brier=0.0; confusion=defaultdict(int)
    for label,p in valid:
        brier += (p-label)**2
        if max(p,1-p) < threshold:
            abstentions += 1; continue
        pred=1 if p>=0.5 else 0
        decisions.append((label,pred)); confusion[(label,pred)]+=1
    n=len(valid); evaluated=len(decisions); coverage=evaluated/n
    accuracy=sum(y==p for y,p in decisions)/evaluated if evaluated else 0.0
    tp=confusion[(1,1)]; fp=confusion[(0,1)]; fn=confusion[(1,0)]
    precision=tp/(tp+fp) if tp+fp else 0.0
    recall=tp/(tp+fn) if tp+fn else 0.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    bins=[{"count":0,"confidence_sum":0.0,"accuracy_sum":0.0} for _ in range(10)]
    for label,p in valid:
        pred=1 if p>=0.5 else 0; confidence=max(p,1-p)
        idx=min(9,int(confidence*10)); bins[idx]["count"]+=1
        bins[idx]["confidence_sum"]+=confidence
        bins[idx]["accuracy_sum"]+=float(pred==label)
    ece=0.0; reliability=[]
    for idx,b in enumerate(bins):
        if not b["count"]: continue
        acc=b["accuracy_sum"]/b["count"]; conf=b["confidence_sum"]/b["count"]
        ece += (b["count"]/n)*abs(acc-conf)
        reliability.append({"bin":idx,"count":b["count"],"accuracy":round(acc,6),"confidence":round(conf,6)})
    return {"status":"OK","count":n,"evaluated":evaluated,"abstentions":abstentions,
            "coverage":round(coverage,6),"accuracy":round(accuracy,6),
            "precision":round(precision,6),"recall":round(recall,6),"f1":round(f1,6),
            "brier_score":round(brier/n,6),"ece":round(ece,6),"reliability":reliability}

def evaluate(rows: Iterable[dict[str, Any]], abstention_threshold: float=0.60) -> dict[str, Any]:
    rows=list(rows); threshold=max(0.5,min(0.99,float(abstention_threshold)))
    metrics=_binary_metrics(rows,threshold)
    ready=metrics.get("status")=="OK" and metrics.get("count",0)>=100
    return {"schema_version":VERSION,"task":"binary_label_evaluation","metrics":metrics,
            "abstention":{"enabled":True,"confidence_threshold":round(threshold,6),
                          "policy":"abstain_when_confidence_is_below_threshold"},
            "calibration":{"status":"EVALUATION_READY" if ready else "NOT_CALIBRATED",
                           "minimum_labelled_records":100,
                           "note":"ECE/Brier are measured; calibration is not declared from insufficient data."},
            "governance":{"accuracy_is_measured_not_declared":True,
                          "unlabelled_results_cannot_be_scored_as_accuracy":True,
                          "abstention_allowed":True,"independent_verification_required":True}}

def fingerprint(record: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(record,sort_keys=True,ensure_ascii=False).encode("utf-8")).hexdigest()

def build_record(rows: Iterable[dict[str, Any]], abstention_threshold: float=0.60) -> dict[str, Any]:
    result=evaluate(rows,abstention_threshold)
    return {**result,"fingerprint":fingerprint(result)}
