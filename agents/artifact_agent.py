"""Artifact hashing and manifest records."""
import hashlib,json
from datetime import datetime,timezone
def manifest_record(kind,language,text,source_ids,generator,status="draft",extra=None):
    return {"artifact_id":hashlib.sha256((kind+"|"+language+"|"+"|".join(map(str,source_ids))+"|"+text).encode()).hexdigest()[:24],"kind":kind,"language":language,"status":status,"sha256":hashlib.sha256(text.encode("utf-8")).hexdigest(),"created_at":datetime.now(timezone.utc).isoformat(),"provenance":{"source_ids":list(source_ids),"generator":generator,"verification":"required"},**(extra or {})}
def append(path,record):
    with open(path,"a",encoding="utf-8") as f: f.write(json.dumps(record,ensure_ascii=False)+"\n")
