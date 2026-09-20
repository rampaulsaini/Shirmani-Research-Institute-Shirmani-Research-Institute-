#!/usr/bin/env python3
"""Attach deterministic reasoning + provenance metadata to generated artifacts.

This is a metadata layer, not a claim-proving engine. It preserves the
distinction between user philosophy, creative expression, hypotheses and
independently verified evidence.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REASONER = ROOT / "factory" / "agents" / "shirmani_reasoning_agent.py"

def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load_reasoner():
    import importlib.util
    spec = importlib.util.spec_from_file_location("shirmani_reasoner", REASONER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def source_ids_from_row(row):
    ids = row.get("source_ids") or []
    if ids:
        return [str(x) for x in ids]
    if row.get("source_id") is not None:
        return [str(row["source_id"])]
    return []

def make_record(kind, artifact_id, text, source_ids, extra=None):
    reasoner = load_reasoner()
    reasoning = reasoner.reason(text, source_ids)
    return {
        "artifact_id": str(artifact_id),
        "kind": kind,
        "content_sha256": sha256(text),
        "source_ids": source_ids,
        "reasoning": reasoning,
        "claim_class": reasoning["claim_class"],
        "method_trace": reasoning["method_trace"],
        "evidence_status": reasoning["evidence_status"],
        "human_review_required": reasoning["human_review_required"],
        "verification_questions": reasoning["verification_questions"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_version": "reasoning-qc-v1",
        **(extra or {}),
    }

def enrich():
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    verse = OUT / "verse-corpus.jsonl"
    if verse.exists():
        for row in (json.loads(x) for x in verse.read_text(encoding="utf-8").splitlines() if x.strip()):
            records.append(make_record("verse", row.get("id"), row.get("text", ""),
                                       source_ids_from_row(row),
                                       {"language": row.get("language", "hi"),
                                        "status": row.get("status", "draft")}))
    verse_rows = [json.loads(x) for x in verse.read_text(encoding="utf-8").splitlines() if x.strip()] if verse.exists() else []
    book_paths = list(OUT.glob("book-*.md"))
    for path, kind in sorted([(p, "book") for p in book_paths] +
                             [(p, "research-paper") for p in OUT.glob("research-paper-draft-*.md")]):
        text = path.read_text(encoding="utf-8")
        source_ids = []
        try:
            n = int(path.stem.rsplit("-", 1)[1])
            if kind == "research-paper" and n <= len(verse_rows):
                source_ids = source_ids_from_row(verse_rows[n - 1])
            elif kind == "book" and verse_rows:
                per = max(1, len(verse_rows) // max(1, len(book_paths)))
                start = (n - 1) * per
                source_ids = sorted({sid for row in verse_rows[start:start + per] for sid in source_ids_from_row(row)})
        except (ValueError, IndexError):
            source_ids = []
        records.append(make_record(kind, path.stem, text, source_ids,
                                   {"path": str(path.relative_to(ROOT)), "status": "draft"}))
    manifest = OUT / "reasoning-manifest.jsonl"
    manifest.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) +
                        ("\n" if records else ""), encoding="utf-8")
    return {"records": len(records), "path": str(manifest.relative_to(ROOT))}

if __name__ == "__main__":
    print(json.dumps(enrich(), ensure_ascii=False))
