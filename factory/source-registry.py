#!/usr/bin/env python3
import json, re
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/"factory/repos.json").read_text(encoding="utf-8"))
sources=[]
for full in cfg["repositories"]:
    owner,name=full.split("/",1)
    sources.append({
        "repository":full,
        "role":"hub" if full==cfg.get("hub_repository") else "source",
        "github":"https://github.com/"+full,
        "clone_url":"https://github.com/"+full+".git",
        "expected_inputs":["README.md","docs","research","src","assets","scripts"],
        "ingestion":"skip-generated-output" if full==cfg.get("hub_repository") else "source-scan"
    })
out=ROOT/"generated"; out.mkdir(exist_ok=True)
payload={"generated_at":datetime.now(timezone.utc).isoformat(),"repository_count":len(sources),"repositories":sources}
(out/"source-registry.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(payload,ensure_ascii=False))
