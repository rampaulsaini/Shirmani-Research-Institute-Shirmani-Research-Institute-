#!/usr/bin/env python3
"""Build a fail-closed provenance ledger from the reasoning manifest."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main() -> None:
    reasoning = OUT / "reasoning-manifest.jsonl"
    target = OUT / "provenance-ledger.jsonl"
    if not reasoning.exists():
        target.write_text("", encoding="utf-8")
        print("No reasoning manifest; wrote empty provenance ledger.")
        return
    rows = []
    for line in reasoning.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        source_ids = [str(x) for x in r.get("source_ids", [])]
        payload = {"artifact_id": str(r.get("artifact_id")), "source_ids": source_ids,
                   "content_sha256": r.get("content_sha256")}
        rows.append({
            "artifact_id": str(r.get("artifact_id")),
            "kind": r.get("kind"),
            "source_ids": source_ids,
            "content_sha256": r.get("content_sha256"),
            "created_at": r.get("created_at") or datetime.now(timezone.utc).isoformat(),
            "generator": "factory/provenance_ledger.py",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "ledger_hash": sha(json.dumps(payload, sort_keys=True, ensure_ascii=False)),
        })
    tmp = target.with_suffix(".jsonl.tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    tmp.replace(target)
    print(json.dumps({"path": "generated/provenance-ledger.jsonl", "records": len(rows)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
