#!/usr/bin/env python3
"""Deterministic gate for perception-to-language records.

The gate is intentionally model-agnostic: it validates the evidence boundary
before an agent is allowed to turn a perception record into natural language.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ALLOWED={"OBSERVED","DERIVED","INFERRED","HYPOTHESIS","AUTHOR_CLAIM","UNVERIFIED"}


def validate(record: dict) -> list[str]:
    errors=[]
    required=("record_id","timestamp","status","modality","content","provenance")
    for key in required:
        if key not in record or record[key] in (None, ""):
            errors.append(f"missing:{key}")
    if record.get("status") not in ALLOWED:
        errors.append("invalid:status")
    if not isinstance(record.get("content"), str):
        errors.append("invalid:content")
    if not isinstance(record.get("provenance"), dict) or not record.get("provenance",{}).get("source_id"):
        errors.append("invalid:provenance")
    u=record.get("uncertainty")
    if u is not None and (not isinstance(u,(int,float)) or not 0 <= u <= 1):
        errors.append("invalid:uncertainty")
    # A subjective-feeling statement about a non-human subject cannot be
    # upgraded merely because a language model produced it.
    if record.get("status") == "INFERRED" and not record.get("evidence_refs"):
        errors.append("inferred_requires_evidence_refs")
    return errors


def main() -> int:
    if len(sys.argv)!=2:
        print("usage: nlp_perception_gate.py RECORD.json", file=sys.stderr)
        return 2
    path=Path(sys.argv[1])
    record=json.loads(path.read_text(encoding="utf-8"))
    errors=validate(record)
    if errors:
        print(json.dumps({"status":"REJECT","errors":errors},ensure_ascii=False))
        return 1
    print(json.dumps({"status":"PASS","record_id":record["record_id"]},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
