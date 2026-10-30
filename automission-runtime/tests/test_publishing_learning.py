import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from product_catalog import ProductCatalog
from product_pipeline import run_quality_gate, prepare_for_publishing
from publishing import PublishingRegistry
from product_learning import capture_product_intelligence, prioritize_product
from product_dashboard import snapshot

class PublishingLearningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "factory.db"
        self.catalog = ProductCatalog(self.db)
        self.product = self.catalog.create("Digital Course", "course")

    def tearDown(self):
        self.tmp.cleanup()

    def test_unknown_channel_is_planned_not_claimed_connected(self):
        registry = PublishingRegistry(self.db)
        self.assertEqual(
            registry.plan(self.product, "global_marketplace"),
            "PLANNED_NO_ADAPTER",
        )

    def test_enabled_channel_still_requires_approval(self):
        registry = PublishingRegistry(self.db)
        registry.register("own_store", "own-store-adapter", ["publish"], enabled=True,
                          status="CONFIGURED")
        self.assertEqual(registry.plan(self.product, "own_store"), "APPROVAL_REQUIRED")

    def test_verified_sales_drive_currency_safe_learning(self):
        run_quality_gate(self.catalog, self.product, 90)
        prepare_for_publishing(self.catalog, self.product, 10, "USD")
        self.catalog.transition(self.product, "PUBLISH_APPROVAL_REQUIRED")
        self.catalog.approve_publish(self.product)
        self.catalog.record_sale(self.product, 20, "USD",
                                 "https://evidence.example/order/1", "own_store")
        intelligence = capture_product_intelligence(self.db)
        self.assertEqual(intelligence["evidence_backed_sales"], 1)
        self.assertGreater(
            prioritize_product(50, "course", "USD", intelligence), 50
        )
        self.assertEqual(
            prioritize_product(50, "course", "INR", intelligence), 50
        )

    def test_dashboard_contains_only_verified_sales(self):
        run_quality_gate(self.catalog, self.product, 90)
        prepare_for_publishing(self.catalog, self.product, 10, "USD")
        self.catalog.transition(self.product, "PUBLISH_APPROVAL_REQUIRED")
        self.catalog.approve_publish(self.product)
        self.catalog.record_sale(self.product, 15, "USD",
                                 "https://evidence.example/order/2", "own_store")
        data = snapshot(self.db)
        self.assertEqual(data["verified_sales_by_currency"]["USD"]["verified_income"], 15)
        self.assertEqual(data["verified_sales_by_currency"]["USD"]["verified_sales"], 1)

if __name__ == "__main__":
    unittest.main()
