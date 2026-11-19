"""Executable contract tests for Character Studio V1–V4.
Static tests are deterministic; real provider/media checks remain blocked until evidence exists.
"""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs/shirmani-supreme/canonical-character-specification.md"
STUDIO = ROOT / "showroom/shirmani-supreme-character-studio.html"
GATE_PATH = ROOT / "scripts/character_release_gate.py"
spec = importlib.util.spec_from_file_location("character_release_gate", GATE_PATH)
gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gate)

def valid_packet():
    build = "test-build-sha-123"
    return {
        "release_candidate": {"build_id": build, "reviewed": True, "security_checks_passed": True},
        "tiers": {
            "V1": {"status": "PASS", "build_id": build, "evidence_urls": ["https://evidence.example/v1"],
                   "assertions": {"hindi_prompt": True, "english_prompt": True, "evidence_states": True,
                                  "insufficient_evidence_notice": True, "original_photo_policy": True}},
            "V2": {"status": "PASS", "build_id": build, "evidence_urls": ["https://evidence.example/v2"],
                   "authorization_verified": True, "audio_output_url": "https://evidence.example/audio.wav"},
            "V3": {"status": "PASS", "build_id": build, "evidence_urls": ["https://evidence.example/v3"],
                   "source_sha256": "a" * 64, "rendered_video_url": "https://evidence.example/render.mp4",
                   "lip_sync_offset_ms": [80, 95, 110], "lip_sync_threshold_ms": 120},
            "V4": {"status": "PASS", "build_id": build, "evidence_urls": ["https://evidence.example/v4"],
                   "latency_ms": [120, 130, 150, 170, 220],
                   "failure_paths": {"timeout": True, "rate_limit": True, "network_disconnect": True,
                                     "provider_outage": True, "insufficient_evidence": True}},
        },
    }

class CharacterStudioV1V4AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec_text = SPEC.read_text(encoding="utf-8")
        cls.studio_text = STUDIO.read_text(encoding="utf-8")

    def test_v1_canonical_spec_and_studio_are_present(self):
        for phrase in ("canonical source", "V1 — Character Studio", "V2 — Authorized voice",
                       "V3 — Original face and lip-sync", "V4 — Live Q&A and audit"):
            self.assertIn(phrase.lower(), self.spec_text.lower())
        self.assertIn("PROTOTYPE — NOT A LIVE AVATAR", self.studio_text)

    def test_v1_hindi_english_evidence_and_photo_policy(self):
        for phrase in ("अभी पर्याप्त प्रमाण उपलब्ध नहीं है।", "INSUFFICIENT EVIDENCE",
                       "PHILOSOPHICAL / IDENTITY", "exact original photograph",
                       "Hindi and English sample prompts"):
            self.assertIn(phrase, self.spec_text)

    def test_v2_v3_v4_remain_pending_until_real_artifacts_exist(self):
        for phrase in ("Authorized HeyGen voice | PENDING", "Original-face rendered video | PENDING",
                       "Live Q&A and latency | PENDING", "production readiness | BLOCKED pending gates"):
            self.assertIn(phrase.lower(), self.spec_text.lower())

    def test_percentile_is_deterministic(self):
        self.assertEqual(gate.percentile([220, 120, 170, 150, 130], 50), 150)
        self.assertEqual(gate.percentile([220, 120, 170, 150, 130], 95), 220)
        with self.assertRaises(ValueError):
            gate.percentile([], 95)

    def test_release_gate_fails_closed_on_missing_evidence(self):
        packet = valid_packet()
        packet["tiers"]["V2"]["authorization_verified"] = False
        packet["tiers"]["V3"]["rendered_video_url"] = ""
        packet["tiers"]["V4"]["failure_paths"]["timeout"] = False
        errors = gate.validate_packet(packet)
        self.assertTrue(any("authorization" in error for error in errors))
        self.assertTrue(any("rendered video" in error for error in errors))
        self.assertTrue(any("failure" in error for error in errors))

    def test_all_tiers_must_use_same_build_and_be_reviewed(self):
        packet = valid_packet()
        packet["tiers"]["V3"]["build_id"] = "different-build"
        packet["release_candidate"]["reviewed"] = False
        errors = gate.validate_packet(packet)
        self.assertTrue(any("V3: build_id" in error for error in errors))
        self.assertTrue(any("reviewed must be true" in error for error in errors))

    def test_structural_success_is_only_eligible_for_human_review(self):
        packet = valid_packet()
        self.assertEqual(gate.validate_packet(packet), [])
        self.assertIn("computed_p50_ms", packet["tiers"]["V4"])
        self.assertIn("computed_p95_ms", packet["tiers"]["V4"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
