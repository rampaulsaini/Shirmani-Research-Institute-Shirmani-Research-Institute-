"""Supreme Accuracy V3 gate: deterministic, fail-closed, evidence-aware quality control.

This is a control/verification layer. It does not claim perfect or absolute
accuracy. Publication requires independent evidence; execution may continue
while publication remains HOLD.
"""
from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
CORPUS = OUT / "verse-corpus.jsonl"
WORKER = OUT / "worker-status.json"
REPORT = OUT / "supreme-accuracy-v3-report.json"
SCHEMA_VERSION = "3.0"


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def _rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    result = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSONL at {path}:{line_no}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"record is not an object at {path}:{line_no}")
            result.append(row)
    return result


def _verification_summary() -> dict[str, Any]:
    candidates = sorted(OUT.glob("independent-verification-status-*.json"))
    if not candidates:
        return {
            "status_file": None,
            "records": 0,
            "independently_verified_records": 0,
            "independent_verified_percent": 0.0,
            "evidence_present": False,
        }
    path = candidates[-1]
    data = json.loads(path.read_text(encoding="utf-8"))
    summary = data.get("verification_summary", {})
    records = data.get("records", [])
    verified = int(summary.get("independently_verified_records") or 0)
    return {
        "status_file": path.name,
        "records": len(records),
        "independently_verified_records": verified,
        "independent_verified_percent": float(
            summary.get("independent_verified_percent") or 0.0
        ),
        "evidence_present": True,
    }


def audit(rows: list[dict[str, Any]], worker: dict[str, Any],
          verification: dict[str, Any]) -> dict[str, Any]:
    ids = [str(r.get("id")) for r in rows]
    duplicate_ids = len(ids) - len(set(ids))
    missing_text = sum(not str(r.get("text", "")).strip() for r in rows)
    bad_hashes = sum(
        r.get("content_hash") != _sha(str(r.get("text", ""))) for r in rows
    )
    missing_provenance = sum(
        not r.get("source_ids") or not r.get("method_trace") for r in rows
    )
    unsafe_verified = sum(r.get("evidence_status") == "VERIFIED" for r in rows)
    missing_claim_class = sum(not r.get("claim_class") for r in rows)

    texts = [str(r.get("text", "")).strip() for r in rows if str(r.get("text", "")).strip()]
    exact_duplicates = sum(n - 1 for n in Counter(texts).values() if n > 1)

    contradiction_flags = sum(
        bool(r.get("contradiction_detected"))
        or str(r.get("contradiction_status", "")).upper() in {"CONTRADICTED", "CONFLICT"}
        for r in rows
    )

    source_sets = [set(map(str, r.get("source_ids", []))) for r in rows]
    source_coverage = (
        sum(bool(s) for s in source_sets) / len(rows) if rows else 0.0
    )
    provenance_coverage = (
        sum(
            bool(r.get("source_ids"))
            and bool(r.get("method_trace"))
            and bool(r.get("content_hash"))
            for r in rows
        ) / len(rows)
        if rows else 0.0
    )

    integrity_agent = 1.0 if (
        duplicate_ids == 0 and bad_hashes == 0 and missing_text == 0
    ) else 0.0
    provenance_agent = provenance_coverage
    nlp_agent = max(0.0, 1.0 - exact_duplicates / max(1, len(rows)))
    contradiction_agent = 1.0 if contradiction_flags == 0 else 0.0
    verification_agent = (
        1.0 if verification["independently_verified_records"] > 0 else 0.0
    )
    worker_agent = 1.0 if bool(worker.get("generated_at")) else 0.0

    agents = {
        "integrity": integrity_agent,
        "provenance": round(provenance_agent, 6),
        "nlp_duplicate_screen": round(nlp_agent, 6),
        "contradiction": contradiction_agent,
        "independent_verification": verification_agent,
        "worker_observability": worker_agent,
    }
    finite_scores = all(_finite(v) and 0.0 <= float(v) <= 1.0 for v in agents.values())
    ensemble_score = round(sum(agents.values()) / len(agents), 6)

    hard_integrity_pass = (
        duplicate_ids == 0
        and bad_hashes == 0
        and missing_text == 0
        and unsafe_verified == 0
        and contradiction_flags == 0
        and finite_scores
    )
    execution_ready = hard_integrity_pass and worker_agent == 1.0
    publication_ready = execution_ready and verification_agent == 1.0

    return {
        "schema_version": SCHEMA_VERSION,
        "claim_policy": "Scores are quality-control signals, not accuracy probabilities.",
        "records_evaluated": len(rows),
        "metrics": {
            "duplicate_ids": duplicate_ids,
            "missing_text": missing_text,
            "bad_hashes": bad_hashes,
            "missing_provenance": missing_provenance,
            "missing_claim_class": missing_claim_class,
            "unsafe_verified_claims": unsafe_verified,
            "exact_duplicate_records": exact_duplicates,
            "contradiction_flags": contradiction_flags,
            "source_coverage": round(source_coverage, 6),
            "provenance_coverage": round(provenance_coverage, 6),
        },
        "agents": agents,
        "ensemble_score": ensemble_score,
        "finite_scores": finite_scores,
        "execution_gate": "PASS" if execution_ready else "HOLD",
        "publication_gate": "PASS" if publication_ready else "HOLD",
        "accuracy_measurement": "NOT_MEASURED",
        "next_action": "CONTINUE_AUTOMISSION" if execution_ready else "STOP_AND_REPAIR",
    }


def main() -> int:
    rows = _rows(CORPUS)
    worker = json.loads(WORKER.read_text(encoding="utf-8")) if WORKER.exists() else {}
    verification = _verification_summary()
    result = audit(rows, worker, verification)
    report = {
        "schema_version": SCHEMA_VERSION,
        "mode": "supreme-accuracy-v3-fail-closed",
        "report_digest": _sha(_canonical(result)),
        "verification": verification,
        "audit": result,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if result["execution_gate"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
