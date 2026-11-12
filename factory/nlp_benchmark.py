#!/usr/bin/env python3
"""Deterministic NLP/signal-to-language benchmark harness.

No external model is invoked here. The harness evaluates records supplied in
benchmarks/nlp-eval.jsonl and returns NOT_READY when no dataset exists.
"""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"benchmarks"/"nlp-eval.jsonl"
OUT=ROOT/"generated"
REQUIRED=("id","input","expected","prediction","confidence","evidence_refs","provenance")

def norm(x): return " ".join(str(x).strip().casefold().split())

def main():
    OUT.mkdir(exist_ok=True)
    report={"schema_version":1,"dataset":str(DATA.relative_to(ROOT)),
            "status":"NOT_READY","records":0,"errors":[]}
    if not DATA.exists():
        report["reason"]="evaluation dataset not present; no accuracy claim is made"
        (OUT/"NLP-BENCHMARK.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(report,ensure_ascii=False)); return
    rows=[]
    for n,line in enumerate(DATA.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: r=json.loads(line)
        except Exception as exc:
            report["errors"].append({"line":n,"error":"invalid_json:"+str(exc)}); continue
        for k in REQUIRED:
            if k not in r: report["errors"].append({"line":n,"error":"missing:"+k})
        c=r.get("confidence")
        if not isinstance(c,(int,float)) or not 0<=c<=1:
            report["errors"].append({"line":n,"error":"confidence_out_of_range"})
        if not isinstance(r.get("evidence_refs"),list):
            report["errors"].append({"line":n,"error":"evidence_refs_not_list"})
        if not isinstance(r.get("provenance"),dict) or not r.get("provenance"):
            report["errors"].append({"line":n,"error":"missing_provenance"})
        rows.append(r)
    if report["errors"]:
        report["status"]="BLOCK"
    elif not rows:
        report["status"]="NOT_READY"; report["reason"]="dataset is empty"
    else:
        n=len(rows); correct=sum(norm(r["expected"])==norm(r["prediction"]) for r in rows)
        brier=sum((float(r["confidence"])-(1.0 if norm(r["expected"])==norm(r["prediction"]) else 0.0))**2 for r in rows)/n
        evidence=sum(bool(r["evidence_refs"]) for r in rows)/n
        report.update({"status":"PASS","records":n,"exact_match_accuracy":correct/n,
                       "brier_score":brier,"evidence_coverage":evidence,
                       "reproducibility_sha256":hashlib.sha256(DATA.read_bytes()).hexdigest(),
                       "interpretation_boundary":"prediction is not proof of subjective feeling or consciousness"})
    (OUT/"NLP-BENCHMARK.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if report["status"]=="BLOCK": raise SystemExit(1)

if __name__=="__main__": main()
