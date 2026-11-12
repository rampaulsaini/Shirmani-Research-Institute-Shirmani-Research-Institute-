"""Deterministic ML evaluation contract with no third-party dependencies."""
from __future__ import annotations
from collections import Counter
def _scores(y_true,y_pred):
    if len(y_true)!=len(y_pred) or not y_true: return None
    labels=sorted(set(y_true)|set(y_pred)); per={}
    for label in labels:
        tp=sum(a==label and b==label for a,b in zip(y_true,y_pred))
        fp=sum(a!=label and b==label for a,b in zip(y_true,y_pred))
        fn=sum(a==label and b!=label for a,b in zip(y_true,y_pred))
        p=tp/(tp+fp) if tp+fp else 0.0; r=tp/(tp+fn) if tp+fn else 0.0
        per[label]={"precision":p,"recall":r,"f1":2*p*r/(p+r) if p+r else 0.0}
    accuracy=sum(a==b for a,b in zip(y_true,y_pred))/len(y_true)
    return {"accuracy":accuracy,"macro_f1":sum(v["f1"] for v in per.values())/len(per),"per_class":per}
def evaluate(y_true,y_pred,*,baseline=None):
    scores=_scores(list(y_true),list(y_pred))
    if scores is None: return {"schema":"ml-evaluation/v1","status":"HOLD","reason":"invalid_eval_set"}
    baseline=baseline or {}
    return {"schema":"ml-evaluation/v1","status":"PASS","sample_count":len(y_true),
            "class_count":len(Counter(y_true)),"metrics":scores,
            "baseline_macro_f1":baseline.get("macro_f1"),
            "delta_macro_f1":(scores["macro_f1"]-float(baseline["macro_f1"])) if "macro_f1" in baseline else None,
            "claim_policy":"No improvement claim without a supplied baseline and labeled evaluation set."}
