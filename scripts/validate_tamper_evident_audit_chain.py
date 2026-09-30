import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/yatharth-governance/tamper-evident-audit-chain.json"

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def event_hash(event):
    payload = dict(event)
    payload.pop("event_hash", None)
    return hashlib.sha256(canonical(payload)).hexdigest()

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert contract["hash_algorithm"] == "sha256"
    assert contract["canonicalization"].startswith("UTF-8 JSON")
    required = {
        "event_id", "timestamp", "actor_or_agent", "authority_or_rule",
        "input_provenance", "model_or_version", "configuration_hash",
        "input_hash", "output_hash", "recommendation_or_decision",
        "uncertainty", "human_reviewer", "appeal_status",
        "correction_history", "prev_event_hash", "event_hash"
    }
    assert required.issubset(set(contract["event_fields"]))
    rules = contract["chain_rules"]
    assert "a_broken_chain_must_fail_closed" in rules
    assert "workflow_success_is_not_independent_verification" in rules
    boundary = contract["verification_boundary"]
    assert boundary["ai_output_can_verify"] is False
    assert boundary["workflow_success_can_verify"] is False
    assert boundary["independent_verified_claims_requires_qualifying_independent_human_review"] is True
    privacy = contract["privacy"]
    assert privacy["store_secrets"] is False
    assert privacy["store_credentials"] is False

    sample = {
        "event_id": "sample-001",
        "timestamp": "2026-10-01T00:00:00Z",
        "actor_or_agent": "test-agent",
        "authority_or_rule": "test-rule",
        "input_provenance": ["sha256:input"],
        "model_or_version": "test-model@1",
        "configuration_hash": "sha256:config",
        "input_hash": "sha256:input",
        "output_hash": "sha256:output",
        "recommendation_or_decision": "NO_RELEASE",
        "uncertainty": "test-only",
        "human_reviewer": None,
        "appeal_status": "not_applicable",
        "correction_history": [],
        "prev_event_hash": None
    }
    first = event_hash(sample)
    sample["event_hash"] = first
    assert sample["event_hash"] == event_hash(sample)

    second = dict(sample)
    second["event_id"] = "sample-002"
    second["prev_event_hash"] = first
    second.pop("event_hash")
    second["event_hash"] = event_hash(second)
    assert second["prev_event_hash"] == first
    tampered = dict(second)
    tampered["output_hash"] = "sha256:tampered"
    assert tampered["event_hash"] != event_hash(tampered)

    print("Automission Tamper-Evident Audit Chain Gate: PASS")

if __name__ == "__main__":
    main()
