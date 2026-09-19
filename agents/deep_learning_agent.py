"""Free-first Deep Learning Lab control plane.
Uses local deterministic experiments when no model/runtime is available.
"""
import hashlib,json,platform
from datetime import datetime,timezone
from pathlib import Path

def dataset_fingerprint(rows):
    raw="\n".join(str(r.get("text","")) for r in rows).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def plan(rows, experiment="multilingual-representation"):
    return {"experiment":experiment,"dataset_size":len(rows),"dataset_sha256":dataset_fingerprint(rows),
            "runtime":{"python":platform.python_version(),"platform":platform.platform()},
            "status":"planned","compute":"local/free-first",
            "created_at":datetime.now(timezone.utc).isoformat(),
            "policy":"No unlimited compute assumption; results require evaluation."}

def run_local(rows, experiment="text-classification"):
    p=plan(rows,experiment)
    p["result"]={"mode":"deterministic-baseline","metric":"not-applicable-without-labeled-eval-set",
                 "note":"No scientific performance claim is made."}
    p["status"]="completed-baseline"
    return p

def save(result,path):
    Path(path).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
