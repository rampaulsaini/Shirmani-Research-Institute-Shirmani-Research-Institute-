#!/usr/bin/env python3
"""Deterministic repository quality gate for the AI/ML/NLP Automission layer.

This gate deliberately does not claim model accuracy. It verifies that the
repository has the controls required to measure accuracy honestly.
"""
from __future__ import annotations
import json, py_compile, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
errors=[]

def fail(msg): errors.append(msg)

contract=ROOT/"automation/supreme-ai-quality-contract.json"
try:
    data=json.loads(contract.read_text(encoding="utf-8"))
    for key in ("version","principles","gates","metrics","promotion"):
        if key not in data: fail(f"contract missing: {key}")
except Exception as exc:
    fail(f"contract invalid: {exc}")

for base in ("agents","factory","scripts"):
    p=ROOT/base
    if p.exists():
        for f in p.rglob("*.py"):
            try: py_compile.compile(str(f), doraise=True)
            except Exception as exc: fail(f"python syntax: {f}: {exc}")

for f in ROOT.rglob("*.json"):
    if ".git" in f.parts: continue
    try: json.loads(f.read_text(encoding="utf-8"))
    except Exception as exc: fail(f"json invalid: {f}: {exc}")

status=ROOT/"generated/independent-verification-status-2026-09-29.json"
if status.exists():
    try:
        d=json.loads(status.read_text(encoding="utf-8"))
        s=d["verification_summary"]
        if s["independently_verified_records"] != 0:
            fail("independent verification status unexpectedly promotes records")
        if any(x.get("status")=="VERIFIED" for x in d.get("records", [])):
            fail("VERIFIED records exist without this gate's independent promotion mechanism")
    except Exception as exc: fail(f"verification registry invalid: {exc}")

if errors:
    print("SUPREME_AI_QUALITY_GATE=FAIL")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)

print("SUPREME_AI_QUALITY_GATE=PASS")
print("Deterministic controls are intact; model accuracy must still be established by an explicit evaluator/test set.")
