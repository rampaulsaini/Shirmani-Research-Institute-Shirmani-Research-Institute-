#!/usr/bin/env node
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const ROOT = path.resolve(__dirname, '..');
function readJson(file) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, file), 'utf8'));
}
function fail(message) {
  console.error('SOCIAL PUBLISHING MANIFEST INVALID:', message);
  process.exitCode = 1;
}
try {
  const manifest = readJson('config/social-publishing-manifest.json');
  const source = readJson('config/social-accounts.json');
  if (manifest.schema_version !== '1.0') fail('unsupported schema_version');
  if (manifest.manifest_id !== 'ANANT-STUDIO-PUBLISHING-001') fail('wrong manifest_id');
  if (manifest.studio?.product_id !== 'P-STUDIO-001') fail('wrong Studio product_id');
  if (manifest.publishing?.mode !== 'DRY_RUN' || manifest.publishing?.live_publish_enabled !== false) {
    fail('live publishing must remain disabled until separate authorization and testing');
  }
  if (manifest.publishing?.approval?.human_approval_required !== true) fail('human approval must be required');
  if (manifest.publishing?.approval?.content_rights_check_required !== true) fail('content rights review must be required');
  if (manifest.publishing?.approval?.translation_review_required !== true) fail('translation review must be required');
  if (!Array.isArray(source.accounts) || !Array.isArray(manifest.accounts)) fail('both account arrays are required');
  else {
    const key = a => [a.platform, a.label, a.url].join('|');
    const sourceKeys = new Set(source.accounts.map(key));
    const seen = new Set();
    for (const account of manifest.accounts) {
      const k = key(account);
      if (!sourceKeys.has(k)) fail('account is not present in source directory: ' + account.label);
      if (seen.has(k)) fail('duplicate account record: ' + account.label);
      seen.add(k);
      if (account.source_api_status === 'EXTERNAL_STORE') {
        if (account.connection_status !== 'NOT_A_SOCIAL_API' || account.permission !== 'NOT_APPLICABLE') {
          fail('external store must not be treated as a social publishing account');
        }
      } else if (account.permission === 'GRANTED' &&
                 (account.connection_status !== 'CONNECTED' || account.source_api_status !== 'CONNECTED')) {
        fail('GRANTED requires verified CONNECTED status and source_api_status CONNECTED: ' + account.label);
      }
    }
    if (manifest.accounts.length !== source.accounts.length) fail('manifest account count does not match source directory');
  }
  const gates = manifest.dispatch_gates || {};
  for (const [name, value] of Object.entries({
    require_verified_account_connection:true,
    require_platform_api_authorization:true,
    require_human_content_approval:true,
    require_content_asset_and_rights_check:true,
    require_destination_allowlist:true,
    require_idempotency_key:true,
    do_not_publish_if_any_gate_fails:true
  })) if (gates[name] !== value) fail('dispatch gate must be true: ' + name);
  if (manifest.security?.secrets_in_repository !== false) fail('secrets must never be stored in repository');
  if (manifest.income_evidence?.views_and_followers_are_not_income !== true) fail('views/followers cannot count as income');
  if (manifest.income_evidence?.do_not_infer_revenue_from_catalog_price !== true) fail('catalog prices cannot count as revenue');
  if (!process.exitCode) console.log('ANANT STUDIO MANIFEST OK — ' + manifest.accounts.length + ' source-matched records; DRY_RUN; live publishing disabled.');
} catch (error) {
  fail(error.message);
}
