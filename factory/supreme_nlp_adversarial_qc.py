"""Adversarial, deterministic QC for the Supreme NLP control contract.

This test suite validates failure handling and evidence boundaries. It does not
claim biological emotion/experience detection accuracy; that requires labelled,
independent domain data and calibration.
"""
from __future__ import annotations

import math

from agents.supreme_nlp import build_record, normalize_signal, summarize, to_simple_language


def main() -> None:
    # Empty input must fail closed.
    empty = summarize([])
    assert empty["status"] == "no_data"
    assert to_simple_language(empty).startswith("अभी पर्याप्त गुणवत्ता")

    # Non-finite values must be sanitized rather than propagated.
    bad = normalize_signal({"modality": "sensor", "feature": "x", "value": float("nan")})
    assert math.isfinite(bad.value)
    inf = normalize_signal({"modality": "sensor", "feature": "x", "value": float("inf")})
    assert math.isfinite(inf.value)

    # Zero-quality observations cannot produce an interpretation.
    low = summarize([
        {"modality": "sensor", "feature": "x", "value": 1, "quality": 0},
        {"modality": "sensor", "feature": "x", "value": 2, "quality": 0},
    ])
    assert low["status"] == "insufficient_quality"

    # Repeated measurements from one source must not masquerade as independent sources.
    one_source = summarize([
        {"modality": "sensor", "feature": "x", "value": 1, "source": "same"},
        {"modality": "sensor", "feature": "y", "value": 1.1, "source": "same"},
        {"modality": "sensor", "feature": "z", "value": 1.2, "source": "same"},
    ])
    assert one_source["features"]["independent_sources"] == 1

    # Strongly discordant observations must surface variability, not certainty.
    discordant = build_record([
        {"modality": "sensor", "feature": "x", "value": 0, "quality": 1, "source": "a"},
        {"modality": "vibration", "feature": "x", "value": 100, "quality": 1, "source": "b"},
    ], "adversarial-discordance")
    result = discordant["result"]
    assert result["features"]["anomaly_score"] >= 0.66
    assert 0 <= result["interpretation"]["confidence"] <= 1
    assert result["interpretation"]["confidence_status"] == "UNCALIBRATED"
    assert result["verification"]["status"] == "UNVERIFIED"
    assert "direct proof" in discordant["simple_language"]

    # Baseline information must be surfaced rather than silently discarded.
    baseline = summarize([
        {
            "modality": "sensor",
            "feature": "electrical",
            "value": 4,
            "baseline_mean": 1,
            "baseline_std": 1,
            "source": "a",
        }
    ])
    assert baseline["features"]["drift_score"] > 0

    # Provenance/verification contract must remain present.
    record = build_record(
        [{"modality": "sensor", "feature": "x", "value": 1, "source": "qc"}],
        "contract-check",
    )
    assert record["schema_version"] == "supreme-nlp-v2"
    assert record["provenance"]["contract"] == "observable-signal-only"
    assert record["provenance"]["verification_status"] == "UNVERIFIED"

    print("SUPREME_NLP_ADVERSARIAL_QC=PASS")


if __name__ == "__main__":
    main()
