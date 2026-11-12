import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_character_assets.py"
SPEC = importlib.util.spec_from_file_location("audit_character_assets", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CharacterAssetAuditTests(unittest.TestCase):
    def test_missing_source_hashes_remain_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "config").mkdir()
            (root / "assets").mkdir()
            (root / "config" / "authorized-voice-integration.json").write_text(
                json.dumps({"source_assets": {"photo_sha256": "a" * 64, "audio_sha256": "b" * 64},
                            "consent": {"status": "USER_PROVIDED_FOR_THIS_CONVERSATION"}}),
                encoding="utf-8")
            (root / "assets" / "candidate.jpg").write_bytes(b"not-the-source-photo")
            report = MODULE.audit(root)
            self.assertTrue(report["photo"]["state"].startswith("BLOCKED"))
            self.assertTrue(report["audio"]["state"].startswith("BLOCKED"))
            self.assertEqual(report["status"], "INVENTORY_ONLY_NOT_PRODUCTION_VERIFICATION")

    def test_hash_match_is_not_authorisation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "config").mkdir()
            (root / "assets").mkdir()
            photo = root / "assets" / "photo.png"
            photo.write_bytes(b"exact fixture bytes")
            digest = MODULE.sha256(photo)
            (root / "config" / "authorized-voice-integration.json").write_text(
                json.dumps({"source_assets": {"photo_sha256": digest, "audio_sha256": "c" * 64},
                            "consent": {"status": "UNCONFIRMED"}}),
                encoding="utf-8")
            report = MODULE.audit(root)
            self.assertIn("HASH_MATCH_FOUND", report["photo"]["state"])
            self.assertIn("AUTHORISATION STILL REQUIRES HUMAN CONFIRMATION", report["photo"]["state"])
            self.assertTrue(report["audio"]["state"].startswith("BLOCKED"))

    def test_external_media_is_hashed_without_copying_or_leaking_full_path(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            outside = Path(temp) / "private" / "recording.mp4"
            (root / "config").mkdir(parents=True)
            outside.parent.mkdir()
            outside.write_bytes(b"video-container-fixture")
            (root / "config" / "authorized-voice-integration.json").write_text(
                json.dumps({"source_assets": {"photo_sha256": "a" * 64, "audio_sha256": "b" * 64},
                            "consent": {"status": "UNCONFIRMED"}}),
                encoding="utf-8")
            report = MODULE.audit(root, [outside])
            self.assertEqual(report["candidate_media_count"], 1)
            self.assertEqual(report["candidate_media"][0]["origin"], "external_input")
            self.assertEqual(report["candidate_media"][0]["path"], "EXTERNAL_MEDIA/1-recording.mp4")
            self.assertNotIn(str(outside.parent), json.dumps(report))
            self.assertTrue(report["audio"]["state"].startswith("BLOCKED"))

    def test_missing_external_media_returns_clear_error(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "config").mkdir()
            (root / "config" / "authorized-voice-integration.json").write_text(
                json.dumps({"source_assets": {}}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "External media file not found"):
                MODULE.audit(root, [root / "absent.mp4"])


if __name__ == "__main__":
    unittest.main()
