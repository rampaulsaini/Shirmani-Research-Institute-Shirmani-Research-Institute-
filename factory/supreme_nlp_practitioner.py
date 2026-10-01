"""Supreme NLP practitioner: signal-to-language translation with explicit uncertainty.

This module never claims to directly read consciousness, feelings, or a
"quantum" state. It converts supplied observable/measurable signals and
context into plain-language observations, hypotheses, and next measurements.
NLP here means both Natural Language Processing and the project's
"Nispaksh Learning Programs" control discipline.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Mapping
import math
import re

SCHEMA_VERSION = "1.1"
VALID_DOMAINS = {"human", "animal", "plant", "material", "environment", "unknown"}
NLP_MODES = ("Natural Language Processing", "Nispaksh Learning Programs")
VALID_MODALITIES = {"sound", "vibration", "temperature", "electrical", "motion", "light", "chemical", "pressure", "image", "text", "other"}


@dataclass(frozen=True)
class Signal:
    name: str
    value: float
    unit: str = ""
    source: str = ""
    observed_at: str = ""
    quality: float = 1.0
    modality: str = "other"

    def normalized_quality(self) -> float:
        return max(0.0, min(1.0, float(self.quality)))


def _finite(value: Any) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return 0.0
    return x if math.isfinite(x) else 0.0


def normalize_signals(raw: Mapping[str, Any] | list[Mapping[str, Any]]) -> list[Signal]:
    items = raw.items() if isinstance(raw, Mapping) else (
        (str(i), item) for i, item in enumerate(raw)
    )
    result = []
    for key, item in items:
        if isinstance(item, Mapping):
            name = str(item.get("name", key))
            value = _finite(item.get("value"))
            unit = str(item.get("unit", ""))
            source = str(item.get("source", ""))
            observed_at = str(item.get("observed_at", ""))
            quality = _finite(item.get("quality", 1.0))
            modality = str(item.get("modality", "other")).lower()
        else:
            name, value, unit, source, observed_at, quality, modality = str(key), _finite(item), "", "", "", 1.0, "other"
        if modality not in VALID_MODALITIES:
            modality = "other"
        result.append(Signal(name, value, unit, source, observed_at, quality, modality))
    return result


def _quality(signals: list[Signal]) -> float:
    if not signals:
        return 0.0
    return round(sum(s.normalized_quality() for s in signals) / len(signals), 6)


def _plain_name(name: str) -> str:
    return re.sub(r"[_-]+", " ", name).strip()


def translate_observations(
    domain: str,
    signals: list[Signal],
    context: str = "",
    baseline: Mapping[str, float] | None = None,
) -> dict[str, Any]:
    domain = str(domain).lower()
    if domain not in VALID_DOMAINS:
        domain = "unknown"
    baseline = baseline or {}
    observations = []
    changes = []
    for s in signals:
        name = _plain_name(s.name)
        observations.append(
            f"{name}: {s.value:g}{(' ' + s.unit) if s.unit else ''}"
        )
        if s.name in baseline:
            delta = s.value - _finite(baseline[s.name])
            changes.append({
                "signal": s.name,
                "delta": round(delta, 6),
                "direction": "up" if delta > 0 else "down" if delta < 0 else "unchanged",
            })

    q = _quality(signals)
    quality_label = "high" if q >= 0.80 else "medium" if q >= 0.50 else "low"
    language = (
        "इन संकेतों के आधार पर अभी इतना कहा जा सकता है: "
        + ("; ".join(observations) if observations else "कोई मापनीय संकेत उपलब्ध नहीं है।")
    )
    if changes:
        language += " तुलना में परिवर्तन: " + "; ".join(
            f"{_plain_name(x['signal'])} {x['direction']} ({x['delta']:g})" for x in changes
        ) + "।"

    return {
        "schema_version": SCHEMA_VERSION,
        "domain": domain,
        "context": context,
        "signals": [asdict(s) for s in signals],
        "observation_quality": q,
        "observation_quality_label": quality_label,
        "nlp_modes": list(NLP_MODES),
        "observations": observations,
        "changes": changes,
        "plain_language_hi": language,
        "interpretation": {
            "status": "observable_signal_translation",
            "claim_boundary": (
                "Signals can support descriptions or hypotheses; they do not by "
                "themselves prove subjective experience, consciousness, intention, "
                "emotion, or a quantum state."
            ),
            "hypotheses": [],
            "required_next_measurements": [],
        },
        "nispaksh_learning_program": {
            "observe_without_prejudgment": True,
            "separate_observation_from_interpretation": True,
            "preserve_source_and_time": True,
            "show_uncertainty": True,
            "allow_revision_when_new_evidence_arrives": True,
        },
    }


def practitioner_report(
    domain: str,
    raw_signals: Mapping[str, Any] | list[Mapping[str, Any]],
    context: str = "",
    baseline: Mapping[str, float] | None = None,
) -> dict[str, Any]:
    signals = normalize_signals(raw_signals)
    report = translate_observations(domain, signals, context, baseline)
    report["ready_for_agent_pipeline"] = bool(signals) and report["observation_quality"] > 0
    return report
