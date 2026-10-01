"""Deterministic quality gate for Supreme Continuous Improvement."""
from __future__ import annotations
import json, pathlib, sys

REQUIRED={"status","interpretation","features","provenance","generated_at"}

def validate(path="generated/supreme-nlp/status.json"):
    p=pathlib.Path(path)
    if not p.exists():
        return False, ["STATUS_MISSING"]
    d=json.loads(p.read_text(encoding="utf-8"))

    # Current Supreme NLP records keep the model result under "result".
    # Accept that canonical shape while retaining compatibility with older
    # flat records.
    result=d.get("result", d)
    errors=[f"MISSING:{k}" for k in REQUIRED if k not in d and k not in result]

    i=result.get("interpretation") or {}
    f=result.get("features") or {}
    status=result.get("status")

    if status == "interpreted":
        if not 0 <= float(i.get("confidence",-1)) <= 1:
            errors.append("CONFIDENCE_OUT_OF_RANGE")
        if f.get("modalities",0) < 1:
            errors.append("NO_MODALITY")
        if "limitations" not in i or not i["limitations"]:
            errors.append("LIMITATIONS_MISSING")
    if not d.get("provenance"):
        errors.append("PROVENANCE_MISSING")

    return not errors, errors

if __name__=="__main__":
    ok,errors=validate()
    print("SUPREME_QUALITY_GATE", "PASS" if ok else "FAIL", errors)
    sys.exit(0 if ok else 1)
