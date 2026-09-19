#!/usr/bin/env python3
import json,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; OUT.mkdir(exist_ok=True)
if len(sys.argv)<2: raise SystemExit("usage: run_stage.py <script> [max_attempts]")
script=sys.argv[1]; attempts=int(sys.argv[2]) if len(sys.argv)>2 else 3; logs=[]
for n in range(1,attempts+1):
    p=subprocess.run([sys.executable,script],cwd=ROOT,text=True,capture_output=True)
    logs.append({"script":script,"attempt":n,"started":datetime.now(timezone.utc).isoformat(),"returncode":p.returncode,"stdout_tail":p.stdout[-2000:],"stderr_tail":p.stderr[-2000:]})
    if p.returncode==0: break
    if n<attempts: time.sleep(2**n)
with (OUT/"stage-retry-log.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(logs[-1],ensure_ascii=False)+"\n")
(OUT/"recovery-state.json").write_text(json.dumps({"generated_at":datetime.now(timezone.utc).isoformat(),"script":script,"attempts":len(logs),"success":logs[-1]["returncode"]==0,"retry_policy":"up to 3 attempts with exponential backoff"},ensure_ascii=False,indent=2),encoding="utf-8")
if logs[-1]["returncode"]!=0: raise SystemExit(logs[-1]["returncode"])
