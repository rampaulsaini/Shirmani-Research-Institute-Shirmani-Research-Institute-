import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from factory.supreme_nlp_evidence_engine import build_record, fuse_observations, render_simple_language

GOOD = {
    "source":"test",
    "modality":"sensor",
    "value":{"x":1},
    "timestamp":"2026-10-02T00:00:00Z",
    "quality":1.0,
    "preprocessing_version":"v1",
    "model_version":"test",
    "provenance_fingerprint":"1234567890abcdef",
}

def main():
    fused = fuse_observations([GOOD])
    assert fused["status"] == "CANDIDATE"
    assert fused["evidence_class"] == "OBSERVED"
    bad = dict(GOOD)
    bad["quality"] = 2
    assert fuse_observations([bad])["status"] == "BLOCKED"
    record = build_record(
        evidence_class="INFERRED",
        status="CANDIDATE",
        observations=[GOOD],
        claims=["pattern"],
        limitations=["unknown"],
        confidence=0.75,
    )
    assert 0 <= record["confidence"] <= 1
    assert len(record["provenance"]["fingerprint"]) == 64
    text = render_simple_language(
        evidence_class="UNKNOWN",
        status="NO_CLAIM",
        measured="signal",
        pattern="none",
        interpretation="should be replaced",
        unknown="unknown",
        confidence=0.0,
    )
    assert "कोई निश्चित दावा" in text
    print("SUPREME_NLP_CONTRACT_TEST: PASS")

if __name__ == "__main__":
    main()
