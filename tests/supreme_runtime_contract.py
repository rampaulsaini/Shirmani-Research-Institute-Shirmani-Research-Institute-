from agents.supreme_runtime import Signal, SupremeAutomission

def main():
    result = SupremeAutomission().run(
        Signal(kind="text", value="great research", source="test", timestamp="2026-10-02T00:00:00Z")
    )
    assert result["status"] == "UNVERIFIED"
    assert result["inference"]["label"] == "positive-pattern"
    assert result["provenance"]["model"] == "deterministic-baseline-nlp"
    assert result["required_next_gate"] == "independent-verification"
    assert "not proof" in result["plain_language"]
    print("SHIRMANI Supreme AI-ML-NLP runtime contract: PASS")

if __name__ == "__main__":
    main()
