"""Durable JSONL queue primitives with retries, leases, and dead-letter handling.

The queue uses atomic replacement for persistence and a small OS lock for
single-writer claim/finish operations. Workers receive immutable claim records
and must return the lease token when finishing a running job.
"""
import json
import os
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path

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
    return [
        json.loads(line)
        for line in p.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _save(path, rows):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    payload = "\n".join(
        json.dumps(row, ensure_ascii=False) for row in rows
    )
    tmp.write_text(payload + ("\n" if rows else ""), encoding="utf-8")
    os.replace(tmp, p)


@contextmanager
def _queue_lock(path):
    """Serialize queue mutations on platforms supporting fcntl."""
    lock_path = Path(path).with_suffix(Path(path).suffix + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        try:
            import fcntl
        except ImportError:
            fcntl = None
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        try:
            if fcntl is not None:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            handle.close()


def enqueue(path, jobs):
    """Append new jobs idempotently by job_id."""
    with _queue_lock(path):
        rows = _load(path)
        known = {job.get("job_id") for job in rows}
        now = _iso(_now())
        for job in jobs:
            candidate = dict(job)
            job_id = candidate.get("job_id")
            if not job_id or job_id in known:
                continue
            candidate.setdefault("status", "pending")
            candidate.setdefault("attempts", 0)
            candidate.setdefault("created_at", now)
            rows.append(candidate)
            known.add(job_id)
        _save(path, rows)


def _ready(job, now):
    status = job.get("status")
    if status == "pending":
        return True
    if status == "retrying":
        retry_at = job.get("retry_at")
        return not retry_at or datetime.fromisoformat(retry_at) <= now
    if status == "running":
        expiry = job.get("lease_expires_at")
        return bool(expiry) and datetime.fromisoformat(expiry) <= now
    return False


def claim(path, limit=100, lease_seconds=900):
    """Claim pending/retry-ready jobs or recover expired leases."""
    if limit <= 0:
        return []
    with _queue_lock(path):
        rows = _load(path)
        now = _now()
        claimed = []
        for job in rows:
            if len(claimed) >= limit or not _ready(job, now):
                continue
            token = str(uuid.uuid4())
            job["status"] = "running"
            job["lease_token"] = token
            job["started_at"] = _iso(now)
            job["lease_expires_at"] = _iso(
                now + timedelta(seconds=lease_seconds)
            )
            claimed.append(dict(job))
        _save(path, rows)
        return claimed


def finish(path, job_id, ok, error="", lease_token=None):
    """Finish a claimed job; reject stale or tokenless running completions."""
    with _queue_lock(path):
        rows = _load(path)
        now = _now()
        for job in rows:
            if job.get("job_id") != job_id:
                continue
            if job.get("status") == "running":
                if not lease_token or job.get("lease_token") != lease_token:
                    return False
            job["attempts"] = int(job.get("attempts", 0)) + 1
            job["finished_at"] = _iso(now)
            job.pop("lease_expires_at", None)
            job.pop("lease_token", None)

            if ok:
                job["status"] = "succeeded"
                job.pop("error", None)
                job.pop("retry_at", None)
                job.pop("retry_after_seconds", None)
            elif job["attempts"] < MAX_ATTEMPTS:
                delay = RETRY_BACKOFF[job["attempts"] - 1]
                job["status"] = "retrying"
                job["retry_after_seconds"] = delay
                job["retry_at"] = _iso(now + timedelta(seconds=delay))
                job["error"] = error
            else:
                job["status"] = "failed"
                job["error"] = error
                job["dead_letter"] = True
                job.pop("retry_at", None)
            _save(path, rows)
            return True
        return False


def language_job(job_id, text, language):
    route = language_route(language)
    return {
        "job_id": job_id,
        "language": language,
        "agent": route["agent"],
        "queue": route["queue"],
        "text": text,
        "status": "pending",
        "attempts": 0,
    }
