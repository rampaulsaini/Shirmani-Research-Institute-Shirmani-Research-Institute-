"""Regression tests for the deterministic multimodal NLP adapter."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.supreme_nlp_adapter import build_record, normalize_observation, to_plain_language


def test_normalize_observation():
    item = normalize_observation(
        modality="bioelectric",
        feature="voltage",
        value="0.42",
        unit="mV",
        source_id="sensor-1",
    )
    assert item["value"] == 0.42
    assert item["id"] == "bioelectric:voltage"
    assert item["unit"] == "mV"


def test_plain_language_is_cautious():
    result = to_plain_language(
        [{"modality": "vibration", "feature": "amplitude", "value": 2.5, "unit": "mm", "id": "obs-1"}],
        context="controlled fixture",
    )
    assert "vibration signal 'amplitude'" in result["plain_language"]
    assert result["claim_type"] == "data_interpretation"
    assert "subjective feelings" in result["epistemic_note"]


def test_invalid_measurement_rejected():
    try:
        normalize_observation(modality="bioelectric", feature="voltage", value="nan")
    except ValueError as exc:
        assert "finite" in str(exc)
    else:
        raise AssertionError("non-finite measurements must be rejected")


def test_unknown_modality_rejected():
    try:
        normalize_observation(modality="unknown", feature="x", value=1)
    except ValueError as exc:
        assert "unsupported modality" in str(exc)
    else:
        raise AssertionError("unknown modalities must be rejected")


def test_build_record_links_evidence_to_all_observations():
    record = build_record(
        event_id="fixture-001",
        source_type="plant_sensor",
        observations=[
            {"id": "obs-1", "modality": "bioelectric", "feature": "voltage", "value": 0.42, "unit": "mV"},
            {"id": "obs-2", "modality": "temperature", "feature": "ambient", "value": 24.1, "unit": "C"},
        ],
        confidence=0.75,
        context="controlled fixture",
    )
    assert record["interpretation"]["claim_type"] == "data_interpretation"
    assert record["verification"]["independent_check"] is False
    assert record["evidence"][0]["observation_ids"] == ["obs-1", "obs-2"]
    assert "subjective feelings" in record["interpretation"]["epistemic_note"]


def test_build_record_rejects_empty_observations():
    try:
        build_record(
            event_id="fixture-002",
            source_type="sensor",
            observations=[],
            confidence=0.5,
        )
    except ValueError as exc:
        assert "at least one observation" in str(exc)
    else:
        raise AssertionError("empty observation batches must be rejected")
