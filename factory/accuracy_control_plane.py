#!/usr/bin/env python3
"""Deterministic accuracy-control plane for research/agent outputs.

This is a quality-control layer, not a truth oracle. It measures traceability,
independent-evidence readiness, contradiction coverage, reproducibility metadata,
and record consistency. It never upgrades a record to VERIFIED.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def score_claim(row: dict[str, Any]) -> tuple[int, list[str]]:
    """Return a conservative readiness score in [0,100], never a truth score."""
    score = 0
    failures: list[str] = []

    claim = str(row.get("claim", "")).strip()
    evidence = row.get("evidence") or []
    verification = row.get("verification") or {}
    provenance = row.get("provenance") or {}
    countercases = row.get("countercases") or []
    formulation = row.get("formulation") or []

    if claim:
        score += 10
    else:
        failures.append("missing_claim")

    if evidence:
        score += 20
    else:
        failures.append("missing_evidence")

    expected_hash = sha256_text(claim)
    if provenance.get("content_hash") == expected_hash:
        score += 15
    else:
        failures.append("missing_or_mismatched_content_hash")

    if provenance.get("repository") and provenance.get("path") is not None:
        score += 10
    else:
        failures.append("incomplete_provenance_locator")

    if formulation and all(x.get("reproducible") is True for x in formulation if isinstance(x, dict)):
        score += 10
    else:
        failures.append("reproducibility_metadata_incomplete")

    if countercases:
        score += 10
    else:
        failures.append("counterevidence_not_recorded")

    independent = str(verification.get("status", "")).upper() in {
        "VERIFIED", "INDEPENDENTLY_VERIFIED"
    }
    if independent:
        score += 25
    else:
        failures.append("independent_verification_missing")

    return min(score, 100), failures


def main() -> int:
    path = GENERATED / "agent-run" / "contracts" / "claim-records.jsonl"
    rows = load_jsonl(path)

    scores = []
    failures = Counter()
    verified = 0
    for row in rows:
        score, row_failures = score_claim(row)
        scores.append(score)
        failures.update(row_failures)
        if str(row.get("status", "")).upper() == "VERIFIED":
            verified += 1

    count = len(scores)
    histogram = Counter(scores)
    mean = round(sum(scores) / count, 2) if count else 0.0

    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "control_plane": "deterministic-accuracy-control",
        "interpretation": "readiness/traceability score, not truth probability or scientific accuracy",
        "records": count,
        "verified_records_observed": verified,
        "verified_records_promoted": 0,
        "mean_readiness_score": mean,
        "score_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "failure_counts": dict(sorted(failures.items())),
        "fail_closed": True,
        "publication_gate": "PASS" if (
            "missing_claim" not in failures
            and "missing_or_invalid_content_hash" not in failures
        ) else "BLOCK",
    }

    out = GENERATED / "ACCURACY-CONTROL.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["publication_gate"] == "BLOCK":
        raise SystemExit("ACCURACY-CONTROL: BLOCK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
