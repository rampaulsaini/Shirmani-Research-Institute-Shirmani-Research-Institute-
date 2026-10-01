"""Fail-closed, deterministic integrity gate for AI/ML/NLP/Automission outputs.

A PASS means integrity prerequisites are met; it never means truth is proven.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import time

WORD_RE = re.compile(r"[\w'-]+", re.UNICODE)
UNKNOWN_SOURCES = {"", "unknown", "n/a", "na", "none", "null"}
REQUIRED_FIELDS = ("artifact_id", "kind", "language", "status", "sha256", "provenance", "created_at")


def _tokens(text: str) -> set[str]:
    return {x.lower() for x in WORD_RE.findall(text or "") if len(x) > 1}


def _jaccard(a: str, b: str) -> float:
    x, y = _tokens(a), _tokens(b)
    return len(x & y) / max(1, len(x | y))


def _read_jsonl(path: Path):
    if not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="strict").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
            rows.append((number, value if isinstance(value, dict) else {"__invalid_record__": True}))
        except Exception as exc:
            rows.append((number, {"__parse_error__": str(exc)}))
    return rows


def _source_is_usable(row: dict) -> bool:
    source = row.get("source")
    if isinstance(source, str):
        return source.strip().lower() not in UNKNOWN_SOURCES
    if isinstance(source, (list, dict)):
        return bool(source)
    provenance = row.get("provenance")
    if isinstance(provenance, dict):
        for key in ("source", "source_url", "evidence", "evidence_refs"):
            value = provenance.get(key)
            if isinstance(value, str) and value.strip().lower() not in UNKNOWN_SOURCES:
                return True
            if isinstance(value, (list, dict)) and bool(value):
                return True
    return False


def _verification_state(row: dict) -> str:
    value = row.get("verification_status")
    if isinstance(value, str):
        return value.strip().upper()
    provenance = row.get("provenance")
    if isinstance(provenance, dict):
        value = provenance.get("verification")
        if isinstance(value, str):
            return value.strip().upper()
    return "UNKNOWN"


def _explicit_contradiction(row: dict) -> bool:
    for key in ("contradiction", "contradicted", "counter_evidence", "conflict"):
        value = row.get(key)
        if value is True:
            return True
        if isinstance(value, (list, dict)) and bool(value):
            return True
        if isinstance(value, str) and value.strip().lower() in {"true", "yes", "found", "detected"}:
            return True
    return False


def _confidence_is_valid(row: dict) -> bool:
    if "confidence" not in row:
        return True
    try:
        value = float(row["confidence"])
    except (TypeError, ValueError):
        return False
    return 0.0 <= value <= 1.0


def _near_duplicate_pairs(texts: list[tuple[str, str]], limit: int = 100) -> list[list[str]]:
    buckets: dict[tuple[int, int], list[tuple[str, str]]] = {}
    for aid, value in texts:
        normalized = " ".join(value.split()).strip().lower()
        key = (len(normalized), len(_tokens(normalized)))
        buckets.setdefault(key, []).append((aid, normalized))
    pairs: list[list[str]] = []
    for bucket in buckets.values():
        for index, (aid_a, text_a) in enumerate(bucket):
            for aid_b, text_b in bucket[index + 1:]:
                if _jaccard(text_a, text_b) >= 0.97:
                    pairs.append([aid_a, aid_b])
                    if len(pairs) >= limit:
                        return pairs
    return pairs


def evaluate(root: str = "generated/agent-run", output: str = "generated/supreme-accuracy-status.json") -> dict:
    started = time.perf_counter()
    manifest = Path(root) / "artifact-manifest.jsonl"
    rows = _read_jsonl(manifest)
    errors: list[str] = []
    warnings: list[str] = []
    ids: set[str] = set()
    hashes: set[str] = set()
    languages: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    verifications: Counter[str] = Counter()
    texts: list[tuple[str, str]] = []

    if not manifest.exists():
        errors.append("ARTIFACT_MANIFEST_MISSING")

    for line_no, row in rows:
        if "__parse_error__" in row:
            errors.append(f"INVALID_JSON_LINE:{line_no}")
            continue
        if "__invalid_record__" in row:
            errors.append(f"INVALID_RECORD_TYPE:{line_no}")
            continue

        for key in REQUIRED_FIELDS:
            if not row.get(key):
                errors.append(f"MISSING_{key.upper()}:{line_no}")

        aid = row.get("artifact_id")
        digest = row.get("sha256")
        if aid:
            if aid in ids:
                errors.append(f"DUPLICATE_ARTIFACT_ID:{aid}")
            ids.add(aid)
        if isinstance(digest, str) and digest:
            if digest in hashes:
                warnings.append(f"DUPLICATE_CONTENT_HASH:{aid}")
            hashes.add(digest)

        languages[str(row.get("language", "unknown"))] += 1
        statuses[str(row.get("status", "unknown"))] += 1
        verification = _verification_state(row)
        verifications[verification] += 1

        if not _source_is_usable(row):
            warnings.append(f"NO_USABLE_SOURCE:{aid}")
        if not _confidence_is_valid(row):
            errors.append(f"INVALID_CONFIDENCE:{aid}")
        if _explicit_contradiction(row):
            warnings.append(f"CONTRADICTION_OR_COUNTER_EVIDENCE:{aid}")
        if isinstance(row.get("text"), str) and row["text"].strip():
            texts.append((str(aid), row["text"]))

    total = len(ids)
    parse_health = 1.0 if not any(x.startswith(("INVALID_JSON_LINE", "INVALID_RECORD_TYPE")) for x in errors) else 0.0
    unusable_sources = sum(1 for x in warnings if x.startswith("NO_USABLE_SOURCE:"))
    source_coverage = max(0.0, (total - unusable_sources) / total) if total else 0.0
    verified = verifications.get("VERIFIED", 0)
    verification_coverage = verified / total if total else 0.0
    near_duplicates = _near_duplicate_pairs(texts)
    uniqueness = max(0.0, 1.0 - len(near_duplicates) / max(1, total))
    contradiction_count = sum(1 for x in warnings if x.startswith("CONTRADICTION_OR_COUNTER_EVIDENCE:"))
    contradiction_rate = contradiction_count / total if total else 0.0

    integrity_score = round(100.0 * (
        0.30 * parse_health
        + 0.30 * source_coverage
        + 0.20 * verification_coverage
        + 0.15 * uniqueness
        + 0.05 * max(0.0, 1.0 - contradiction_rate)
    ), 2)

    gate = "PASS" if (
        total > 0
        and not errors
        and integrity_score >= 95
        and source_coverage >= 0.95
        and verification_coverage >= 0.95
        and contradiction_rate == 0.0
    ) else "HOLD"

    if gate == "HOLD":
        warnings.append("ABSTAIN: integrity checks do not establish truth or scientific validity")
    if verification_coverage < 0.95:
        warnings.append("FAIL_CLOSED: insufficient independently verified records for publication")
    if source_coverage < 0.95:
        warnings.append("FAIL_CLOSED: insufficient usable evidence/source coverage")

    result = {
        "schema_version": "3.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "supreme-accuracy-integrity-gate",
        "truth_claim": False,
        "gate": gate,
        "integrity_score": integrity_score,
        "metrics": {
            "artifact_records": total,
            "source_coverage": round(source_coverage, 4),
            "independent_verification_coverage": round(verification_coverage, 4),
            "verified_records": verified,
            "parse_health": parse_health,
            "near_duplicate_pairs": len(near_duplicates),
            "uniqueness_proxy": round(uniqueness, 4),
            "contradiction_or_counter_evidence_rate": round(contradiction_rate, 4),
            "latency_ms": round((time.perf_counter() - started) * 1000, 2),
        },
        "status_counts": dict(statuses),
        "verification_counts": dict(verifications),
        "language_counts": dict(languages),
        "errors": errors[:200],
        "warnings": warnings[:200],
        "next_actions": (
            [
                "obtain usable source/evidence for every publishable record",
                "run independent verification before publication",
                "resolve contradiction/counter-evidence findings",
                "publish only after the fail-closed gate passes",
            ]
            if gate == "HOLD"
            else [
                "continue independent verification",
                "monitor drift, duplication and failure rates",
                "retain provenance for every published artifact",
            ]
        ),
    }
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(evaluate(), ensure_ascii=False, indent=2))
