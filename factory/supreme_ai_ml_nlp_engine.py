"""Dependency-free, deterministic AI/ML/NLP quality ensemble for SHIRMANI Automission.

This module is an evaluation/quality-control layer, not a claim of perfect
accuracy. It is designed to be reproducible, bounded in runtime, fail-closed,
and explicit about what each signal actually measures.
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from statistics import median
from typing import Any

TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)
SCHEMA_VERSION = "2.0"


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


def _shingles(text: str, width: int = 3) -> set[tuple[str, ...]]:
    ts = tokens(text)
    if len(ts) <= width:
        return {tuple(ts)} if ts else set()
    return {tuple(ts[i:i + width]) for i in range(len(ts) - width + 1)}


def jaccard(a: str, b: str) -> float:
    aa, bb = _shingles(a), _shingles(b)
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


def _near_duplicate_pairs(rows: list[dict[str, Any]], limit: int = 200_000) -> int:
    """Count high-similarity candidate pairs without an unrestricted O(n²) scan."""
    if len(rows) < 2:
        return 0
    buckets: dict[tuple[str, ...], list[int]] = defaultdict(list)
    shingles = [_shingles(r.get("text", "")) for r in rows]
    for i, ss in enumerate(shingles):
        for s in sorted(ss):
            buckets[s].append(i)
    candidates: set[tuple[int, int]] = set()
    for ids in buckets.values():
        if len(ids) > 64:
            ids = ids[:64]
        for p, i in enumerate(ids):
            for j in ids[p + 1:]:
                candidates.add((i, j) if i < j else (j, i))
                if len(candidates) >= limit:
                    return limit
    count = 0
    for i, j in sorted(candidates):
        if jaccard(rows[i].get("text", ""), rows[j].get("text", "")) >= 0.98:
            count += 1
    return count


def _score_stats(scores: list[float]) -> dict[str, float]:
    if not scores:
        return {"mean": 0.0, "min": 0.0, "max": 0.0, "spread": 0.0}
    return {
        "mean": round(sum(scores) / len(scores), 6),
        "min": round(min(scores), 6),
        "max": round(max(scores), 6),
        "spread": round(max(scores) - min(scores), 6),
    }


def evaluate(rows: list[dict[str, Any]], verification: dict[str, Any],
             worker: dict[str, Any]) -> dict[str, Any]:
    profiles = [lexical_profile(r.get("text", "")) for r in rows]
    lengths = [p["tokens"] for p in profiles]
    anomalies = robust_anomaly_scores(lengths)

    exact_texts = Counter(
        str(r.get("text", "")).strip() for r in rows if r.get("text")
    )
    exact_duplicate_records = sum(max(0, n - 1) for n in exact_texts.values())
    pair_high_similarity = _near_duplicate_pairs(rows)

    evidence = [evidence_score(r) for r in rows]
    nlp_agent = 1.0
    if rows:
        nlp_agent = max(
            0.0,
            1.0
            - (exact_duplicate_records / len(rows))
            - (pair_high_similarity / max(1, len(rows))) * 0.5,
        )

    anomalous = sum(a > 0.0 for a in anomalies)
    ml_agent = 1.0 - (anomalous / max(1, len(anomalies)))
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
            "basis": "exact duplicates plus bounded token-shingle near-duplicate screening",
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

    scores = [float(v["score"]) for v in agents.values()]
    stats = _score_stats(scores)
    # A single record cannot establish an observable multi-agent consensus.
    # Keep the controller fail-closed until there is a minimally independent sample.
    consensus = (
        len(rows) >= 2
        and len(scores) >= 6
        and stats["min"] >= 0.90
        and stats["spread"] <= 0.10
        and verification_agent == 1.0
        and worker_agent == 1.0
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "method": "deterministic-bounded-multi-agent-consensus",
        "claim_policy": "Heuristic quality scores are not accuracy probabilities.",
        "records_evaluated": len(rows),
        "exact_duplicate_records": exact_duplicate_records,
        "near_duplicate_pairs": pair_high_similarity,
        "agents": agents,
        "score_stats": stats,
        "ensemble_score": stats["mean"],
        "consensus_pass": consensus,
        "next_action": "CONTINUE_AUTOMISSION" if consensus else "STOP_AND_REPAIR",
    }
