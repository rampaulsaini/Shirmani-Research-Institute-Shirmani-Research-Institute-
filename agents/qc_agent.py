"""Semantic-ish QC gates that are deterministic and auditable."""
from pathlib import Path
import json,hashlib

def run(root):
    root=Path(root); errors=[]; warnings=[]; seen_ids=set(); seen_hashes=set()
    for p in root.rglob("*"):
        if p.is_file() and not p.read_text(encoding="utf-8",errors="ignore").strip():
            errors.append("empty:"+str(p))
    manifest=root/"artifact-manifest.jsonl"
    if manifest.exists():
        for line_no,line in enumerate(manifest.read_text(encoding="utf-8").splitlines(),1):
            if not line.strip(): continue
            try: r=json.loads(line)
            except Exception: errors.append(f"invalid-json:{manifest}:{line_no}"); continue
            for k in ("artifact_id","kind","language","status","sha256","provenance","created_at"):
                if not r.get(k): errors.append(f"missing:{k}:{line_no}")
            if r.get("artifact_id") in seen_ids: errors.append(f"duplicate-artifact-id:{r.get('artifact_id')}")
            seen_ids.add(r.get("artifact_id"))
            if r.get("sha256") in seen_hashes: warnings.append(f"duplicate-content-hash:{r.get('sha256')}")
            seen_hashes.add(r.get("sha256"))
            if r.get("status")=="verified": warnings.append(f"verified-status-requires-evidence-review:{r.get('artifact_id')}")
    return {"ok":not errors,"errors":errors,"warnings":warnings,
            "artifact_records":len(seen_ids),"policy":"QC is a gate, not independent scientific validation."}
