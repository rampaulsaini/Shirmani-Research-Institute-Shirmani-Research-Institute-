import json, hashlib
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/"factory/cloud-storage.json").read_text(encoding="utf-8"))
out=ROOT/"generated"; out.mkdir(exist_ok=True)
files=[]
for p in sorted(out.rglob("*")):
    if p.is_file() and p.name not in {"cloud-sync-manifest.json"}:
        data=p.read_bytes()
        files.append({"path":str(p.relative_to(out)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()})
manifest={
 "generated_at":datetime.now(timezone.utc).isoformat(),
 "mode":"cloud-backup-manifest",
 "primary":cfg["primary"]["provider"],
 "secondary":cfg["secondary"]["provider"],
 "files":files,
 "note":"This stage prepares provenance-safe cloud synchronization. Actual upload requires a connected cloud account/connector."
}
(out/"cloud-sync-manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print("cloud manifest:",len(files),"files")
