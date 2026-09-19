"""Run an optional, small NVIDIA enrichment batch.

This script is deliberately additive: it never replaces the deterministic factory
and never treats model output as independently verified truth.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from agents.nvidia_agent import enabled, enrich_record

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
INPUT = OUT / "source-units.jsonl"
TARGET = OUT / "nvidia-enrichment.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=25)
    args = parser.parse_args()

    if not enabled():
        print("NVIDIA integration disabled: NVIDIA_API_KEY is not configured.")
        return

    existing = set()
    if TARGET.exists():
        for line in TARGET.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.add(json.loads(line)["id"])

    rows = [
        json.loads(line) for line in INPUT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    pending = [r for r in rows if r["id"] not in existing][:args.batch_size]
    with TARGET.open("a", encoding="utf-8") as f:
        for row in pending:
            result = enrich_record(row["text"], row.get("source", "unknown"))
            result.update({
                "id": row["id"],
                "source": row.get("source", "unknown"),
                "source_hash": row.get("hash"),
                "status": "model-generated-draft",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "verification": "unverified",
                "provenance_note": "NVIDIA model output is a draft and is not independent proof.",
            })
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
    print(json.dumps({
        "enabled": True,
        "processed": len(pending),
        "target": str(TARGET),
        "model": result["model"] if pending else None,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
