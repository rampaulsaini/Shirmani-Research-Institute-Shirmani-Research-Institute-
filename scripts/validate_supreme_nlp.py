"""Deterministic smoke/contract tests for the Supreme NLP layer."""
from agents.supreme_nlp import build_record, summarize

def main():
    samples = [
        {"modality":"sensor","feature":"voltage","value":1.0,"unit":"mV","quality":0.95,"source":"synthetic"},
        {"modality":"sensor","feature":"voltage","value":1.2,"unit":"mV","quality":0.92,"source":"synthetic"},
        {"modality":"audio","feature":"vibration_rms","value":0.8,"unit":"a.u.","quality":0.88,"source":"synthetic"},
    ]
    record = build_record(samples, "smoke-001")
    assert record["schema_version"] == "1.0"
    assert record["result"]["status"] == "interpreted"
    assert 0 <= record["result"]["interpretation"]["confidence"] <= 1
    assert record["fingerprint"]
    assert "proof" in " ".join(record["result"]["interpretation"]["limitations"]).lower()
    empty = summarize([])
    assert empty["status"] == "no_data"
    print("SUPREME_NLP_SMOKE_OK")
    print(record["simple_language"])

if __name__ == "__main__":
    main()
