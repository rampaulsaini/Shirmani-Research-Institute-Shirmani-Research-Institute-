from dataclasses import dataclass, asdict
from typing import Any, Mapping
import hashlib
import json
import re


@dataclass(frozen=True)
class Signal:
    source: str
    modality: str
    value: Any
    timestamp: str | None = None
    provenance: str | None = None


@dataclass(frozen=True)
class Interpretation:
    statement: str
    evidence: list[str]
    confidence: float
    status: str


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u200b", " ").strip())


def stable_fingerprint(payload: Mapping[str, Any]) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def interpret_signal(signal: Signal) -> Interpretation:
    evidence = [
        f"source={signal.source}",
        f"modality={signal.modality}",
        f"value={signal.value!r}",
    ]
    if signal.value is None:
        return Interpretation(
            "No interpretable signal was supplied.",
            evidence,
            0.0,
            "insufficient-evidence",
        )
    confidence = 0.70 if signal.provenance else 0.55
    statement = (
        f"An observable {signal.modality} signal was received from {signal.source}. "
        "Its measured pattern can be analyzed, but this record alone does not "
        "establish subjective experience or intention."
    )
    return Interpretation(statement, evidence, confidence, "hypothesis")


def audit_record(signal: Signal, interpretation: Interpretation) -> dict[str, Any]:
    record = {
        "signal": asdict(signal),
        "interpretation": asdict(interpretation),
    }
    record["fingerprint"] = stable_fingerprint(record)
    return record
