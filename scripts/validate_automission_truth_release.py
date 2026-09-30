import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gate = json.loads((ROOT / "docs/yatharth-governance/automission-quality-gate.json").read_text())
registry = json.loads((ROOT / "docs/yatharth-system/feature-status-registry.json").read_text())
lifecycle = json.loads((ROOT / "docs/yatharth-system/claim-lifecycle-contract.json").read_text())

# The release gate is a truth boundary, not a deployment or verification claim.
assert gate["truth_rule"] == "architecture_is_not_deployment"
assert gate["verification_rule"] == "workflow_success_is_not_independent_verification"

# Safety capabilities are deliberately disabled; enabling any of them is a contract violation.
assert all(value is False for value in gate["non_negotiable"].values())

# Independent verification must never rise automatically.
assert gate["status"]["independent_verified_claims"] == 0
assert gate["status"]["live_claim"] is False
assert registry["verification"]["independent_verified_claims"] == 0
assert registry["verification"]["rule"] == "increase only after qualifying independent human review is recorded"
assert registry["domains"]["independent_verification"] == "REVIEW_REQUIRED"

# Claim lifecycle must preserve the human boundary.
assert lifecycle["verification_requirements"]["ai_output_can_verify"] is False
assert lifecycle["transitions"]["VERIFIED"] == ["ARCHIVED"]

# Required public truth vocabulary and completion controls must remain present.
required_statuses = {"LIVE","BETA","ARCHITECTURE","RESEARCH","REVIEW_REQUIRED","DISABLED","INCONCLUSIVE","NOT_VERIFIED"}
assert required_statuses <= set(registry["status_vocabulary"])
required_completion = {"implementation","tests","security_privacy","monitoring","user_facing_status","rollback_or_appeal"}
assert required_completion <= set(registry["completion_contract"]["required"])

print("Automission Truth Release Gate: PASS")
print("Independent verification remains: 0")
print("Live deployment claim: false")
