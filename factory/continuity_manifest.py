#!/usr/bin/env python3
"""Build a durable, deterministic execution manifest for factory continuity."""

from __future__ import annotations
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
TRACKED = [
    "repository-intelligence.json", "manifest.json", "source-units.jsonl",
    "canonical-knowledge.jsonl", "canonical-knowledge-manifest.json",
    "canonical-index.json", "verse-corpus.jsonl", "reasoning-manifest.jsonl",
    "claim-evidence.jsonl", "provenance-ledger.jsonl", "independent-verification-queue.jsonl",
    "VERIFICATION-QUEUE.json", "VERIFICATION-QUEUE-QC.json", "independent-verification-registry.jsonl", "VERIFICATION-REGISTRY.json", "VERIFICATION-REGISTRY-QC.json", "VERIFICATION-PROMOTION-QC.json", "PUBLICATION-GATE.json", "QC-REPORT.json", "worker-status.json",
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    qc_path = OUT / "QC-REPORT.json"
    qc = json.loads(qc_path.read_text(encoding="utf-8")) if qc_path.exists() else {}
    artifacts = {}
    for name in TRACKED:
        path = OUT / name
        if path.exists():
            artifacts[name] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
    manifest = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git": {
            "sha": os.getenv("GITHUB_SHA"), "ref": os.getenv("GITHUB_REF"),
            "workflow": os.getenv("GITHUB_WORKFLOW"), "run_id": os.getenv("GITHUB_RUN_ID"),
            "run_number": os.getenv("GITHUB_RUN_NUMBER"), "event": os.getenv("GITHUB_EVENT_NAME"),
        },
        "continuity": {
            "policy": "resume from durable generated outputs; preserve canonical/source records",
            "last_good_workflow_run": os.getenv("GITHUB_RUN_ID"),
            "qc_publication_gate": qc.get("publication_gate"),
            "qc_error_count": qc.get("error_count"),
        },
        "artifacts": artifacts,
    }
    (OUT / "continuity-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"path": "generated/continuity-manifest.json",
                      "artifact_count": len(artifacts),
                      "publication_gate": qc.get("publication_gate"),
                      "error_count": qc.get("error_count")}, ensure_ascii=False))

if __name__ == "__main__":
    main()
