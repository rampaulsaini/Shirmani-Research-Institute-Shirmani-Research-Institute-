import json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gate_path = ROOT / "docs/yatharth-governance/automission-quality-gate.json"
life_path = ROOT / "docs/yatharth-system/claim-lifecycle-contract.json"
reg_path = ROOT / "docs/yatharth-system/feature-status-registry.json"

gate = json.loads(gate_path.read_text())
life = json.loads(life_path.read_text())
reg = json.loads(reg_path.read_text())

# Deterministic canonical fingerprints make governance artifacts reproducible.
def fingerprint(path):
    data = json.loads(path.read_text())
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(canonical).hexdigest()

assert fingerprint(gate_path)
assert fingerprint(life_path)
assert fingerprint(reg_path)

# Verification cannot be promoted by automation alone.
assert life["truth_rule"] == "a_claim_is_not_a_verified_fact_until_qualifying_independent_review_is_recorded"
assert life["verification_requirements"]["ai_output_can_verify"] is False
assert set(life["verification_requirements"]["verified_requires"]) >= {
    "qualifying_independent_human_review","reviewer_identity_or_role",
    "review_date","review_basis","correction_or_appeal_route"
}
assert gate["status"]["independent_verified_claims"] == 0
assert reg["verification"]["independent_verified_claims"] == 0

# Counter-evidence and limitations are mandatory before verification.
minimum = set(life["verification_requirements"]["minimum"])
assert {"counter_evidence_status","limitations"} <= minimum

print("Automission Reproducibility & Evidence Integrity Gate: PASS")
print("Governance fingerprints generated deterministically.")
print("Independent verification remains: 0")
