"""Continuous Supreme NLP multimodal integration contract."""
import json
from pathlib import Path
from agents.supreme_nlp_multimodal import analyze, to_simple_language, fingerprint

def main():
    rows = [
        {"modality":"electrical","feature":"signal","value":1.00,"quality":0.98,"source":"sensor-a"},
        {"modality":"audio","feature":"signal","value":1.02,"quality":0.97,"source":"sensor-b"},
        {"modality":"vibration","feature":"signal","value":0.99,"quality":0.96,"source":"sensor-c"},
    ]
    record = analyze(rows, request="भाव/एहसास interpretation", source_type="plant")
    assert record["status"] == "CANDIDATE"
    assert record["evidence_class"] == "INFERRED"
    assert 0 <= record["confidence"] <= 1
    assert record["uncertainty"]["abstention_available"] is True
    assert record["verification"]["status"] == "UNVERIFIED"
    assert record["verification"]["promotion_allowed"] is False
    assert record["provenance"]["fingerprint"] == fingerprint(record)
    text = to_simple_language(record)
    assert "प्रत्यक्ष भाव" in text and "चेतना" in text
    blocked = analyze([
        {"modality":"electrical","feature":"signal","value":0,"quality":1,"source":"a"},
        {"modality":"audio","feature":"signal","value":100,"quality":1,"source":"b"},
    ])
    assert blocked["status"] == "BLOCKED"
    assert blocked["uncertainty"]["abstention_available"] is True
    out = Path("generated/supreme-nlp/multimodal-contract-status.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"status":"PASS","contract":"supreme-nlp-multimodal-continuous","candidate":record,"conflict_case":blocked}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("SUPREME_NLP_MULTIMODAL_CONTINUOUS_CONTRACT: PASS")

if __name__ == "__main__":
    main()