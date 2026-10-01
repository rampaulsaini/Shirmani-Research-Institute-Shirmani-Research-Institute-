import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "docs/yatharth-governance/automission-quality-gate.json",
    "docs/yatharth-governance/tamper-evident-audit-chain.json",
    "docs/yatharth-system/claim-lifecycle-contract.json",
    "docs/yatharth-system/feature-status-registry.json",
]

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    gate = load(FILES[0])
    audit = load(FILES[1])
    lifecycle = load(FILES[2])
    registry = load(FILES[3])

    assert gate["truth_rule"] == "architecture_is_not_deployment"
    assert gate["verification_rule"] == "workflow_success_is_not_independent_verification"
    assert gate["status"]["independent_verified_claims"] == 0
    assert gate["status"]["live_claim"] is False

    assert audit["hash_algorithm"] == "sha256"
    assert audit["verification_boundary"]["ai_output_can_verify"] is False
    assert audit["verification_boundary"]["workflow_success_can_verify"] is False
    assert audit["privacy"]["store_secrets"] is False
    assert audit["privacy"]["store_credentials"] is False

    assert lifecycle["truth_rule"] == "a_claim_is_not_a_verified_fact_until_qualifying_independent_review_is_recorded"
    assert lifecycle["verification_requirements"]["ai_output_can_verify"] is False
    assert "qualifying_independent_human_review" in lifecycle["verification_requirements"]["verified_requires"]

    assert registry["truth_rule"] == "architecture_is_not_deployment"
    assert registry["verification"]["independent_verified_claims"] == 0
    assert registry["verification"]["rule"] == "increase only after qualifying independent human review is recorded"

    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        revision = "unknown"

    snapshot = {
        "schema_version": "1.0.0",
        "generated_by": "validate_automission_integrity_release.py",
        "repository_revision": revision,
        "truth_status": {
            "architecture_is_not_deployment": True,
            "workflow_success_is_not_independent_verification": True,
            "ai_output_can_verify": False,
            "independent_verified_claims": 0,
            "live_claim": False
        },
        "contract_sha256": {
            path: sha256_file(ROOT / path) for path in FILES
        },
        "release_decision": "NO_AUTOMATED_VERIFICATION_CLAIM",
        "reason": "Independent verification requires qualifying independent human review."
    }
    out = ROOT / "automission-integrity-snapshot.json"
    out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(snapshot, ensure_ascii=False, indent=2))
    print("Automission Unified Integrity Release Gate: PASS")

if __name__ == "__main__":
    main()
