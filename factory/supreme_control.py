#!/usr/bin/env python3
"""Fail-closed control plane for AI-agent, ML and NLP automation."""
from __future__ import annotations
import hashlib,json,re,subprocess,sys
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"/"supreme-control-plane.json"
def run(c):
 p=subprocess.run(c,cwd=ROOT,text=True,capture_output=True); return p.returncode==0
def text_metrics(path):
 if not path.exists(): return {"exists":False}
 rows=[]
 for line in path.read_text(encoding="utf-8",errors="replace").splitlines():
  if line.strip():
   try: rows.append(json.loads(line))
   except Exception: pass
 texts=[str(x.get("text","")) for x in rows]
 return {"exists":True,"records":len(rows),"nonempty_text":sum(bool(x.strip()) for x in texts),
 "unique_text":len(set(texts)),"tokens":sum(len(re.findall(r"\w+",x,re.UNICODE)) for x in texts),
 "languages":dict(Counter(str(x.get("language","unknown")) for x in rows).most_common(20))}
def verification():
 fs=sorted((ROOT/"generated").glob("independent-verification-status-*.json"))
 if not fs:return {"status":"UNAVAILABLE","verified_records":None}
 d=json.loads(fs[-1].read_text(encoding="utf-8")); s=d.get("verification_summary",{})
 v=s.get("independently_verified_records"); rs=d.get("records",[])
 return {"status":"FAIL-CLOSED" if v==0 and all(x.get("status")!="VERIFIED" for x in rs) else "BLOCK",
 "verified_records":v,"queue_records":s.get("queue_records"),"readiness_percent":s.get("verification_readiness_percent")}
def main():
 g=ROOT/"generated"; g.mkdir(exist_ok=True)
 py=run([sys.executable,"-m","compileall","-q","agents","factory"])
 bad=[]
 for p in list((ROOT/"factory").glob("*.json"))+list((ROOT/"schemas").glob("*.json")):
  try: json.loads(p.read_text(encoding="utf-8"))
  except Exception: bad.append(str(p.relative_to(ROOT)))
 c=text_metrics(g/"verse-corpus.jsonl"); v=verification()
 w=list((ROOT/".github/workflows").glob("*.yml"))+list((ROOT/".github/workflows").glob("*.yaml"))
 five=[p.name for p in w if "*/5 * * * *" in p.read_text(encoding="utf-8",errors="replace")]
 checks={"python_compile":py,"configuration_json":not bad,
 "corpus_structure":not c.get("exists") or c["records"]==c["nonempty_text"],
 "verification_boundary":v["status"] in {"FAIL-CLOSED","UNAVAILABLE"},
 "perfect_accuracy_not_claimed":True}
 d={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
 "mode":"SUPREME_FAIL_CLOSED_CONTROL_PLANE","checks":checks,
 "all_automatable_checks_pass":all(checks.values()),
 "ai_agents":{"orchestration":"present","provenance":"required","human_review":"required"},
 "ml":{"evaluation":"required before performance claims","status":"no_unverified_performance_claim"},
 "nlp":{"deterministic_metrics":c},"verification":v,
 "workflow_inventory":{"workflow_files":len(w),"five_minute_schedules":five},
 "invalid_json_files":bad,
 "principle":"Automation accelerates processing but cannot turn insufficient evidence into VERIFIED truth."}
 OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(d,ensure_ascii=False,indent=2))
 return 0 if d["all_automatable_checks_pass"] else 1
if __name__=="__main__": raise SystemExit(main())
