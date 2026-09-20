#!/usr/bin/env python3
"""Resumable, provider-free audio production manifest.

Default mode prepares deterministic audio jobs from audio-prompts.jsonl.
No paid API or remote service is required. Actual rendering is opt-in and
must use a local/open-source renderer; rendered files are never evidence.
"""
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
PROMPTS=OUT/"audio-prompts.jsonl"
MANIFEST=OUT/"audio-production-manifest.jsonl"

def digest(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
def load_rows():
    if not PROMPTS.exists(): return []
    return [json.loads(x) for x in PROMPTS.read_text(encoding="utf-8").splitlines() if x.strip()]
def load_existing():
    if not MANIFEST.exists(): return {}
    return {str(r["id"]):r for r in (json.loads(x) for x in MANIFEST.read_text(encoding="utf-8").splitlines() if x.strip())}

def build(limit=None):
    existing, rows = load_existing(), load_rows()
    selected=rows[:limit] if limit else rows
    for row in selected:
        text=str(row.get("lyric_seed","")).strip()
        job={"id":int(row["id"]),"language":row.get("language","hi"),
             "prompt_sha256":digest(text),"status":"queued","renderer":None,
             "audio_file":None,"audio_sha256":None,
             "created_at":datetime.now(timezone.utc).isoformat(),
             "verification":{"content_integrity":"pending","render_integrity":"pending","human_review_required":True}}
        old=existing.get(str(row["id"]))
        if old and old.get("prompt_sha256")==job["prompt_sha256"]: job=old
        existing[str(row["id"])]=job
    ordered=[existing[k] for k in sorted(existing,key=lambda x:int(x))]
    tmp=MANIFEST.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in ordered),encoding="utf-8")
    tmp.replace(MANIFEST)
    return len(ordered)

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--limit",type=int); args=ap.parse_args()
    print(json.dumps({"audio_jobs":build(args.limit),"manifest":str(MANIFEST.relative_to(ROOT)),
                      "mode":"manifest-only","paid_api_required":False},ensure_ascii=False))
