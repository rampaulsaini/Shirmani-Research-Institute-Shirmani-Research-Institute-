import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.supreme_nlp.core import Signal, audit_record, interpret_signal


def main():
    examples = [
        Signal("synthetic", "text", "system audit", provenance="fixture"),
        Signal("synthetic", "bioelectric", {"delta": 0.1}, provenance="fixture"),
        Signal("synthetic", "vibration", {"hz": 42.0}, provenance="fixture"),
    ]
    records = [audit_record(s, interpret_signal(s)) for s in examples]
    report = {
        "schema_version": "1.0",
        "mode": "evidence-first",
        "records": records,
        "all_fingerprints_present": all(r["fingerprint"] for r in records),
        "no_unverified_subjective_claims": all(
            "does not establish subjective experience" in r["interpretation"]["statement"]
            for r in records
        ),
    }
    out = ROOT / "generated" / "supreme-nlp-audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("SUPREME_NLP_AUDIT=PASS" if report["all_fingerprints_present"] and report["no_unverified_subjective_claims"] else "SUPREME_NLP_AUDIT=FAIL")
    return 0 if report["all_fingerprints_present"] and report["no_unverified_subjective_claims"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
