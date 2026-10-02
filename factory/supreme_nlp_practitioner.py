"""Deterministic, evidence-first NLP practitioner runtime.

Translates structured measured signals into a plain-language report while
preserving the distinction between measurement, inference and interpretation.
"""
from __future__ import annotations
import hashlib, json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Mapping

VERIFICATION_STATES = {"REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"}

@dataclass(frozen=True)
class PractitionerResult:
    record_id: str
    status: str
    measured_signal: str
    detected_pattern: str
    model_inference: str
    interpretation: str
    confidence: float | None
    provenance: list[str]
    alternative_interpretations: list[str]
    unresolved_unknowns: list[str]
    verification_state: str
    fingerprint: str

def _fingerprint(payload: Mapping[str, Any]) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def evaluate(record: Mapping[str, Any]) -> PractitionerResult:
    required = ("record_id", "signal", "pattern", "inference", "provenance")
    missing = [k for k in required if not record.get(k)]
    if missing:
        return PractitionerResult(
            str(record.get("record_id", "unknown")), "BLOCKED",
            str(record.get("signal", "")), str(record.get("pattern", "")),
            str(record.get("inference", "")),
            "Cannot interpret safely because required evidence fields are missing: " + ", ".join(missing),
            None, list(record.get("provenance", [])), [], ["Missing required evidence fields"],
            "BLOCKED", _fingerprint(dict(record))
        )
    confidence = record.get("confidence")
    try:
        confidence = float(confidence) if confidence is not None else None
    except (TypeError, ValueError):
        confidence = None
    if confidence is not None and not 0.0 <= confidence <= 1.0:
        confidence = None

    alternatives = [str(x) for x in record.get("alternative_interpretations", [])]
    unknowns = [str(x) for x in record.get("unresolved_unknowns", [])]
    interpretation = (
        "Measured data show the reported pattern. The model inference is: "
        f"{record['inference']}. This is an interpretation of measured signals, "
        "not proof of subjective feeling, consciousness, intention, or inner experience."
    )
    if alternatives:
        interpretation += " Alternative interpretation(s) remain: " + "; ".join(alternatives) + "."

    state = str(record.get("verification_state", "UNVERIFIED")).upper()
    if state not in VERIFICATION_STATES:
        state = "BLOCKED"
        unknowns.append("Invalid verification state supplied")
    if state == "VERIFIED" and not record.get("verification_evidence"):
        state = "REVIEW"
        unknowns.append("VERIFIED state requires explicit verification evidence")

    return PractitionerResult(
        str(record["record_id"]), "INTERPRETED", str(record["signal"]),
        str(record["pattern"]), str(record["inference"]), interpretation,
        confidence, [str(x) for x in record["provenance"]], alternatives,
        unknowns, state, _fingerprint(dict(record))
    )

def report(record: Mapping[str, Any]) -> dict[str, Any]:
    result = evaluate(record)
    return {**asdict(result), "generated_at": datetime.now(timezone.utc).isoformat(),
            "contract": {"measured_signal_distinct_from_inference": True,
                         "subjective_experience_claim_allowed": False,
                         "provenance_required": True, "fail_closed": True}}

if __name__ == "__main__":
    import sys
    source = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 1 else {}
    print(json.dumps(report(source), ensure_ascii=False, indent=2))
