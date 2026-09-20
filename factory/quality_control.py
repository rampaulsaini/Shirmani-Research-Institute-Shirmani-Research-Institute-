#!/usr/bin/env python3
"""Deterministic QC for source, generated and reasoning records.

The QC layer is provider-free and fail-closed: it validates structure,
provenance, hashes, framework alignment, method traces and review gates.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SOURCE = ("id", "repository", "branch", "path", "source_hash", "text", "source_type", "collected_at")
REQUIRED_GENERATED = ("id", "agent", "source_ids", "content_hash", "status", "text")
VALID_STATUS = {"draft", "review", "verified", "published", "rejected"}
VALID_EVIDENCE_STATUS = {"requires_independent_verification", "independently_verified", "insufficient_evidence"}

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load_framework():
    return json.loads((ROOT / "factory" / "shirmani-framework.json").read_text(encoding="utf-8"))

def check_jsonl(path, required, hash_field, unique_hash=True):
    seen, errors, count = set(), [], 0
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            count += 1
            try:
                record = json.loads(line)
            except Exception as exc:
                errors.append({"line": line_no, "error": f"invalid_json:{exc}"})
                continue
            for key in required:
                if key not in record:
                    errors.append({"line": line_no, "error": f"missing:{key}"})
            h = record.get(hash_field)
            if unique_hash and h:
                if h in seen:
                    errors.append({"line": line_no, "error": f"duplicate_{hash_field}"})
                seen.add(h)
            if "text" in record and not isinstance(record["text"], str):
                errors.append({"line": line_no, "error": "text_not_string"})
    return {"records": count, "unique_hashes": len(seen), "errors": errors}

def check_source_integrity(path):
    result = check_jsonl(path, REQUIRED_SOURCE, "source_hash", unique_hash=False)
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                if r.get("source_hash") != sha(r["text"]):
                    result["errors"].append({"line": line_no, "error": "source_hash_mismatch"})
            except Exception:
                pass
    return result

def check_generated(path, framework):
    result = check_jsonl(path, REQUIRED_GENERATED, "content_hash")
    allowed_classes = set(framework.get("claim_classes", []))
    allowed_methods = set(framework.get("method_stack", []))
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                if r.get("status") not in VALID_STATUS:
                    result["errors"].append({"line": line_no, "error": "invalid_status"})
                if not isinstance(r.get("source_ids"), list) or not r.get("source_ids"):
                    result["errors"].append({"line": line_no, "error": "missing_source_ids"})
                if r.get("content_hash") != sha(r.get("text", "")):
                    result["errors"].append({"line": line_no, "error": "content_hash_mismatch"})
                if r.get("claim_class") not in allowed_classes:
                    result["errors"].append({"line": line_no, "error": "invalid_generated_claim_class"})
                methods = r.get("method_trace")
                if not isinstance(methods, list) or not methods:
                    result["errors"].append({"line": line_no, "error": "missing_generated_method_trace"})
                elif sorted(set(methods) - allowed_methods):
                    result["errors"].append({"line": line_no, "error": "unknown_generated_method_trace"})
                if r.get("evidence_status") not in VALID_EVIDENCE_STATUS:
                    result["errors"].append({"line": line_no, "error": "invalid_generated_evidence_status"})
                if r.get("human_review_required") is not True:
                    result["errors"].append({"line": line_no, "error": "generated_human_review_not_required"})
                if (r.get("framework") or {}).get("framework_id") != framework.get("framework_id"):
                    result["errors"].append({"line": line_no, "error": "generated_framework_id_mismatch"})
            except Exception as exc:
                result["errors"].append({"line": line_no, "error": f"generated_record_error:{exc}"})
    return result

def build_artifact_index(generated):
    index = {}
    verse = generated / "verse-corpus.jsonl"
    if verse.exists():
        with open(verse, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        r = json.loads(line)
                        index[("verse", str(r.get("id")))] = r.get("text", "")
                    except Exception:
                        pass
    for path in sorted(generated.glob("book-*.md")):
        index[("book", path.stem)] = path.read_text(encoding="utf-8")
    for path in sorted(generated.glob("research-paper-draft-*.md")):
        index[("research-paper", path.stem)] = path.read_text(encoding="utf-8")
    return index

def check_reasoning(path, generated, framework):
    result = check_jsonl(path, ("artifact_id", "kind", "content_sha256", "source_ids", "reasoning",
                                "claim_class", "method_trace", "evidence_status",
                                "human_review_required", "verification_questions"), "content_sha256")
    allowed_classes = set(framework.get("claim_classes", []))
    allowed_methods = set(framework.get("method_stack", []))
    artifacts = build_artifact_index(generated)
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
                reasoning = r.get("reasoning") or {}
                text = artifacts.get((r.get("kind"), str(r.get("artifact_id"))))
                if text is None:
                    result["errors"].append({"line": line_no, "error": "artifact_not_found"})
                elif r.get("content_sha256") != sha(text):
                    result["errors"].append({"line": line_no, "error": "content_sha256_mismatch"})
                if r.get("claim_class") not in allowed_classes:
                    result["errors"].append({"line": line_no, "error": "invalid_claim_class"})
                if reasoning.get("claim_class") not in allowed_classes:
                    result["errors"].append({"line": line_no, "error": "reasoning_invalid_claim_class"})
                if r.get("evidence_status") not in VALID_EVIDENCE_STATUS:
                    result["errors"].append({"line": line_no, "error": "invalid_evidence_status"})
                methods = r.get("method_trace")
                if not isinstance(methods, list) or not methods:
                    result["errors"].append({"line": line_no, "error": "missing_method_trace"})
                elif sorted(set(methods) - allowed_methods):
                    result["errors"].append({"line": line_no, "error": "unknown_method_trace"})
                if not isinstance(r.get("verification_questions"), list) or not r.get("verification_questions"):
                    result["errors"].append({"line": line_no, "error": "missing_verification_questions"})
                if r.get("human_review_required") is not True:
                    result["errors"].append({"line": line_no, "error": "human_review_not_required"})
                if not isinstance(r.get("source_ids"), list) or not r.get("source_ids"):
                    result["errors"].append({"line": line_no, "error": "missing_reasoning_source_ids"})
                if reasoning.get("method_trace") != r.get("method_trace"):
                    result["errors"].append({"line": line_no, "error": "method_trace_mismatch"})
                if reasoning.get("claim_class") != r.get("claim_class"):
                    result["errors"].append({"line": line_no, "error": "claim_class_mismatch"})
                if reasoning.get("framework_id") != framework.get("framework_id"):
                    result["errors"].append({"line": line_no, "error": "framework_id_mismatch"})
                if reasoning.get("evidence_status") != r.get("evidence_status"):
                    result["errors"].append({"line": line_no, "error": "evidence_status_mismatch"})
                if reasoning.get("source_ids") != r.get("source_ids"):
                    result["errors"].append({"line": line_no, "error": "source_ids_mismatch"})
                if reasoning.get("human_review_required") is not True:
                    result["errors"].append({"line": line_no, "error": "reasoning_human_review_not_required"})
            except Exception as exc:
                result["errors"].append({"line": line_no, "error": f"reasoning_record_error:{exc}"})
    return result

def check_claim_evidence(path):
    result = {"records": 0, "unique_ids": 0, "errors": []}
    seen = set()
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            result["records"] += 1
            try:
                r = json.loads(line)
            except Exception as exc:
                result["errors"].append({"line": line_no, "error": f"invalid_claim_evidence_json:{exc}"})
                continue
            for key in ("id", "claim", "definitions", "source", "evidence",
                        "formulation", "countercases", "verification",
                        "conclusion", "provenance"):
                if key not in r:
                    result["errors"].append({"line": line_no, "error": f"claim_evidence_missing:{key}"})
            rid = r.get("id")
            if rid in seen:
                result["errors"].append({"line": line_no, "error": "duplicate_claim_evidence_id"})
            if rid:
                seen.add(rid)
            if not isinstance(r.get("source"), list) or not r.get("source"):
                result["errors"].append({"line": line_no, "error": "claim_evidence_missing_source"})
            if not isinstance(r.get("evidence"), list) or not r.get("evidence"):
                result["errors"].append({"line": line_no, "error": "claim_evidence_missing_evidence"})
            statuses = {e.get("status") for e in (r.get("evidence") or []) if isinstance(e, dict)}
            if not statuses or not statuses.issubset({"SUPPORTED", "PARTIAL", "UNAVAILABLE", "CONTRADICTED", "NOT_VERIFIED"}):
                result["errors"].append({"line": line_no, "error": "invalid_claim_evidence_status"})
            verification = r.get("verification") or {}
            if verification.get("status") not in {"PASS", "CHECK", "FAIL", "NOT_VERIFIED"}:
                result["errors"].append({"line": line_no, "error": "invalid_claim_verification_status"})
            if verification.get("status") == "PASS" or verification.get("independent") is True:
                result["errors"].append({"line": line_no, "error": "unearned_verification"})
            provenance = r.get("provenance") or {}
            if not provenance.get("created_at") or not provenance.get("generator"):
                result["errors"].append({"line": line_no, "error": "claim_evidence_missing_provenance"})
    result["unique_ids"] = len(seen)
    return result

def main():
    generated = ROOT / "generated"
    framework = load_framework()
    checks = []
    src = generated / "source-units.jsonl"
    verse = generated / "verse-corpus.jsonl"
    reasoning = generated / "reasoning-manifest.jsonl"
    claim_evidence = generated / "claim-evidence.jsonl"
    if src.exists():
        checks.append({"file": str(src.relative_to(ROOT)), **check_source_integrity(src)})
    if verse.exists():
        checks.append({"file": str(verse.relative_to(ROOT)), **check_generated(verse, framework)})
    if reasoning.exists():
        checks.append({"file": str(reasoning.relative_to(ROOT)), **check_reasoning(reasoning, generated, framework)})
    if claim_evidence.exists():
        checks.append({"file": str(claim_evidence.relative_to(ROOT)), **check_claim_evidence(claim_evidence)})
    errors = sum(len(c["errors"]) for c in checks)
    blocking_errors = sum(1 for c in checks for e in c["errors"]
                          if e.get("error") != "duplicate_source_hash" and not e.get("error", "").startswith("duplicate_hash"))
    report = {"version": 5, "framework_id": framework.get("framework_id"), "checks": checks,
              "error_count": errors, "blocking_error_count": blocking_errors,
              "publication_gate": "PASS" if blocking_errors == 0 else "BLOCK"}
    (generated / "QC-REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
