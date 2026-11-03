#!/usr/bin/env python3
"""Fail-closed validation for the Anant Studio publishing manifest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))

def main():
    manifest = load("config/social-publishing-manifest.json")
    accounts = load("config/social-accounts.json")["accounts"]
    catalog = load("factory/product-catalog.json")

    assert manifest["studio"]["product_id"] == "P-STUDIO-001"
    assert manifest["publishing"]["mode"] == "DRY_RUN"
    assert manifest["publishing"]["live_publish_enabled"] is False
    assert manifest["publishing"]["approval"]["human_approval_required"] is True
    assert manifest["dispatch_gates"]["do_not_publish_if_any_gate_fails"] is True

    registered = [
        offer for lane in catalog["lanes"] for offer in lane["offers"]
        if offer.get("id") == "P-STUDIO-001"
    ]
    assert len(registered) == 1, "P-STUDIO-001 must exist exactly once in canonical source catalog"
    offer = registered[0]
    assert offer.get("asset_evidence") == "NOT_IN_REPOSITORY", "Do not promote an unbuilt demo to verified"
    assert offer.get("release_status") == "DEMO_PROPOSED"

    source_by_url = {item["url"]: item for item in accounts}
    manifest_by_url = {item["url"]: item for item in manifest["accounts"]}
    assert len(manifest_by_url) == len(manifest["accounts"]), "Duplicate account URLs in manifest"
    assert set(manifest_by_url) == set(source_by_url), "Manifest URLs must match canonical social link directory"

    for url, source in source_by_url.items():
        item = manifest_by_url[url]
        assert item["platform"] == source["platform"], f"Platform mismatch for {url}"
        assert item["source_api_status"] == source["api_status"], f"Source status mismatch for {url}"
        if source["api_status"] != "EXTERNAL_STORE":
            assert item["permission"] == "PENDING_VERIFICATION", f"Unverified permission promoted for {url}"
            assert item["connection_status"] == "PENDING_VERIFICATION", f"Unverified connection promoted for {url}"

    formats = manifest["publishing"]["formats"]
    assert {"short_video", "long_video", "podcast"} <= set(formats)
    assert manifest["income_evidence"]["views_and_followers_are_not_income"] is True
    assert manifest["income_evidence"]["payment_status"] == "NO_PAYMENT_CLAIMED"

    forbidden_keys = {"access_token", "refresh_token", "password", "client_secret", "api_key"}
    def inspect(value, path="$"):
        if isinstance(value, dict):
            for key, child in value.items():
                assert key.lower() not in forbidden_keys, f"Secret-like field {path}.{key} is forbidden"
                inspect(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                inspect(child, f"{path}[{index}]")
    inspect(manifest)

    print("PASS: Anant Studio manifest, canonical offer, account directory, dry-run and evidence gates")
    print(f"Accounts checked: {len(manifest['accounts'])}; catalog offer: P-STUDIO-001; live publishing: disabled")

if __name__ == "__main__":
    main()
