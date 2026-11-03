#!/usr/bin/env python3
"""Fail-closed consistency checks for the Anant Studio product and publishing manifest."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "factory" / "product-catalog.json"
MANIFEST = ROOT / "config" / "social-publishing-manifest.json"
SOCIAL_ACCOUNTS = ROOT / "config" / "social-accounts.json"
STUDIO_ID = "P-STUDIO-001"


def load(path: Path):
    if not path.is_file():
        raise SystemExit(f"FAIL: required file missing: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FAIL: invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def main() -> None:
    catalog = load(CATALOG)
    manifest = load(MANIFEST)
    social_directory = load(SOCIAL_ACCOUNTS).get("accounts", [])
    offers = [
        offer
        for lane in catalog.get("lanes", [])
        for offer in lane.get("offers", [])
        if isinstance(offer, dict)
    ]
    matches = [offer for offer in offers if offer.get("id") == STUDIO_ID]
    errors = []
    if len(matches) != 1:
        errors.append(f"expected exactly one {STUDIO_ID} catalog offer; found {len(matches)}")
    if manifest.get("studio", {}).get("product_id") != STUDIO_ID:
        errors.append("manifest studio.product_id does not match the canonical catalog ID")
    if manifest.get("catalog_source_path") != "factory/product-catalog.json":
        errors.append("manifest must point to factory/product-catalog.json")
    if matches:
        offer = matches[0]
        if offer.get("delivery") != "creative-service":
            errors.append("Studio must remain a creative-service until a real digital deliverable exists")
        if offer.get("asset_evidence") != "NOT_IN_REPOSITORY":
            errors.append("missing Studio media must not be represented as verified")
        if offer.get("release_status") != "DEMO_PROPOSED":
            errors.append("Studio release status must remain DEMO_PROPOSED")
        if offer.get("voice_status") != "ORIGINAL_USER_AUDIO_REQUIRED":
            errors.append("voice must remain pending until original authorised audio exists")
    publishing = manifest.get("publishing", {})
    if publishing.get("mode") != "DRY_RUN" or publishing.get("live_publish_enabled") is not False:
        errors.append("live publishing must remain disabled")
    if publishing.get("approval", {}).get("human_approval_required") is not True:
        errors.append("human content approval must be required")
    accounts = manifest.get("accounts", [])
    if not isinstance(accounts, list) or len(accounts) != 20:
        errors.append("expected the 20 existing account/link records; do not imply all are social accounts")
    source_by_url = {item.get("url"): item for item in social_directory if isinstance(item, dict)}
    manifest_by_url = {item.get("url"): item for item in accounts if isinstance(item, dict)}
    if len(manifest_by_url) != len(accounts):
        errors.append("manifest contains duplicate or invalid account records")
    if set(source_by_url) != set(manifest_by_url):
        errors.append("manifest URLs must exactly match config/social-accounts.json")
    for url, source in source_by_url.items():
        account = manifest_by_url.get(url)
        if not account:
            continue
        if account.get("platform") != source.get("platform"):
            errors.append(f"platform mismatch for {account.get('label', url)}")
        if account.get("source_api_status") != source.get("api_status"):
            errors.append(f"source API status mismatch for {account.get('label', url)}")
        if account.get("account_kind") == "external_store_link":
            if account.get("permission") != "NOT_APPLICABLE" or account.get("connection_status") != "NOT_A_SOCIAL_API":
                errors.append("external store must not be counted as a social API account")
        elif account.get("permission") != "PENDING_VERIFICATION" or account.get("connection_status") != "PENDING_VERIFICATION":
            errors.append(f"account permission/connection must remain pending: {account.get('label', 'unknown')}")
    if manifest.get("income_evidence", {}).get("payment_status") != "NO_PAYMENT_CLAIMED":
        errors.append("no payment may be claimed without provider/bank evidence")
    if errors:
        for error in errors:
            print("FAIL:", error)
        raise SystemExit(1)
    print("PASS: Anant Studio catalog and publishing manifest are consistent.")
    print("PASS: Studio media/voice evidence remains unverified until real assets are supplied.")
    print("PASS: 20 link records match the source directory; social permissions remain pending and the store is correctly excluded.")
    print("PASS: payment status remains NO_PAYMENT_CLAIMED.")


if __name__ == "__main__":
    main()
