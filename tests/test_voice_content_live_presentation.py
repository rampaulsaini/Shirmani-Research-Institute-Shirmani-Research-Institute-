import json
from pathlib import Path


SCHEMA = Path(__file__).resolve().parents[1] / "schemas" / "voice-content-live-presentation.schema.json"


def load_schema():
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def test_voice_presentation_schema_is_fail_closed():
    schema = load_schema()
    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False
    assert {
        "packet_id",
        "voice_asset_id",
        "content_asset_id",
        "visual_asset_id",
        "renderer",
        "renderer_version",
        "language",
        "consent_status",
        "provenance",
        "qc",
        "verification_state",
        "publication_state",
        "created_at",
    } == set(schema["required"])


def test_verification_states_cannot_claim_success_by_default():
    states = set(
        load_schema()["properties"]["verification_state"]["enum"]
    )
    assert "UNVERIFIED" in states
    assert "INDEPENDENT_REVIEW_PENDING" in states
    assert "VERIFIED" in states


def test_live_publication_requires_explicit_human_approval_state():
    states = set(
        load_schema()["properties"]["publication_state"]["enum"]
    )
    assert "HUMAN_APPROVED" in states
    assert "LIVE" in states
    assert "QC_FAIL" in states
    assert "UNAUTHORIZED" in states
    assert "PROVENANCE_MISSING" in states
    assert "IDENTITY_REVIEW_REQUIRED" in states
