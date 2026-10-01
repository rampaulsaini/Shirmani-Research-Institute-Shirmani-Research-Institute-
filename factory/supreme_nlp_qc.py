"""Deterministic QC for the Supreme NLP v2 control layer."""
from agents.supreme_nlp_agent import detect_script, interpret, signal_summary, text_features

def main():
    observation = {
        "context": "निष्पक्ष multilingual baseline",
        "signals": [
            {"type": "electrical", "value": 1.0, "unit": "u", "source_id": "s1", "timestamp": "t1", "quality": 0.9},
            {"type": "vibration", "value": 0.5, "unit": "u", "source_id": "s2", "timestamp": "t2", "quality": 0.8},
            {"type": "thermal", "value": 2.0, "unit": "u", "source_id": "s3", "timestamp": "t3", "quality": 0.7},
        ],
    }
    out = interpret(observation)
    required = {
        "schema_version", "status", "input_sha256", "natural_language",
        "evidence_boundary", "confidence", "confidence_basis",
        "verification", "next_actions", "observation",
    }
    assert required <= set(out), f"missing={sorted(required - set(out))}"
    assert out["schema_version"] == "supreme-nlp-v2"
    assert out["status"] == "UNVERIFIED"
    assert out["confidence"] == 0.0
    assert out["verification"]["independent_reviewer_required"] is True
    assert out["verification"]["counter_evidence_required"] is True
    assert out["evidence_boundary"] == "observable_signal_only"
    assert out["observation"]["summary"]["numeric_observations"] == 3
    assert out["observation"]["summary"]["provenance_completeness"] == 1.0
    assert detect_script("हिंदी") == "hi"
    assert detect_script("ਪੰਜਾਬੀ") == "pa"
    assert detect_script("English") == "en"
    assert text_features("hello world")["tokens"] == 2
    assert signal_summary([])["signal_count"] == 0

    evaluated = interpret({
        "context": "validated example",
        "signals": [],
        "validation": {"n": 100, "accuracy": 0.91},
    })
    assert evaluated["status"] == "EVALUATED"
    assert evaluated["confidence"] == 0.91
    assert evaluated["confidence_basis"]["validation_n"] == 100

    invalid = interpret({
        "context": "invalid validation",
        "signals": [],
        "validation": {"n": 0, "accuracy": 1.2},
    })
    assert invalid["status"] == "UNVERIFIED"
    assert invalid["confidence"] == 0.0
    print("SUPREME_NLP_V2_QC=PASS")

if __name__ == "__main__":
    main()
