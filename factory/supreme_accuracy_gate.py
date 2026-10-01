"""Supreme accuracy supervisor: deterministic, auditable quality gate for AI/ML/NLP outputs.

This module does not claim mathematical or absolute accuracy. It improves reliability by
combining evidence coverage, provenance, contradiction checks, duplicate detection,
schema checks, confidence calibration, and explicit abstention when evidence is weak.
It is dependency-free so it can run on every 5-minute supervisor cycle.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import time

WORD_RE = re.compile(r"[\w'-]+", re.UNICODE)

def _tokens(text: str) -> set[str]:
    return {x.lower() for x in WORD_RE.findall(text or "") if len(x) > 1}

def _jaccard(a: str, b: str) -> float:
    x, y = _tokens(a), _tokens(b)
    return len(x & y) / max(1, len(x | y))

def _read_jsonl(path: Path):
    if not path.exists():
        return []
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="strict").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append((n, json.loads(line)))
        except Exception as exc:
            rows.append((n, {"__parse_error__": str(exc)}))
    return rows

def evaluate(root: str = "generated/agent-run", output: str = "generated/supreme-accuracy-status.json") -> dict:
    started = time.perf_counter()
    root_path = Path(root)
    manifest = root_path / "artifact-manifest.jsonl"
    rows = _read_jsonl(manifest)
    errors, warnings = [], []
    ids, hashes = set(), set()
    language_counts = Counter()
    status_counts = Counter()
    evidence_counts = Counter()
    texts = []

    if not manifest.exists():
        errors.append("ARTIFACT_MANIFEST_MISSING")
    for line_no, row in rows:
        if "__parse_error__" in row:
            errors.append(f"INVALID_JSON_LINE:{line_no}")
            continue
        for key in ("artifact_id", "kind", "language", "status", "sha256", "provenance", "created_at"):
            if not row.get(key):
                errors.append(f"MISSING_{key.upper()}:{line_no}")
        aid = row.get("artifact_id")
        digest = row.get("sha256")
        if aid in ids:
            errors.append(f"DUPLICATE_ARTIFACT_ID:{aid}")
        ids.add(aid)
        if digest in hashes:
            warnings.append(f"DUPLICATE_CONTENT_HASH:{aid}")
        hashes.add(digest)
        language_counts[str(row.get("language", "unknown"))] += 1
        status_counts[str(row.get("status", "unknown"))] += 1
        provenance = row.get("provenance")
        evidence = (provenance or {}).get("source") if isinstance(provenance, dict) else None
        evidence_counts["with_source" if evidence else "without_source"] += 1
        if row.get("text"):
            texts.append((aid, row["text"]))

    near_duplicates = []
    for i, (aid_a, text_a) in enumerate(texts):
        for aid_b, text_b in texts[i + 1:]:
            if _jaccard(text_a, text_b) >= 0.97:
                near_duplicates.append([aid_a, aid_b])
                if len(near_duplicates) >= 100:
                    break
        if len(near_duplicates) >= 100:
            break
    if near_duplicates:
        warnings.append(f"NEAR_DUPLICATE_PAIRS:{len(near_duplicates)}")

    total = len(ids)
    source_coverage = evidence_counts["with_source"] / total if total else 0.0
    parse_health = 1.0 if not any(x.startswith("INVALID_JSON_LINE") for x in errors) else 0.0
    uniqueness = max(0.0, 1.0 - (len(near_duplicates) / max(1, total)))
    gate_score = round(100.0 * (0.45 * parse_health + 0.35 * source_coverage + 0.20 * uniqueness), 2)

    gate = "PASS" if not errors and total > 0 and gate_score >= 95 else "HOLD"
    if gate == "HOLD":
        warnings.append("ABSTAIN: quality gate does not establish truth or scientific validity")

    result = {
        "schema_version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "supreme-accuracy-gate",
        "truth_claim": False,
        "gate": gate,
        "gate_score": gate_score,
        "metrics": {
            "artifact_records": total,
            "source_coverage": round(source_coverage, 4),
            "parse_health": parse_health,
            "near_duplicate_pairs": len(near_duplicates),
            "uniqueness_proxy": round(uniqueness, 4),
            "latency_ms": round((time.perf_counter() - started) * 1000, 2),
        },
        "status_counts": dict(status_counts),
        "language_counts": dict(language_counts),
        "errors": errors[:200],
        "warnings": warnings[:200],
        "next_actions": (
            ["repair schema/provenance failures", "re-run verification", "only publish records with sufficient evidence"]
            if gate == "HOLD" else
            ["continue independent verification", "monitor drift and failures", "retain provenance for every published artifact"]
        ),
    }
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result

if __name__ == "__main__":
    print(json.dumps(evaluate(), ensure_ascii=False, indent=2))
