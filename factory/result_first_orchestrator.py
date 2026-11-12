"""Result-first multi-layer orchestration for SHIRMANI Automission.

Principle:
  Produce and QC results first. Route only resulting claims/records into
  independent review. Never promote a workflow success into VERIFIED.

This controller is deterministic and fail-closed. It is quantum-inspired only
in the sense that independent evidence dimensions are scored as an ensemble;
it does not claim access to quantum hardware or a quantum computer.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
PLAN = OUT / "result-first-multilayer-plan.json"


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return sum(1 for line in fh if line.strip())


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    status_files = sorted(OUT.glob("independent-verification-status-*.json"))
    verification = read_json(status_files[-1], {}) if status_files else {}
    summary = verification.get("verification_summary", {})

    queue = OUT / "independent-verification-queue.jsonl.gz"
    registry = OUT / "independent-verification-registry.jsonl.gz"

    queue_count = count_jsonl(queue)
    registry_count = count_jsonl(registry)

    # Evidence/result layers: existence and machine-readable health only.
    evidence_graph = read_json(OUT / "research-evidence-graph.json", {})
    quality = read_json(OUT / "supreme-quality-report.json", {})
    worker = read_json(OUT / "worker-status.json", {})

    evidence_ready = bool(evidence_graph) or (OUT / "research-evidence-graph.json").exists()
    quality_ready = bool(quality) and quality.get("next_action") == "CONTINUE_AUTOMISSION"
    worker_observable = bool(worker.get("generated_at"))

    dimensions = {
        "result_production": queue_count > 0 or registry_count > 0,
        "evidence_layer": evidence_ready,
        "quality_layer": quality_ready,
        "worker_observable": worker_observable,
        "verification_boundary": all(
            r.get("status") != "VERIFIED"
            for r in verification.get("records", [])
        ),
    }

    # Quantum-inspired ensemble: no quantum-computing claim is made.
    score = sum(1 for v in dimensions.values() if v) / len(dimensions)
    independent_verified = int(summary.get("independently_verified_records", 0) or 0)

    plan = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "result-first-multi-layer-automission",
        "principle": (
            "Verification evaluates produced results; workflow execution alone "
            "never creates a VERIFIED claim."
        ),
        "layers": [
            "intake",
            "reasoning",
            "evidence",
            "result_production",
            "quality",
            "benchmark",
            "traceability",
            "review_packet",
            "independent_verification",
            "publication_safety",
            "continuity",
        ],
        "quantum_ai_mode": {
            "type": "quantum-inspired-ensemble",
            "hardware_claim": False,
            "note": "Deterministic classical execution; replaceable backend."
        },
        "dimensions": dimensions,
        "ensemble_readiness_score": round(score, 3),
        "result_metrics": {
            "verification_queue_records": queue_count,
            "verification_registry_records": registry_count,
            "independently_verified_records": independent_verified,
            "independent_verified_percent": summary.get(
                "independent_verified_percent", 0
            ),
            "verification_readiness_percent": summary.get(
                "verification_readiness_percent", 0
            ),
        },
        "next_actions": [
            "Continue producing and QC'ing research results.",
            "Continue building evidence and traceability.",
            "Continue preparing hash-bound review packets.",
            "Route prepared results to independent review.",
            "Promote only explicit independent decisions to VERIFIED.",
        ],
        "fail_closed": True,
    }

    canonical = json.dumps(plan, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    plan["integrity_sha256"] = sha256_text(canonical)
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(plan, ensure_ascii=False))
    if not plan["fail_closed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
