#!/usr/bin/env python3
"""Attach deterministic reasoning + provenance metadata to generated artifacts.

This is a metadata layer, not a claim-proving engine. It preserves the
distinction between user philosophy, creative expression, hypotheses and
independently verified evidence.
"""
import hashlib
import json
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
    """Resolve source IDs from inline labels and Markdown source sections.

    A source may be written on the same line as a Source heading or on the
    following non-empty line. Unresolved sources remain unresolved; IDs are
    never invented.
    """
    found = []
    lines = text.splitlines()
    for pos, line in enumerate(lines):
        stripped = line.strip()
        candidate = None
        if "स्रोत:" in stripped:
            candidate = stripped.split("स्रोत:", 1)[1].split("·", 1)[0].strip()
        elif stripped.lower().startswith("## source"):
            remainder = stripped[len("## source"):].strip(" :")
            if remainder:
                candidate = remainder
            else:
                for next_line in lines[pos + 1:]:
                    next_stripped = next_line.strip()
                    if not next_stripped:
                        continue
                    if next_stripped.startswith("#"):
                        break
                    candidate = next_stripped
                    break
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

def load_source_locations():
    path = OUT / "source-units.jsonl"
    locations = {}
    if not path.exists():
        return locations
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        locations[str(row.get("id"))] = "{}:{}".format(row.get("repository", "unknown"), row.get("path", "unknown"))
    return locations

def claim_evidence_record(record, locations):
    source_ids = [str(x) for x in record.get("source_ids", [])]
    sources = [{"type": "SOURCE_RECORD", "locator": locations.get(sid, "source-id:" + sid),
                "source_id": sid} for sid in source_ids]
    traceable = bool(source_ids and all(sid in locations for sid in source_ids))
    return {
        "id": "claim:" + record["kind"] + ":" + str(record["artifact_id"]),
        "claim": record.get("reasoning", {}).get("claim", ""),
        "definitions": ["Generated artifact claim; operational meaning requires human review."],
        "source": sources,
        "evidence": [{"kind": "SOURCE_TRACE", "status": "NOT_VERIFIED",
                      "detail": "Source trace is provenance, not independent proof."}],
        "formulation": {"method": "deterministic provenance/reasoning metadata",
                        "result_status": "NOT_VERIFIED"},
        "countercases": [
            "Source may be incomplete, ambiguous, outdated, or interpreted differently.",
            "Independent evidence may contradict the generated formulation."
        ],
        "source_traceability": {
            "status": "PASS" if traceable else "BLOCK",
            "source_ids": source_ids,
            "resolved": traceable
        },
        "verification": {"status": "NOT_VERIFIED",
                          "method": "Independent human/source verification required.",
                          "independent": False},
        "conclusion": "No independently verified conclusion is asserted by the factory.",
        "provenance": {"created_at": record["created_at"],
                       "generator": "factory/reasoning_pipeline.py",
                       "content_hash": record["content_sha256"]}
    }

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
            verse_source_ids = source_ids_from_row(row)
            if not verse_source_ids and row.get("source"):
                source_key = str(row.get("source"))
                if source_key in source_index:
                    verse_source_ids = [source_index[source_key]]
            records.append(make_record("verse", row.get("id"), row.get("text", ""),
                                       verse_source_ids,
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

    locations = load_source_locations()
    ce = OUT / "claim-evidence.jsonl"
    tmp = ce.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(claim_evidence_record(r, locations), ensure_ascii=False) + "\n")
    tmp.replace(ce)
    return {"records": len(records), "path": str(manifest.relative_to(ROOT)),
            "claim_evidence_records": len(records),
            "claim_evidence_path": str(ce.relative_to(ROOT))}

if __name__ == "__main__":
    print(json.dumps(enrich(), ensure_ascii=False))
