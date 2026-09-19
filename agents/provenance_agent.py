import hashlib

def stable_id(kind, source, text, index=""):
    raw=f"{kind}|{source}|{index}|{text}".encode("utf-8")
    return f"{kind}-{hashlib.sha256(raw).hexdigest()[:20]}"

def record(kind, source, text, index="", status="source-backed", topics=None):
    return {"id":stable_id(kind,source,text,index),"kind":kind,"source":source,
            "source_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "status":status,"topics":topics or [],"text":text}

def validate(r):
    return bool(r.get("id") and r.get("kind") and r.get("source") and r.get("status"))
