#!/usr/bin/env python3
"""High-assurance deterministic quality gate for Automission outputs.

The gate never declares a claim true. It only checks whether generated records
meet strict traceability, structure, evidence, consistency, and queue contracts.
Unsupported or ambiguous records remain quarantined for review.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
MAX_SAMPLE = 50000


def read_jsonl(path: Path):
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rows.append((line_no, json.loads(line)))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSONL: {exc}") from exc
    return rows


def check_claim_records(errors, warnings, metrics):
    path = GENERATED / "agent-run" / "contracts" / "claim-records.jsonl"
    rows = read_jsonl(path)
    metrics["claim_records"] = len(rows)
    seen = set()

    for line_no, row in rows[:MAX_SAMPLE]:
        rid = str(row.get("id", ""))
        if not rid:
            errors.append(f"claim-record:{line_no}:missing-id")
            continue
        if rid in seen:
            errors.append(f"claim-record:{line_no}:duplicate-id:{rid}")
        seen.add(rid)

        if not str(row.get("claim", "")).strip():
            errors.append(f"claim-record:{line_no}:empty-claim:{rid}")

        status = row.get("status")
        evidence = row.get("evidence") or []
        verification = row.get("verification") or {}

        if status in {"SUPPORTED", "REFUTED"} and not evidence:
            errors.append(f"claim-record:{line_no}:status-without-evidence:{rid}")

        if verification.get("status") == "INDEPENDENTLY_CHECKED":
            if not evidence:
                errors.append(f"claim-record:{line_no}:independent-check-without-evidence:{rid}")
            if not verification.get("method"):
                errors.append(f"claim-record:{line_no}:independent-check-without-method:{rid}")

        if status == "NOT_VERIFIED":
            metrics["not_verified"] += 1

    if len(rows) > MAX_SAMPLE:
        warnings.append(f"claim-records-sampled:{MAX_SAMPLE}/{len(rows)}")


def check_artifact_manifest(errors, warnings, metrics):
    path = GENERATED / "agent-run" / "artifact-manifest.jsonl"
    rows = read_jsonl(path)
    metrics["artifact_records"] = len(rows)
    ids, hashes = set(), Counter()

    for line_no, row in rows[:MAX_SAMPLE]:
        aid = row.get("artifact_id")
        if not aid:
            errors.append(f"artifact:{line_no}:missing-artifact-id")
        elif aid in ids:
            errors.append(f"artifact:{line_no}:duplicate-artifact-id:{aid}")
        else:
            ids.add(aid)

        content_hash = row.get("sha256")
        if not content_hash:
            errors.append(f"artifact:{line_no}:missing-sha256")
        else:
            hashes[content_hash] += 1

        for key in ("kind", "language", "status", "provenance", "created_at"):
            if not row.get(key):
                errors.append(f"artifact:{line_no}:missing-{key}")

        if row.get("status") == "verified":
            warnings.append(f"artifact:{line_no}:verified-status-requires-independent-evidence-review")

    metrics["duplicate_content_hashes"] = sum(1 for n in hashes.values() if n > 1)


def check_language_queues(errors, warnings, metrics):
    queue_dir = GENERATED / "agent-run" / "queues"
    counts = Counter()
    if not queue_dir.exists():
        warnings.append("language-queues-missing")
        return

    for path in queue_dir.glob("*.jsonl"):
        for line_no, row in read_jsonl(path):
            counts[path.name] += 1
            if row.get("status") not in {"pending", "running", "completed", "quarantined"}:
                errors.append(f"queue:{path.name}:{line_no}:invalid-status")
            if not row.get("agent"):
                errors.append(f"queue:{path.name}:{line_no}:missing-agent")

    metrics["queue_records"] = sum(counts.values())
    metrics["language_queues"] = dict(counts)


def main():
    errors, warnings = [], []
    metrics = {
        "not_verified": 0,
        "claim_records": 0,
        "artifact_records": 0,
        "queue_records": 0,
        "duplicate_content_hashes": 0,
    }

    check_claim_records(errors, warnings, metrics)
    check_artifact_manifest(errors, warnings, metrics)
    check_language_queues(errors, warnings, metrics)

    result = {
        "gate": "SUPREME_AUTOMISSION_QUALITY_GATE",
        "status": "PASS" if not errors else "QUARANTINE",
        "absolute_truth_claim": False,
        "policy": "high_assurance_traceability_and_verification_gate",
        "errors": errors[:200],
        "warnings": warnings[:200],
        "metrics": metrics,
    }

    out = GENERATED / "supreme-quality-gate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
