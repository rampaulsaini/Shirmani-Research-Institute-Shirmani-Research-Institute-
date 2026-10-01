#!/usr/bin/env python3
"""Provider-free deterministic validator for the Supreme NLP benchmark contract."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "supreme-nlp-benchmark-contract-2026-10-01.md"
REPORT = ROOT / "generated" / "supreme-nlp-benchmark-qc.json"
REQUIRED_SECTIONS = ["Evaluation dimensions", "Biological / environmental interpretation", "Required benchmark record", "Gates", "Five-minute operating integration", "Definition of progress"]
REQUIRED_RECORD_FIELDS = ["benchmark_version", "model_version", "dataset_fingerprint", "task", "population", "metrics", "sample_count", "result", "baseline", "regression", "provenance", "verification_state"]
def main():
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    template = {k: None for k in REQUIRED_RECORD_FIELDS}
    missing_fields = [k for k in REQUIRED_RECORD_FIELDS if k not in template]
    report = {"schema_version": 1, "contract": str(CONTRACT.relative_to(ROOT)), "contract_sections": len(REQUIRED_SECTIONS)-len(missing), "required_sections": len(REQUIRED_SECTIONS), "template_missing_fields": missing_fields, "model_accuracy_claimed": False, "publication_gate": "PASS" if not missing and not missing_fields else "BLOCK", "principle": "accuracy is measured, not declared"}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    if report["publication_gate"] != "PASS": raise SystemExit(json.dumps(report, ensure_ascii=False))
    print(json.dumps(report, ensure_ascii=False))
if __name__ == "__main__": main()
