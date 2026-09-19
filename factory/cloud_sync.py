import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/"factory/cloud-storage.json").read_text(encoding="utf-8"))
out=ROOT/"generated"; out.mkdir(exist_ok=True)
manifest_path=out/"cloud-sync-manifest.json"
previous={}
if manifest_path.exists():
    try:
        previous=json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        previous={}

files=[]
for p in sorted(out.rglob("*")):
    if p.is_file() and p.name not in {"cloud-sync-manifest.json"}:
        data=p.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        files.append({
            "path":str(p.relative_to(out)),
            "bytes":len(data),
            "sha256":digest
        })

old={x["path"]:x for x in previous.get("files",[])}
changed=[x for x in files if old.get(x["path"],{}).get("sha256") != x["sha256"]]
unchanged=[x for x in files if old.get(x["path"],{}).get("sha256") == x["sha256"]]

manifest={
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "mode":"incremental-cloud-backup-manifest",
    "primary":cfg["primary"]["provider"],
    "secondary":cfg["secondary"]["provider"],
    "total_files":len(files),
    "changed_files":len(changed),
    "unchanged_files":len(unchanged),
    "changed_paths":[x["path"] for x in changed],
    "files":files,
    "upload_policy":"Upload only changed files after QC; deduplicate by SHA-256; preserve provenance.",
    "note":"Actual external-cloud upload requires a connected cloud account/connector."
}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print("cloud sync manifest:",len(files),"files;",len(changed),"changed")
