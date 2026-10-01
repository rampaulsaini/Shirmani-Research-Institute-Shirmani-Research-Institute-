import math

import pytest

from factory.supreme_nlp import canonical_hash, interpret, observe


def test_canonical_hash_is_stable():
    assert canonical_hash({"b": 2, "a": 1}) == canonical_hash({"a": 1, "b": 2})


def test_observation_has_traceable_evidence():
    obs = observe(
        "test-001",
        "PLANT",
        "ELECTRICAL",
        {"signal": 1.0},
        "relative-unit",
        "synthetic",
        {"test": True},
    )
    assert len(obs.evidence_hash) == 64
    assert obs.context["test"] is True


def test_interpretation_defaults_to_unverified():
    obs = observe(
        "test-002", "DEVICE", "TEMPERATURE",
        {"celsius": 21.5}, "C", "synthetic"
    )
    result = interpret(
        obs,
        "Measured temperature pattern detected.",
        ["environmental change may be present"],
        0.5,
    )
    assert result.verification_status == "UNVERIFIED"


@pytest.mark.parametrize(
    "values",
    [{"signal": math.nan}, {"signal": math.inf}, {"signal": -math.inf}],
)
def test_non_finite_signals_are_rejected(values):
    with pytest.raises(ValueError):
        observe("bad-signal", "PLANT", "ELECTRICAL", values, "unit", "synthetic")


def test_invalid_confidence_is_rejected():
    obs = observe(
        "test-003", "ANIMAL", "MOTION",
        {"velocity": 1.0}, "m/s", "synthetic"
    )
    with pytest.raises(ValueError):
        interpret(obs, "x", ["y"], 1.01)
