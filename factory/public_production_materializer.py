#!/usr/bin/env python3
"""Materialize queued Automission work into concrete public production outputs.

Production-first policy:
- every queued work unit becomes a provenance-linked PRODUCED record;
- lane-specific production packets summarize the actual work burst;
- public pages expose the result surface;
- no production record is automatically promoted to VERIFIED.
"""
from __future__ import annotations
import hashlib, html, json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
QUEUE = GEN / "production-work-queue.jsonl"
RESULTS = GEN / "production-results.jsonl"
DASHBOARD = GEN / "public-production-index.html"
LANE_OUTPUTS = GEN / "production-lane-output.json"

def now():
    return datetime.now(timezone.utc).isoformat()

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def main():
    GEN.mkdir(parents=True, exist_ok=True)
    tasks = []
    if QUEUE.exists():
        for line in QUEUE.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.strip():
                tasks.append(json.loads(line))

    results = []
    lane_groups = defaultdict(list)
    for task in tasks:
        source = ROOT / task["module"]
        source_text = source.read_text(encoding="utf-8", errors="ignore") if source.is_file() else ""
        normalized = " ".join(source_text.split())
        result = {
            "result_id": digest(task["task_id"] + "|production")[:24],
            "task_id": task["task_id"],
            "cycle": task["cycle"],
            "slot": task["slot"],
            "lane": task["lane"],
            "module": task["module"],
            "module_kind": task["module_kind"],
            "produced_at": now(),
            "status": "PRODUCED",
            "verification_status": "PENDING",
            "deliverable": {
                "type": "concrete-production-record",
                "production_action": "source-bound lane output generated",
                "source_fingerprint": digest(source_text)[:16],
                "source_excerpt": normalized[:1000],
                "next_route": "public module -> QC/evidence -> downstream verification",
            },
            "integrity": {
                "source_bound": True,
                "independent_verification": "NOT_YET_PERFORMED",
                "production_is_not_verification": True,
            },
        }
        results.append(result)
        lane_groups[task["lane"]].append(result)

    RESULTS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in results), encoding="utf-8")

    lane_outputs = {}
    for lane, items in sorted(lane_groups.items()):
        lane_outputs[lane] = {
            "status": "PRODUCED",
            "cycle_count": len({r["cycle"] for r in items}),
            "result_count": len(items),
            "task_ids": [r["task_id"] for r in items],
            "source_modules": sorted({r["module"] for r in items}),
            "artifact_policy": "source-bound production record; downstream verification required",
        }
    LANE_OUTPUTS.write_text(json.dumps({
        "generated_at": now(),
        "lane_count": len(lane_outputs),
        "total_results": len(results),
        "lanes": lane_outputs,
        "verification_boundary": "PRODUCED is not VERIFIED",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cards = []
    for r in results[:100]:
        excerpt = html.escape(r["deliverable"]["source_excerpt"][:450])
        cards.append(f"<article><h3>{html.escape(r['lane'].upper())}</h3><small>{html.escape(r['module'])}</small><p>{excerpt}</p><b>PRODUCED</b> · verification downstream</article>")

    lane_cards = []
    for lane, info in sorted(lane_outputs.items()):
        lane_cards.append(f"<article><h3>{html.escape(lane.upper())}</h3><div class='metric'>{info['result_count']:,}</div><small>concrete results in current queue surface</small></article>")

    status_path = GEN / "multi-layer-production-status.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    status["last_cycle_concrete_results"] = len(results)
    status["production_outputs"]["concrete_results_this_cycle"] = len(results)
    status["production_outputs"]["lane_packets"] = len(lane_outputs)
    status["lane_output_counts"] = {k: v["result_count"] for k, v in sorted(lane_outputs.items())}
    status["artifacts"] = [
        "generated/production-results.jsonl",
        "generated/production-work-queue.jsonl",
        "generated/production-lane-output.json",
        "generated/multi-layer-production-status.json",
    ]
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    page = f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SHIRMANI Public Production</title>
<style>body{{margin:0;background:#0b0d14;color:#f5f5f5;font-family:system-ui,sans-serif;line-height:1.5}}main{{max-width:1250px;margin:auto;padding:24px}}h1,h2{{color:#d4af37}}.hero,article{{background:rgba(255,255,255,.05);border:1px solid rgba(212,175,55,.25);border-radius:14px;padding:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:16px 0}}.metric{{font-size:1.8rem;font-weight:800;color:#d4af37}}small{{color:#aeb5c2}}b{{color:#6ee7b7}}a{{color:#d4af37}}</style></head><body><main>
<section class="hero"><h1>꙰ SHIRMANI Public Production</h1><p><strong>Production-first Automission:</strong> platform work becomes concrete, traceable result records before downstream quality/verification.</p><h2>{len(results):,} concrete results in the current production surface</h2><p><strong>{len(lane_outputs)}</strong> production lanes materialized. Verification state: <strong>DOWNSTREAM</strong> — produced output is not automatically verified.</p><p><a href="multi-layer-production-status.json">Status JSON</a> · <a href="production-results.jsonl">Result stream</a> · <a href="production-lane-output.json">Lane packets</a> · <a href="production-work-queue.jsonl">Work queue</a> · <a href="../factory-dashboard.html">Factory Dashboard</a> · <a href="../index.html">Main Hub</a></p></section>
<h2>Lane production</h2><div class="grid">{''.join(lane_cards)}</div><h2>Latest production results (first 100)</h2><div class="grid">{''.join(cards)}</div>
</main></body></html>"""
    DASHBOARD.write_text(page, encoding="utf-8")
    print(json.dumps({"produced": len(results), "lane_packets": len(lane_outputs), "lanes": {k: v["result_count"] for k, v in sorted(lane_outputs.items())}}, ensure_ascii=False))

if __name__ == "__main__":
    main()
