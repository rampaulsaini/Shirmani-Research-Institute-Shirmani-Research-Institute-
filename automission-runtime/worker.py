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
from master_automission import MasterAutomission
from factory_cycle import load_requests, run_factory_cycle
from education_factory import build_program, validate_program
from justice_factory import build_case_plan, validate_case_plan
from task_ledger import AgentTaskLedger
from master_learning import capture_master_intelligence, write_intelligence, capture_fulfillment_intelligence
from master_dashboard import snapshot as master_dashboard_snapshot

ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = Path(os.getenv("AUTOMISSION_STATE_DIR", str(Path(__file__).parent / "state")))
STATE_DIR.mkdir(parents=True, exist_ok=True)
DB = STATE_DIR / "automission.db"
INTERVAL = int(os.getenv("AUTOMISSION_HEARTBEAT_SECONDS", "300"))
STALE_PROCESSING_SECONDS = int(os.getenv("AUTOMISSION_STALE_PROCESSING_SECONDS", "1800"))
MAX_CONSECUTIVE_FAILURES = int(os.getenv("AUTOMISSION_MAX_CONSECUTIVE_FAILURES", "3"))
PRODUCT_REQUEST_FILE = os.getenv("AUTOMISSION_PRODUCT_REQUEST_FILE", "")
EDUCATION_REQUEST_FILE = os.getenv("AUTOMISSION_EDUCATION_REQUEST_FILE", "")
JUSTICE_REQUEST_FILE = os.getenv("AUTOMISSION_JUSTICE_REQUEST_FILE", "")
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

def run_master_orchestration():
    master = MasterAutomission()
    master.register("research-cycle", "research", "research-orchestrator", "research")
    master.register("education-cycle", "education", "education-orchestrator", "build_program")
    master.register("product-cycle", "products", "product-orchestrator", "create_blueprint")
    master.register("qc-cycle", "qc", "quality-agent", "quality_control")
    master.register("justice-cycle", "research", "legal-access-orchestrator", "case_analysis")
    fulfillment_db = STATE_DIR / "fulfillment.db"
    fulfillment_learning = capture_fulfillment_intelligence(fulfillment_db)
    planning_intelligence = {"fulfillment_learning": fulfillment_learning}
    plan = master.plan(planning_intelligence)
    routed = master.route(planning_intelligence)
    ledger = AgentTaskLedger(STATE_DIR / "master-task-ledger.db")
    for task, route in zip(master.tasks, routed):
        key = ledger.record(task)
        ledger.set_status(key, route["status"])

    product_results = []
    if PRODUCT_REQUEST_FILE:
        requests = load_requests(Path(PRODUCT_REQUEST_FILE))
        from product_catalog import ProductCatalog
        catalog = ProductCatalog(STATE_DIR / "product-factory.db")
        product_results = run_factory_cycle(catalog, requests)

    education_results = []
    if EDUCATION_REQUEST_FILE:
        requests = load_requests(Path(EDUCATION_REQUEST_FILE))
        for request in requests:
            try:
                program = build_program(**request)
                validate_program(program)
                education_results.append({"status": "PROGRAM_READY", "program_hash": program["program_hash"]})
            except (TypeError, ValueError) as exc:
                education_results.append({"status": "REJECTED", "reason": str(exc)})

    justice_results = []
    if JUSTICE_REQUEST_FILE:
        requests = load_requests(Path(JUSTICE_REQUEST_FILE))
        for request in requests:
            try:
                case_plan = build_case_plan(**request)
                validate_case_plan(case_plan)
                justice_results.append({"status": "CASE_PLAN_READY", "plan_hash": case_plan["plan_hash"], "human_review_required": True, "binding_judgment": False})
            except (TypeError, ValueError) as exc:
                justice_results.append({"status": "REJECTED", "reason": str(exc)})

    intelligence = capture_master_intelligence(
        DB, STATE_DIR / "master-task-ledger.db",
        STATE_DIR / "product-factory.db",
    )
    intelligence["fulfillment_learning"] = fulfillment_learning
    write_intelligence(STATE_DIR / "master-intelligence.db", intelligence)
    dashboard = master_dashboard_snapshot(
        DB, STATE_DIR / "master-task-ledger.db",
        STATE_DIR / "product-factory.db",
        fulfillment_db=fulfillment_db,
    )

    emit("master_automission", {
        "status": "ORCHESTRATED",
        "task_count": plan["task_count"],
        "routes": routed,
        "product_results": product_results,
        "education_results": education_results,
        "justice_results": justice_results,
        "external_irreversible_actions": "authorization_required",
        "task_ledger": ledger.snapshot(),
        "master_intelligence": intelligence,
        "dashboard": dashboard,
    })

def cycle():
    validate_contracts()
    run_master_orchestration()
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
        payload = json.loads(item.get("payload", "{}") or "{}")
        currency = item.get("currency") or payload.get("currency")
        learned_score = prioritize_score(
            item.get("score", 0), item.get("channel", ""), features, currency
        )
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
