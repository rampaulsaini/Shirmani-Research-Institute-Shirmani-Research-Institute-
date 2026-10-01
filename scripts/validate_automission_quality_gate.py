import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gate = json.loads((ROOT / "docs/yatharth-governance/automission-quality-gate.json").read_text())
registry = json.loads((ROOT / "docs/yatharth-system/feature-status-registry.json").read_text())
schema = json.loads((ROOT / "docs/yatharth-system/continuity-integrity-schema.json").read_text())

assert gate["truth_rule"] == "architecture_is_not_deployment"
assert gate["verification_rule"] == "workflow_success_is_not_independent_verification"
assert [x["id"] for x in gate["layers"]] == [f"L{i}" for i in range(1, 9)]
assert gate["layers"][5]["authority"] == "human_required"
assert all(value is False for value in gate["non_negotiable"].values())
assert len(gate["required_audit_fields"]) >= 10
assert gate["status"]["automission"] == registry["domains"]["automission"]
assert gate["status"]["independent_verified_claims"] == registry["verification"]["independent_verified_claims"] == 0
assert schema["verification_gate"]["workflow_success_is_verification"] is False
assert schema["verification_gate"]["ai_output_is_verification"] is False
assert schema["high_impact_human_boundary"] is True
assert schema["fail_closed"] is True

print("AI/ML/NLP/Automission quality gate: PASS")
