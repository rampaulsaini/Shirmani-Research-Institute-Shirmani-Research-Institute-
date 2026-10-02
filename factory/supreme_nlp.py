#!/usr/bin/env python3
"""Deterministic Supreme NLP control-plane baseline."""
from __future__ import annotations
import hashlib, json, math, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
OUT_JSONL = GENERATED / "supreme-nlp-records.jsonl"
OUT_STATUS = GENERATED / "supreme-nlp-status.json"

LANGUAGE_HINTS = {
    "hi": "है हैं और का की के में से को यह वह मैं हम",
    "pa": "ਹੈ ਹਨ ਅਤੇ ਦਾ ਦੀ ਦੇ ਵਿੱਚ ਤੋਂ ਨੂੰ ਇਹ ਉਹ ਮੈਂ ਅਸੀਂ",
    "en": "the is are and of to in from this that I we",
}

def sha256_obj(obj: Any) -> str:
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def detect_language(text: str) -> str:
    scores = {k: 0 for k in LANGUAGE_HINTS}
    for lang, hints in LANGUAGE_HINTS.items():
        scores[lang] = sum(1 for token in re.findall(r"\S+", hints) if token in text)
    if scores["hi"] or re.search(r"[ऀ-ॿ]", text):
        return "hi"
    if scores["pa"] or re.search(r"[਀-੿]", text):
        return "pa"
    return "en"

def observable_signal_summary(signal: dict[str, Any]) -> dict[str, Any]:
    numeric = []
    for k, v in signal.items():
        if isinstance(v, (int, float)) and math.isfinite(float(v)):
            numeric.append((k, float(v)))
    return {
        "numeric_channels": len(numeric),
        "channels": [k for k, _ in numeric],
        "range_summary": (
            {"min": min(v for _, v in numeric), "max": max(v for _, v in numeric),
             "mean": sum(v for _, v in numeric) / len(numeric)}
            if numeric else None
        ),
        "interpretation_boundary": "observable_signal_only",
    }

def translate_signal_to_plain_language(signal: dict[str, Any], context: str = "") -> dict[str, Any]:
    summary = observable_signal_summary(signal)
    if summary["numeric_channels"] == 0:
        text = "कोई संख्यात्मक sensor signal उपलब्ध नहीं है; इसलिए observable अवस्था का निष्कर्ष नहीं निकाला जा सकता।"
        confidence = 0.0
    else:
        rs = summary["range_summary"]
        text = (f"इस नमूने में {summary['numeric_channels']} मापनीय signal channel मिले। "
                f"मूल्य सीमा {rs['min']:.4g} से {rs['max']:.4g} और औसत {rs['mean']:.4g} है।")
        if context:
            text += " संदर्भ उपलब्ध है, लेकिन subjective भावना का प्रत्यक्ष प्रमाण नहीं माना गया है।"
        confidence = 0.5
    return {
        "plain_language": text,
        "confidence": confidence,
        "claim_status": "OBSERVATION_ONLY",
        "human_experience_inference": "NOT_ESTABLISHED",
    }

def process_record(record: dict[str, Any]) -> dict[str, Any]:
    text = str(record.get("text", ""))
    signals = record.get("signals") or {}
    tokens = re.findall(r"\b[\wऀ-ॿ਀-੿]+\b", text.lower())
    counts = Counter(tokens)
    return {
        "record_id": str(record.get("id") or sha256_obj(record)[:16]),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "language": detect_language(text),
        "text_stats": {
            "characters": len(text), "tokens": len(tokens),
            "unique_tokens": len(counts), "top_terms": counts.most_common(10),
        },
        "signal_analysis": translate_signal_to_plain_language(signals, record.get("context", "")),
        "provenance": {
            "source": record.get("source") or record.get("repository") or "unknown",
            "input_hash": sha256_obj(record), "generator": "factory/supreme_nlp.py",
        },
        "verification": {
            "status": "NOT_VERIFIED", "independent": False,
            "reason": "Deterministic control-plane transformation; no empirical performance claim.",
        },
    }

def main() -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    source = GENERATED / "source-units.jsonl"
    rows = []
    if source.exists():
        for line in source.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    processed = [process_record(r) for r in rows[:1000]]
    OUT_JSONL.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in processed), encoding="utf-8")
    status = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "engine": "deterministic-supreme-nlp-control-plane",
        "input_records": len(rows), "processed_records": len(processed),
        "supported_modes": ["text", "observable_sensor_signal", "multilingual_routing"],
        "epistemic_policy": {
            "subjective_experience_direct_read": False,
            "observable_signal_translation": True,
            "unverified_claims_remain_unverified": True,
            "accuracy_is_measured_not_declared": True,
        },
        "status": "READY" if source.exists() else "WAITING_FOR_SOURCE",
        "output": str(OUT_JSONL.relative_to(ROOT)),
    }
    OUT_STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    main()
