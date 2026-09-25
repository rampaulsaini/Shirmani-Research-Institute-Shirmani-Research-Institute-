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

ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = Path(os.getenv("AUTOMISSION_STATE_DIR", str(Path(__file__).parent / "state")))
STATE_DIR.mkdir(parents=True, exist_ok=True)
DB = STATE_DIR / "automission.db"
INTERVAL = int(os.getenv("AUTOMISSION_HEARTBEAT_SECONDS", "300"))
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

def emit(kind, payload):
    with sqlite3.connect(DB) as db:
        db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)",
                   (utc_now(), kind, json.dumps(payload, sort_keys=True)))
    print(json.dumps({"ts": utc_now(), "kind": kind, **payload}), flush=True)

def heartbeat():
    with sqlite3.connect(DB) as db:
        db.execute("INSERT INTO heartbeats(ts,status,pid) VALUES(?,?,?)",
                   (utc_now(), "HEARTBEAT_OK", os.getpid()))
    emit("heartbeat", {"status": "HEARTBEAT_OK"})

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
    accepted = 0
    for raw in discover():
        item = prepare(raw)
        if item:
            store.upsert_opportunity(item)
            accepted += 1
    routed = route_pending(store)
    emit("cycle", {"runtime":"income-command-center","mode":"standalone",
                    "chatgpt_dependency":False,"execution":"discover-verify-route",
                    "opportunities_accepted":accepted,"routed_actions":len(routed),
                    "approval_required":sum(1 for r in routed if r["status"]=="APPROVAL_REQUIRED"),
                    "queue_depth":len(store.pending())})
    heartbeat()

def shutdown(signum, frame):
    global stop
    stop = True
    emit("shutdown", {"signal": signum})

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    init_db()
    while not stop:
        try:
            cycle()
        except Exception as exc:
            emit("runtime_error", {"error": str(exc), "fail_closed": True})
        if RUN_ONCE:
            break
        time.sleep(INTERVAL)
