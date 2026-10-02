"""Provider-neutral Supreme AI/ML/NLP Automission runtime.

This module is intentionally dependency-light. It provides a deterministic
orchestration contract and a transparent baseline NLP adapter. External model
providers can be added behind the same interface without weakening provenance,
uncertainty, or fail-closed rules.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, asdict
from typing import Any, Dict, List


@dataclass(frozen=True)
class Signal:
    kind: str
    value: Any
    source: str
    timestamp: str


@dataclass(frozen=True)
class Inference:
    label: str
    evidence: List[str]
    confidence: str
    provider: str = "deterministic-baseline"


class BaselineNLP:
    """Transparent baseline; not a claim of human-level or universal accuracy."""

    POSITIVE = {"good", "great", "happy", "love", "excellent", "श्रेष्ठ", "अच्छा", "प्रेम"}
    NEGATIVE = {"bad", "sad", "hate", "poor", "danger", "खराब", "दुख", "घृणा", "खतरा"}

    def infer(self, text: str) -> Inference:
        tokens = re.findall(r"[\w\u0900-\u097F]+", text.lower())
        pos = sorted(set(tokens) & self.POSITIVE)
        neg = sorted(set(tokens) & self.NEGATIVE)
        if len(pos) > len(neg):
            label, evidence = "positive-pattern", pos
        elif len(neg) > len(pos):
            label, evidence = "negative-pattern", neg
        else:
            label, evidence = "neutral-or-uncertain", pos + neg
        confidence = "heuristic; uncalibrated"
        return Inference(label=label, evidence=evidence, confidence=confidence)


class SupremeAutomission:
    """Observe → Normalize → Infer → Explain → Audit.

    No external side effect is performed by this class. High-impact actions
    must be handled by a separately authorized integration.
    """

    def __init__(self) -> None:
        self.nlp = BaselineNLP()

    @staticmethod
    def fingerprint(value: Any) -> str:
        raw = repr(value).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def run(self, signal: Signal) -> Dict[str, Any]:
        observed = asdict(signal)
        text = str(signal.value)
        inference = self.nlp.infer(text)
        result = {
            "status": "UNVERIFIED",
            "observed_signal": observed,
            "inference": asdict(inference),
            "plain_language": (
                f"Observed a {inference.label} pattern in the supplied signal. "
                f"Evidence tokens: {', '.join(inference.evidence) or 'none'}. "
                "This is a baseline model inference, not proof of subjective "
                "feeling, consciousness, intention, or inner experience."
            ),
            "provenance": {
                "source": signal.source,
                "signal_fingerprint": self.fingerprint(observed),
                "model": "deterministic-baseline-nlp",
                "model_version": "0.1",
            },
            "uncertainty": inference.confidence,
            "required_next_gate": "independent-verification",
        }
        return result
