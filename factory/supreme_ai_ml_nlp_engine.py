"""Dependency-free AI/ML/NLP quality ensemble for SHIRMANI Automission.

This is a deterministic quality/evaluation layer, not a claim of perfect
accuracy. It combines independent heuristic agents so weak evidence cannot be
silently promoted to a VERIFIED result.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from statistics import median
from typing import Any

TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)


def tokens(text: str) -> list[str]:
    return [x.casefold() for x in TOKEN_RE.findall(str(text or ""))]


def lexical_profile(text: str) -> dict[str, float]:
    ts = tokens(text)
    n = len(ts)
    unique = len(set(ts))
    if not n:
        return {"tokens": 0.0, "unique": 0.0, "diversity": 0.0, "entropy": 0.0}
    counts = Counter(ts)
    entropy = -sum((c / n) * math.log2(c / n) for c in counts.values())
    return {
        "tokens": float(n),
        "unique": float(unique),
        "diversity": unique / n,
        "entropy": entropy,
    }


def jaccard(a: str, b: str) -> float:
    aa, bb = set(tokens(a)), set(tokens(b))
    if not aa and not bb:
        return 1.0
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def robust_anomaly_scores(values: list[float]) -> list[float]:
    if len(values) < 4:
        return [0.0] * len(values)
    m = median(values)
    deviations = [abs(v - m) for v in values]
    mad = median(deviations)
    if mad == 0:
        return [1.0 if v != m else 0.0 for v in values]
    return [min(1.0, abs(v - m) / (3.0 * mad)) for v in values]


def evidence_score(row: dict[str, Any]) -> float:
    checks = [
        bool(row.get("source_ids")),
        bool(row.get("method_trace")),
        bool(row.get("content_hash")),
        bool(row.get("text")),
    ]
    return sum(checks) / len(checks)


def evaluate(rows: list[dict[str, Any]], verification: dict[str, Any],
             worker: dict[str, Any]) -> dict[str, Any]:
    profiles = [lexical_profile(r.get("text", "")) for r in rows]
    lengths = [p["tokens"] for p in profiles]
    anomalies = robust_anomaly_scores(lengths)

    exact_texts = Counter(str(r.get("text", "")).strip() for r in rows if r.get("text"))
    exact_duplicate_records = sum(max(0, n - 1) for n in exact_texts.values())

    pair_high_similarity = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if jaccard(rows[i].get("text", ""), rows[j].get("text", "")) >= 0.98:
                pair_high_similarity += 1

    evidence = [evidence_score(r) for r in rows]
    nlp_agent = 1.0
    if rows:
        nlp_agent = max(
            0.0,
            1.0
            - (exact_duplicate_records / len(rows))
            - (pair_high_similarity / max(1, len(rows) * (len(rows) - 1) / 2)) * 0.5,
        )

    ml_agent = 1.0 - (sum(a > 0.0 for a in anomalies) / max(1, len(anomalies)))
    evidence_agent = sum(evidence) / max(1, len(evidence))
    verification_agent = 1.0 if verification.get("fail_closed") is True else 0.0
    worker_agent = 1.0 if worker.get("worker_observable") is True else 0.0

    agents = {
        "integrity_agent": {
            "score": 1.0 if all(e == 1.0 for e in evidence) else evidence_agent,
            "basis": "provenance/hash/text presence",
        },
        "nlp_consistency_agent": {
            "score": round(nlp_agent, 6),
            "basis": "token diversity and near-duplicate detection",
        },
        "ml_anomaly_agent": {
            "score": round(ml_agent, 6),
            "basis": "robust median/MAD length anomaly screening",
        },
        "evidence_agent": {
            "score": round(evidence_agent, 6),
            "basis": "source, method trace, hash and text completeness",
        },
        "verification_agent": {
            "score": verification_agent,
            "basis": "independent verification remains fail-closed",
        },
        "worker_agent": {
            "score": worker_agent,
            "basis": "worker state is observable",
        },
    }

    scores = [v["score"] for v in agents.values()]
    consensus = min(scores) >= 0.90 and verification_agent == 1.0
    return {
        "schema_version": "1.0",
        "method": "deterministic-multi-agent-consensus",
        "claim_policy": "Heuristic quality scores are not accuracy probabilities.",
        "records_evaluated": len(rows),
        "exact_duplicate_records": exact_duplicate_records,
        "near_duplicate_pairs": pair_high_similarity,
        "agents": agents,
        "ensemble_score": round(sum(scores) / len(scores), 6),
        "consensus_pass": consensus,
        "next_action": "CONTINUE_AUTOMISSION" if consensus else "STOP_AND_REPAIR",
    }
