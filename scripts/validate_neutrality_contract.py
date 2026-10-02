#!/usr/bin/env python3
"""Validate the machine-auditable neutrality/evidence contract."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "SHIRMANI-NEUTRALITY-EVIDENCE-CONTRACT.md"
SCHEMA = ROOT / "schemas" / "neutrality-evidence-record.schema.json"

required_terms = [
    "Symmetric treatment","No authority shortcut","Evidence separation",
    "Counter-evidence required","Uncertainty is explicit","Independent verification",
    "Fail closed","No fabricated experience","Reproducibility",
    "Human review for high-impact actions",
]

if not DOC.is_file() or not DOC.read_text(encoding="utf-8").strip():
    raise SystemExit("NEUTRALITY_CONTRACT: missing or empty contract document")

doc = DOC.read_text(encoding="utf-8")
for term in required_terms:
    if term not in doc:
        raise SystemExit(f"NEUTRALITY_CONTRACT: missing required rule: {term}")

schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
assert schema["properties"]["schema_version"]["const"] == "neutrality-evidence-v1"
assert "counter_evidence" in schema["required"]
assert schema["properties"]["verification"]["properties"]["independent_required"]["const"] is True

print("NEUTRALITY_CONTRACT: PASS")
print(f"Rules checked: {len(required_terms)}")
print("Evidence symmetry: required")
print("Counter-evidence: required")
print("Independent verification: required")
print("Fail-closed promotion: required")
