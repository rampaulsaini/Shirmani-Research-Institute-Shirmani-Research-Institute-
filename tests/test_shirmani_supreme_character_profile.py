#!/usr/bin/env python3
"""Deterministic contract tests; not proof of live media/provider integrations."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "config" / "shirmani-supreme-character-profile.json"


class CharacterProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    def test_approved_but_specification_only(self):
        self.assertEqual(self.profile["decision"], "APPROVED")
        self.assertEqual(self.profile["status"], "SPECIFICATION_ONLY")

    def test_exact_insufficient_evidence_notice(self):
        self.assertEqual(self.profile["communication"]["insufficient_evidence_exact_hi"],
                         "अभी पर्याप्त प्रमाण उपलब्ध नहीं है।")

    def test_photo_identity_lock(self):
        lock = self.profile["media_identity_lock"]
        self.assertTrue(lock["original_photo_only"])
        self.assertEqual(set(lock["allowed_photo_changes"]),
                         {"proportional_resize", "display_scaling", "layout_placement"})
        for item in ("generate", "redraw", "retouch", "recolour", "beautify", "reshape", "replace"):
            self.assertIn(item, lock["forbidden_photo_changes"])

    def test_missing_original_assets_block_substitution(self):
        lock = self.profile["media_identity_lock"]
        self.assertTrue(lock["never_substitute_missing_original_media"])
        self.assertEqual(lock["missing_photo_state"], "BLOCKED — PHOTO ASSET REQUIRED")
        self.assertEqual(lock["missing_voice_state"], "BLOCKED — VOICE ASSET REQUIRED")

    def test_evidence_categories_remain_distinct(self):
        states = self.profile["evidence_states"]
        self.assertIn("INDEPENDENTLY VERIFIED", states)
        self.assertIn("PHILOSOPHICAL / PERSONAL PERSPECTIVE", states)
        self.assertIn("INSUFFICIENT EVIDENCE", states)
        self.assertTrue(self.profile["communication"]["philosophy_is_not_independent_scientific_proof"])

    def test_each_product_requires_its_own_media(self):
        media = self.profile["product_media_contract"]
        for key in ("unique_product_id_and_version", "product_specific_qr_upper_right",
                    "short_description_on_image", "long_description_passport_destination",
                    "real_vip_screenshot_required", "actual_product_specific_demo_video_required",
                    "qr_must_be_mobile_scan_tested"):
            self.assertTrue(media[key], key)

    def test_unintegrated_tiers_are_blocked(self):
        tiers = {tier["id"]: tier for tier in self.profile["capability_tiers"]}
        self.assertEqual(tiers["V2"]["status"], "BLOCKED_UNTIL_ASSET_AND_TEST")
        self.assertEqual(tiers["V3"]["status"], "BLOCKED_UNTIL_ASSET_PROVIDER_AND_TEST")
        self.assertEqual(tiers["V4"]["status"], "BLOCKED_UNTIL_END_TO_END_TEST")

    def test_release_requires_real_evidence(self):
        policy = self.profile["release_policy"]
        self.assertTrue(policy["completion_claim_requires_test_evidence"])
        self.assertTrue(policy["workflow_success_is_not_product_verification"])
        self.assertTrue(policy["critical_gate_failure_blocks_release"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
