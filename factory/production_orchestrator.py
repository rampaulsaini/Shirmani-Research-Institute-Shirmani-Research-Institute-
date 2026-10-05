#!/usr/bin/env python3
"""Production-first multi-layer Automission orchestration and platform telemetry."""
from pathlib import Path
from datetime import datetime, timezone
import json, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"; OUT.mkdir(exist_ok=True)

def load(path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return default

def lines(path):
    return sum(1 for x in path.open(encoding="utf-8",errors="ignore") if x.strip()) if path.exists() else 0

def counts():
    return {
      "verses": lines(OUT/"verse-corpus.jsonl"),
      "research_papers": len(list(OUT.glob("research-paper-draft-*.md"))),
      "digital_books": len(list(OUT.glob("book-*.md"))),
      "certificates": len(list((OUT/"certificates").glob("certificate-*.md"))) if (OUT/"certificates").exists() else 0,
      "audio_prompts": lines(OUT/"audio-prompts.jsonl"),
    }

def modules():
    out=[]
    for p in sorted(ROOT.rglob("*.html")):
        if ".git" in p.parts: continue
        s=p.read_text(encoding="utf-8",errors="ignore"); low=s.lower()
        markers=[x for x in ("coming soon","todo","placeholder","under construction","empty","no content") if x in low]
        out.append({
          "module":str(p.relative_to(ROOT)),
          "bytes":p.stat().st_size,
          "links":len(re.findall(r"<a\b[^>]*href=",s,re.I)),
          "scripts":len(re.findall(r"<script\b",s,re.I)),
          "forms":len(re.findall(r"<form\b",s,re.I)),
          "expansion_markers":markers,
          "production_status":"EXPAND" if markers else "ACTIVE"
        })
    return out

def main():
    now=datetime.now(timezone.utc).isoformat()
    repos=load(ROOT/"factory/repos.json",{})
    reg=load(ROOT/"factory/agent-registry.json",{})
    agents=load(ROOT/"factory/agents.json",{})
    targets=repos.get("product_targets",{})
    done=counts(); mods=modules()
    backlog={}
    for k,t in targets.items():
        n=int(t); d=int(done.get(k,0))
        backlog[k]={"completed":d,"target":n,"remaining":max(0,n-d),
                    "completion_pct":round(min(100,d/n*100),4) if n else 100}
    lanes=[
      ("source-intelligence","source"),("research-production","research"),
      ("knowledge-structure","concept-mapper"),("mahagranth-production","mahagranth"),
      ("verse-production","verse"),("multilingual-production","translation"),
      ("audio-production","audio"),("product-packaging","product"),
      ("marketing-discovery","marketing"),("platform-module-expansion","publisher"),
      ("deep-learning","deep-learning-lab"),("optimization-quantum","job-router"),
      ("quality-downstream","quality"),("continuity","archive")
    ]
    packets=[]
    for i,m in enumerate(mods,1):
        packets.append({"task_id":f"MODULE-{i:04d}","lane":"platform-module-expansion",
                        "agent":"publisher","module":m["module"],
                        "priority":"P1" if m["production_status"]=="EXPAND" else "P2",
                        "status":"QUEUED"})
    for lane,agent in lanes:
        packets.append({"task_id":f"LANE-{lane}","lane":lane,"agent":agent,
                        "priority":"P0","status":"QUEUED"})
    dashboard={
      "schema_version":"1.0","generated_at":now,
      "mode":"production-first-multi-layer-automission",
      "platform":{"html_modules":len(mods),
        "modules_marked_for_expansion":sum(m["production_status"]=="EXPAND" for m in mods),
        "repository_count_configured":len(repos.get("repositories",[])),
        "agent_registry_count":len(reg.get("agents",[])),
        "factory_agent_count":len(agents.get("agents",[]))},
      "production":{"counts":done,"targets":targets,"backlog":backlog,
                    "work_packets_this_cycle":len(packets)},
      "lanes":[{"lane":x,"agent":a,"status":"ACTIVE"} for x,a in lanes],
      "routing":{"ai_ml_nlp":"free-first deterministic orchestration; optional external model adapter",
                 "nvidia":"optional when NVIDIA_API_KEY exists",
                 "quantum":"optimization/simulation label only; no quantum-hardware claim"},
      "verification_boundary":{"production_is_not_verification":True,
        "role":"downstream quality gate",
        "generated_research_is_draft_until_independently_verified":True}
    }
    (OUT/"production-dashboard.json").write_text(json.dumps(dashboard,ensure_ascii=False,indent=2),encoding="utf-8")
    (OUT/"platform-module-inventory.json").write_text(json.dumps({"generated_at":now,"modules":mods},ensure_ascii=False,indent=2),encoding="utf-8")
    with (OUT/"production-ledger.jsonl").open("w",encoding="utf-8") as f:
        for p in packets: f.write(json.dumps(p,ensure_ascii=False)+"\n")
    rows="".join(f"<tr><td>{k}</td><td>{v['completed']:,}</td><td>{v['target']:,}</td><td>{v['remaining']:,}</td><td>{v['completion_pct']:.2f}%</td></tr>" for k,v in backlog.items())
    lane_html="".join(f"<li>{a} — {x}</li>" for x,a in lanes)
    html=f"""<!doctype html><html lang="hi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SHIRMANI Supreme Production Dashboard</title>
<style>body{{font-family:system-ui;max-width:1200px;margin:auto;padding:24px;background:#10131a;color:#eee}}h1,h2{{color:#f0c75e}}.card{{background:#181d27;border:1px solid #303846;border-radius:14px;padding:18px;margin:14px 0}}table{{width:100%;border-collapse:collapse}}th,td{{padding:9px;border-bottom:1px solid #303846;text-align:left}}a{{color:#8fd3ff}}</style>
<h1>꙰ SHIRMANI Supreme Production Dashboard</h1><div class="card"><b>PRODUCTION-FIRST AUTOMISSION</b><p>Generated {now}. Production and verification are separate layers.</p></div>
<div class="card"><h2>Production Backlog</h2><table><tr><th>Product</th><th>Done</th><th>Target</th><th>Remaining</th><th>Progress</th></tr>{rows}</table></div>
<div class="card"><h2>Platform Expansion</h2><p>HTML modules: <b>{len(mods)}</b>; expansion markers: <b>{sum(m["production_status"]=="EXPAND" for m in mods)}</b>; work packets: <b>{len(packets)}</b>.</p></div>
<div class="card"><h2>Multi-layer lanes</h2><ul>{lane_html}</ul></div>
<div class="card"><h2>Execution boundary</h2><p>AI/ML/NLP is free-first/deterministic unless an external adapter is configured. The quantum lane is optimization/simulation only unless a real backend is configured.</p>
<p><a href="generated/production-dashboard.json">JSON</a> · <a href="generated/production-ledger.jsonl">Ledger</a> · <a href="generated/platform-module-inventory.json">Module inventory</a></p></div>"""
    (ROOT/"production-dashboard.html").write_text(html,encoding="utf-8")
    print(json.dumps({"html_modules":len(mods),"expansion_markers":sum(m["production_status"]=="EXPAND" for m in mods),
      "work_packets":len(packets),"backlog_remaining":sum(v["remaining"] for v in backlog.values())},ensure_ascii=False))
if __name__=="__main__": main()
