#!/usr/bin/env python3
"""Fail-closed structural control check for the Supreme Automission architecture."""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "docs/yatharth-governance/supreme-ai-ml-nlp-automission-operating-contract.md",
    "schemas/supreme-ai-ml-nlp-automission-contract.schema.json",
]
errors=[]
for rel in REQUIRED:
    p=ROOT/rel
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f"missing-or-empty:{rel}")
schema=ROOT/"schemas/supreme-ai-ml-nlp-automission-contract.schema.json"
try:
    data=json.loads(schema.read_text(encoding="utf-8"))
    expected={"run_id","timestamp","stage","status","provenance","confidence","uncertainty","verification_state"}
    if not expected.issubset(set(data.get("required",[]))):
        errors.append("evidence-contract-required-fields-incomplete")
except Exception as exc:
    errors.append(f"invalid-json-schema:{exc}")
if errors:
    print("SUPREME_AUTOMISSION_CONTROL=FAIL")
    for e in errors: print(e)
    sys.exit(1)
print("SUPREME_AUTOMISSION_CONTROL=PASS")
print("fail-closed structural controls: OK")
print("accuracy remains measured; independent verification remains distinct from QC")
