from pathlib import Path

from production_readiness import check_repository


def test_production_readiness_contracts_exist():
    root = Path(__file__).resolve().parents[2]
    result = check_repository(root)
    assert result["all_required_contracts"] is True
    assert result["runtime_safety"] is True
