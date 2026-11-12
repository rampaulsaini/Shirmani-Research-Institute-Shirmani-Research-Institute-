#!/usr/bin/env python3
"""Deterministic quality gate for the Signal -> NLP pipeline."""
from __future__ import annotations
import json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-nlp-evaluation.json"
required=("statement","confidence","evidence_level","alternative_explanations","evidence_refs")

def main() -> int:
    samples=[
      {"record_id":"smoke-1","source_type":"sensor","observations":[
        {"feature":"signal_strength","value":0.7,"quality":0.95}
      ]},
      {"record_id":"smoke-2","source_type":"environmental","observations":[]}
    ]
    sys.path.insert(0,str(ROOT))
    from agents.signal_to_nlp_agent import interpret_signal
    results=[]
    for sample in samples:
        out=interpret_signal(sample)
        ok=(set(required)<=set(out)
            and 0.0<=float(out["confidence"])<=1.0
            and out["evidence_level"] in {"observed","inferred","hypothesis","unverified"}
            and isinstance(out["alternative_explanations"],list))
        results.append({"record_id":sample["record_id"],"passed":ok,"output":out})
    passed=all(x["passed"] for x in results)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({"passed":passed,"tests":results},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":passed,"tests":len(results)},ensure_ascii=False))
    return 0 if passed else 1

if __name__=="__main__":
    raise SystemExit(main())
