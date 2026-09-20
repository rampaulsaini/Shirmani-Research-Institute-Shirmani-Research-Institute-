"""Durable JSONL queue primitives with retry, leases, and dead-letter tracking."""
import json
import os
import uuid
from pathlib import Path
from datetime import datetime, timezone, timedelta
from agents.language_agents import route as language_route

RETRY_BACKOFF = (30, 120, 300)
MAX_ATTEMPTS = 3

def _now():
    return datetime.now(timezone.utc)

def _iso(dt):
    return dt.isoformat()

def _load(path):
    p = Path(path)
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]

def _save(path, rows):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + ("\n" if rows else ""), encoding="utf-8")
    os.replace(tmp, p)

def enqueue(path, jobs):
    rows = _load(path)
    known = {j.get("job_id") for j in rows}
    now = _iso(_now())
    for job in jobs:
        j = dict(job)
        if not j.get("job_id") or j["job_id"] in known:
            continue
        j.setdefault("status", "pending")
        j.setdefault("attempts", 0)
        j.setdefault("created_at", now)
        rows.append(j)
        known.add(j["job_id"])
    _save(path, rows)

def claim(path, limit=100, lease_seconds=900):
    rows = _load(path)
    now = _now()
    claimed = []
    for job in rows:
        if len(claimed) >= limit:
            break
        status = job.get("status")
        retry_at = job.get("retry_at")
        retry_ready = not retry_at or datetime.fromisoformat(retry_at) <= now
        lease_expired = status == "running" and job.get("lease_expires_at") and datetime.fromisoformat(job["lease_expires_at"]) <= now
        if status in ("pending", "retrying") and retry_ready or lease_expired:
            token = str(uuid.uuid4())
            job["status"] = "running"
            job["lease_token"] = token
            job["started_at"] = _iso(now)
            job["lease_expires_at"] = _iso(now + timedelta(seconds=lease_seconds))
            claimed.append(dict(job))
    _save(path, rows)
    return claimed

def finish(path, job_id, ok, error="", lease_token=None):
    rows = _load(path)
    found = False
    now = _now()
    for job in rows:
        if job.get("job_id") != job_id:
            continue
        if lease_token and job.get("lease_token") != lease_token:
            continue
        found = True
        job["attempts"] = int(job.get("attempts", 0)) + 1
        job["finished_at"] = _iso(now)
        job.pop("lease_expires_at", None)
        if ok:
            job["status"] = "succeeded"
            job.pop("error", None)
            job.pop("retry_at", None)
        elif job["attempts"] < MAX_ATTEMPTS:
            job["status"] = "retrying"
            job["retry_after_seconds"] = RETRY_BACKOFF[min(job["attempts"] - 1, len(RETRY_BACKOFF) - 1)]
            job["retry_at"] = _iso(now + timedelta(seconds=job["retry_after_seconds"]))
            job["error"] = error
        else:
            job["status"] = "failed"
            job["error"] = error
            job["dead_letter"] = True
        break
    if found:
        _save(path, rows)
    return found

def language_job(job_id, text, language):
    r = language_route(language)
    return {"job_id": job_id, "language": language, "agent": r["agent"],
            "queue": r["queue"], "text": text, "status": "pending", "attempts": 0}
