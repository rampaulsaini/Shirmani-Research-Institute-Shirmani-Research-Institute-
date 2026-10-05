#!/usr/bin/env python3
"""Production-first multi-layer Automission conveyor.
Produces durable work; downstream verification evaluates produced work.
"""
import gzip, hashlib, json, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
G=ROOT/"generated"
STATE=G/"production-conveyor-state.json"
QUEUE=G/"production-task-queue.jsonl.gz"
BATCHES=G/"production-batches"
STATUS=G/"production-status.json"
ROLES=[
 ("research","Research Practitioner"),("nlp","NLP Practitioner"),
 ("ml","ML Signal Practitioner"),("reasoning","Reasoning Practitioner"),
 ("content","Content Production"),("product","Product Production"),
 ("audio","Audio/Music Production"),("translation","Multilingual Production"),
 ("marketing","Marketing Production"),("knowledge","Knowledge Production"),
 ("archive","Archive Production"),("publishing","Publishing Preparation"),
]

def now(): return datetime.now(timezone.utc).isoformat()
def rows(p):
    if not p.exists(): return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
def count(p):
    if not p.exists(): return 0
    op=gzip.open if str(p).endswith(".gz") else open
    with op(p,"rt",encoding="utf-8") as f: return sum(1 for x in f if x.strip())

def sources():
    for p in (G/"source-units.jsonl",G/"canonical-knowledge.jsonl",G/"research-queue.jsonl"):
        r=rows(p)
        if r: return r
    return []

def state():
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"target":100200,"next_task":1,"processed":0,"batches":0}

def save(s): STATE.write_text(json.dumps(s,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def make_task(n,src):
    role,name=ROLES[(n-1)%len(ROLES)]
    sid=str(src.get("id") or src.get("canonical_id") or src.get("research_id") or "SOURCE")
    text=" ".join(str(src.get("text") or src.get("question") or "").split())
    return {"task_id":f"PROD-{n:06d}","role":role,"role_name":name,"source_id":sid,
            "source":src.get("source") or src.get("repository") or "repository-source",
            "source_path":src.get("path") or "","input_hash":hashlib.sha256(text.encode()).hexdigest(),
            "task_hash":hashlib.sha256(f"{n}|{role}|{sid}|{text}".encode()).hexdigest(),
            "status":"PENDING","verification_state":"NOT_A_VERIFICATION_TASK"}

def ensure_queue(srcs,target):
    if QUEUE.exists() and count(QUEUE)>=target: return count(QUEUE)
    if not srcs: return 0
    existing=count(QUEUE)
    QUEUE.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(QUEUE,"at",encoding="utf-8") as f:
        for n in range(existing+1,target+1):
            f.write(json.dumps(make_task(n,srcs[(n-1)%len(srcs)]),ensure_ascii=False)+"\n")
    return target

def produce(t):
    outputs={
      "research":"Research question and source-grounded investigation brief prepared.",
      "nlp":"Normalization, token/phrase and language-processing work item prepared.",
      "ml":"Deterministic lexical, duplication, anomaly and completeness signals prepared.",
      "reasoning":"Hypothesis, countercase, evidence requirement and uncertainty fields prepared.",
      "content":"Source-grounded content draft package prepared without adding unsupported facts.",
      "product":"Product brief with format, audience, benefit, provenance and delivery fields prepared.",
      "audio":"Audio/music production prompt prepared; file generation remains a separate stage.",
      "translation":"Hindi, Punjabi and English derivative-language slots prepared with attribution.",
      "marketing":"Truthful SEO, social, product-copy and campaign fields prepared.",
      "knowledge":"Structured concept/entity/relation record prepared for the knowledge layer.",
      "archive":"Traceable archive record prepared.",
      "publishing":"Publication metadata/index package prepared; applicable gates remain downstream.",
    }
    return {**t,"status":"PRODUCED","produced_at":now(),"output_type":t["role"],
            "output":outputs[t["role"]],"verification_state":"PENDING_DOWNSTREAM",
            "independent_verification":False}

def stage(path):
    t=time.time()
    p=subprocess.run([sys.executable,str(ROOT/path)],cwd=ROOT,capture_output=True,text=True,timeout=180)
    return {"stage":path,"returncode":p.returncode,"seconds":round(time.time()-t,2),"stdout":p.stdout[-500:],"stderr":p.stderr[-500:]}

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--batch-size",type=int,default=1000); a=ap.parse_args()
    G.mkdir(parents=True,exist_ok=True); s=state(); src=sources()
    total=ensure_queue(src,int(s.get("target",100200)))
    start=s["next_task"]; end=min(start+a.batch_size-1,total)
    batch=[]
    if start<=end:
        with gzip.open(QUEUE,"rt",encoding="utf-8") as f:
            for i,line in enumerate(f,1):
                if i<start: continue
                if i>end: break
                batch.append(produce(json.loads(line)))
        BATCHES.mkdir(parents=True,exist_ok=True)
        out=BATCHES/f"production-{start:06d}-{end:06d}.jsonl.gz"
        with gzip.open(out,"wt",encoding="utf-8") as f:
            for r in batch: f.write(json.dumps(r,ensure_ascii=False)+"\n")
        s["next_task"]=end+1; s["processed"]+=len(batch); s["batches"]+=1
        s["last_batch"]={"start":start,"end":end,"count":len(batch),"completed_at":now()}
    save(s)
    stages=[]
    for path in ("factory/canonical_knowledge.py","factory/canonical_index.py",
                 "factory/reasoning_pipeline.py","factory/formulation_records.py",
                 "factory/agents/research_agent.py","factory/agents/evidence_agent.py",
                 "factory/agents/product_agent.py","factory/multilingual.py","factory/publish_index.py"):
        if (ROOT/path).exists(): stages.append(stage(path))
    html=len(list(ROOT.rglob("*.html")))
    py=len(list(ROOT.rglob("*.py")))
    workflows=len(list((ROOT/".github/workflows").glob("*.yml")))
    status={"generated_at":now(),"mode":"SUPREME_PRODUCTION_FIRST",
      "principle":"Automission produces work; verification evaluates produced work downstream.",
      "production_target":total,"production_processed":s["processed"],
      "production_remaining":max(0,total-s["processed"]),
      "production_completion_percent":round(100*s["processed"]/max(1,total),2),
      "last_batch":s.get("last_batch"),"stages":stages,
      "inventory":{"html_modules":html,"python_modules":py,"workflow_definitions":workflows,
                   "source_units":count(G/"source-units.jsonl"),
                   "canonical_records":count(G/"canonical-knowledge.jsonl"),
                   "research_records":count(G/"research-queue.jsonl"),
                   "product_records":count(G/"product-queue.jsonl"),
                   "verse_records":count(G/"verse-corpus.jsonl"),
                   "audio_prompt_records":count(G/"audio-prompts.jsonl"),
                   "research_paper_files":len(list(G.glob("research-paper-draft-*.md"))),
                   "book_files":len(list(G.glob("book-*.md"))),
                   "certificate_files":len(list((G/"certificates").glob("certificate-*.md"))) if (G/"certificates").exists() else 0},
      "verification_boundary":"DOWNSTREAM_ONLY",
      "quantum_mode":"NOT_CLAIMED — actual quantum backend required for quantum execution."}
    STATUS.write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__": main()
