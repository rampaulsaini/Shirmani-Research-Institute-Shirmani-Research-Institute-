#!/usr/bin/env python3
"""Deterministic QC for canonical source units and generated records.

The QC layer is intentionally provider-free: it validates JSONL structure,
provenance, hashes, duplicate content and publication-gate conditions.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SOURCE = ("id", "repository", "branch", "path", "source_hash", "text", "source_type", "collected_at")
REQUIRED_GENERATED = ("id", "agent", "source_ids", "content_hash", "status", "text")
VALID_STATUS = {"draft", "review", "verified", "published", "rejected"}

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def check_jsonl(path, required, hash_field, unique_hash=True):
    seen = set()
    errors = []
    count = 0
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            count += 1
            try:
                record = json.loads(line)
            except Exception as exc:
                errors.append({"line": line_no, "error": f"invalid_json:{exc}"})
                continue
            for key in required:
                if key not in record:
                    errors.append({"line": line_no, "error": f"missing:{key}"})
            h = record.get(hash_field)
            if unique_hash and h:
                if h in seen:
                    errors.append({"line": line_no, "error": f"duplicate_{hash_field}"})
                seen.add(h)
            if "text" in record and not isinstance(record["text"], str):
                errors.append({"line": line_no, "error": "text_not_string"})
    return {"records": count, "unique_hashes": len(seen), "errors": errors}

def check_source_integrity(path):
    result = check_jsonl(path, REQUIRED_SOURCE, "source_hash")
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                expected = sha(r["text"])
                if r.get("source_hash") != expected:
                    result["errors"].append({"line": line_no, "error": "source_hash_mismatch"})
            except Exception:
                pass
    return result

def check_generated(path):
    result = check_jsonl(path, REQUIRED_GENERATED, "content_hash")
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                if r.get("status") not in VALID_STATUS:
                    result["errors"].append({"line": line_no, "error": "invalid_status"})
                if not isinstance(r.get("source_ids"), list) or not r.get("source_ids"):
                    result["errors"].append({"line": line_no, "error": "missing_source_ids"})
            except Exception:
                pass
    return result

def main():
    generated = ROOT / "generated"
    checks = []
    src = generated / "source-units.jsonl"
    verse = generated / "verse-corpus.jsonl"
    if src.exists():
        checks.append({"file": str(src.relative_to(ROOT)), **check_source_integrity(src)})
    if verse.exists():
        checks.append({"file": str(verse.relative_to(ROOT)), **check_generated(verse)})

    errors = sum(len(c["errors"]) for c in checks)
    report = {
        "version": 2,
        "checks": checks,
        "error_count": errors,
        "publication_gate": "PASS" if errors == 0 else "BLOCK",
    }
    (generated / "QC-REPORT.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
