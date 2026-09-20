#!/usr/bin/env python3
"""Deterministic local content discovery with hashes and explicit availability.

This stage inventories files from a checked-out repository. It does not claim
that registered external repositories have been ingested, and it does not
generate claims from content.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED_DIRS = {".git", ".github_cache", "__pycache__", "node_modules", ".venv", "venv"}
EXCLUDED_ROOTS = {"generated", "dist", "build", ".pytest_cache"}
TEXT_EXTENSIONS = {
    ".md", ".txt", ".rst", ".py", ".js", ".ts", ".tsx", ".jsx", ".html", ".css",
    ".json", ".jsonl", ".yaml", ".yml", ".toml", ".ini", ".csv", ".xml",
    ".svg", ".sql", ".sh", ".bat"
}

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def language_hint(path):
    ext = path.suffix.lower()
    return {
        ".py":"python", ".js":"javascript", ".ts":"typescript", ".tsx":"typescript",
        ".jsx":"javascript", ".html":"html", ".css":"css", ".json":"json",
        ".jsonl":"jsonl", ".yaml":"yaml", ".yml":"yaml", ".md":"markdown",
        ".txt":"text", ".rst":"restructuredtext", ".csv":"csv", ".xml":"xml",
        ".sql":"sql", ".sh":"shell"
    }.get(ext)

def discover(root):
    root = Path(root)
    records = []
    for path in sorted(root.rglob("*"), key=lambda p: p.as_posix()):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        parts = rel.parts
        if any(part in EXCLUDED_DIRS for part in parts):
            continue
        if parts and parts[0] in EXCLUDED_ROOTS:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            records.append({
                "id": f"content:{rel.as_posix()}",
                "source_path": rel.as_posix(),
                "content_hash": "0" * 64,
                "bytes": 0,
                "language_hint": language_hint(path),
                "content_status": "UNAVAILABLE",
                "provenance": {"recorded_at": datetime.now(timezone.utc).isoformat(),
                               "repository": None, "commit": None}
            })
            continue
        status = "AVAILABLE" if path.suffix.lower() in TEXT_EXTENSIONS else "BINARY_SKIPPED"
        records.append({
            "id": f"content:{rel.as_posix()}",
            "source_path": rel.as_posix(),
            "content_hash": sha256(data),
            "bytes": len(data),
            "language_hint": language_hint(path),
            "content_status": status,
            "provenance": {"recorded_at": datetime.now(timezone.utc).isoformat(),
                           "repository": None, "commit": None}
        })
    return records

def main():
    p = argparse.ArgumentParser()
    p.add_argument("root")
    p.add_argument("output")
    args = p.parse_args()
    rows = discover(args.root)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows),
                   encoding="utf-8")
    print(f"CONTENT_RECORDS: {len(rows)}")
    print(f"TEXT_RECORDS: {sum(x['content_status']=='AVAILABLE' for x in rows)}")
    print(f"BINARY_SKIPPED: {sum(x['content_status']=='BINARY_SKIPPED' for x in rows)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
