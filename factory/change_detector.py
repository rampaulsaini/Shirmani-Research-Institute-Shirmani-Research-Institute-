#!/usr/bin/env python3
import json, subprocess, hashlib, os
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
manifest=json.loads((OUT/"manifest.json").read_text(encoding="utf-8"))
state_path=OUT/"source-state.json"; previous=json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
old=previous.get("sources",{}); current={}
for item in manifest.get("sources",[]):
    repo=item["repository"]; available=bool(item.get("available")); entry={"available":available,"head_sha":None,"content_fingerprint":None}
    dest=ROOT/"factory/_sources"/repo.split("/",1)[1]
    if available and dest.exists():
        p=subprocess.run(["git","-C",str(dest),"rev-parse","HEAD"],text=True,capture_output=True,check=False)
        if p.returncode==0: entry["head_sha"]=p.stdout.strip()
        h=hashlib.sha256()
        for f in sorted(dest.rglob("*")):
            if ".git" in f.parts or not f.is_file() or f.suffix.lower() not in {".md",".txt",".html",".htm",".json",".yml",".yaml"}: continue
            h.update(str(f.relative_to(dest)).encode()); h.update(f.read_bytes())
        entry["content_fingerprint"]=h.hexdigest()
    current[repo]=entry
new=[]; changed=[]; unchanged=[]; unavailable=[]
for repo,cur in current.items():
    prev=old.get(repo)
    if not cur["available"]: unavailable.append(repo)
    elif prev is None: new.append(repo)
    elif prev.get("head_sha")!=cur.get("head_sha") or prev.get("content_fingerprint")!=cur.get("content_fingerprint"): changed.append(repo)
    else: unchanged.append(repo)
report={"generated_at":datetime.now(timezone.utc).isoformat(),"new":new,"changed":changed,"unchanged":unchanged,"unavailable":unavailable,"process_required":bool(new or changed) or os.environ.get("GITHUB_EVENT_NAME")=="push" or any(not (OUT / req).exists() for req in ["provenance-ledger.jsonl","canonical-corpus.jsonl","evidence-index.jsonl","verification-report.json","research-queue.jsonl","product-queue.jsonl","ai-output.jsonl"]),"previous_state_exists":state_path.exists(),"policy":"Only new or changed sources are marked changed; unavailable sources are never fabricated."}
(OUT/"source-change-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
state_path.write_text(json.dumps({"generated_at":report["generated_at"],"sources":current},ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(report,ensure_ascii=False))
if __import__("os").environ.get("GITHUB_OUTPUT"):
    with open(__import__("os").environ["GITHUB_OUTPUT"],"a",encoding="utf-8") as f:
        f.write(f"process_required={str(report['process_required']).lower()}\n")
