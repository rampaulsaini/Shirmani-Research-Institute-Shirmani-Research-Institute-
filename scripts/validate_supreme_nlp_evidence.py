#!/usr/bin/env python3
"""Deterministic, dependency-free validation for Supreme NLP evidence records."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ALLOWED_INPUTS = {"text", "speech", "image", "video", "sensor", "multimodal"}
ALLOWED_STATUS = {"UNVERIFIED", "PENDING", "VERIFIED", "REJECTED"}

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

def validate(record: dict) -> None:
    required = {"record_id","input_type","observations","inference","confidence","uncertainty","verification"}
    missing = required - record.keys()
    if missing:
        fail(f"missing required fields: {sorted(missing)}")
    if not isinstance(record["record_id"], str) or not record["record_id"].strip():
        fail("record_id must be a non-empty string")
    if record["input_type"] not in ALLOWED_INPUTS:
        fail("input_type is not supported")
    if not isinstance(record["observations"], list) or not record["observations"]:
        fail("observations must contain at least one item")
    if not all(isinstance(x, str) and x.strip() for x in record["observations"]):
        fail("observations must contain non-empty strings")
    if not isinstance(record["inference"], str) or not record["inference"].strip():
        fail("inference must be a non-empty string")
    if not isinstance(record["confidence"], (int, float)) or isinstance(record["confidence"], bool):
        fail("confidence must be numeric")
    if not 0 <= record["confidence"] <= 1:
        fail("confidence must be between 0 and 1")
    if not isinstance(record["uncertainty"], list):
        fail("uncertainty must be a list")
    if not all(isinstance(x, str) and x.strip() for x in record["uncertainty"]):
        fail("uncertainty must contain non-empty strings")
    verification = record["verification"]
    if not isinstance(verification, dict):
        fail("verification must be an object")
    if verification.get("status") not in ALLOWED_STATUS:
        fail("verification.status is invalid")
    if not isinstance(verification.get("independent"), bool):
        fail("verification.independent must be boolean")
    if verification["status"] == "VERIFIED" and verification["independent"] is not True:
        fail("VERIFIED records require independent=true")

def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        fail("provide one or more JSON record paths")
    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{path}: invalid JSON: {exc}")
        if not isinstance(record, dict):
            fail(f"{path}: root must be an object")
        validate(record)
        print(f"PASS: {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
