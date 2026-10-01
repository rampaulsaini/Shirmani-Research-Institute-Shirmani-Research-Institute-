"""QC for the Supreme NLP contract."""
from __future__ import annotations

import json
from pathlib import Path

SCHEMA = Path("schemas/supreme-nlp-contract.json")


def main() -> None:
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert data["name"] == "SHIRMANI HEART-VIEW SUPREME NLP CONTRACT"
    rules = data["rules"]
    for key in (
        "no_mind_reading",
        "no_unearned_certainty",
        "observation_must_be_separated_from_interpretation",
        "unsupported_claims_default_to_unverified",
        "missing_evidence_default_to_unverified",
        "provenance_required",
        "human_review_for_high_impact_output",
    ):
        assert rules.get(key) is True, f"missing fail-closed rule: {key}"
    assert data["confidence_range"] == [0.0, 1.0]
    assert set(data["status_model"]) == {"OBSERVED", "INFERRED", "UNVERIFIED", "REJECTED"}

    from agents.supreme_nlp_agent import translate_signal

    unverified = translate_signal(
        source="qc",
        observation="example signal",
        model_interpretation="example interpretation",
        confidence=0.4,
        evidence=[],
    )
    assert unverified["status"] == "UNVERIFIED"

    inferred = translate_signal(
        source="qc",
        observation="example signal",
        model_interpretation="example interpretation",
        confidence=0.8,
        evidence=["controlled-test-1"],
    )
    assert inferred["status"] == "INFERRED"
    assert inferred["provenance"]

    print("SUPREME NLP QC: PASS")


if __name__ == "__main__":
    main()
