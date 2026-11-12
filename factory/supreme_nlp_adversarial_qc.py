#!/usr/bin/env python3
"""Adversarial regression gate for SHIRMANI Supreme NLP."""
from __future__ import annotations
from agents.supreme_nlp_multimodal import analyze, to_simple_language

def semantic_view(record: dict) -> dict:
    x = dict(record)
    x.pop("generated_at", None)
    p = dict(x.get("provenance") or {})
    p.pop("timestamp", None)
    p.pop("fingerprint", None)
    x["provenance"] = p
    return x

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("BLOCK: " + message)

def main() -> int:
    clean = [
        {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "a"},
        {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 1.0, "source": "b"},
        {"modality": "thermal", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "c"},
    ]
    clean_a = analyze(clean, request="measurement", source_type="synthetic")
    clean_b = analyze(clean, request="measurement", source_type="synthetic")
    require(semantic_view(clean_a) == semantic_view(clean_b), "semantic output is not reproducible for identical input")
    require(0.0 <= clean_a["confidence"] <= 1.0, "confidence escaped [0,1]")
    require(clean_a["verification"]["status"] == "UNVERIFIED", "clean signal was incorrectly promoted")
    require(clean_a["verification"]["promotion_allowed"] is False, "promotion boundary was opened")
    plain = to_simple_language(clean_a).lower()
    require("subjective" in plain or "भाव" in plain, "plain-language boundary is missing")

    empty = analyze([], request="measurement", source_type="synthetic")
    require(empty["status"] == "NO_CLAIM", "empty input must abstain")
    require(empty["verification"]["promotion_allowed"] is False, "empty input must never be promoted")

    conflict = [
        {"modality": "electrical", "feature": "signal", "value": 0.0, "quality": 1.0, "source": "a"},
        {"modality": "audio", "feature": "signal", "value": 100.0, "quality": 1.0, "source": "b"},
    ]
    conflicted = analyze(conflict, request="experience interpretation", source_type="synthetic")
    require(conflicted["status"] == "BLOCKED", "strongly conflicting observations must block")
    require(conflicted["verification"]["promotion_allowed"] is False, "conflicting observations must never be promoted")

    malformed = [
        {"modality": "sensor", "feature": "signal", "value": "not-a-number", "quality": 1.0, "source": "a"},
        {"modality": "sensor", "feature": "signal", "value": float("nan"), "quality": 1.0, "source": "b"},
    ]
    safe = analyze(malformed, request="measurement", source_type="synthetic")
    require(0.0 <= safe["confidence"] <= 1.0, "malformed input escaped confidence bounds")
    require(safe["verification"]["status"] == "UNVERIFIED", "malformed input was treated as verified")
    print("SHIRMANI Supreme NLP Adversarial Regression Gate: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
