"""Evidence-first multimodal-to-NLP control layer.

v2 goals:
- accept heterogeneous observable signals with provenance;
- produce deterministic, human-readable summaries;
- expose uncertainty and data-quality boundaries explicitly;
- route multilingual text by script without pretending that routing is translation;
- never infer subjective experience directly from a signal.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "supreme-nlp-v2"

SCRIPT_RANGES = {
    "hi": (0x0900, 0x097F),
    "pa": (0x0A00, 0x0A7F),
    "bn": (0x0980, 0x09FF),
    "gu": (0x0A80, 0x0AFF),
    "ta": (0x0B80, 0x0BFF),
    "te": (0x0C00, 0x0C7F),
    "kn": (0x0C80, 0x0CFF),
    "ml": (0x0D00, 0x0D7F),
    "or": (0x0B00, 0x0B7F),
    "ur": (0x0600, 0x06FF),
}

def _sha(obj: Any) -> str:
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()

def detect_script(text: str) -> str:
    counts = {k: 0 for k in SCRIPT_RANGES}
    latin = 0
    for char in str(text):
        code = ord(char)
        for name, (lo, hi) in SCRIPT_RANGES.items():
            if lo <= code <= hi:
                counts[name] += 1
                break
        elif "A" <= char <= "Z" or "a" <= char <= "z":
            latin += 1
    if max(counts.values(), default=0) > 0:
        return max(counts, key=counts.get)
    return "en" if latin or str(text).strip() else "unknown"

def text_features(text: str) -> dict[str, Any]:
    clean = normalize_text(text)
    tokens = re.findall(r"\S+", clean)
    return {
        "characters": len(clean),
        "tokens": len(tokens),
        "script": detect_script(clean),
        "has_text": bool(clean),
    }

def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))

def normalize_signal(signal: dict[str, Any], index: int) -> dict[str, Any]:
    value = signal.get("value")
    return {
        "index": index,
        "type": str(signal.get("type", "unknown")),
        "value": float(value) if _finite_number(value) else None,
        "unit": str(signal.get("unit", "")),
        "timestamp": signal.get("timestamp"),
        "source_id": str(signal.get("source_id", "")),
        "quality": signal.get("quality"),
    }

def signal_summary(signals: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = [normalize_signal(s, i) for i, s in enumerate(signals)]
    kinds: dict[str, int] = {}
    values: list[float] = []
    missing_provenance = 0
    qualities: list[float] = []
    for s in normalized:
        kinds[s["type"]] = kinds.get(s["type"], 0) + 1
        if s["value"] is not None:
            values.append(s["value"])
        if not s["source_id"] or not s["timestamp"]:
            missing_provenance += 1
        if _finite_number(s["quality"]):
            qualities.append(float(s["quality"]))
    summary = {
        "signal_count": len(normalized),
        "signal_types": kinds,
        "numeric_observations": len(values),
        "numeric_mean": statistics.fmean(values) if values else None,
        "numeric_min": min(values) if values else None,
        "numeric_max": max(values) if values else None,
        "numeric_stddev": statistics.pstdev(values) if len(values) > 1 else 0.0 if values else None,
        "missing_provenance": missing_provenance,
        "mean_quality": statistics.fmean(qualities) if qualities else None,
    }
    summary["provenance_completeness"] = (
        1.0 - missing_provenance / len(normalized) if normalized else 0.0
    )
    return summary

def _confidence_boundary(validation: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(validation, dict):
        return {
            "confidence": 0.0,
            "status": "UNVERIFIED",
            "reason": "No evaluated validation set supplied.",
        }
    n = validation.get("n")
    accuracy = validation.get("accuracy")
    if not (_finite_number(n) and n > 0 and _finite_number(accuracy) and 0 <= float(accuracy) <= 1):
        return {
            "confidence": 0.0,
            "status": "UNVERIFIED",
            "reason": "Validation record is incomplete or outside allowed bounds.",
        }
    return {
        "confidence": float(accuracy),
        "status": "EVALUATED",
        "reason": "Reported as validation accuracy, not as subjective-state certainty.",
        "validation_n": int(n),
    }

def interpret(observation: dict[str, Any]) -> dict[str, Any]:
    signals = observation.get("signals") or []
    context = normalize_text(observation.get("context", ""))
    validation = observation.get("validation")
    summary = signal_summary(signals)
    confidence = _confidence_boundary(validation)
    text_info = text_features(context)

    natural_language = (
        f"Received {summary['signal_count']} observable signal(s) across "
        f"{len(summary['signal_types'])} signal type(s). "
        "The system can describe measurable patterns and their provenance, "
        "but the measurements alone do not establish subjective emotion or consciousness."
    )

    return {
        "schema_version": VERSION,
        "status": confidence["status"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_sha256": _sha(observation),
        "observation": {
            "context": context,
            "text_features": text_info,
            "summary": summary,
        },
        "natural_language": natural_language,
        "evidence_boundary": "observable_signal_only",
        "confidence": confidence["confidence"],
        "confidence_basis": confidence,
        "verification": {
            "required": True,
            "independent_reviewer_required": True,
            "counter_evidence_required": True,
        },
        "next_actions": [
            "collect repeated observations",
            "compare with labelled/control data",
            "test alternative explanations",
            "record counter-evidence",
            "audit provenance and data quality",
            "independently verify before promotion",
        ],
    }

def save(observation: dict[str, Any], path: str) -> dict[str, Any]:
    result = interpret(observation)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result

if __name__ == "__main__":
    print(json.dumps(
        interpret({"context": "baseline", "signals": []}),
        ensure_ascii=False,
        indent=2,
    ))
