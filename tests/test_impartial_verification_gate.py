from factory.impartial_verification_gate import check_record


POLICY = {
    "allowed_decisions": ["PENDING", "VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"],
    "rules": {
        "author_cannot_self_verify": True,
        "proposal_is_not_evidence": True,
        "evidence_is_not_verification": True,
        "workflow_success_is_not_verification": True,
        "pending_fields_block_promotion": True,
        "counter_evidence_required": True,
        "reproducibility_required": True,
        "reviewer_identity_required": True,
        "reviewer_role_required": True,
        "conflict_of_interest_disclosure_required": True,
        "independent_reviewer_must_differ_from_author": True,
        "decision_timestamp_required": True,
    },
}


def record(decision="VERIFIED", reviewer="independent-reviewer"):
    return {
        "id": "TEST-001",
        "author_identity": "author-1",
        "source_status": "EVIDENCE-SUPPORTED",
        "status": "EVIDENCE-SUPPORTED",
        "evidence": {"sources": ["source-a"]},
        "independent_test": {"protocol": "protocol", "result": "PASS"},
        "reproducibility": {"result_match": True},
        "counter_evidence": {"reviewed": True},
        "audit": {"passed": True},
        "reviewer_decision": {
            "decision": decision,
            "reviewer_identity": reviewer,
            "reviewer_role": "independent reviewer",
            "conflict_of_interest": False,
            "timestamp": "2026-10-08T00:00:00Z",
        },
    }


def test_complete_independent_record_is_eligible():
    ok, errors = check_record(record(), POLICY)
    assert ok is True
    assert errors == []


def test_author_cannot_self_verify():
    ok, errors = check_record(record(reviewer="author-1"), POLICY)
    assert ok is False
    assert "AUTHOR_SELF_VERIFICATION_FORBIDDEN" in errors


def test_verified_requires_reviewer_and_author_provenance():
    r = record()
    r["author_identity"] = ""
    r["reviewer_decision"]["reviewer_identity"] = ""
    ok, errors = check_record(r, POLICY)
    assert ok is False
    assert "AUTHOR_IDENTITY_MISSING" in errors
    assert "REVIEWER_IDENTITY_MISSING" in errors


def test_conflict_of_interest_blocks_promotion():
    r = record()
    r["reviewer_decision"]["conflict_of_interest"] = True
    ok, errors = check_record(r, POLICY)
    assert ok is False
    assert "CONFLICT_OF_INTEREST_BLOCKS_PROMOTION" in errors


def test_pending_is_not_promoted():
    ok, errors = check_record(record(decision="PENDING"), POLICY)
    assert ok is True
    assert errors == []
