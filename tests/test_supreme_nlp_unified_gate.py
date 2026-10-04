import json
from pathlib import Path

from factory import supreme_nlp_unified_gate as gate


def main():
    rc = gate.main()
    assert rc == 0

    report = json.loads(gate.OUT.read_text(encoding="utf-8"))
    assert report["status"] == "PASS"
    assert report["promotion_allowed"] is False
    assert report["checks"]["v3_promotion_blocked"] is True
    assert report["v3"]["verification_status"] == "UNVERIFIED"
    assert report["v3"]["independent_replication_verified"] is False
    assert report["governance"]["promotion_requires_independent_evidence"] is True
    assert report["governance"]["declared_experiment_identifiers_are_not_replication"] is True
    assert report["fingerprint"]

    # A record claiming verification without independent replication must still
    # remain blocked; promotion requires both conditions simultaneously.
    original_build = gate.build_record
    try:
        def forged_record(signals, task_id):
            record = original_build(signals, task_id)
            record["result"]["interpretation"]["verification_status"] = "VERIFIED"
            record["provenance"]["independent_replication_verified"] = False
            return record

        gate.build_record = forged_record
        assert gate.main() == 0
        forged = json.loads(gate.OUT.read_text(encoding="utf-8"))
        assert forged["promotion_allowed"] is False
        assert forged["checks"]["v3_promotion_blocked"] is True
    finally:
        gate.build_record = original_build


if __name__ == "__main__":
    main()
