from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_federation_inventory_and_health_have_distinct_outputs():
    inventory_writer = (ROOT / "factory" / "federation.py").read_text(encoding="utf-8")
    health_writer = (ROOT / "scripts" / "sync-central-factory-status.py").read_text(encoding="utf-8")

    assert '"federation-inventory.json"' in inventory_writer
    assert 'HEALTH_TARGET = Path("generated/federation-health.json")' in health_writer
    assert '"generated"/"federation-status.json"' not in inventory_writer
    assert 'Path("generated/federation-status.json")' not in health_writer
    assert '"central_health_source_verified": True' in health_writer
    assert '"federation_verified": False' in health_writer
    assert 'health["federation_verified"] = False' in health_writer
    assert 'health["central_health_source_verified"] = True' in health_writer
    assert 'DISPATCH_TARGET = Path("generated/federation-dispatch.json")' in health_writer
    assert 'DISPATCH_PATH = "federation/status/latest.json"' in health_writer
    assert 'dispatch_record_verified' in health_writer


def test_dashboards_consume_the_matching_federation_artifacts():
    factory_dashboard = (ROOT / "factory-dashboard.html").read_text(encoding="utf-8")
    federation_dashboard = (ROOT / "federation-dashboard.html").read_text(encoding="utf-8")
    factory_workflow = (ROOT / ".github" / "workflows" / "omniverse-factory.yml").read_text(encoding="utf-8")

    assert "generated/federation-health.json" in factory_dashboard
    assert "generated/federation-health.json" in federation_dashboard
    assert "generated/federation-inventory.json" in federation_dashboard
    assert "generated/federation-dispatch.json" in federation_dashboard
    assert "Promise.allSettled" in federation_dashboard
    assert "dispatchResult" in federation_dashboard
    assert "h.dispatch" not in federation_dashboard
    assert "Promise.all([" in factory_dashboard
    assert "scripts/sync-central-factory-status.py" in factory_workflow
    assert "ORCHESTRATOR_TOKEN: ${{ secrets.SHIRMANI_GITHUB_TOKEN }}" in factory_workflow
