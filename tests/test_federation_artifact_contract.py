from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FederationArtifactContractTests(unittest.TestCase):
    def test_federation_inventory_and_health_have_distinct_outputs(self):
        inventory_writer = (ROOT / "factory" / "federation.py").read_text(encoding="utf-8")
        health_writer = (ROOT / "scripts" / "sync-central-factory-status.py").read_text(encoding="utf-8")

        self.assertIn('"federation-inventory.json"', inventory_writer)
        self.assertIn('HEALTH_TARGET = Path("generated/federation-health.json")', health_writer)
        self.assertNotIn('"generated"/"federation-status.json"', inventory_writer)
        self.assertNotIn('Path("generated/federation-status.json")', health_writer)
        self.assertIn('"central_health_source_verified": True', health_writer)
        self.assertIn('"federation_verified": False', health_writer)
        self.assertIn('health["federation_verified"] = False', health_writer)
        self.assertIn('health["central_health_source_verified"] = True', health_writer)
        self.assertIn('DISPATCH_TARGET = Path("generated/federation-dispatch.json")', health_writer)
        self.assertIn('DISPATCH_PATH = "federation/status/latest.json"', health_writer)
        self.assertIn("dispatch_record_verified", health_writer)

    def test_dashboards_consume_the_matching_federation_artifacts(self):
        factory_dashboard = (ROOT / "factory-dashboard.html").read_text(encoding="utf-8")
        federation_dashboard = (ROOT / "federation-dashboard.html").read_text(encoding="utf-8")
        factory_workflow = (ROOT / ".github" / "workflows" / "omniverse-factory.yml").read_text(encoding="utf-8")

        self.assertIn("generated/federation-health.json", factory_dashboard)
        self.assertIn("generated/federation-health.json", federation_dashboard)
        self.assertIn("generated/federation-inventory.json", federation_dashboard)
        self.assertIn("generated/federation-dispatch.json", federation_dashboard)
        self.assertIn("Promise.allSettled", federation_dashboard)
        self.assertIn("dispatchResult", federation_dashboard)
        self.assertNotIn("h.dispatch", federation_dashboard)
        self.assertIn("Promise.all([", factory_dashboard)
        self.assertIn("scripts/sync-central-factory-status.py", factory_workflow)
        self.assertIn("ORCHESTRATOR_TOKEN: ${{ secrets.SHIRMANI_GITHUB_TOKEN }}", factory_workflow)


if __name__ == "__main__":
    unittest.main()
