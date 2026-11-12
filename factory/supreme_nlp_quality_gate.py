#!/usr/bin/env python3
"""Deterministic quality gate for the Supreme NLP Practitioner pipeline.

This gate validates structure and evidence discipline; it does not claim
scientific proof of subjective experience from sensor or model outputs.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

REQUIRED_STAGES = [
    "signal", "quality_check", "normalization", "representation", "context",
    "inference", "plain_language", "confidence", "evidence",
    "independent_verification", "audit",
]

def validate(payload: dict) -> list[str]:
    errors=[]
    stages=payload.get("stages")
    if not isinstance(stages, list):
        return ["stages must be a list"]
    names=[s.get("name") for s in stages if isinstance(s,dict)]
    missing=[x for x in REQUIRED_STAGES if x not in names]
    if missing:
        errors.append("missing stages: "+", ".join(missing))
    if payload.get("claim_status") == "VERIFIED" and not payload.get("independent_verification"):
        errors.append("VERIFIED requires independent_verification evidence")
    if payload.get("confidence") is not None:
        c=payload["confidence"]
        if not isinstance(c,(int,float)) or not 0 <= c <= 1:
            errors.append("confidence must be numeric in [0,1]")
    if payload.get("interpretation") and not payload.get("evidence"):
        errors.append("interpretation requires evidence reference")
    return errors

def main() -> int:
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path("schemas/supreme-nlp-sample.json")
    if not path.exists():
        print(f"QC_INPUT_MISSING: {path}")
        return 2
    payload=json.loads(path.read_text(encoding="utf-8"))
    errors=validate(payload)
    report={"status":"PASS" if not errors else "FAIL","errors":errors,"required_stages":REQUIRED_STAGES}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
