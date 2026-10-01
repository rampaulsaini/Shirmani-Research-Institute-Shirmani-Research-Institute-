"""Deterministic orchestration contract for the AI/ML/NLP/Automission pipeline.

This module does not claim that heuristics prove truth. It converts each stage
into an explicit contract so failures are isolated, measurable, and fail-closed.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Mapping, Sequence
import hashlib
import json
import re

TOKEN_RE = re.compile(r"[\w'-]+", re.UNICODE)

STAGES = (
    "AGENT_INGEST",
    "NLP_NORMALIZE",
    "ML_SCORE",
    "EVIDENCE_FUSION",
    "CONTRADICTION_CHECK",
    "INDEPENDENT_VERIFY",
    "SUPREME_QC",
    "PUBLICATION_GATE",
)

@dataclass(frozen=True)
class StageResult:
    stage: str
    ok: bool
    score: float
    reason: str

    def normalized(self) -> dict[str, Any]:
        return asdict(self)

def stable_fingerprint(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def normalize_text(value: str) -> str:
    tokens = TOKEN_RE.findall(value or "")
    return " ".join(token.casefold() for token in tokens)

def lexical_similarity(a: str, b: str) -> float:
    left = set(TOKEN_RE.findall(normalize_text(a)))
    right = set(TOKEN_RE.findall(normalize_text(b)))
    if not left and not right:
        return 1.0
    return len(left & right) / max(1, len(left | right))

def _bounded(value: Any, default: float = 0.0) -> float:
    try:
        return min(1.0, max(0.0, float(value)))
    except (TypeError, ValueError):
        return default

def evaluate_record(record: Mapping[str, Any]) -> list[StageResult]:
    text = str(record.get("text", "")).strip()
    source = record.get("source") or record.get("source_url")
    verification = str(
        record.get("verification_status")
        or (record.get("provenance") or {}).get("verification", "UNKNOWN")
    ).upper()
    confidence = _bounded(record.get("confidence"), 0.0)
    evidence = record.get("evidence") or record.get("evidence_refs") or (
        (record.get("provenance") or {}).get("evidence_refs")
    )
    contradiction = bool(
        record.get("contradiction")
        or record.get("contradicted")
        or record.get("counter_evidence")
        or record.get("conflict")
    )

    results: list[StageResult] = []
    results.append(StageResult("AGENT_INGEST", bool(record.get("artifact_id")) and bool(text), 1.0 if text else 0.0,
                               "artifact_id and non-empty text required"))
    normalized = normalize_text(text)
    results.append(StageResult("NLP_NORMALIZE", bool(normalized), 1.0 if normalized else 0.0,
                               "deterministic Unicode token normalization"))
    ml_score = confidence if "confidence" in record else 0.5
    results.append(StageResult("ML_SCORE", 0.0 <= ml_score <= 1.0, _bounded(ml_score),
                               "confidence must be bounded to [0,1]"))
    evidence_ok = bool(source) or bool(evidence)
    results.append(StageResult("EVIDENCE_FUSION", evidence_ok, 1.0 if evidence_ok else 0.0,
                               "at least one usable evidence/source reference"))
    results.append(StageResult("CONTRADICTION_CHECK", not contradiction, 0.0 if contradiction else 1.0,
                               "explicit contradiction/counter-evidence must be resolved"))
    verified = verification == "VERIFIED"
    results.append(StageResult("INDEPENDENT_VERIFY", verified, 1.0 if verified else 0.0,
                               "independent verification is mandatory for publication"))
    prior = record.get("prior_text")
    drift_ok = True if not prior else lexical_similarity(text, str(prior)) < 0.995
    results.append(StageResult("SUPREME_QC", drift_ok, 1.0 if drift_ok else 0.0,
                               "near-identical regeneration is flagged for review"))
    publication_ok = all(r.ok for r in results)
    results.append(StageResult("PUBLICATION_GATE", publication_ok, 1.0 if publication_ok else 0.0,
                               "publish only when every prerequisite stage passes"))
    return results

def evaluate_batch(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    fingerprints = [stable_fingerprint(r) for r in records]
    duplicate_count = len(fingerprints) - len(set(fingerprints))
    per_record = [evaluate_record(r) for r in records]
    publishable = sum(1 for stages in per_record if stages[-1].ok)
    total = len(records)
    stage_rates = {}
    for stage in STAGES:
        values = [next(x for x in stages if x.stage == stage).ok for stages in per_record]
        stage_rates[stage] = round(sum(values) / max(1, total), 4)
    return {
        "schema_version": "1.0",
        "records": total,
        "duplicate_record_count": duplicate_count,
        "publishable_records": publishable,
        "publishable_rate": round(publishable / max(1, total), 4),
        "stage_pass_rates": stage_rates,
        "fail_closed": publishable < total,
        "truth_claim": False,
    }
