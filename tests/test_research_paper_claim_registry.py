#!/usr/bin/env python3
"""Fail-closed validation for the Shirmani Research Paper claim registry."""
import json
from pathlib import Path

p = Path("generated/research-paper-claims.json")
data = json.loads(p.read_text(encoding="utf-8"))

assert data["source_repository"] == "rampaulsaini/Shirmani-Research-Paper"
assert data["default_verification_status"] == "UNVERIFIED"
assert data["claims"]
assert any(c["id"] == "SRP-C006" and c["category"] == "metaphysical_philosophy" for c in data["claims"])

required = {"id","title","category","claim","status","verification_status","evidence_required"}
for claim in data["claims"]:
    assert required <= claim.keys()
    assert claim["status"] == "AUTHOR_PROPOSITION"
    assert claim["verification_status"] == "UNVERIFIED"
    assert claim["evidence_required"]

print(f"Research Paper claims: PASS ({len(data['claims'])} fail-closed propositions)")
