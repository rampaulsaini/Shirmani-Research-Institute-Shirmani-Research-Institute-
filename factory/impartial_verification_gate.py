"""Fail-closed impartiality gate for independent verification.

This gate does not create or infer VERIFIED decisions. It only validates whether
an existing record contains enough independent-review metadata to be eligible
for promotion. Missing, self-authored, conflicted, or incomplete records remain
blocked.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "config/impartial-verification-policy.json"
REGISTRY = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/impartial-verification-status.json"


def fail(code: str, detail: str = "") -> None:
    payload = {"status": "BLOCKED", "code": code}
    if detail:
        payload["detail"] = detail
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    raise SystemExit(1)


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def check_record(record: dict, policy: dict) -> tuple[bool, list[str]]:
    rules = policy["rules"]
    errors: list[str] = []
    decision = record.get("reviewer_decision", {}).get("decision", "PENDING")

    if decision not in policy["allowed_decisions"]:
        errors.append("INVALID_DECISION")

    author = str(record.get("author_identity", "")).strip()
    reviewer = record.get("reviewer_decision", {})
    reviewer_identity = str(reviewer.get("reviewer_identity", "")).strip()
    reviewer_role = str(reviewer.get("reviewer_role", "")).strip()

    if decision == "VERIFIED" and not author:
        errors.append("AUTHOR_IDENTITY_MISSING")
    if decision == "VERIFIED" and not reviewer_identity:
        errors.append("REVIEWER_IDENTITY_MISSING")
    if rules["author_cannot_self_verify"] and author and reviewer_identity and author == reviewer_identity:
        errors.append("AUTHOR_SELF_VERIFICATION_FORBIDDEN")
    if rules["independent_reviewer_must_differ_from_author"] and author and not reviewer_identity:
        errors.append("REVIEWER_IDENTITY_MISSING")
    if rules["independent_reviewer_must_differ_from_author"] and author and reviewer_identity == author:
        errors.append("REVIEWER_MUST_DIFFER_FROM_AUTHOR")
    if rules["reviewer_role_required"] and not reviewer_role:
        errors.append("REVIEWER_ROLE_MISSING")
    if rules["decision_timestamp_required"] and decision != "PENDING" and not reviewer.get("timestamp"):
        errors.append("DECISION_TIMESTAMP_MISSING")

    conflict = reviewer.get("conflict_of_interest")
    if rules["conflict_of_interest_disclosure_required"] and conflict not in (True, False):
        errors.append("CONFLICT_OF_INTEREST_DISCLOSURE_MISSING")
    if conflict is True:
        errors.append("CONFLICT_OF_INTEREST_BLOCKS_PROMOTION")

    evidence = record.get("evidence", {})
    test = record.get("independent_test", {})
    reproducibility = record.get("reproducibility", {})
    counter = record.get("counter_evidence", {})
    audit = record.get("audit", {})

    if rules["proposal_is_not_evidence"] and record.get("source_status") in {
        "AUTHOR-DEFINED", "AUTHOR-PROPOSED"
    } and decision == "VERIFIED":
        errors.append("AUTHOR_PROPOSAL_CANNOT_BE_VERIFIED_AS_EVIDENCE")

    if rules["evidence_is_not_verification"] and decision == "VERIFIED":
        if record.get("status") == "EVIDENCE-SUPPORTED" and not test.get("result"):
            errors.append("EVIDENCE_SUPPORT_ALONE_CANNOT_VERIFY")

    if not isinstance(evidence.get("sources"), list) or not evidence.get("sources"):
        errors.append("INDEPENDENT_SOURCES_MISSING")
    if not test.get("protocol") or test.get("result") in (None, "", "PENDING"):
        errors.append("INDEPENDENT_TEST_MISSING")
    if reproducibility.get("result_match") is not True:
        errors.append("REPRODUCIBILITY_NOT_ESTABLISHED")
    if counter.get("reviewed") is not True:
        errors.append("COUNTER_EVIDENCE_NOT_REVIEWED")
    if audit.get("passed") is not True:
        errors.append("AUDIT_NOT_PASSED")

    if decision == "VERIFIED" and errors:
        return False, errors
    return True, errors


def main() -> int:
    policy = load(POLICY)
    data = load(REGISTRY)
    records = data.get("records", [])
    if not isinstance(records, list):
        fail("REGISTRY_RECORDS_NOT_LIST")

    eligible = 0
    blocked = 0
    verified = 0
    reasons: dict[str, int] = {}

    for record in records:
        ok, errors = check_record(record, policy)
        if ok and record.get("reviewer_decision", {}).get("decision") == "VERIFIED":
            eligible += 1
            verified += 1
        elif errors:
            blocked += 1
            for error in sorted(set(errors)):
                reasons[error] = reasons.get(error, 0) + 1

    result = {
        "schema_version": 1,
        "status": "PASS" if blocked == 0 else "BLOCKED",
        "records_checked": len(records),
        "verified_records": verified,
        "promotion_eligible_verified_records": eligible,
        "blocked_records": blocked,
        "block_reasons": dict(sorted(reasons.items())),
        "principle": "NO_RECORD_IS_PROMOTED_BY_AUTOMATION_ALONE",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # Existing PENDING records are expected to remain pending. The gate only
    # fails when a claimed VERIFIED record violates impartiality requirements.
    if any(
        record.get("reviewer_decision", {}).get("decision") == "VERIFIED"
        and not check_record(record, policy)[0]
        for record in records
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
