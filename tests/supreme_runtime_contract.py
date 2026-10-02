from agents.supreme_runtime import Signal, SupremeAutomission


def main():
    runtime = SupremeAutomission()

    result = runtime.run(
        Signal(
            kind="text",
            value="great research",
            source="test",
            timestamp="2026-10-02T00:00:00Z",
        )
    )
    assert result["status"] == "UNVERIFIED"
    assert result["verification_state"] == "UNVERIFIED"
    assert result["inference"]["label"] == "positive-pattern"
    assert result["inference"]["task"] == "lexical-pattern-detection"
    assert result["provenance"]["model"] == "deterministic-baseline-nlp"
    assert result["provenance"]["model_version"] == "0.2"
    assert result["required_next_gate"] == "independent-verification"
    assert "not proof" in result["plain_language"]

    hindi = runtime.run(
        Signal(
            kind="text",
            value="श्रेष्ठ प्रेम",
            source="test",
            timestamp="2026-10-02T00:00:00Z",
        )
    )
    assert hindi["inference"]["label"] == "positive-pattern"
    assert set(hindi["inference"]["evidence"]) == {"श्रेष्ठ", "प्रेम"}

    plant = runtime.run(
        Signal(
            kind="plant-electrical",
            value={"voltage": [0.1, 0.2, 0.3]},
            source="instrument-test",
            timestamp="2026-10-02T00:00:00Z",
        )
    )
    assert plant["status"] == "UNVERIFIED"
    assert plant["inference"]["label"] == "modality-not-evaluated"
    assert plant["required_next_gate"] == "modality-specific-independent-verification"
    assert "subjective feeling" in plant["plain_language"]

    blocked = runtime.run(
        Signal(kind="text", value="", source="test", timestamp="2026-10-02T00:00:00Z")
    )
    assert blocked["status"] == "BLOCKED"
    assert blocked["verification_state"] == "BLOCKED"
    assert "missing-signal-value" in blocked["quality_errors"]

    print("SHIRMANI Supreme AI-ML-NLP runtime contract: PASS")


if __name__ == "__main__":
    main()
