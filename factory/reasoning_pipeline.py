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

def load_source_index():
    path = OUT / "source-units.jsonl"
    if not path.exists():
        return {}
    index = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        key = "{}:{}".format(row.get("repository"), row.get("path"))
        index[key] = str(row.get("id"))
    return index

def source_ids_from_text(text, index):
    found = []
    for line in text.splitlines():
        candidate = None
        if "स्रोत:" in line:
            candidate = line.split("स्रोत:", 1)[1].split("·", 1)[0].strip()
        elif line.strip().lower().startswith("## source"):
            candidate = line.split("## source", 1)[1].strip(" :")
        if candidate and candidate in index:
            found.append(index[candidate])
    return sorted(set(found))

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
    source_index = load_source_index()
    verse = OUT / "verse-corpus.jsonl"
    if verse.exists():
        for row in (json.loads(x) for x in verse.read_text(encoding="utf-8").splitlines() if x.strip()):
            records.append(make_record("verse", row.get("id"), row.get("text", ""),
                                       source_ids_from_row(row),
                                       {"language": row.get("language", "hi"),
                                        "status": row.get("status", "draft")}))
    for path, kind in sorted([(p, "book") for p in OUT.glob("book-*.md")] +
                             [(p, "research-paper") for p in OUT.glob("research-paper-draft-*.md")]):
        text = path.read_text(encoding="utf-8")
        records.append(make_record(kind, path.stem, text, source_ids_from_text(text, source_index),
                                   {"path": str(path.relative_to(ROOT)), "status": "draft"}))
    manifest = OUT / "reasoning-manifest.jsonl"
    manifest.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) +
                        ("\n" if records else ""), encoding="utf-8")
    return {"records": len(records), "path": str(manifest.relative_to(ROOT))}

if __name__ == "__main__":
    print(json.dumps(enrich(), ensure_ascii=False))
