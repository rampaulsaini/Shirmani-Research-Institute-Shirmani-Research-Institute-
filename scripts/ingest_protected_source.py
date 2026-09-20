#!/usr/bin/env python3
"""Create immutable protected-source records from supplied exact text.

This utility never normalizes or rewrites the supplied text. The caller is
responsible for providing the actual source text and traceable locator.
"""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

def make_record(source_id, exact_text, language, source_kind, locator, parent_context=None):
    return {
        "source_id": source_id,
        "exact_text": exact_text,
        "language": language,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "parent_context": parent_context,
        "content_hash": hashlib.sha256(exact_text.encode("utf-8")).hexdigest(),
        "provenance": {
            "source_kind": source_kind,
            "locator": locator,
            "repository": None,
            "path": None,
            "commit": None
        },
        "derivative_links": [],
        "preservation_status": "HASHED"
    }

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: ingest_protected_source.py <source.json> <output.jsonl>")
    source = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    required = ["source_id", "exact_text", "language", "source_kind", "locator"]
    missing = [x for x in required if x not in source]
    if missing:
        raise SystemExit("Missing fields: " + ", ".join(missing))
    record = make_record(
        source["source_id"], source["exact_text"], source["language"],
        source["source_kind"], source["locator"], source.get("parent_context")
    )
    with Path(sys.argv[2]).open("a", encoding="utf-8") as out:
        out.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(record["source_id"], record["content_hash"])

if __name__ == "__main__":
    main()
