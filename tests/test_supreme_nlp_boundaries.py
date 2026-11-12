import json
from agents.supreme_nlp_practitioner import build_practitioner_record

def test_empty_signals_fail_closed():
    result = build_practitioner_record([], "भाव")
    assert result["result"]["status"] == "insufficient_quality"

def test_multimodal_record_is_bounded():
    rows = [
        {"modality": "electrical", "feature": "x", "value": 1.0, "quality": 1.0, "source": "a"},
        {"modality": "vibration", "feature": "x", "value": 1.1, "quality": 1.0, "source": "b"},
    ]
    result = build_practitioner_record(rows, "भाव")
    assert result["result"]["status"] == "interpreted"
    assert 0.0 <= result["result"]["features"]["confidence"] <= 1.0
    assert result["governance"]["subjective_experience_claim_allowed"] is False
    assert result["governance"]["code_mutation_allowed"] is False
    assert result["governance"]["independent_verification_required"] is True

def test_record_is_json_serializable():
    rows = [{"modality": "demo", "feature": "x", "value": 1.0, "source": "a"}]
    record = build_practitioner_record(rows)
    json.dumps(record, ensure_ascii=False)
