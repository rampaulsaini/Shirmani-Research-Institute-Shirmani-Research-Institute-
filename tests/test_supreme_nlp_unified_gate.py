import json

from factory import supreme_nlp_unified_gate as gate


def main():
    rc = gate.main()
    assert rc == 0

    report = json.loads(gate.OUT.read_text(encoding="utf-8"))
    assert report["status"] == "PASS"
    assert report["promotion_allowed"] is False
    assert report["checks"]["v3_promotion_blocked"] is True
    assert report["checks"]["v3_fingerprint_valid"] is True
    assert report["v3"]["verification_status"] == "UNVERIFIED"
    assert report["v3"]["independent_replication_verified"] is False
    assert report["governance"]["promotion_requires_independent_evidence"] is True
    assert report["governance"]["declared_experiment_identifiers_are_not_replication"] is True
    assert report["fingerprint"]

    # A forged verification claim changes the result after its original
    # fingerprint was computed. The gate must fail closed on integrity mismatch
    # rather than trusting the modified record.
    original_build = gate.build_record
    try:
        def forged_record(signals, task_id):
            record = original_build(signals, task_id)
            record["result"]["interpretation"]["verification_status"] = "VERIFIED"
            record["provenance"]["independent_replication_verified"] = True
            return record

        gate.build_record = forged_record
        assert gate.main() == 1
        forged = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert forged["status"] == "BLOCK"
        assert forged["promotion_allowed"] is False
        assert forged["checks"]["v3_promotion_blocked"] is False
        assert forged["checks"]["v3_fingerprint_valid"] is False
    finally:
        gate.build_record = original_build

    # A real UNVERIFIED record remains blocked even when its fingerprint is valid.
    assert gate.main() == 0
    restored = json.loads(gate.OUT.read_text(encoding="utf-8"))
    assert restored["status"] == "PASS"
    assert restored["promotion_allowed"] is False
    assert restored["checks"]["v3_fingerprint_valid"] is True


if __name__ == "__main__":
    main()
