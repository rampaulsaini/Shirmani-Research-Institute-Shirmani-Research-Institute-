#!/usr/bin/env python3
"""Resumable product worker.

The worker uses stable product IDs plus factory/state.json as a compact queue.
It never claims that generated philosophy is independently verified science.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents.provenance_agent import record, validate
from agents.verification_agent import classify
from agents.topic_agent import enrich
from agents.research_agent import question
from factory.state import load, save

CFG = json.loads((ROOT / "factory" / "agent_config.json").read_text(encoding="utf-8"))
SHIRMANI_AGENT = ROOT / "factory" / "agents" / "shirmani-heart-view-agent.md"
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
    for kind in ("verse", "book", "research-paper", "certificate", "audio-prompt"):
        done[kind] = sorted(set(done.get(kind, [])) | set(range(1, existing_count(kind) + 1)))
    data["status"] = "running"
    save(STATE, data)
    return data

def shirmani_orientation():
    return SHIRMANI_AGENT.read_text(encoding="utf-8").strip() if SHIRMANI_AGENT.exists() else ""

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

def write_verses(data, rows, ids):
    if not rows:
        return 0
    CORPUS.parent.mkdir(parents=True, exist_ok=True)
    with CORPUS.open("a", encoding="utf-8") as f:
        for i in ids:
            base = rows[(i - 1) % len(rows)]
            text = f"सूत्र {i:06d}: {base['text']} — यह स्रोत-आधारित चिंतन-प्रारूप है; स्वतंत्र सत्यापन आवश्यक है।"
            f.write(json.dumps({
                "id": i, "source": base.get("source", "unknown"),
                "text": text, "status": "draft"
            }, ensure_ascii=False) + "\n")
            mark(data, "verse", i)
    return len(ids)

def write_papers(data, rows, ids):
    if not rows:
        return 0
    for i in ids:
        base = rows[(i - 1) % len(rows)]
        (OUT / f"research-paper-draft-{i:03d}.md").write_text(
            f"# Research Paper Draft {i:03d}\n\n"
            "## Abstract\n"
            "यह स्वचालित शोध-प्रारूप उपलब्ध स्रोत-सामग्री को व्यवस्थित करता है।\n\n"
            "## Research question\n" + question(base["text"]) + "\n\n"
            "## Method\nस्रोत-संग्रह, पाठ-सफाई, प्रश्न-निर्माण और provenance tracing।\n\n"
            "## Status\nDraft only; independent peer review, empirical testing and source verification are required.\n\n"
            "## Source\n" + base.get("source", "unknown") + "\n",
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
    if not rows:
        return 0
    p = OUT / "audio-prompts.jsonl"
    with p.open("a", encoding="utf-8") as f:
        for i in ids:
            base = rows[(i - 1) % len(rows)]
            f.write(json.dumps({
                "id": i, "language": CFG.get("languages", ["hi"])[(i - 1) % len(CFG.get("languages", ["hi"]))],
                "lyric_seed": base["text"], "status": "prompt-only",
                "audio_file": None
            }, ensure_ascii=False) + "\n")
            mark(data, "audio-prompt", i)
    return len(ids)

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
            lines += [f"## {n:06d}", row["text"], f"स्रोत: {row.get('source', 'unknown')} · स्वतंत्र परीक्षण अपेक्षित।", ""]
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
    summary = {"agent_orientation": "shirmani-heart-view", "orientation_loaded": bool(shirmani_orientation())}
    summary["verse"] = write_verses(data, rows, next_ids(data, "verse", int(target["verses"]), limit))
    verse_rows = corpus_rows()
    summary["research-paper"] = write_papers(data, rows, next_ids(data, "research-paper", int(target["research_papers"]), max(1, limit // 10)))
    summary["certificate"] = write_certificates(data, next_ids(data, "certificate", int(target["certificates"]), max(1, limit // 5)))
    summary["audio-prompt"] = write_audio_prompts(data, rows, next_ids(data, "audio-prompt", int(target["audio_prompts"]), limit))
    summary["book"] = write_books(data, verse_rows)
    data["status"] = "complete" if all(
        len(data["completed"].get(k, [])) >= int(target["digital_books" if k == "book" else k.replace("-", "_") + "s"])
        for k in ("verse", "book", "research-paper", "certificate", "audio-prompt")
    ) else "running"
    data["last_batch"] = summary
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
