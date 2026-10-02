"""Deterministic contract tests for the Supreme NLP neutrality gate."""
from agents.neutrality_gate import audit, classify


def main():
    source = classify({
        "claim_type": "SOURCE_WORLDVIEW",
        "verification_status": "UNVERIFIED",
        "provenance": "user-source-2026-09-20",
        "evidence": [],
    })
    assert source.status == "HOLD"
    assert "SOURCE_AS_FACT" in source.reason_codes

    experience = classify({
        "claim_type": "SUBJECTIVE_EXPERIENCE",
        "verification_status": "UNVERIFIED",
        "provenance": "sensor-experiment-001",
        "evidence": [{"type": "sensor", "id": "s1"}],
    })
    assert experience.status == "HOLD"
    assert "SUBJECTIVE_EXPERIENCE_UNPROVEN" in experience.reason_codes

    verified = classify({
        "claim_type": "OBSERVABLE_SIGNAL_INTERPRETATION",
        "verification_status": "VERIFIED",
        "provenance": "experiment-001",
        "evidence": [{"type": "replication", "id": "r1"}],
    })
    assert verified.status == "PASS"
    assert verified.production_mutation_allowed is False

    report = audit([{
        "claim_type": "OBSERVABLE_SIGNAL_INTERPRETATION",
        "verification_status": "VERIFIED",
        "provenance": "experiment-001",
        "evidence": [{"type": "replication", "id": "r1"}],
    }])
    assert report["status"] == "PASS"
    assert report["records"] == 1
    assert len(report["fingerprint"]) == 64
    print("SUPREME_NLP_NEUTRALITY_GATE_OK")


if __name__ == "__main__":
    main()
