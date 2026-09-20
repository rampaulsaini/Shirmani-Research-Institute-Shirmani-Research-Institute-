#!/usr/bin/env python3
"""Validate exact protected user-source JSONL records."""
import hashlib
import json
import sys
from pathlib import Path

FIELDS = {"source_id", "exact_text", "language", "captured_at", "content_hash", "provenance"}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_protected_sources.py <jsonl>")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit("Missing protected source file: " + str(path))
    seen = set()
    errors = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc}")
            continue
        missing = FIELDS - row.keys()
        if missing:
            errors.append(f"{path}:{line_no}: missing fields: {sorted(missing)}")
            continue
        source_id = row["source_id"]
        if source_id in seen:
            errors.append(f"{path}:{line_no}: duplicate source_id: {source_id}")
        seen.add(source_id)
        if not isinstance(row["exact_text"], str):
            errors.append(f"{path}:{line_no}: exact_text must be a string")
            continue
        actual = hashlib.sha256(row["exact_text"].encode("utf-8")).hexdigest()
        if row["content_hash"] != actual:
            errors.append(f"{path}:{line_no}: content_hash mismatch for {source_id}")
        provenance = row["provenance"]
        if not isinstance(provenance, dict) or not provenance.get("source_kind") or not provenance.get("locator"):
            errors.append(f"{path}:{line_no}: provenance requires source_kind and locator")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Protected source validation OK: {len(seen)} record(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
