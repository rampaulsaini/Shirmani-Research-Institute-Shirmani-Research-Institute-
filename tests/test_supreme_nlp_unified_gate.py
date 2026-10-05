import json

from factory import supreme_nlp_unified_gate as gate
from agents.supreme_nlp_v3 import record_integrity_payload, sha256


def main():
    rc = gate.main()
    assert rc == 0

    report = json.loads(gate.OUT.read_text(encoding="utf-8"))
    assert report["status"] == "PASS"
    assert report["promotion_allowed"] is False
    assert report["checks"]["v3_unverified_safe_state"] is True
    assert report["checks"]["v3_promotion_boundary_consistent"] is True
    assert report["checks"]["v3_fingerprint_valid"] is True
    assert report["v3"]["verification_status"] == "UNVERIFIED"
    assert report["v3"]["independent_replication_verified"] is False
    assert report["governance"]["promotion_requires_independent_evidence"] is True
    assert report["governance"]["declared_experiment_identifiers_are_not_replication"] is True
    assert report["fingerprint"] == gate.report_fingerprint(report)

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
        assert forged["checks"]["v3_promotion_boundary_consistent"] is False
        assert forged["checks"]["v3_fingerprint_valid"] is False
    finally:
        gate.build_record = original_build

    # Provenance-only tampering must also invalidate the record fingerprint.
    try:
        def forged_provenance(signals, task_id):
            record = original_build(signals, task_id)
            record["provenance"]["independent_replication_verified"] = True
            return record

        gate.build_record = forged_provenance
        assert gate.main() == 1
        provenance_forged = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert provenance_forged["status"] == "BLOCK"
        assert provenance_forged["promotion_allowed"] is False
        assert provenance_forged["checks"]["v3_fingerprint_valid"] is False
    finally:
        gate.build_record = original_build

    # A real UNVERIFIED record remains blocked even when its fingerprint is valid.
    assert gate.main() == 0
    restored = json.loads(gate.OUT.read_text(encoding="utf-8"))
    assert restored["status"] == "PASS"
    assert restored["promotion_allowed"] is False
    assert restored["checks"]["v3_fingerprint_valid"] is True

    # Verification alone is not sufficient: calibration must also be complete.
    try:
        def uncalibrated_verified_record(signals, task_id):
            record = original_build(signals, task_id)
            interpretation = record["result"]["interpretation"]
            interpretation["verification_status"] = "VERIFIED"
            record["provenance"]["independent_replication_verified"] = True
            record["fingerprint"] = sha256(record_integrity_payload(record))
            return record

        gate.build_record = uncalibrated_verified_record
        assert gate.main() == 0
        blocked = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert blocked["status"] == "PASS"
        assert blocked["promotion_allowed"] is False
        assert blocked["checks"]["v3_verification_ready"] is False
        assert blocked["checks"]["v3_promotion_boundary_consistent"] is True
    finally:
        gate.build_record = original_build

    # Calibration alone is also insufficient: verification and replication are required.
    try:
        def calibrated_unverified_record(signals, task_id):
            record = original_build(signals, task_id)
            interpretation = record["result"]["interpretation"]
            interpretation["confidence_status"] = "CALIBRATED"
            interpretation["calibration_required"] = False
            record["fingerprint"] = sha256(record_integrity_payload(record))
            return record

        gate.build_record = calibrated_unverified_record
        assert gate.main() == 0
        blocked = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert blocked["status"] == "PASS"
        assert blocked["promotion_allowed"] is False
        assert blocked["checks"]["v3_verification_ready"] is False
        assert blocked["checks"]["v3_promotion_boundary_consistent"] is True
    finally:
        gate.build_record = original_build

    # The same gate must also support the opposite, evidence-backed state.
    # Promotion is allowed only when verification, replication and calibration
    # are all explicitly present and the record fingerprint is valid.
    try:
        def verified_record(signals, task_id):
            record = original_build(signals, task_id)
            interpretation = record["result"]["interpretation"]
            interpretation["verification_status"] = "VERIFIED"
            interpretation["confidence_status"] = "CALIBRATED"
            interpretation["calibration_required"] = False
            record["provenance"]["independent_replication_verified"] = True
            record["fingerprint"] = sha256(record_integrity_payload(record))
            return record

        gate.build_record = verified_record
        assert gate.main() == 0
        promoted = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert promoted["status"] == "PASS"
        assert promoted["promotion_allowed"] is True
        assert promoted["checks"]["v3_verification_ready"] is True
        assert promoted["checks"]["v3_promotion_boundary_consistent"] is True
        assert promoted["checks"]["v3_fingerprint_valid"] is True
    finally:
        gate.build_record = original_build


if __name__ == "__main__":
    main()
