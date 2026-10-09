#!/usr/bin/env python3
"""Production-first public artifact materializer.

Every queued work unit becomes a concrete source-bound production artifact.
Verification is a downstream quality/promotion layer and is never auto-promoted.
"""
from __future__ import annotations
import hashlib, html, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; QUEUE=GEN/"production-work-queue.jsonl"
RESULTS=GEN/"production-results.jsonl"; DASHBOARD=GEN/"public-production-index.html"
MODULE_INDEX=GEN/"public-production-by-module.html"; MODULE_JSON=GEN/"public-production-module-index.json"
ARTIFACT_DIR=GEN/"public-production"
ARCHIVE_DIR=ARTIFACT_DIR/"archive"

def now(): return datetime.now(timezone.utc).isoformat()
def digest(v): return hashlib.sha256(v.encode("utf-8")).hexdigest()
def load_tasks():
    if not QUEUE.exists(): return []
    out=[]
    for line in QUEUE.read_text(encoding="utf-8",errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            task=json.loads(line)
        except json.JSONDecodeError:
            continue
        # Backward-compatible queue handling: older work units may not have
        # the current "module" key. Never let one legacy record abort the
        # entire production cycle.
        module=task.get("module") or task.get("path") or task.get("module_path")
        if not module:
            continue
        task["module"]=module
        task.setdefault("module_kind","legacy")
        task.setdefault("lane","automation")
        task.setdefault("cycle",0)
        task.setdefault("slot",0)
        task.setdefault("task_id",digest(json.dumps(task,sort_keys=True))[:20])
        task.setdefault("objective",f"Produce a concrete, provenance-linked output for {module}")
        out.append(task)
    return out
def title(text,fallback):
    return (re.sub(r"\\s+"," ",text or "").strip()[:110] or fallback).strip()

def deliverable(task,source):
    lane=task["lane"]; t=title(source,task["module"]); excerpt=" ".join(source.split())[:1400]
    base={"production_objective":task["objective"],"source_excerpt":excerpt,
          "source_fingerprint":digest(source)[:16],"verification_state":"PENDING_DOWNSTREAM"}
    if lane=="research":
        base.update(artifact_type="research-work-card",question=f"What concrete research output can be developed from: {t}?",
                    method=["define","collect sources","compare evidence","state limitations"],next_action="research/evidence")
    elif lane=="ai-ml-nlp":
        base.update(artifact_type="ai-ml-nlp-work-card",tasks=["normalize","extract topics/entities","derive features","evaluate"],
                    languages=["hi","pa","en"],next_action="NLP/ML evaluation")
    elif lane=="content":
        base.update(artifact_type="content-production-card",title=t,draft=f"{t}\n\n{excerpt}",
                    variants=["short","long","audio-prompt","social-caption"],next_action="editorial/package")
    elif lane=="platform":
        base.update(artifact_type="public-module-production-card",module=task["module"],
                    activation=["content","status","navigation","telemetry"],next_action="public surface")
    elif lane=="economic":
        base.update(artifact_type="economic-production-card",offer_title=t,
                    deliverables=["product description","service description","audience segment","promotion draft"],
                    commercial_status="DRAFT_ONLY",next_action="owner-approved packaging")
    elif lane=="social-media":
        base.update(artifact_type="social-publication-card",title=t,caption=excerpt,
                    channels=["YouTube","Facebook","Blog","Public Hub"],next_action="channel packaging")
    elif lane=="federation":
        base.update(artifact_type="federation-integration-card",module=task["module"],
                    integration_steps=["discover","route","produce","publish","report"],next_action="cross-repository publication")
    elif lane=="security-quality":
        base.update(artifact_type="quality-work-card",
                    checks=["schema","provenance","source-boundness","output completeness","failure handling"],next_action="QC/evidence")
    else:
        base.update(artifact_type="automation-work-card",execution_plan=["queue","produce","persist","publish","measure"],next_action="next cycle")
    return base

def main():
    GEN.mkdir(parents=True,exist_ok=True); ARTIFACT_DIR.mkdir(parents=True,exist_ok=True); ARCHIVE_DIR.mkdir(parents=True,exist_ok=True)
    tasks=load_tasks(); results=[]; counts=Counter(); rows=defaultdict(list)
    for task in tasks:
        p=ROOT/task["module"]; source=p.read_text(encoding="utf-8",errors="ignore") if p.is_file() else ""
        r={"result_id":digest(task["task_id"]+"|production")[:24],"task_id":task["task_id"],
           "cycle":task["cycle"],"slot":task["slot"],"lane":task["lane"],"module":task["module"],
           "module_kind":task["module_kind"],"produced_at":now(),"status":"PRODUCED",
           "verification_status":"PENDING","deliverable":deliverable(task,source),
           "integrity":{"source_bound":True,"independent_verification":"NOT_YET_PERFORMED",
                        "production_is_not_verification":True}}
        results.append(r); counts[task["lane"]]+=1; rows[task["lane"]].append(r)
    # Keep the public "latest results" stream bounded, and preserve history in
    # one immutable-sized JSONL shard per production cycle.
    RESULTS.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in results),encoding="utf-8")
    cycle=max((int(r.get("cycle",0)) for r in results), default=0)
    archive_path=ARCHIVE_DIR/f"production-cycle-{cycle:06d}.jsonl"
    archive_path.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in results),encoding="utf-8")
    archive_files=sorted(p.name for p in ARCHIVE_DIR.glob("production-cycle-*.jsonl"))
    (ARCHIVE_DIR/"index.json").write_text(json.dumps({
        "generated_at":now(),
        "shard_strategy":"one JSONL file per production cycle",
        "cycle_shards":len(archive_files),
        "files":archive_files,
        "latest_cycle":cycle,
        "latest_cycle_records":len(results),
        "integrity":{"records_are_produced_artifacts":True,"independent_verification_claim":False}
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for lane,items in rows.items():
        (ARTIFACT_DIR/f"{lane}.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in items),encoding="utf-8")
    module_stats=defaultdict(lambda: {"lane":"","module_kind":"","outputs":0,"latest_cycle":0,"latest_status":"PRODUCED"})
    for r in results:
        s=module_stats[r["module"]]; s["lane"]=r["lane"]; s["module_kind"]=r["module_kind"]; s["outputs"]+=1
        s["latest_cycle"]=max(s["latest_cycle"], int(r["cycle"])); s["latest_status"]=r["status"]
    module_payload={"generated_at":now(),"principle":"Every discovered module receives production work; verification remains downstream.","module_count":len(module_stats),"production_modules":len(module_stats),"modules":dict(sorted(module_stats.items())),"integrity":{"source_bound":True,"independent_verification_claim":False}}
    MODULE_JSON.write_text(json.dumps(module_payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    module_table=[]
    for m,s in sorted(module_stats.items()):
        module_table.append("<tr><td>"+html.escape(m)+"</td><td>"+html.escape(s["lane"])+"</td><td>"+html.escape(s["module_kind"])+"</td><td>"+str(s["outputs"])+"</td><td>"+str(s["latest_cycle"])+"</td><td>PRODUCED</td></tr>")
    module_page="<!doctype html><html lang=\"hi\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>SHIRMANI Module-wise Production</title><style>body{margin:0;background:#0b0d14;color:#f5f5f5;font-family:system-ui,sans-serif;line-height:1.5}main{max-width:1300px;margin:auto;padding:24px}h1,h2{color:#d4af37}.hero,.card{background:rgba(255,255,255,.05);border:1px solid rgba(212,175,55,.25);border-radius:14px;padding:18px;margin:12px 0}table{width:100%;border-collapse:collapse}th,td{padding:8px;border-bottom:1px solid #293241;text-align:left}th{color:#d4af37}a{color:#67e8f9}.ok{color:#6ee7b7}</style></head><body><main><section class=\"hero\"><h1>꙰ SHIRMANI — Module-wise Production</h1><p><strong>Production-first visibility:</strong> each discovered module receives concrete production work. Verification remains downstream.</p><div class=\"card\"><b>"+str(len(module_stats))+"</b> modules · <b>"+str(len(results))+"</b> concrete results · <b>"+str(len(counts))+"</b> lanes</div><p><a href=\"public-production-index.html\">Production Results</a> · <a href=\"public-production-module-index.json\">Machine-readable index</a> · <a href=\"../public-platform-modules.html\">Public Module Map</a> · <a href=\"../index.html\">Main Hub</a></p></section><section class=\"card\"><table><thead><tr><th>Module</th><th>Lane</th><th>Kind</th><th>Outputs</th><th>Latest cycle</th><th>Status</th></tr></thead><tbody>"+"" .join(module_table)+"</tbody></table></section><section class=\"hero\"><b>Integrity:</b> PRODUCED means a repository-bound production artifact was materialized. It is not independent verification.</section></main></body></html>"
    MODULE_INDEX.write_text(module_page,encoding="utf-8")
    catalog={"generated_at":now(),"principle":"Production first; verification downstream.",
             "cycle_results":len(results),"lanes":dict(sorted(counts.items())),
             "artifacts":[f"generated/public-production/{x}.jsonl" for x in sorted(rows)] + ["generated/public-production-module-index.json","generated/public-production-by-module.html","generated/public-production/archive/index.json"],
             "integrity":{"generated_output_is_concrete":True,"source_bound":True,"independent_verification_claim":False}}
    (GEN/"public-production-catalog.json").write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    status_path=GEN/"multi-layer-production-status.json"
    status=json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else {}
    status["last_cycle_concrete_results"]=len(results); status.setdefault("production_outputs",{})
    status["production_outputs"]["concrete_results_this_cycle"]=len(results)
    status["production_outputs"]["lane_artifacts"]=dict(sorted(counts.items()))
    status["production_outputs"]["public_catalog"]="generated/public-production-catalog.json"
    status["production_outputs"]["verification"]="downstream"
    status["artifacts"]=["generated/production-results.jsonl","generated/production-work-queue.jsonl","generated/public-production-catalog.json","generated/public-production-module-index.json","generated/public-production-by-module.html"]
    status["production_outputs"]["production_modules"]=len(module_stats)
    status["production_outputs"]["module_index"]="generated/public-production-by-module.html"
    status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    cards=[]
    for r in results[:120]:
        d=r["deliverable"]; preview=html.escape((d.get("draft") or d.get("source_excerpt") or d.get("production_objective") or "")[:500])
        cards.append(f"<article><h3>{html.escape(r['lane'].upper())}</h3><small>{html.escape(r['module'])}</small><h4>{html.escape(str(d.get('title') or d.get('offer_title') or d.get('artifact_type')))}</h4><p>{preview}</p><b>PRODUCED</b> · downstream verification</article>")
    links="".join(f"<a href='public-production/{html.escape(l)}.jsonl'>{html.escape(l)} · {n:,} outputs</a>" for l,n in sorted(counts.items()))
    page=f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SHIRMANI Public Production</title><style>body{{margin:0;background:#0b0d14;color:#f5f5f5;font-family:system-ui,sans-serif;line-height:1.5}}main{{max-width:1250px;margin:auto;padding:24px}}h1,h2{{color:#d4af37}}.hero,article,.links{{background:rgba(255,255,255,.05);border:1px solid rgba(212,175,55,.25);border-radius:14px;padding:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:16px 0}}.links{{display:flex;flex-wrap:wrap;gap:10px}}a{{color:#67e8f9;text-decoration:none;padding:8px 12px;border:1px solid #365;border-radius:9px}}small{{color:#aeb5c2}}b{{color:#6ee7b7}}</style></head><body><main><section class="hero"><h1>꙰ SHIRMANI Public Production</h1><p><strong>Production-first Automission:</strong> every queued work unit becomes a concrete source-bound production card. Verification is downstream.</p><h2>{len(results):,} concrete results this cycle</h2><p>Generated: {catalog["generated_at"]}</p><p><a href="public-production-catalog.json">Catalog</a> · <a href="multi-layer-production-status.json">Status</a> · <a href="production-results.jsonl">Latest cycle stream</a> · <a href="public-production/archive/index.json">Cycle archive index</a> · <a href="../index.html">Main Hub</a></p></section><h2>Production lanes</h2><div class="links">{links}</div><h2>Actual production cards</h2><div class="grid">{''.join(cards)}</div><section class="hero"><strong>Integrity:</strong> PRODUCED means a concrete artifact was generated from a repository-bound source. It is not automatically scientifically verified, commercially sold, or independently validated.</section></main></body></html>"""
    DASHBOARD.write_text(page,encoding="utf-8")
    print(json.dumps({"produced":len(results),"lanes":dict(counts)},ensure_ascii=False))
if __name__=="__main__": main()
