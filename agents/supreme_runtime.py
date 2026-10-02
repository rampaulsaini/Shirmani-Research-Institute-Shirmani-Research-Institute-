"""Provider-neutral Supreme AI/ML/NLP Automission runtime.

This module is a deterministic, dependency-light reference runtime. It keeps
measured signals, model inference, interpretation, uncertainty and verification
state separate so richer ML/NLP providers can be added without weakening the
fail-closed contract.
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
    task: str = "lexical-pattern-detection"


class BaselineNLP:
    """Transparent lexical baseline; never a claim of universal accuracy."""

    POSITIVE = {
        "good", "great", "happy", "love", "excellent",
        "श्रेष्ठ", "अच्छा", "प्रेम", "उत्तम",
    }
    NEGATIVE = {
        "bad", "sad", "hate", "poor", "danger",
        "खराब", "दुख", "घृणा", "खतरा",
    }

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
        return Inference(
            label=label,
            evidence=evidence,
            confidence="heuristic; uncalibrated",
        )


class SupremeAutomission:
    """Observe → Quality Check → Normalize → Infer → Explain → Audit.

    This reference runtime performs no external side effects. High-impact
    actions require a separately authorized integration and independent gates.
    """

    def __init__(self) -> None:
        self.nlp = BaselineNLP()

    @staticmethod
    def fingerprint(value: Any) -> str:
        raw = repr(value).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    @staticmethod
    def quality_check(signal: Signal) -> List[str]:
        errors = []
        if not signal.kind or not signal.kind.strip():
            errors.append("missing-signal-kind")
        if signal.value is None or (isinstance(signal.value, str) and not signal.value.strip()):
            errors.append("missing-signal-value")
        if not signal.source or not signal.source.strip():
            errors.append("missing-provenance-source")
        if not signal.timestamp or not signal.timestamp.strip():
            errors.append("missing-timestamp")
        return errors

    def run(self, signal: Signal) -> Dict[str, Any]:
        observed = asdict(signal)
        quality_errors = self.quality_check(signal)

        if quality_errors:
            return {
                "status": "BLOCKED",
                "observed_signal": observed,
                "inference": None,
                "plain_language": (
                    "The supplied signal was blocked by the quality gate: "
                    + ", ".join(quality_errors)
                ),
                "provenance": {
                    "source": signal.source,
                    "signal_fingerprint": self.fingerprint(observed),
                    "model": "none",
                    "model_version": "none",
                },
                "uncertainty": "not assessed",
                "verification_state": "BLOCKED",
                "required_next_gate": "correct-input-and-provenance",
                "quality_errors": quality_errors,
            }

        # The deterministic baseline is intentionally text-only. Other
        # modalities must be routed to modality-specific models rather than
        # being silently coerced into text or subjective-state claims.
        if signal.kind.lower() not in {"text", "speech", "audio-transcript"}:
            return {
                "status": "UNVERIFIED",
                "observed_signal": observed,
                "inference": {
                    "label": "modality-not-evaluated",
                    "evidence": [],
                    "confidence": "not assessed by this baseline",
                    "provider": "deterministic-baseline",
                    "task": "text-only-reference-runtime",
                },
                "plain_language": (
                    f"Measured {signal.kind} signal was accepted, but this "
                    "text-only baseline does not interpret that modality. "
                    "A modality-specific validated model is required. This "
                    "record is not evidence of subjective feeling, consciousness, "
                    "intention, or inner experience."
                ),
                "provenance": {
                    "source": signal.source,
                    "signal_fingerprint": self.fingerprint(observed),
                    "model": "deterministic-baseline-nlp",
                    "model_version": "0.2",
                },
                "uncertainty": "not assessed",
                "verification_state": "UNVERIFIED",
                "required_next_gate": "modality-specific-independent-verification",
            }

        text = str(signal.value)
        inference = self.nlp.infer(text)
        return {
            "status": "UNVERIFIED",
            "observed_signal": observed,
            "inference": asdict(inference),
            "plain_language": (
                f"Observed a {inference.label} lexical pattern in the supplied "
                f"signal. Evidence tokens: {', '.join(inference.evidence) or 'none'}. "
                "This is a baseline model inference, not proof of subjective "
                "feeling, consciousness, intention, or inner experience."
            ),
            "provenance": {
                "source": signal.source,
                "signal_fingerprint": self.fingerprint(observed),
                "model": "deterministic-baseline-nlp",
                "model_version": "0.2",
            },
            "uncertainty": inference.confidence,
            "verification_state": "UNVERIFIED",
            "required_next_gate": "independent-verification",
        }


if __name__ == "__main__":
    print("SHIRMANI Supreme runtime module: importable")
