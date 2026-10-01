"""Contract tests for the fail-closed Automission supervisor."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from agents.automission_supervisor import inspect


def main():
    with TemporaryDirectory() as td:
        missing = inspect(str(Path(td) / "missing.json"))
        assert missing["state"] == "NO_STATUS"
        assert missing["governance"] if "governance" in missing else True

        p = Path(td) / "status.json"
        p.write_text(json.dumps({
            "fingerprint": "a" * 64,
            "result": {
                "status": "interpreted",
                "features": {
                    "evidence_grade": "A",
                    "agreement": 0.95,
                    "modalities": 3,
                    "independent_sources": 3,
                    "sample_count": 100,
                    "drift_score": 0.02,
                },
                "interpretation": {
                    "confidence": 0.92,
                    "limitations": ["observable signal interpretation only"],
                },
            },
        }), encoding="utf-8")
        plan = inspect(str(p))
        assert plan["state"] == "MONITOR"
        assert plan["governance"]["fail_closed"] is True
        assert plan["governance"]["subjective_experience_claim_allowed"] is False
        assert plan["governance"]["scheduled_code_mutation_allowed"] is False
        assert plan["governance"]["independent_verification_required"] is True
        print("AUTOMISSION_SUPERVISOR_CONTRACT_OK")


if __name__ == "__main__":
    main()
