"""Regression checks for the public Pages overlay route and URL diagnostics."""
from pathlib import Path
import unittest
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
SMOKE = ROOT / "factory" / "public_pages_runtime_smoke.py"
OVERLAY_ROUTE = "generated/public-production-asset-overlay.json"


class PublicPagesRouteDiagnosticsTest(unittest.TestCase):
    def test_overlay_is_part_of_deployed_route_gate(self):
        source = SMOKE.read_text(encoding="utf-8")
        self.assertIn(f'"{OVERLAY_ROUTE}"', source)
        self.assertIn('overlay = read_json("generated/public-production-asset-overlay.json")', source)

    def test_root_hosted_and_project_path_urls_preserve_base_path(self):
        route = OVERLAY_ROUTE
        cases = (
            ("https://owner.github.io/", "https://owner.github.io/generated/public-production-asset-overlay.json"),
            ("https://owner.github.io/project/", "https://owner.github.io/project/generated/public-production-asset-overlay.json"),
        )
        for base, expected in cases:
            with self.subTest(base=base):
                self.assertEqual(urljoin(base, route), expected)

    def test_failure_diagnostics_preserve_http_evidence(self):
        source = SMOKE.read_text(encoding="utf-8")
        for marker in ("requested_url=", "final_url=", "content_type=", "body_snippet=", "status="):
            with self.subTest(marker=marker):
                self.assertIn(marker, source)


if __name__ == "__main__":
    unittest.main()
