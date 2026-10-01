"""Deterministic contract tests for Supreme NLP."""
from agents.supreme_nlp import build_record, summarize

def main():
    samples = [
        {"modality":"sensor","feature":"voltage","value":1.0,"unit":"mV","quality":.95,"source":"synthetic"},
        {"modality":"sensor","feature":"voltage","value":1.2,"unit":"mV","quality":.92,"source":"synthetic"},
        {"modality":"audio","feature":"vibration_rms","value":.8,"unit":"a.u.","quality":.88,"source":"synthetic"},
    ]
    record = build_record(samples, "smoke-001")
    assert record["schema_version"] == "1.1"
    assert record["result"]["status"] == "interpreted"
    assert 0 <= record["result"]["interpretation"]["confidence"] <= 1
    assert record["result"]["features"]["evidence_grade"] in {"A","B","C","D"}
    assert len(record["fingerprint"]) == 64
    assert "proof" in " ".join(record["result"]["interpretation"]["limitations"]).lower()
    assert summarize([])["status"] == "no_data"
    assert summarize([{"modality":"x","feature":"q","value":1,"quality":0}])["status"] == "insufficient_quality"
    print("SUPREME_NLP_CONTRACT_OK")
    print(record["simple_language"])

if __name__ == "__main__":
    main()
