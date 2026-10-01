"""Fail-closed Supreme Quality Controller for the SHIRMANI Automission plane."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from factory.supreme_ai_ml_nlp_engine import SCHEMA_VERSION, evaluate

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REPORT = OUT / "supreme-quality-report.json"


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def jsonl(path: Path):
    if not path.exists():
        raise FileNotFoundError(path)
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at {path}:{line_no}") from exc
    return rows


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_corpus():
    path = OUT / "verse-corpus.jsonl"
    rows = jsonl(path)
    ids = [str(r.get("id")) for r in rows]
    return rows, {
        "source_file": path.name,
        "records": len(rows),
        "duplicate_ids": len(ids) - len(set(ids)),
        "bad_content_hashes": sum(
            1 for r in rows
            if r.get("content_hash") != sha(str(r.get("text", "")))
        ),
        "missing_provenance": sum(
            1 for r in rows if not r.get("source_ids") or not r.get("method_trace")
        ),
        "unsafe_verified_claims": sum(
            1 for r in rows if r.get("evidence_status") == "VERIFIED"
        ),
        "nonempty": bool(rows),
    }


def check_verification():
    candidates = sorted(OUT.glob("independent-verification-status-*.json"))
    if not candidates:
        return {
            "source_file": None,
            "queue_records": 0,
            "independently_verified_records": None,
            "independent_verified_percent": None,
            "artifact_present": False,
            "fail_closed": True,
        }
    d = read_json(candidates[-1], {})
    if not isinstance(d, dict):
        return {
            "source_file": candidates[-1].name,
            "queue_records": 0,
            "independently_verified_records": None,
            "independent_verified_percent": None,
            "artifact_present": False,
            "fail_closed": True,
        }
    s = d.get("verification_summary", {})
    records = d.get("records", [])
    if not isinstance(records, list):
        records = []
    return {
        "source_file": candidates[-1].name,
        "queue_records": len(records),
        "independently_verified_records": s.get("independently_verified_records"),
        "independent_verified_percent": s.get("independent_verified_percent"),
        "artifact_present": True,
        "fail_closed": all(r.get("status") != "VERIFIED" for r in records),
    }


def check_worker():
    d = read_json(OUT / "worker-status.json", {})
    return {
        "worker_observable": bool(d.get("generated_at")),
        "generated_at": d.get("generated_at"),
        "completed": d.get("completed", {}),
    }


def main():
    hard_failures = []
    try:
        rows, corpus = check_corpus()
    except (FileNotFoundError, ValueError) as exc:
        rows = []
        corpus = {
            "source_file": "verse-corpus.jsonl",
            "records": 0,
            "duplicate_ids": 0,
            "bad_content_hashes": 0,
            "missing_provenance": 0,
            "unsafe_verified_claims": 0,
            "nonempty": False,
            "error": str(exc),
        }
        hard_failures.append(f"corpus.unavailable={exc}")
    verification = check_verification()
    worker = check_worker()

    if not corpus.get("nonempty"):
        hard_failures.append("corpus.nonempty=false")
    for key in (
        "duplicate_ids",
        "bad_content_hashes",
        "missing_provenance",
        "unsafe_verified_claims",
    ):
        if corpus[key] != 0:
            hard_failures.append(f"corpus.{key}={corpus[key]}")
    if not verification["artifact_present"]:
        hard_failures.append("verification.artifact_present=false")
    if verification["fail_closed"] is False:
        hard_failures.append("verification.fail_closed=false")
    if not worker["worker_observable"]:
        hard_failures.append("worker.worker_observable=false")

    ensemble = evaluate(rows, verification, worker)
    if ensemble["consensus_pass"] is False:
        hard_failures.append("ensemble.consensus_pass=false")

    checks = {
        "corpus_integrity": (
            corpus.get("nonempty") is True
            and all(corpus[k] == 0 for k in (
                "duplicate_ids",
                "bad_content_hashes",
                "missing_provenance",
                "unsafe_verified_claims",
            ))
        ),
        "verification_boundary": (
            verification["artifact_present"] and verification["fail_closed"]
        ),
        "worker_observable": worker["worker_observable"],
        "multi_agent_consensus": ensemble["consensus_pass"],
        "schema_integrity": ensemble["schema_version"] == SCHEMA_VERSION,
        "finite_scores": all(
            isinstance(a.get("score"), (int, float))
            and 0.0 <= float(a["score"]) <= 1.0
            for a in ensemble["agents"].values()
        ),
    }
    report = {
        "schema_version": "3.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "fail-closed-deterministic-ai-ml-nlp-quality-control",
        "claim_policy": (
            "Only mechanically checked properties and explicitly labeled "
            "heuristic scores are reported; perfect accuracy is not asserted."
        ),
        "checks": checks,
        "passed_checks": sum(checks.values()),
        "total_checks": len(checks),
        "corpus": corpus,
        "verification": verification,
        "worker": worker,
        "ensemble": ensemble,
        "hard_failures": hard_failures,
        "next_action": (
            "CONTINUE_AUTOMISSION" if not hard_failures else "STOP_AND_REPAIR"
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if hard_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
