"""Deterministic multimodal benchmark for the Supreme NLP contract."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from factory.supreme_nlp_adapter import build_record

FIXTURE = Path(__file__).with_name("supreme-nlp-multimodal-fixtures.json")


def run_benchmark() -> Dict[str, Any]:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise ValueError("benchmark fixture must contain cases")

    results = []
    for case in cases:
        record = build_record(
            event_id=case["id"],
            source_type="benchmark_fixture",
            observations=[{
                "id": case["id"] + ":obs",
                "modality": case["modality"],
                "feature": case["feature"],
                "value": case["value"],
                "unit": case.get("unit"),
            }],
            confidence=0.5,
            context="deterministic benchmark fixture",
        )
        results.append({
            "id": case["id"],
            "modality": case["modality"],
            "claim_type": record["interpretation"]["claim_type"],
            "evidence_linked": record["evidence"][0]["observation_ids"] == [case["id"] + ":obs"],
            "plain_language_nonempty": bool(record["interpretation"]["plain_language"].strip()),
            "subjective_experience_guard": "does not by itself establish subjective feelings" in record["interpretation"]["epistemic_note"],
        })

    guards = {
        "all_cases_processed": len(results) == len(cases),
        "all_evidence_linked": all(item["evidence_linked"] for item in results),
        "all_language_nonempty": all(item["plain_language_nonempty"] for item in results),
        "all_subjective_experience_guards": all(item["subjective_experience_guard"] for item in results),
    }
    return {
        "ok": all(guards.values()),
        "case_count": len(results),
        "modalities": sorted({item["modality"] for item in results}),
        "guards": guards,
        "results": results,
    }


if __name__ == "__main__":
    print(json.dumps(run_benchmark(), indent=2))
