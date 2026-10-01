#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(os.environ.get("GITHUB_WORKSPACE",".")).resolve()
OUT=ROOT/"artifacts"; OUT.mkdir(exist_ok=True)
IGNORE={".git","node_modules","__pycache__",".venv","venv","artifacts"}

all_files=[p for p in ROOT.rglob("*") if p.is_file() and not any(x in IGNORE for x in p.parts)]
text_files=[p for p in all_files if p.suffix.lower() in {".md",".yml",".yaml",".json",".py",".js",".ts",".txt"}]
workflows=list((ROOT/".github/workflows").glob("*.yml"))+list((ROOT/".github/workflows").glob("*.yaml")) if (ROOT/".github/workflows").exists() else []

terms=("nlp","natural language","semantic","embedding","transformer","automission","automation","agent","workflow")
signals={t:0 for t in terms}
secret_patterns=(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}",
                 r"(?i)(secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}")
secret_hits=[]
for p in text_files:
    try: s=p.read_text(errors="ignore").lower()
    except Exception: continue
    for t in signals: signals[t]+=s.count(t)
    if any(re.search(x,s) for x in secret_patterns): secret_hits.append(str(p.relative_to(ROOT)))

checks={
 "repository_files_discovered":bool(all_files),
 "github_actions_present":(ROOT/".github/workflows").exists(),
 "workflow_present":bool(workflows),
 "automation_signal_present":sum(signals[t] for t in terms[5:])>0,
 "nlp_signal_present":sum(signals[t] for t in terms[:5])>0,
 "no_obvious_hardcoded_secret_pattern":not secret_hits,
}
score=round(100*sum(checks.values())/len(checks),1)
inventory="\n".join(sorted(str(p.relative_to(ROOT)) for p in all_files))
report={"schema":"shirmani.supreme-nlp-automission.audit.v1",
"generated_at":datetime.now(timezone.utc).isoformat(),
"inventory":{"files":len(all_files),"workflows":[p.name for p in workflows]},
"signals":signals,"checks":checks,"health_signal_percent":score,
"secret_pattern_files":sorted(set(secret_hits)),
"inventory_sha256":hashlib.sha256(inventory.encode()).hexdigest(),
"scientific_boundary":"Signals and model outputs require empirical validation; this audit does not establish subjective experience, consciousness, or quantum claims."}
(OUT/"supreme-nlp-audit.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report,indent=2,ensure_ascii=False))
