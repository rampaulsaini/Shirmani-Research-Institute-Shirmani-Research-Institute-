#!/usr/bin/env python3
"""Resumable product worker.

The worker uses stable product IDs plus factory/state.json as a compact queue.
It never claims that generated philosophy is independently verified science.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from factory.state import load, save

CFG = json.loads((ROOT / "factory" / "agent_config.json").read_text(encoding="utf-8"))
SHIRMANI_AGENT = ROOT / "factory" / "agents" / "shirmani-heart-view-agent.md"
FRAMEWORK = ROOT / "factory" / "shirmani-framework.json"
STATE = ROOT / "factory" / "state.json"
OUT = ROOT / "generated"
CORPUS = OUT / "verse-corpus.jsonl"
SOURCE_UNITS = OUT / "source-units.jsonl"

def existing_count(kind):
    if kind == "verse":
        p = CORPUS
        if not p.exists():
            return 0
        return sum(1 for line in p.open(encoding="utf-8") if line.strip())
    if kind == "book":
        return len(list(OUT.glob("book-*.md")))
    if kind == "research-paper":
        return len(list(OUT.glob("research-paper-draft-*.md")))
    if kind == "certificate":
        return len(list((OUT / "certificates").glob("certificate-*.md"))) if (OUT / "certificates").exists() else 0
    if kind == "audio-prompt":
        p = OUT / "audio-prompts.jsonl"
        return sum(1 for line in p.open(encoding="utf-8") if line.strip()) if p.exists() else 0
    return 0

def bootstrap_state():
    data = load(STATE)
    done = data.setdefault("completed", {})
    data.setdefault("version", 2)
    data["state_repaired_from_outputs"] = True
    for kind in ("verse", "book", "research-paper", "certificate", "audio-prompt"):
        done[kind] = sorted(set(done.get(kind, [])) | set(range(1, existing_count(kind) + 1)))
    data["status"] = "running"
    save(STATE, data)
    return data

def shirmani_orientation():
    return SHIRMANI_AGENT.read_text(encoding="utf-8").strip() if SHIRMANI_AGENT.exists() else ""

def framework_policy():
    return json.loads(FRAMEWORK.read_text(encoding="utf-8")) if FRAMEWORK.exists() else {}

def framework_meta():
    policy = framework_policy()
    return {
        "framework_id": policy.get("framework_id", "unknown"),
        "framework_version": policy.get("version"),
        "claim_classes": policy.get("claim_classes", []),
        "method_stack": policy.get("method_stack", [])
    }

def claim_record(text, source_id=None):
    lower = text.lower()
    if any(x in lower for x in ("सर्वश्रेष्ठ", "यथार्थ युग", "शिरोमणि", "संपूर्ण संतुष्टि", "हृदय दृष्टिकोण")):
        claim_class = "user_philosophy"
    elif any(x in lower for x in ("सिद्ध", "प्रमाण", "वैज्ञानिक", "science", "empirical")):
        claim_class = "unverified_claim"
    else:
        claim_class = "creative_expression"
    return {
        "framework_id": framework_meta()["framework_id"],
        "claim_class": claim_class,
        "method_trace": ["source_provenance", "textual_context", "cross-source_comparison", "independent_verification"],
        "source_ids": [source_id] if source_id else [],
        "evidence_status": "requires_independent_verification",
        "human_review_required": True
    }

def research_question(text):
    """Create a deterministic research question without external model dependencies."""
    cleaned = " ".join(str(text).split())
    if not cleaned:
        return "उपलब्ध स्रोत-सामग्री से कौन-सा प्रश्न स्वतंत्र रूप से जाँचा जा सकता है?"
    return f"उपलब्ध स्रोत-सामग्री के आधार पर यह कथन किस सीमा तक सत्यापन योग्य है: {cleaned[:600]}?"

def content_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def source_rows():
    if not SOURCE_UNITS.exists():
        return []
    return [json.loads(x) for x in SOURCE_UNITS.read_text(encoding="utf-8").splitlines() if x.strip()]

def corpus_rows():
    if not CORPUS.exists():
        return []
    return [json.loads(x) for x in CORPUS.read_text(encoding="utf-8").splitlines() if x.strip()]

def next_ids(data, kind, target, limit):
    done = set(data.get("completed", {}).get(kind, []))
    return [i for i in range(1, target + 1) if i not in done][:limit]

def mark(data, kind, number):
    data.setdefault("completed", {}).setdefault(kind, [])
    if number not in data["completed"][kind]:
        data["completed"][kind].append(number)
        data["completed"][kind].sort()

def _atomic_jsonl_merge(path, new_rows, key="id"):
    """Append only missing stable IDs; never rewrite a large canonical corpus."""
    if not new_rows:
        return 0
    existing_ids = set()
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        existing_ids.add(str(json.loads(line)[key]))
                    except (json.JSONDecodeError, KeyError):
                        continue
    pending = [r for r in new_rows if str(r[key]) not in existing_ids]
    if not pending:
        return 0
    pending.sort(key=lambda r: int(r[key]))
    tmp = path.with_suffix(path.suffix + ".append.tmp")
    tmp.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in pending),
        encoding="utf-8",
    )
    with path.open("ab") as out, tmp.open("rb") as src:
        while True:
            chunk = src.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
        out.flush()
    tmp.unlink(missing_ok=True)
    return len(pending)

def write_verses(data, rows, ids):
    if not rows or not ids:
        return 0
    CORPUS.parent.mkdir(parents=True, exist_ok=True)
    generated = []
    for i in ids:
        base = rows[(i - 1) % len(rows)]
        text = f"सूत्र {i:06d}: {base['text']} — यह स्रोत-आधारित चिंतन-प्रारूप है; स्वतंत्र सत्यापन आवश्यक है।"
        meta = claim_record(text, base.get("id"))
        generated.append({
            "id": i, "agent": "shirmani-heart-view",
            "source": base.get("source", "unknown"),
            "source_ids": meta["source_ids"],
            "content_hash": content_hash(text),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "text": text, "status": "draft",
            "framework": framework_meta(),
            "claim_class": meta["claim_class"],
            "method_trace": meta["method_trace"],
            "evidence_status": meta["evidence_status"],
            "human_review_required": meta["human_review_required"]
        })
    added = _atomic_jsonl_merge(CORPUS, generated)
    for i in ids:
        mark(data, "verse", i)
    return added

def write_papers(data, rows, ids):
    if not rows:
        return 0
    for i in ids:
        base = rows[(i - 1) % len(rows)]
        (OUT / f"research-paper-draft-{i:03d}.md").write_text(
            f"# Research Paper Draft {i:03d}\n\n"
            "## Abstract\n"
            "यह स्वचालित शोध-प्रारूप उपलब्ध स्रोत-सामग्री को व्यवस्थित करता है।\n\n"
            "## Research question\n" + research_question(base["text"]) + "\n\n"
            "## Method\nस्रोत-संग्रह, पाठ-सफाई, प्रश्न-निर्माण और provenance tracing।\n\n"
            "## Status\nDraft only; independent peer review, empirical testing and source verification are required.\n\n"
            "## Source\n" + "{}:{}\n".format(base.get("repository", "unknown"), base.get("path", "unknown")),
            encoding="utf-8")
        mark(data, "research-paper", i)
    return len(ids)

def write_certificates(data, ids):
    d = OUT / "certificates"
    d.mkdir(parents=True, exist_ok=True)
    for i in ids:
        (d / f"certificate-{i:04d}.md").write_text(
            f"# Digital Research Certificate {i:04d}\n\n"
            "यह केवल archival/participation record है; academic, governmental, "
            "professional या scientific accreditation नहीं।\n",
            encoding="utf-8")
        mark(data, "certificate", i)
    return len(ids)

def write_audio_prompts(data, rows, ids):
    if not rows or not ids:
        return 0
    p = OUT / "audio-prompts.jsonl"
    generated = []
    languages = CFG.get("languages", ["hi"])
    for i in ids:
        base = rows[(i - 1) % len(rows)]
        generated.append({
            "id": i,
            "language": languages[(i - 1) % len(languages)],
            "lyric_seed": base["text"],
            "status": "prompt-only",
            "audio_file": None
        })
    added = _atomic_jsonl_merge(p, generated)
    for i in ids:
        mark(data, "audio-prompt", i)
    return added

def write_books(data, rows):
    target = int(CFG["products"]["digital_books"])
    if len(rows) < int(CFG["products"]["verses"]):
        return 0
    per = int(CFG["products"]["verses"]) // target
    made = 0
    for b in range(1, target + 1):
        if b in set(data.get("completed", {}).get("book", [])):
            continue
        start, end = (b - 1) * per + 1, b * per
        lines = [
            f"# डिजिटल महाग्रंथ {b:03d}", "",
            "स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।", ""
        ]
        for n in range(start, end + 1):
            row = rows[n - 1]
            lines += [f"## {n:06d}", row["text"], f"स्रोत: {row.get('repository', 'unknown')}:{row.get('path', 'unknown')} · स्वतंत्र परीक्षण अपेक्षित।", ""]
        (OUT / f"book-{b:03d}.md").write_text("\n".join(lines), encoding="utf-8")
        mark(data, "book", b)
        made += 1
    return made

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=int(CFG.get("batch_size", 1000)))
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    data = bootstrap_state()
    rows = source_rows()
    target = CFG["products"]
    limit = max(1, args.batch_size)
    summary = {"agent_orientation": "shirmani-heart-view", "orientation_loaded": bool(shirmani_orientation()),
        "framework_id": framework_meta()["framework_id"],
        "framework_loaded": bool(framework_policy()),
        "continuity_policy": "canonical-preservation-first; resumable; provenance-required"}
    summary["verse"] = write_verses(data, rows, next_ids(data, "verse", int(target["verses"]), limit))
    verse_rows = corpus_rows()
    summary["research-paper"] = write_papers(data, rows, next_ids(data, "research-paper", int(target["research_papers"]), max(1, limit // 10)))
    summary["certificate"] = write_certificates(data, next_ids(data, "certificate", int(target["certificates"]), max(1, limit // 5)))
    summary["audio-prompt"] = write_audio_prompts(data, rows, next_ids(data, "audio-prompt", int(target["audio_prompts"]), limit))
    summary["book"] = write_books(data, verse_rows)
    target_map = {"verse":"verses","book":"digital_books","research-paper":"research_papers","certificate":"certificates","audio-prompt":"audio_prompts"}
    data["status"] = "complete" if all(
        len(data["completed"].get(k, [])) >= int(target[target_map[k]])
        for k in ("verse", "book", "research-paper", "certificate", "audio-prompt")
    ) else "running"
    data["last_batch"] = summary
    data["last_successful_batch_at"] = datetime.now(timezone.utc).isoformat()
    save(STATE, data)
    (OUT / "worker-status.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "batch_size": limit, "batch": summary,
        "completed": {k: len(v) for k, v in data["completed"].items()},
        "targets": target
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
