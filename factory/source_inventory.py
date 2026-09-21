#!/usr/bin/env python3
"""Build a stable, additive source inventory from generated source units.

This is an inventory of collected/normalized units, not a claim that the
normalized text is an immutable copy of the user's original source.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
INPUT = GEN / "source-units.jsonl"
MANIFEST = GEN / "manifest.json"
OUTPUT = GEN / "source-inventory.jsonl"
REPORT = GEN / "SOURCE-INVENTORY-QC.json"

TYPE_MAP = {
    "research": "document",
    "philosophy": "document",
    "documentation": "document",
    "workflow": "code",
    "code": "code",
    "media-metadata": "index",
}

def stable_id(repository, branch, path, source_hash):
    key = "|".join([repository or "", branch or "", path or "", source_hash or ""])
    return "src_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:24]

def main():
    if not INPUT.exists() or INPUT.stat().st_size == 0:
        raise SystemExit("generated/source-units.jsonl is missing or empty")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    recorded_at = manifest.get("generated_at") or datetime.now(timezone.utc).isoformat()
    rows = []
    seen = set()

    for line_no, line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        repository = row.get("repository", "UNKNOWN")
        branch = row.get("branch")
        path = row.get("path", "")
        source_hash = row.get("source_hash") or hashlib.sha256((row.get("text") or "").encode("utf-8")).hexdigest()
        source_id = stable_id(repository, branch, path, source_hash)
        content_hash = hashlib.sha256((row.get("text") or "").encode("utf-8")).hexdigest()
        if source_id in seen:
            raise SystemExit(f"duplicate stable source_id at line {line_no}: {source_id}")
        seen.add(source_id)

        source_type = TYPE_MAP.get(row.get("source_type"), "other")
        status = "REVIEW"
        notes = (
            "Inventory record derived from generated source-unit collection; "
            "classification/provenance requires independent review before being "
            "treated as an original source record."
        )
        rows.append({
            "source_id": source_id,
            "source_repository": repository,
            "source_path_or_url": f"{repository}:{path}",
            "source_type": source_type,
            "source_status": status,
            "title_or_label": path,
            "content_hash": content_hash,
            "recorded_at": recorded_at,
            "version": branch or "UNKNOWN",
            "attribution": "UNKNOWN",
            "parent_source_id": None,
            "notes": notes,
            "branch": branch,
            "source_unit_id": row.get("id"),
            "source_hash": source_hash,
        })

    rows.sort(key=lambda x: x["source_id"])
    OUTPUT.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows),
        encoding="utf-8",
    )
    report = {
        "version": 1,
        "record_count": len(rows),
        "unique_source_ids": len(seen),
        "source_status_counts": {
            status: sum(1 for x in rows if x["source_status"] == status)
            for status in ["ORIGINAL","DERIVED","INDEX","INTERPRETATION","ARCHIVED","REVIEW"]
        },
        "generated_output_is_not_source": True,
        "publication_gate": "PASS" if rows else "BLOCK",
        "independent_verification": "NOT_VERIFIED",
        "notes": "Inventory structure is validated; it does not establish truth or original-source status.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not rows:
        raise SystemExit("No inventory records generated")

if __name__ == "__main__":
    main()
