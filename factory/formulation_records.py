#!/usr/bin/env python3
"""Build deterministic formulation/test records from the reasoning manifest.

This layer performs reproducible checks over generated artifacts. It does not
claim that a philosophical or textual proposition is scientifically proven.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

_VERSE_INDEX = None

def artifact_text(kind, artifact_id):
    global _VERSE_INDEX
    if kind == "verse":
        if _VERSE_INDEX is None:
            path = OUT / "verse-corpus.jsonl"
            if not path.exists():
                return None
            _VERSE_INDEX = {}
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    row = json.loads(line)
                    _VERSE_INDEX[str(row.get("id"))] = row.get("text", "")
        return _VERSE_INDEX.get(str(artifact_id))
    if kind == "book":
        path = OUT / ("book-" + str(artifact_id) + ".md")
    elif kind == "research-paper":
        path = OUT / ("research-paper-draft-" + str(artifact_id) + ".md")
    else:
        return None
    return path.read_text(encoding="utf-8") if path.exists() else None

def build():
    reasoning_path = OUT / "reasoning-manifest.jsonl"
    if not reasoning_path.exists():
        raise SystemExit("reasoning-manifest.jsonl is missing")
    records = []
    for line in reasoning_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        text = artifact_text(r["kind"], r["artifact_id"])
        content_hash = sha(text) if text is not None else None
        records.append({
            "id": "formulation:" + r["kind"] + ":" + str(r["artifact_id"]),
            "artifact_id": str(r["artifact_id"]),
            "kind": r["kind"],
            "formulation_type": "deterministic_content_integrity",
            "inputs": {
                "content_sha256_from_artifact": content_hash,
                "content_sha256_from_reasoning": r.get("content_sha256"),
                "source_ids": r.get("source_ids", [])
            },
            "procedure": [
                "resolve the generated artifact by stable kind/id",
                "recompute SHA-256 over the exact artifact text",
                "compare it with reasoning-manifest content_sha256",
                "preserve source IDs without upgrading them to evidence"
            ],
            "result": {
                "artifact_resolved": text is not None,
                "hash_match": text is not None and content_hash == r.get("content_sha256"),
                "status": "PASS" if text is not None and content_hash == r.get("content_sha256") else "FAIL"
            },
            "limitations": [
                "hash agreement proves byte-level content identity only",
                "source traceability is not independent verification",
                "semantic, historical, scientific, or factual truth requires appropriate external verification"
            ],
            "verification": {
                "independent": False,
                "status": "NOT_VERIFIED",
                "required": True
            },
            "provenance": {
                "generator": "factory/formulation_records.py",
                "reasoning_record_hash": r.get("content_sha256")
            }
        })
    path = OUT / "formulation-records.jsonl"
    path.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in records) + ("\n" if records else ""),
        encoding="utf-8"
    )
    print(json.dumps({"records": len(records), "path": str(path.relative_to(ROOT))}, ensure_ascii=False))

if __name__ == "__main__":
    build()
