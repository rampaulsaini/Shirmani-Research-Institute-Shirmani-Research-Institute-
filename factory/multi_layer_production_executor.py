#!/usr/bin/env python3
"""Execute a bounded slice of the SHIRMANI production queue.

This worker is deliberately production-first: it converts routed module tasks
into durable, provenance-linked production records and visible summaries.
Independent verification is a downstream quality/promotion layer.

The worker is deterministic by default. Optional hosted/accelerated AI, ML, NLP,
or quantum backends may be attached later through explicit adapters; no backend
is claimed unless it actually executes.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
QUEUE = OUT / "production-work-queue.jsonl"
STATE = OUT / "production-execution-state.json"
LEDGER = OUT / "production-results.jsonl"
STATUS = OUT / "production-execution-status.json"
SUMMARY = OUT / "PRODUCTION-EXECUTION.md"

LANE_ACTIONS = {
    "research": "derive a research work-product record: question, source target, evidence route, next production step",
    "ai-ml-nlp": "derive an AI/ML/NLP work-product record: model route, language task, deterministic baseline, acceleration hook",
    "content": "derive a content work-product record: format, source context, production brief, publishing route",
    "platform": "derive a platform work-product record: module surface, user-facing result, integration route, dashboard exposure",
    "economic": "derive an economic work-product record: product/value surface, audience, transaction route, next production action",
    "social-media": "derive a distribution work-product record: channel, content surface, publishing/SEO route, next action",
    "federation": "derive a federation work-product record: repository/module surface, handoff route, continuity action",
    "security-quality": "derive a resilience/quality work-product record: module surface, deterministic check route, remediation action",
    "automation": "derive an automation work-product record: workflow/module, execution route, recurrence, downstream result path",
}

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def stable_id(*parts: str) -> str:
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:24]

def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def read_queue() -> list[dict]:
    if not QUEUE.exists():
        return []
    rows = []
    with QUEUE.open(encoding="utf-8", errors="ignore") as f:
        for line in f:
            try:
                row = json.loads(line)
                if row.get("task_id"):
                    rows.append(row)
            except Exception:
                continue
    return rows

def module_fingerprint(module: str) -> dict:
    path = ROOT / module
    if not path.exists() or not path.is_file():
        return {"exists": False, "bytes": 0, "sha256": None, "headings": []}
    data = path.read_bytes()
    text = data.decode("utf-8", errors="replace")
    headings = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append(stripped[:240])
        if len(headings) >= 8:
            break
    return {
        "exists": True,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "headings": headings,
    }

def make_result(task: dict) -> dict:
    module = task.get("module", "")
    lane = task.get("lane", "automation")
    fp = module_fingerprint(module)
    rid = stable_id(task.get("task_id", ""), fp.get("sha256") or "missing")
    action = LANE_ACTIONS.get(lane, LANE_ACTIONS["automation"])
    return {
        "result_id": rid,
        "generated_at": now(),
        "task_id": task["task_id"],
        "lane": lane,
        "module": module,
        "module_kind": task.get("module_kind"),
        "status": "PRODUCED",
        "production_action": action,
        "work_product": {
            "module_fingerprint": fp,
            "objective": task.get("objective"),
            "source_provenance": module,
            "result_type": "durable-production-record",
        },
        "execution": {
            "deterministic_worker": True,
            "ai_ml_nlp_backend": "optional-adapter",
            "quantum_backend": "optional-adapter-not-claimed",
            "verification": "downstream",
        },
    }

def append_results(results: list[dict]) -> int:
    existing = set()
    if LEDGER.exists():
        with LEDGER.open(encoding="utf-8", errors="ignore") as f:
            for line in f:
                try:
                    existing.add(json.loads(line)["result_id"])
                except Exception:
                    pass
    added = [r for r in results if r["result_id"] not in existing]
    if added:
        with LEDGER.open("a", encoding="utf-8") as f:
            for r in added:
                f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")
    return len(added)

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    queue = read_queue()
    state = load_json(STATE, {
        "version": 1,
        "cursor": 0,
        "cycles": 0,
        "produced_records": 0,
        "failed_module_records": 0,
    })
    capacity = 100
    cursor = int(state.get("cursor", 0))
    if queue and cursor >= len(queue):
        cursor = 0

    selected = queue[cursor:cursor + capacity] if queue else []
    if queue and not selected:
        cursor = 0
        selected = queue[:capacity]

    results = [make_result(t) for t in selected]
    added = append_results(results)
    missing = sum(1 for r in results if not r["work_product"]["module_fingerprint"]["exists"])

    next_cursor = (cursor + len(selected)) % max(1, len(queue))
    state.update({
        "version": 1,
        "generated_at": now(),
        "cycles": int(state.get("cycles", 0)) + 1,
        "cursor": next_cursor,
        "cycle_capacity": capacity,
        "last_cycle_tasks": len(selected),
        "last_cycle_new_results": added,
        "produced_records": int(state.get("produced_records", 0)) + added,
        "failed_module_records": int(state.get("failed_module_records", 0)) + missing,
        "policy": "production-first; independent verification is downstream",
    })
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    lane_counts = {}
    for r in results:
        lane_counts[r["lane"]] = lane_counts.get(r["lane"], 0) + 1

    status = {
        "generated_at": now(),
        "engine": "SHIRMANI Multi-Layer Production Executor",
        "mode": "production-first",
        "queue_total": len(queue),
        "cursor": cursor,
        "cycle_capacity": capacity,
        "last_cycle_tasks": len(selected),
        "last_cycle_new_results": added,
        "total_produced_records": state["produced_records"],
        "missing_source_records": state["failed_module_records"],
        "lane_counts_last_cycle": lane_counts,
        "result_ledger": "generated/production-results.jsonl",
        "verification": "downstream quality/promotion; never manufactured by this worker",
        "ai_ml_nlp": "optional adapter; deterministic production remains available",
        "quantum": "optional adapter contract only; no unsupported quantum execution claim",
    }
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# ꙰ SHIRMANI Production Execution",
        "",
        f"Generated: {status['generated_at']}",
        "",
        "## Production result",
        f"- Queue available: **{len(queue):,}**",
        f"- Tasks executed this cycle: **{len(selected):,}**",
        f"- New durable production records: **{added:,}**",
        f"- Total produced records tracked by worker: **{state['produced_records']:,}**",
        f"- Missing module-source records: **{missing:,}**",
        "",
        "## Multi-level lanes executed",
    ]
    for lane in sorted(LANE_ACTIONS):
        lines.append(f"- **{lane}** — {lane_counts.get(lane, 0)} this cycle")
    lines += [
        "",
        "## Result contract",
        "Each produced record contains a task ID, source module, source fingerprint, lane-specific production action, and downstream verification state.",
        "",
        "The worker does not turn production into VERIFIED status. Verification remains a separate result-quality/promotion stage.",
    ]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    main()
