"""Regression tests for the multimodal Supreme NLP benchmark."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmarks.supreme_nlp_benchmark import run_benchmark


def test_multimodal_benchmark_passes():
    result = run_benchmark()
    assert result["ok"] is True
    assert result["case_count"] >= 9
    assert len(result["modalities"]) >= 9
    assert all(result["guards"].values())


def test_benchmark_never_upgrades_signal_to_subjective_experience():
    result = run_benchmark()
    assert all(
        item["subjective_experience_guard"] and item["claim_type"] == "data_interpretation"
        for item in result["results"]
    )
