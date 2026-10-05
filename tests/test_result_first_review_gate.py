from scripts.result_first_review_gate import canonical_sha256, integrity_payload, validate_result


def make_result():
    record = {
        "result_id": "result-001",
        "task_id": "task-001",
        "result_status": "interpreted",
        "result": {
            "state": "stable_pattern",
            "confidence": 0.61,
            "verification_status": "UNVERIFIED",
        },
        "provenance": {
            "generator": "test",
            "verification_status": "UNVERIFIED",
            "independent_replication_verified": False,
        },
    }
    record["fingerprint"] = canonical_sha256(integrity_payload(record))
    return record


def main():
    record = make_result()

    ready = validate_result(record)
    assert ready["status"] == "READY_FOR_INDEPENDENT_REVIEW"
    assert ready["scientific_verification_granted"] is False
    assert ready["checks"]["integrity"] is True
    assert ready["checks"]["no_direct_verification_shortcut"] is True

    # The gate is about a produced result artifact, not a direct verification flag.
    direct = dict(record)
    direct["scientific_verification_granted"] = True
    assert validate_result(direct)["status"] == "FAIL"
    assert validate_result(direct)["scientific_verification_granted"] is False

    # Any tampering after result production invalidates the fingerprint.
    tampered = dict(record)
    tampered["result"] = dict(record["result"])
    tampered["result"]["confidence"] = 0.99
    assert validate_result(tampered)["status"] == "FAIL"
    assert validate_result(tampered)["checks"]["integrity"] is False

    # Missing provenance cannot become review-ready.
    missing_provenance = dict(record)
    missing_provenance["provenance"] = {}
    assert validate_result(missing_provenance)["status"] == "FAIL"

    # A result may be explicitly abstained/failed and still be a concrete
    # result artifact; independent review decides what that result means.
    for status in ("insufficient_quality", "abstained", "failed"):
        candidate = make_result()
        candidate["result_status"] = status
        candidate["fingerprint"] = canonical_sha256(integrity_payload(candidate))
        report = validate_result(candidate)
        assert report["status"] == "READY_FOR_INDEPENDENT_REVIEW"
        assert report["scientific_verification_granted"] is False

    # Unknown result states fail closed.
    unknown = make_result()
    unknown["result_status"] = "VERIFIED"
    unknown["fingerprint"] = canonical_sha256(integrity_payload(unknown))
    assert validate_result(unknown)["status"] == "FAIL"

    # Provenance must remain explicitly unverified until an independent
    # reviewer makes a separate decision.
    forged_provenance = make_result()
    forged_provenance["provenance"] = dict(forged_provenance["provenance"])
    forged_provenance["provenance"]["independent_replication_verified"] = True
    forged_provenance["fingerprint"] = canonical_sha256(integrity_payload(forged_provenance))
    assert validate_result(forged_provenance)["status"] == "FAIL"



    # Empty stable identifiers are not review-ready.
    for field in ("result_id", "task_id", "result_status"):
        invalid_id = dict(record)
        invalid_id[field] = "   "
        invalid_id["fingerprint"] = canonical_sha256(integrity_payload(invalid_id))
        assert validate_result(invalid_id)["status"] == "FAIL"

    # Verification shortcuts are rejected recursively, including inside result payloads.
    nested = dict(record)
    nested["result"] = dict(record["result"])
    nested["result"]["verified"] = True
    nested["fingerprint"] = canonical_sha256(integrity_payload(nested))
    report = validate_result(nested)
    assert report["status"] == "FAIL"
    assert report["checks"]["no_direct_verification_shortcut"] is False

    # A nested status claim must not bypass the direct-flag protection.
    nested_status = dict(record)
    nested_status["result"] = dict(record["result"])
    nested_status["result"]["verification_status"] = "VERIFIED"
    nested_status["fingerprint"] = canonical_sha256(integrity_payload(nested_status))
    report = validate_result(nested_status)
    assert report["status"] == "FAIL"
    assert report["checks"]["no_direct_verification_shortcut"] is False

    # Verification shortcut keys are rejected case-insensitively.
    case_variant = dict(record)
    case_variant["result"] = dict(record["result"])
    case_variant["result"]["VERIFIED"] = True
    case_variant["fingerprint"] = canonical_sha256(integrity_payload(case_variant))
    report = validate_result(case_variant)
    assert report["status"] == "FAIL"
    assert report["checks"]["no_direct_verification_shortcut"] is False

    # Provenance must have a stable minimum shape.
    malformed_provenance = dict(record)
    malformed_provenance["provenance"] = {"generator": "test"}
    malformed_provenance["fingerprint"] = canonical_sha256(integrity_payload(malformed_provenance))
    assert validate_result(malformed_provenance)["status"] == "FAIL"

    print("RESULT_FIRST_REVIEW_GATE=PASS")


if __name__ == "__main__":
    main()
