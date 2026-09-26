import json
from pathlib import Path


REQUIRED_CONTRACTS = (
    "income/runtime-contract.json",
    "income/master-orchestrator.yml",
    "income/master-task-ledger.json",
    "income/master-learning.json",
    "income/master-dashboard.json",
)


def check_repository(root: Path):
    checks = {}
    for relative in REQUIRED_CONTRACTS:
        path = root / relative
        checks[relative] = path.exists()

    checks["runtime_safety"] = False
    runtime = root / "income/runtime-contract.json"
    if runtime.exists():
        data = json.loads(runtime.read_text(encoding="utf-8"))
        checks["runtime_safety"] = (
            data.get("mode") == "continuous"
            and data.get("safety", {}).get("fabrication_forbidden") is True
            and data.get("safety", {}).get(
                "irreversible_actions_require_authorization"
            ) is True
        )

    checks["all_required_contracts"] = all(
        value for key, value in checks.items()
        if key != "all_required_contracts"
    )
    return checks
