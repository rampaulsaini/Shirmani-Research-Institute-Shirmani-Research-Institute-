#!/usr/bin/env python3
"""Fail-closed checks for the v3 scientific validation contract."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "scientific-validation-record-v3.schema.json"
DOC = ROOT / "research" / "scientific-validation-framework-v3.md"

def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    expected = {
        "record_id","claim_class","claim","operational_definition","protocol",
        "dataset_fingerprint","model","metrics","uncertainty","provenance",
        "verification_state"
    }
    if required != expected:
        raise SystemExit("Scientific validation schema required fields mismatch")
    states = schema["properties"]["verification_state"]["enum"]
    if states != ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"]:
        raise SystemExit("Verification state contract is not fail-closed")
    classes = schema["properties"]["claim_class"]["enum"]
    if "AUTHOR_SOURCE" not in classes or "NOT_VERIFIED" not in classes or "TESTABLE_EMPIRICAL" not in classes:
        raise SystemExit("Claim classification boundary is incomplete")
    text = DOC.read_text(encoding="utf-8")
    for term in [
        "OPERATIONAL DEFINITION","INDEPENDENT REPLICATION",
        "calibrated uncertainty","alternative explanations",
        "GitHub Actions PASS = operational execution evidence",
        "Universal claims require evidence appropriate to their universal scope",
    ]:
        if term not in text:
            raise SystemExit(f"Scientific validation framework missing: {term}")
    print("SHIRMANI Scientific Validation Framework v3: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
