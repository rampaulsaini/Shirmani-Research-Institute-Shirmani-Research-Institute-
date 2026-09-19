#!/usr/bin/env python3
import json,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
OUT.mkdir(exist_ok=True)
if len(sys.argv)<2:
    raise SystemExit("usage: run_stage.py <script> [max_attempts]")
script=sys.argv[1]
attempts=int(sys.argv[2]) if len(sys.argv)>2 else 3
logs=[]
for n in range(1,attempts+1):
    started=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(
        [sys.executable,script],
        cwd=ROOT,text=True,capture_output=True
    )
    entry={
        "script":script,
        "attempt":n,
        "started":started,
        "finished":datetime.now(timezone.utc).isoformat(),
        "returncode":p.returncode,
        "stdout_tail":p.stdout[-4000:],
        "stderr_tail":p.stderr[-4000:]
    }
    logs.append(entry)
    if p.returncode==0:
        break
    print(f"STAGE FAILED: {script} attempt {n}/{attempts}", file=sys.stderr)
    if p.stdout:
        print("STDOUT (tail):", file=sys.stderr)
        print(p.stdout[-4000:], file=sys.stderr)
    if p.stderr:
        print("STDERR (tail):", file=sys.stderr)
        print(p.stderr[-4000:], file=sys.stderr)
    if n<attempts:
        time.sleep(2**n)

with (OUT/"stage-retry-log.jsonl").open("a",encoding="utf-8") as f:
    for item in logs:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

ok=logs[-1]["returncode"]==0
(OUT/"recovery-state.json").write_text(
    json.dumps({
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "script":script,
        "attempts":len(logs),
        "success":ok,
        "retry_policy":"up to 3 attempts with exponential backoff"
    },ensure_ascii=False,indent=2),
    encoding="utf-8"
)
if not ok:
    raise SystemExit(logs[-1]["returncode"])
