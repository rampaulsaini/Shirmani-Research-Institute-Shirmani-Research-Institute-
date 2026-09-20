#!/usr/bin/env python3
"""Build a deterministic source-integrity manifest from generated source records.

This manifest proves what was collected and hashed; it does not prove the
truth of the collected content.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    manifest_path = GENERATED / "manifest.json"
    units_path = GENERATED / "source-units.jsonl"
    if not manifest_path.exists() or not units_path.exists():
        raise SystemExit("Required generated source records are missing")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_repo = {}
    unit_count = 0

    for line in units_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        unit_count += 1
        repo = row.get("repository", "UNKNOWN")
        key = (repo, row.get("branch"))
        bucket = by_repo.setdefault(key, {"repository": repo, "branch": row.get("branch"), "records": []})
        bucket["records"].append({
            "id": row.get("id"),
            "path": row.get("path"),
            "source_hash": row.get("source_hash"),
            "content_hash": sha256_bytes((row.get("text") or "").encode("utf-8")),
            "source_type": row.get("source_type"),
        })

    repositories = []
    for source in manifest.get("sources", []):
        repo = source.get("repository")
        item = {
            "repository": repo,
            "available": bool(source.get("available")),
            "default_branch": source.get("default_branch"),
            "head_sha": source.get("head_sha"),
            "remote_ok": source.get("remote_ok"),
            "skipped": source.get("skipped"),
        }
        item["unit_record_count"] = sum(
            len(v["records"]) for v in by_repo.values()
            if v["repository"] == repo
        )
        repositories.append(item)

    # Stable ordering makes the artifact reproducible for identical inputs.
    for bucket in by_repo.values():
        bucket["records"].sort(key=lambda x: (x["path"] or "", x["id"] or 0))

    payload = {
        "manifest_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_manifest_generated_at": manifest.get("generated_at"),
        "unit_count": unit_count,
        "repositories": sorted(repositories, key=lambda x: x["repository"] or ""),
        "records": sorted(
            by_repo.values(),
            key=lambda x: (x["repository"] or "", x["branch"] or "")
        ),
        "integrity_contract": {
            "hash_scope": "normalized generated source-unit text",
            "source_hash_meaning": "hash recorded by the source-unit collector",
            "content_hash_meaning": "SHA-256 of the normalized source-unit text",
            "truth_claim": False,
            "missing_values": "preserved explicitly; never fabricated",
        },
    }

    body = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    digest = sha256_bytes(body.encode("utf-8"))
    output = {
        **payload,
        "manifest_sha256": digest,
    }
    (GENERATED / "source-integrity-manifest.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
