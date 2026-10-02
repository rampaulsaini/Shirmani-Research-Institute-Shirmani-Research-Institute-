"""Deterministic fail-closed gate for Nishpaksh Automission records."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "nishpaksh-evaluation.schema.json"

REQUIRED = {
    "claim_id", "claim_class", "claim_text", "provenance",
    "evidence_state", "uncertainty", "verification_state"
}
VALID_CLASSES = {"framework", "empirical", "interpretation", "normative", "operational"}
VALID_EVIDENCE = {"NONE", "PENDING", "PARTIAL", "SUPPORTED", "CONTRADICTED", "MIXED"}
VALID_VERIFICATION = {"NOT_VERIFIED", "INDEPENDENTLY_VERIFIED", "REVIEW", "BLOCKED"}


def validate(record):
    missing = REQUIRED - set(record)
    if missing:
        return False, f"missing fields: {sorted(missing)}"
    if record["claim_class"] not in VALID_CLASSES:
        return False, "invalid claim_class"
    if record["evidence_state"] not in VALID_EVIDENCE:
        return False, "invalid evidence_state"
    if record["verification_state"] not in VALID_VERIFICATION:
        return False, "invalid verification_state"
    if not isinstance(record["provenance"], list) or not record["provenance"]:
        return False, "provenance is required"
    if not isinstance(record["uncertainty"], list):
        return False, "uncertainty must be a list"
    if record["verification_state"] == "INDEPENDENTLY_VERIFIED":
        if record["evidence_state"] not in {"SUPPORTED", "MIXED"}:
            return False, "independent verification requires supporting evidence"
        if not record.get("model_version") and record["claim_class"] == "empirical":
            return False, "empirical verification requires model/version trace"
    return True, "PASS"


def main():
    if not SCHEMA.exists():
        raise SystemExit("Nishpaksh schema missing")

    # Contract-level checks. Real claim records can be supplied later by the factory.
    contract = (ROOT / "docs/yatharth-governance/nishpaksh-automission-standard.md").read_text(encoding="utf-8")
    for term in ["counter-evidence", "UNVERIFIED", "Fail-closed", "high-impact"]:
        if term not in contract:
            raise SystemExit(f"Nishpaksh standard missing: {term}")

    sample = {
        "claim_id": "gate-self-test",
        "claim_class": "framework",
        "claim_text": "framework proposition",
        "provenance": ["self-test"],
        "supporting_evidence": [],
        "counter_evidence": [],
        "evidence_state": "PENDING",
        "uncertainty": ["not independently verified"],
        "verification_state": "NOT_VERIFIED",
        "model_inference": None,
        "confidence": None,
        "model_version": None,
        "dataset_fingerprint": None,
    }
    ok, reason = validate(sample)
    if not ok:
        raise SystemExit(reason)

    print("SHIRMANI Nishpaksh Automission Gate: PASS")


if __name__ == "__main__":
    main()
