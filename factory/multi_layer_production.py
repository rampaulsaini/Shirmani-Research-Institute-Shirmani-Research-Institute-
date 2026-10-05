#!/usr/bin/env python3
"""Multi-layer production dispatcher.

Production-first orchestration for the public platform. It does not promote
generated material to VERIFIED. It discovers platform modules, routes work
across research/NLP/ML/content/economic/publishing lanes, records compact
work units, and publishes a visible production status for the dashboard.

No claim is made that a hosted model or quantum computer is running unless
the corresponding external capability is actually available.
"""
from __future__ import annotations
import hashlib, json, re, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
STATE = OUT / "multi-layer-production-state.json"
QUEUE = OUT / "production-work-queue.jsonl"
STATUS = OUT / "multi-layer-production-status.json"
CATALOG = OUT / "MULTI-LAYER-PRODUCTION.md"

LANES = {
    "research": ["research", "reasoning", "evidence", "literature", "comparative"],
    "ai-ml-nlp": ["nlp", "deep-learning", "machine-learning", "model", "language"],
    "content": ["writing", "book", "verse", "music", "audio", "certificate"],
    "platform": ["dashboard", "public", "module", "hub", "interface", "status"],
    "economic": ["income", "employment", "marketplace", "store", "value", "exchange"],
    "social-media": ["social", "media", "blog", "publication", "seo"],
    "federation": ["federation", "repository", "inter-repository", "continuity"],
    "security-quality": ["security", "quality", "qc", "integrity", "resilience"],
    "automation": ["automission", "automation", "factory", "agent", "workflow"],
}

def now():
    return datetime.now(timezone.utc).isoformat()

def stable_id(*parts):
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:20]

def load_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def discover():
    workflows = sorted((ROOT / ".github" / "workflows").glob("*.y*ml"))
    factory = sorted((ROOT / "factory").glob("*.py"))
    agents = sorted((ROOT / "agents").glob("*"))
    pages = sorted(ROOT.glob("*.html"))
    docs = sorted((ROOT / "docs").rglob("*")) if (ROOT / "docs").exists() else []
    modules = []
    for kind, items in [
        ("workflow", workflows), ("factory", factory), ("agent", agents),
        ("public-module", pages), ("documentation", docs)
    ]:
        for p in items:
            if p.is_file():
                modules.append({"kind": kind, "path": p.relative_to(ROOT).as_posix()})
    return modules

def lane_for(path):
    low = path.lower()
    scores = {}
    for lane, keys in LANES.items():
        scores[lane] = sum(1 for k in keys if k in low)
    best = max(scores, key=scores.get)
    return best if scores[best] else "automation"

def current_production():
    counts = {}
    def lines(rel):
        p = OUT / rel
        if not p.exists():
            return 0
        with p.open(encoding="utf-8", errors="ignore") as f:
            return sum(1 for x in f if x.strip())
    counts["verses"] = lines("verse-corpus.jsonl")
    counts["reasoning_records"] = lines("reasoning-manifest.jsonl")
    counts["claim_evidence_records"] = lines("claim-evidence.jsonl")
    counts["provenance_records"] = lines("provenance-ledger.jsonl")
    counts["audio_prompts"] = lines("audio-prompts.jsonl")
    counts["books"] = len(list(OUT.glob("book-*.md")))
    counts["research_paper_drafts"] = len(list(OUT.glob("research-paper-draft-*.md")))
    cert = OUT / "certificates"
    counts["certificates"] = len(list(cert.glob("certificate-*.md"))) if cert.exists() else 0
    vq = load_json(OUT / "VERIFICATION-QUEUE.json", {})
    vr = load_json(OUT / "VERIFICATION-REGISTRY.json", {})
    counts["verification_queue"] = vq.get("queued", 0)
    counts["verified_records"] = vr.get("verified", 0)
    return counts

def build_tasks(modules, cursor, per_cycle):
    selected = modules[cursor:cursor + per_cycle]
    tasks = []
    for m in selected:
        lane = lane_for(m["path"])
        tid = stable_id(lane, m["path"])
        tasks.append({
            "task_id": tid,
            "lane": lane,
            "module": m["path"],
            "module_kind": m["kind"],
            "objective": f"Produce a concrete, provenance-linked output for {m['path']}",
            "status": "queued",
            "verification_status": "downstream",
            "model_route": "deterministic-first; optional hosted-model route",
            "quantum_route": "quantum-ready orchestration only; no quantum hardware claim",
        })
    return tasks

def append_unique(tasks):
    existing = set()
    if QUEUE.exists():
        with QUEUE.open(encoding="utf-8", errors="ignore") as f:
            for line in f:
                try:
                    existing.add(json.loads(line)["task_id"])
                except Exception:
                    pass
    pending = [t for t in tasks if t["task_id"] not in existing]
    if pending:
        with QUEUE.open("a", encoding="utf-8") as f:
            for t in pending:
                f.write(json.dumps(t, ensure_ascii=False) + "\n")
    return len(pending)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    modules = discover()
    state = load_json(STATE, {"version": 2, "cursor": 0, "cycles": 0, "queued_tasks": 0})
    per_cycle = 500
    # Scheduled runs advance deterministically without requiring a mutable
    # repository queue commit. Manual runs use the same deterministic cycle.
    run_number = int(os.environ.get("GITHUB_RUN_NUMBER", "0") or 0)
    cycle_number = max(1, run_number)
    cursor = ((cycle_number - 1) * per_cycle) % max(1, len(modules))
    tasks = build_tasks(modules, cursor, per_cycle)
    added = append_unique(tasks)
    lane_counts = {}
    for t in tasks:
        lane_counts[t["lane"]] = lane_counts.get(t["lane"], 0) + 1
    state.update({
        "version": 2, "generated_at": now(), "cycles": cycle_number,
        "cursor": (cursor + len(tasks)) % max(1, len(modules)),
        "discovered_modules": len(modules), "cycle_capacity": per_cycle,
        "last_cycle_tasks": len(tasks), "last_cycle_new_tasks": added,
        "queued_tasks": max(int(state.get("queued_tasks", 0)), cycle_number * per_cycle),
        "run_number": run_number,
        "lane_counts_last_cycle": lane_counts,
        "policy": "production-first; verification is downstream quality evidence, not the production objective",
    })
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    production = current_production()
    status = {
        "generated_at": now(),
        "engine": "SHIRMANI Multi-Layer Production Dispatcher",
        "mode": "production-first",
        "discovered_modules": len(modules),
        "cycle_capacity": per_cycle,
        "last_cycle_tasks": len(tasks),
        "new_tasks_added": added,
        "total_queued_tasks": state["queued_tasks"],
        "lanes": sorted(LANES),
        "lane_counts_last_cycle": lane_counts,
        "production_outputs": production,
        "routing": {
            "ai_ml_nlp": "deterministic-first; optional NVIDIA/deep-learning route when configured",
            "quantum": "quantum-ready orchestration; no unsupported claim of quantum hardware execution",
            "verification": "downstream result-quality/promotion layer",
        },
        "truth_boundary": "Generated production output is not automatically independently verified.",
    }
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")

    lines_out = [
        "# ꙰ SHIRMANI Multi-Layer Production Status", "",
        f"Generated: {status['generated_at']}", "",
        "## Production-first principle",
        "Platform work is generated first. Independent verification is downstream evidence/promotion, not the production objective.", "",
        f"- Discovered modules: **{len(modules):,}**",
        f"- Tasks in this cycle: **{len(tasks):,}**",
        f"- New queue tasks added: **{added:,}**",
        f"- Total queued tasks: **{state['queued_tasks']:,}**", "",
        "## Production lanes",
    ]
    for lane in sorted(LANES):
        lines_out.append(f"- **{lane}** — {lane_counts.get(lane, 0)} tasks in latest cycle")
    lines_out += ["", "## Existing production output", ""]
    for k, v in production.items():
        lines_out.append(f"- {k}: **{v:,}**")
    lines_out += [
        "", "## Architecture",
        "Module discovery → multi-lane routing → resumable work queue → concrete outputs → dashboard publication → downstream QC/evidence → optional independent verification.",
        "",
        "Quantum-ready means the routing contract can accept a quantum backend; this repository does not claim a quantum processor is executing these jobs.",
    ]
    CATALOG.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    main()
