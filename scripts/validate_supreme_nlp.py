"""Deterministic contract tests for Supreme NLP v2."""
from agents.supreme_nlp import build_record, summarize

def main():
    samples = [
        {"modality":"sensor","feature":"voltage","value":1.0,"unit":"mV","quality":.95,"source":"sensor-a","baseline_mean":1.0,"baseline_std":.1},
        {"modality":"sensor","feature":"voltage","value":1.2,"unit":"mV","quality":.92,"source":"sensor-b","baseline_mean":1.0,"baseline_std":.1},
        {"modality":"audio","feature":"vibration_rms","value":.8,"unit":"a.u.","quality":.88,"source":"audio-a"},
    ]
    record = build_record(samples, "smoke-001")
    assert record["schema_version"] == "supreme-nlp-v2"
    assert record["result"]["status"] == "interpreted"
    i = record["result"]["interpretation"]
    f = record["result"]["features"]
    assert 0 <= i["confidence"] <= 1
    assert i["confidence_status"] == "UNCALIBRATED"
    assert f["independent_sources"] == 3
    assert f["sample_count"] == 3
    assert 0 <= f["drift_score"] <= 1
    assert f["evidence_grade"] in {"A","B","C","D"}
    assert record["result"]["verification"]["status"] == "UNVERIFIED"
    assert record["provenance"]["verification_status"] == "UNVERIFIED"
    assert len(record["fingerprint"]) == 64
    assert summarize([])["status"] == "no_data"
    assert summarize([{"modality":"x","feature":"q","value":1,"quality":0}])["status"] == "insufficient_quality"
    print("SUPREME_NLP_V2_CONTRACT_OK")
    print(record["simple_language"])

if __name__ == "__main__":
    main()
