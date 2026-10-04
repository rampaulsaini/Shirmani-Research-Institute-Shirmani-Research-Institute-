#!/usr/bin/env python3
"""Regression test for the Research Paper claim/evidence adapter."""
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
adapter = ROOT / "factory" / "research_paper_claim_adapter.py"
intake = json.loads((ROOT/"federation/research-paper-source-intake.json").read_text())
claims = json.loads((ROOT/"generated/research-paper-claims.json").read_text())

assert adapter.exists()
assert intake["verification_status"] == "UNVERIFIED"
assert intake["independent_verification_required"] is True
assert all(c["verification_status"] == "UNVERIFIED" for c in claims["claims"])
assert all(c["status"] == "AUTHOR_PROPOSITION" for c in claims["claims"])
print(f"Research Paper claim adapter contract: PASS ({len(claims['claims'])} claims)")

assert "PREFIX = \"claim:research-paper:\"" in adapter.read_text(encoding="utf-8")

# Every emitted claim must carry traceability metadata without implying proof.\nassert "AUTHOR_DECLARATION" in adapter.read_text(encoding="utf-8")
assert 'source_units = OUT/"source-units.jsonl"' in adapter.read_text(encoding="utf-8")
assert 'intake["source_id"]' in adapter.read_text(encoding="utf-8")
