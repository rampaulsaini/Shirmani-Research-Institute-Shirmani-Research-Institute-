#!/usr/bin/env python3
"""Small atomic state store for resumable factory production."""
import json
import os
from pathlib import Path
from datetime import datetime, timezone

DEFAULT = {
    "version": 1,
    "status": "initialized",
    "completed": {},
    "updated_at": None,
}

def load(path):
    p = Path(path)
    if not p.exists():
        return dict(DEFAULT)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("state must be an object")
        data.setdefault("completed", {})
        data.setdefault("version", 1)
        return data
    except (OSError, json.JSONDecodeError, ValueError):
        return dict(DEFAULT)

def save(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = dict(data)
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, p)

def mark_completed(path, kind, number):
    data = load(path)
    key = str(kind)
    done = set(data.get("completed", {}).get(key, []))
    done.add(int(number))
    data["completed"][key] = sorted(done)
    data["status"] = "running"
    save(path, data)
    return data
