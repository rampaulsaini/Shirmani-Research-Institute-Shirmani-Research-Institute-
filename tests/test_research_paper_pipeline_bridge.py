#!/usr/bin/env python3
"""Regression contract for Research Paper -> verification pipeline ordering."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
claims = json.loads((ROOT/"generated/research-paper-claims.json").read_text(encoding="utf-8"))
intake = json.loads((ROOT/"federation/research-paper-source-intake.json").read_text(encoding="utf-8"))
workflow = (ROOT/".github/workflows/omniverse-factory.yml").read_text(encoding="utf-8")

ids = [f"claim:research-paper:{c['id']}" for c in claims["claims"]]
adapter = workflow.index("python3 factory/research_paper_claim_adapter.py")
formulation = workflow.index("python3 factory/formulation_records.py")
queue = workflow.index("python3 factory/verification_queue.py")
graph = workflow.index("python3 factory/research_evidence_graph.py")
assert adapter < formulation < queue < graph

text = (ROOT/"factory/research_paper_claim_adapter_v2.py").read_text(encoding="utf-8")
assert 'verification":{"status":"NOT_VERIFIED"' in text
assert '"independent":False' in text
assert '"independent_verification_required":True' in text
assert '"AUTHOR_DECLARED_RESEARCH_PAPER"' in text

for claim_id in ids:
    assert claim_id.startswith("claim:research-paper:")
assert intake["source_id"] == "SRP-SOURCE-001"
assert intake["verification_status"] == "UNVERIFIED"
print(f"Research Paper pipeline bridge: PASS ({len(ids)} claims; adapter→formulation→queue→graph)")
