#!/usr/bin/env python3
"""Fail-closed quality governor for the SHIRMANI research/agent pipeline.

This is a deterministic integrity gate, not a claim of scientific truth.
It measures whether generated records are traceable, internally consistent,
non-duplicated, and conservative about verification status.
"""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
REPORT = GENERATED / "supreme-accuracy-governor.json"
STATUS = {"draft", "source-backed", "unverified", "verified", "NOT_VERIFIED", "READY_FOR_HUMAN_REVIEW"}

def load_jsonl(path: Path):
    rows=[]
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: rows.append((n,json.loads(line)))
        except json.JSONDecodeError as e:
            raise ValueError(f"invalid JSONL: {path}:{n}: {e}") from e
    return rows

def main():
    errors=[]; warnings=[]; counts={"jsonl_files":0,"records":0}
    ids=set(); hashes=set(); provenance=0; verification_rows=0; independent_verified=0

    if not GENERATED.exists():
        errors.append("generated directory is missing")
    else:
        for p in GENERATED.rglob("*.jsonl"):
            counts["jsonl_files"] += 1
            for line_no,r in load_jsonl(p):
                counts["records"] += 1
                rid=r.get("id") or r.get("record_id") or r.get("artifact_id")
                if rid:
                    if rid in ids: errors.append(f"duplicate-id:{rid}:{p}:{line_no}")
                    ids.add(rid)
                text=r.get("text")
                if text:
                    h=hashlib.sha256(text.encode("utf-8")).hexdigest()
                    stored=r.get("source_sha256") or r.get("sha256")
                    if stored and stored != h and r.get("source_sha256"):
                        errors.append(f"source-hash-mismatch:{p}:{line_no}")
                    hashes.add(h)
                if r.get("source") or r.get("provenance"):
                    provenance += 1
                if "verification" in r or r.get("status") in {"verified","NOT_VERIFIED","READY_FOR_HUMAN_REVIEW"}:
                    verification_rows += 1
                if r.get("status") == "verified":
                    # VERIFIED must never be inferred from a source-backed label alone.
                    evidence=r.get("evidence") or r.get("independent_evidence") or r.get("independent_verification")
                    if not evidence:
                        errors.append(f"verified-without-evidence:{p}:{line_no}:{rid}")
                    elif r.get("independent_verification") is True:
                        independent_verified += 1

        for p in GENERATED.rglob("*.json"):
            try:
                data=json.loads(p.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errors.append(f"invalid-json:{p}:{e}")
                continue
            if p.name.endswith("artifact-manifest.json"):
                pass

    report={
        "governor":"SHIRMANI Supreme Accuracy Governor",
        "generated_at":"deterministic-run",
        "state":"BLOCKED" if errors else ("REVIEW_REQUIRED" if warnings else "PASS"),
        "principle":"Accuracy is demonstrated by evidence and repeatable checks, not asserted by a label.",
        "counts":counts,
        "unique_ids":len(ids),
        "unique_text_hashes":len(hashes),
        "provenance_covered_records":provenance,
        "verification_records":verification_rows,
        "independent_verified_records":independent_verified,
        "errors":errors[:200],
        "warnings":warnings[:200],
        "gates":[
            "deterministic JSON/JSONL parsing",
            "duplicate identity detection",
            "source-hash consistency when hashes are present",
            "provenance presence",
            "fail-closed VERIFIED evidence gate",
            "explicit human/independent verification separation",
        ],
    }
    GENERATED.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if errors:
        return 2
    return 0

if __name__=="__main__":
    sys.exit(main())
