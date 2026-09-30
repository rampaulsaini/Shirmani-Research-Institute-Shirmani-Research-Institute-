import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gate = json.loads((ROOT / "docs/yatharth-governance/automission-quality-gate.json").read_text())
required = set(gate["required_audit_fields"])

# Provenance is mandatory at every auditable Automission event.
expected = {
    "event_id","timestamp","actor_or_agent","authority_or_rule",
    "input_provenance","model_or_version","recommendation_or_decision",
    "uncertainty","human_reviewer","appeal_status","correction_history"
}
assert required == expected

# Human verification and uncertainty cannot be silently omitted.
assert "human_reviewer" in required
assert "uncertainty" in required
assert gate["verification_rule"] == "workflow_success_is_not_independent_verification"

# The governance contract must keep independent verification at zero until
# a qualifying independent human review is recorded.
assert gate["status"]["independent_verified_claims"] == 0
assert gate["status"]["live_claim"] is False

print("Automission Evidence Provenance Gate: PASS")
print("Audit fields:", len(required))
print("Independent verification:", gate["status"]["independent_verified_claims"])
