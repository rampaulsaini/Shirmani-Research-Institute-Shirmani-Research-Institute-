import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const manifestUrl = new URL("../../config/social-publishing-manifest.json", import.meta.url);
const accountDirectoryUrl = new URL("../../config/social-accounts.json", import.meta.url);

test("Anant Studio publishing manifest is valid JSON with a fail-closed publishing state", async () => {
  const manifest = JSON.parse(await readFile(manifestUrl, "utf8"));
  assert.equal(manifest.schema_version, "1.0");
  assert.equal(manifest.manifest_id, "ANANT-STUDIO-PUBLISHING-001");
  assert.equal(manifest.studio.product_id, "P-STUDIO-001");
  assert.equal(manifest.studio.release_status, "DEMO_PROPOSED");
  assert.equal(manifest.publishing.mode, "DRY_RUN");
  assert.equal(manifest.publishing.live_publish_enabled, false);
  assert.equal(manifest.publishing.approval.human_approval_required, true);
  assert.equal(manifest.dispatch_gates.do_not_publish_if_any_gate_fails, true);
});

test("manifest accounts preserve every supplied link without granting API permission", async () => {
  const manifest = JSON.parse(await readFile(manifestUrl, "utf8"));
  const directory = JSON.parse(await readFile(accountDirectoryUrl, "utf8"));
  assert.equal(manifest.accounts.length, directory.accounts.length);
  const keys = new Set(manifest.accounts.map(account => `${account.platform}|${account.label}|${account.url}`));
  for (const account of directory.accounts) {
    assert.ok(keys.has(`${account.platform}|${account.label}|${account.url}`), `missing source link: ${account.label}`);
  }
  for (const account of manifest.accounts) {
    assert.ok(account.url.startsWith("https://") || account.url.startsWith("http://"));
    if (account.account_kind === "external_store_link") {
      assert.equal(account.permission, "NOT_APPLICABLE");
    } else {
      assert.equal(account.connection_status, "PENDING_VERIFICATION");
      assert.equal(account.permission, "PENDING_VERIFICATION");
    }
  }
});

test("all proposed media formats require production evidence before release", async () => {
  const manifest = JSON.parse(await readFile(manifestUrl, "utf8"));
  assert.equal(manifest.publishing.formats.short_video.aspect_ratio, "9:16");
  assert.equal(manifest.publishing.formats.short_video.target_duration_seconds, 15);
  assert.equal(manifest.publishing.formats.long_video.aspect_ratio, "16:9");
  assert.equal(manifest.publishing.formats.long_video.target_duration_seconds, 300);
  assert.equal(manifest.publishing.formats.podcast.status, "ORIGINAL_USER_AUDIO_REQUIRED");
  assert.equal(manifest.studio.voice_status, "ORIGINAL_USER_AUDIO_REQUIRED");
  assert.equal(manifest.studio.languages.target_count, 16);
  assert.equal(manifest.studio.languages.status, "TRANSLATION_AND_HUMAN_REVIEW_REQUIRED");
});

test("income evidence is not inferred from views, followers, or catalog prices", async () => {
  const manifest = JSON.parse(await readFile(manifestUrl, "utf8"));
  assert.equal(manifest.income_evidence.views_and_followers_are_not_income, true);
  assert.equal(manifest.income_evidence.do_not_infer_revenue_from_catalog_price, true);
  assert.equal(manifest.income_evidence.payment_status, "NO_PAYMENT_CLAIMED");
});
