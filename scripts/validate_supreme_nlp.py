"""Deterministic contract/regression tests for Supreme NLP."""
from agents.supreme_nlp import build_record, summarize


def main():
    samples = [
        {"modality":"sensor","feature":"voltage","value":1.0,"unit":"mV","quality":.95,"source":"synthetic"},
        {"modality":"sensor","feature":"voltage","value":1.2,"unit":"mV","quality":.92,"source":"synthetic"},
        {"modality":"audio","feature":"vibration_rms","value":.8,"unit":"a.u.","quality":.88,"source":"synthetic"},
    ]
    record = build_record(samples, "smoke-001")
    assert record["schema_version"] == "1.2"
    assert record["result"]["status"] == "interpreted"
    assert 0 <= record["result"]["interpretation"]["confidence"] <= .95
    assert record["result"]["features"]["evidence_grade"] in {"A","B","C","D"}
    assert len(record["fingerprint"]) == 64
    assert record["uncertainty"]["confidence_is_calibrated"] is False
    assert record["uncertainty"]["independent_verification"] == "NOT_VERIFIED"
    assert record["uncertainty"]["causal_claim"] == "NOT_ESTABLISHED"
    assert record["provenance"]["source_count"] == 3
    assert record["result"]["quality_diagnostics"]["dropped_count"] == 0
    assert "proof" in " ".join(record["result"]["interpretation"]["limitations"]).lower()

    assert summarize([])["status"] == "no_data"
    assert summarize([{"modality":"x","feature":"q","value":1,"quality":0}])["status"] == "insufficient_quality"
    assert summarize([{"modality":"x","feature":"q","value":"not-a-number"}])["status"] == "no_data"
    assert summarize([{"modality":"x","feature":"q","value":1,"quality":0.5,"timestamp":"t"}])["quality_diagnostics"]["usable_count"] == 1

    # Regression: deterministic state classification remains bounded.
    low = summarize([{"modality":"sensor","feature":"x","value":1,"quality":1}])
    high = summarize([
        {"modality":"sensor","feature":"x","value":0.1,"quality":1},
        {"modality":"sensor","feature":"x","value":10,"quality":1},
    ])
    assert low["interpretation"]["confidence"] <= .95
    assert high["interpretation"]["confidence"] <= .95

    print("SUPREME_NLP_CONTRACT_OK")
    print(record["simple_language"])


if __name__ == "__main__":
    main()
