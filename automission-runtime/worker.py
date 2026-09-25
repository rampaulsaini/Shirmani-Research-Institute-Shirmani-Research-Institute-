import json
import os
import signal
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

from queue import QueueStore
from sources import discover
from agents import prepare
from router import route_pending
from execution import run
from outcomes import record
from learning import capture_cycle_features, prioritize_score
from connectors import health_all

ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = Path(os.getenv("AUTOMISSION_STATE_DIR", str(Path(__file__).parent / "state")))
STATE_DIR.mkdir(parents=True, exist_ok=True)
DB = STATE_DIR / "automission.db"
INTERVAL = int(os.getenv("AUTOMISSION_HEARTBEAT_SECONDS", "300"))
STALE_PROCESSING_SECONDS = int(os.getenv("AUTOMISSION_STALE_PROCESSING_SECONDS", "1800"))
MAX_CONSECUTIVE_FAILURES = int(os.getenv("AUTOMISSION_MAX_CONSECUTIVE_FAILURES", "3"))
RUN_ONCE = os.getenv("AUTOMISSION_RUN_ONCE", "false").lower() == "true"
stop = False

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def init_db():
    with sqlite3.connect(DB) as db:
        db.execute("""CREATE TABLE IF NOT EXISTS heartbeats
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL,
                      status TEXT NOT NULL, pid INTEGER NOT NULL)""")
        db.execute("""CREATE TABLE IF NOT EXISTS events
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL,
                      kind TEXT NOT NULL, payload TEXT NOT NULL)""")
        db.execute("""CREATE TABLE IF NOT EXISTS execution_receipts
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL,
                      channel TEXT NOT NULL, action TEXT NOT NULL,
                      status TEXT NOT NULL, details TEXT NOT NULL)""")

def emit(kind, payload):
    with sqlite3.connect(DB) as db:
        db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)",
                   (utc_now(), kind, json.dumps(payload, sort_keys=True)))
    print(json.dumps({"ts": utc_now(), "kind": kind, **payload}), flush=True)

def receipt(plan):
    with sqlite3.connect(DB) as db:
        db.execute("""INSERT INTO execution_receipts
            (ts,channel,action,status,details) VALUES(?,?,?,?,?)""",
            (utc_now(), plan.get("channel","unknown"), plan.get("action","review"),
             plan.get("status","UNKNOWN"), json.dumps(plan, sort_keys=True)))

def heartbeat():
    with sqlite3.connect(DB) as db:
        db.execute("INSERT INTO heartbeats(ts,status,pid) VALUES(?,?,?)",
                   (utc_now(), "HEARTBEAT_OK", os.getpid()))
    emit("heartbeat", {"status":"HEARTBEAT_OK"})

def validate_contracts():
    required = [ROOT/"income"/"command-center.json", ROOT/"income"/"agent-registry.json",
                ROOT/"income"/"master-orchestrator.yml", ROOT/"income"/"runtime-contract.json"]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise RuntimeError("missing runtime contracts: " + ", ".join(missing))
    contract = json.loads((ROOT/"income"/"runtime-contract.json").read_text())
    if contract.get("mode") != "continuous":
        raise RuntimeError("runtime contract is not continuous")
    if contract["safety"].get("fabrication_forbidden") is not True:
        raise RuntimeError("fabrication safety gate missing")
    if contract["safety"].get("irreversible_actions_require_authorization") is not True:
        raise RuntimeError("authorization gate missing")

def cycle():
    validate_contracts()
    store = QueueStore(DB)
    recovered = store.recover_stale_processing(STALE_PROCESSING_SECONDS)
    if recovered:
        emit("queue_recovery", {"stale_processing_requeued": recovered})
    adapter_health = health_all()
    accepted = 0
    for raw in discover():
        item = prepare(raw)
        if item:
            store.upsert_opportunity(item)
            accepted += 1

    # Route only the current queue snapshot. Claims are atomic and idempotent,
    # so concurrent workers cannot execute the same opportunity twice.
    candidates = store.pending()
    routed = route_pending(store)
    results = []
    for item in candidates:
        if not store.claim(item):
            continue
        try:
            result = run(item)
            receipt(result)
            status = record(DB, item["id"], result)
            if status == "APPROVAL_REQUIRED":
                store.set_status(item["id"], "APPROVAL_REQUIRED")
            elif status in {"PLANNED", "REJECTED", "REJECTED_NO_INCOME_EVIDENCE"}:
                store.set_status(item["id"], status)
            else:
                store.set_status(item["id"], "EXECUTED")
            store.mark_idempotency(item, status)
            results.append({"id":item["id"],"status":status})
        except Exception as exc:
            store.mark_idempotency(item, "FAILED")
            store.release_for_retry(item["id"])
            results.append({"id":item["id"],"status":"FAILED","error":str(exc)})

    approvals = sum(1 for r in results if r["status"] == "APPROVAL_REQUIRED")
    features = capture_cycle_features(DB, accepted, len(routed), approvals)
    # Verified-income learning remains evidence-first; apply only a bounded,
    # deterministic score boost to future opportunities in channels with
    # evidence-backed historical income.
    for item in store.pending():
        learned_score = prioritize_score(item.get("score", 0), item.get("channel", ""), features)
        if learned_score != float(item.get("score", 0) or 0):
            with sqlite3.connect(DB) as db:
                db.execute("UPDATE opportunities SET score=?, updated_at=? WHERE id=?",
                           (learned_score, utc_now(), item["id"]))
    emit("cycle", {"runtime":"income-command-center","mode":"standalone",
                    "chatgpt_dependency":False,
                    "execution":"discover-verify-route-atomic-claim-adapter-outcome-learn",
                    "adapter_health":adapter_health,
                    "opportunities_accepted":accepted,"routed_actions":len(routed),
                    "outcomes_recorded":len(results),"approval_required":approvals,
                    "queue_depth":len(store.pending()),"learning_features":features})
    heartbeat()

def shutdown(signum, frame):
    global stop
    stop = True
    emit("shutdown", {"signal":signum})

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    init_db()
    consecutive_failures = 0
    while not stop:
        try:
            cycle()
            consecutive_failures = 0
        except Exception as exc:
            consecutive_failures += 1
            emit("runtime_error", {"error":str(exc),"fail_closed":True,"consecutive_failures":consecutive_failures})
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                emit("fatal_runtime_error", {"reason":"restart_threshold_reached","restart_requested":True})
                raise SystemExit(2)
        if RUN_ONCE:
            break
        time.sleep(INTERVAL)
