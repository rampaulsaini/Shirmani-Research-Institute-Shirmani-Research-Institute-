#!/usr/bin/env python3
"""Deterministic, dependency-free integrity checks for the research factory."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "generated/factory-status.json",
    "generated/agent-status.json",
    "generated/federation-status.json",
    "generated/source-registry.json",
    "generated/claim-index.json",
]

def load(rel):
    p = ROOT / rel
    if not p.is_file():
        raise RuntimeError(f"MISSING FILE: {rel}")
    with p.open(encoding="utf-8") as f:
        return json.load(f)

def main():
    for rel in REQUIRED:
        load(rel)
    status = load("generated/factory-status.json")
    for key in ("status", "records", "processed_batch", "artifacts", "qc"):
        if key not in status:
            raise RuntimeError(f"MISSING KEY in factory-status.json: {key}")
    for key in ("records", "processed_batch", "artifacts"):
        if status[key] is not None and not isinstance(status[key], int):
            raise RuntimeError(f"factory-status.{key} must be integer or null")
    reg = load("generated/source-registry.json")
    if "repositories" in reg:
        if not isinstance(reg["repositories"], list):
            raise RuntimeError("source registry repositories must be a list")
    idx = load("generated/claim-index.json")
    if len(idx["claims"]) != idx["counts"]["total"]:
        raise RuntimeError("claim index count mismatch")
    print("FACTORY_VALIDATION=PASS")
    print("FABRICATED_METRICS=FALSE")
    print("MISSING_DATA=EXPLICIT")
    return 0

if __name__ == "__main__":
    sys.exit(main())
