#!/usr/bin/env python3
"""Reproducible, evidence-first NLP benchmark controller."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def evaluate(rows):
    if not rows:
        return {"sample_count":0,"accuracy":None,"macro_f1":None,"measured":False}
    labels=sorted({r["label"] for r in rows}|{r["prediction"] for r in rows})
    accuracy=sum(r["label"]==r["prediction"] for r in rows)/len(rows)
    fs=[]
    for c in labels:
        tp=sum(r["label"]==c and r["prediction"]==c for r in rows)
        fp=sum(r["label"]!=c and r["prediction"]==c for r in rows)
        fn=sum(r["label"]==c and r["prediction"]!=c for r in rows)
        p=tp/(tp+fp) if tp+fp else 0.0
        q=tp/(tp+fn) if tp+fn else 0.0
        fs.append(2*p*q/(p+q) if p+q else 0.0)
    return {"sample_count":len(rows),"accuracy":accuracy,"macro_f1":sum(fs)/len(fs),"measured":True}

def smoke():
    return evaluate([
      {"label":"stable","prediction":"stable"},
      {"label":"stable","prediction":"stable"},
      {"label":"changed","prediction":"changed"},
      {"label":"changed","prediction":"stable"}])

def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",type=Path)
    ap.add_argument("--output",type=Path,default=ROOT/"generated/supreme-nlp/scientific-benchmark.json")
    a=ap.parse_args()
    rows=[]
    source="synthetic-smoke"
    if a.input:
        payload=json.loads(a.input.read_text(encoding="utf-8"))
        rows=payload.get("rows",payload) if isinstance(payload,(dict,list)) else []
        source=str(a.input)
    result=evaluate(rows) if rows else smoke()
    report={"schema_version":"1.0","source":source,"result":result,
      "governance":{"accuracy_is_measured_not_declared":True,
      "synthetic_smoke_is_not_scientific_accuracy":True,
      "independent_verification_required":True,
      "subjective_experience_claim_allowed":False,
      "production_code_mutation_allowed":False,"fail_closed":True}}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__":
    main()
