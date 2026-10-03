#!/usr/bin/env python3
"""Fail-closed structural gate for scientific validation records.

This validates the research contract; it does not itself establish scientific truth.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "scientific-validation-record.schema.json"

REQUIRED = {
    "record_id","claim_type","hypothesis","operational_definition",
    "population_scope","primary_endpoint","protocol_fingerprint",
    "dataset_fingerprint","model_or_method","result","uncertainty",
    "controls","provenance","replication_level","verification_state","limitations"
}

def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    missing = sorted(REQUIRED - required)
    if missing:
        print("BLOCK: schema missing required fields:", ", ".join(missing))
        return 1

    verification = schema["properties"]["verification_state"]["enum"]
    if "INDEPENDENTLY_VERIFIED" not in verification or "BLOCKED" not in verification:
        print("BLOCK: verification state contract incomplete")
        return 1

    replication = schema["properties"]["replication_level"]["enum"]
    if len(replication) < 6:
        print("BLOCK: replication ladder incomplete")
        return 1

    print("PASS: scientific validation contract is structurally complete")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
