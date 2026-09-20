#!/usr/bin/env python3
"""Deterministic, dependency-free normalization helpers for research records."""

import hashlib
import json
import re
import unicodedata
from pathlib import Path


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("\u200b", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def content_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(record: dict) -> str:
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def normalize_record(record: dict) -> dict:
    result = dict(record)
    for key in ("id", "title", "author", "language", "locator", "definition"):
        if isinstance(result.get(key), str):
            result[key] = normalize_text(result[key])
    return result


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("usage: normalize_records.py RECORD.json")
    path = Path(sys.argv[1])
    record = json.loads(path.read_text(encoding="utf-8"))
    normalized = normalize_record(record)
    normalized["_canonical_sha256"] = content_hash(canonical_json(normalized))
    print(json.dumps(normalized, ensure_ascii=False, indent=2))
