"""Supreme NLP v2 benchmark: leakage-aware classification metrics and calibration.

Provider-neutral and dependency-free so Automission can run it in CI.
Input JSONL fields: specimen_id, experiment_id, split, y_true, y_pred, confidence.
The evaluator rejects obvious train/test leakage by specimen or experiment.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

def load(path: str) -> list[dict[str, Any]]:
    rows=[]
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            x=json.loads(line)
            if isinstance(x,dict): rows.append(x)
    return rows

def validate_partitions(rows):
    train={str(x.get("specimen_id")) for x in rows if x.get("split")=="train"}
    test={str(x.get("specimen_id")) for x in rows if x.get("split")=="test"}
    train_exp={str(x.get("experiment_id")) for x in rows if x.get("split")=="train"}
    test_exp={str(x.get("experiment_id")) for x in rows if x.get("split")=="test"}
    return sorted(train & test), sorted(train_exp & test_exp)

def classification(rows):
    test=[x for x in rows if x.get("split")=="test"]
    if not test: return {"status":"INSUFFICIENT_DATA"}
    tp=tn=fp=fn=0
    for x in test:
        y=str(x.get("y_true")); p=str(x.get("y_pred"))
        if y=="1" and p=="1": tp+=1
        elif y=="0" and p=="0": tn+=1
        elif y=="0" and p=="1": fp+=1
        elif y=="1" and p=="0": fn+=1
    precision=tp/(tp+fp) if tp+fp else 0.0
    recall=tp/(tp+fn) if tp+fn else 0.0
    specificity=tn/(tn+fp) if tn+fp else 0.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    accuracy=(tp+tn)/len(test)
    return {"status":"OK","test_n":len(test),"accuracy":accuracy,"precision":precision,"recall":recall,"specificity":specificity,"f1":f1}

def brier(rows):
    test=[x for x in rows if x.get("split")=="test" and isinstance(x.get("confidence"),(int,float))]
    if not test:return None
    return sum((float(x["confidence"])-float(x["y_true"]))**2 for x in test)/len(test)

def evaluate(path: str) -> dict[str,Any]:
    rows=load(path)
    overlap,exp_overlap=validate_partitions(rows)
    if overlap or exp_overlap:
        return {"status":"BLOCKED","reason":"DATA_LEAKAGE","specimen_overlap":overlap,"experiment_overlap":exp_overlap}
    metrics=classification(rows)
    metrics["brier_score"]=brier(rows)
    metrics["verification_state"]="UNVERIFIED"
    metrics["gate"]="PASS" if metrics.get("status")=="OK" else "NOT_READY"
    return metrics

if __name__=="__main__":
    import sys
    result=evaluate(sys.argv[1] if len(sys.argv)>1 else "generated/supreme-nlp/benchmark.jsonl")
    print(json.dumps(result,ensure_ascii=False,indent=2))
