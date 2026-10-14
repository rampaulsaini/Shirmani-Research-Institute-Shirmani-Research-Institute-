import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from scripts.audit_character_assets import audit, find_hash_matches


class CharacterAssetAuditTests(unittest.TestCase):
    def test_finds_exact_photo_and_audio_hashes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            photo = root / "assets" / "portrait.jpg"
            audio = root / "assets" / "voice.wav"
            photo.parent.mkdir()
            photo.write_bytes(b"original portrait bytes")
            audio.write_bytes(b"original voice bytes")
            config = root / "config.json"
            config.write_text(json.dumps({
                "source_assets": {
                    "photo_sha256": hashlib.sha256(photo.read_bytes()).hexdigest(),
                    "audio_sha256": hashlib.sha256(audio.read_bytes()).hexdigest(),
                },
                "consent": {"status": "USER_PROVIDED_FOR_THIS_CONVERSATION"},
            }), encoding="utf-8")

            result = audit(config, root)
            self.assertEqual(result["overall_status"], "HASH MATCH")
            self.assertEqual(result["assets"]["photo"]["matches"], ["assets/portrait.jpg"])
            self.assertEqual(result["assets"]["audio"]["matches"], ["assets/voice.wav"])
            self.assertEqual(result["provider_integration"], "NOT VERIFIED")

    def test_missing_original_assets_remain_unverified(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = root / "config.json"
            config.write_text(json.dumps({
                "source_assets": {
                    "photo_sha256": "0" * 64,
                    "audio_sha256": "1" * 64,
                }
            }), encoding="utf-8")
            result = audit(config, root)
            self.assertEqual(result["overall_status"], "NOT VERIFIED")
            self.assertEqual(result["assets"]["photo"]["matches"], [])
            self.assertEqual(result["assets"]["audio"]["matches"], [])

    def test_rejects_invalid_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                find_hash_matches(Path(temp), "not-a-hash", "photo")

    def test_ignores_svg_and_non_media_placeholders(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "logo.svg").write_text("<svg/>", encoding="utf-8")
            (root / "profile.jpg").write_bytes(b"")
            expected = hashlib.sha256(b"").hexdigest()
            self.assertEqual(find_hash_matches(root, expected, "photo"), ["profile.jpg"])


if __name__ == "__main__":
    unittest.main()
