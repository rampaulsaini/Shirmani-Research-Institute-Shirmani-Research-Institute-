#!/usr/bin/env node
'use strict';

/**
 * Safe, idempotent social dispatch gateway.
 * Default is DRY RUN. Never embeds credentials or claims a post succeeded
 * until the configured Make.com webhook confirms a successful response.
 */
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const manifestPath = path.join(root, process.env.SHOWROOM_MANIFEST || 'showroom-products.json');
const enabled = process.env.DISPATCH_ENABLED === 'true';
const webhook = process.env.MAKE_WEBHOOK_URL || '';
const requestedId = process.env.DISPATCH_PRODUCT_ID || '';

function fail(message) {
  console.error(JSON.stringify({ ok: false, error: message }));
  process.exitCode = 1;
}

function main() {
  if (!fs.existsSync(manifestPath)) return fail('Manifest not found: ' + manifestPath);
  let manifest;
  try { manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8')); }
  catch { return fail('Manifest is not valid JSON'); }
  if (!manifest || !Array.isArray(manifest.products)) return fail('Manifest must contain a products array');

  const products = manifest.products;
  // An explicit ID narrows selection; it must never bypass the readiness gate.
  const product = requestedId
    ? products.find(item => item && String(item.id) === requestedId && item.dispatch_ready === true && item.dispatch !== 'SENT')
    : products.find(item => item && item.dispatch_ready === true && item.dispatch !== 'SENT');
  if (!product) {
    console.log(JSON.stringify({ ok: true, mode: enabled ? 'dispatch' : 'dry-run', dispatched: false, reason: requestedId ? 'requested_product_missing_or_not_dispatch_ready' : 'no_explicitly_dispatch_ready_product', product_count: products.length }));
    return;
  }
  if (!product.id || !product.name || !product.artifact_url) return fail('Selected product requires id, name, and artifact_url');
  const payload = {
    event: 'showroom.product.dispatch.requested',
    schema_version: 1,
    idempotency_key: crypto.createHash('sha256').update([product.id, product.version || '1', product.artifact_url].join('|')).digest('hex'),
    product: {
      id: String(product.id),
      name: String(product.name),
      description: String(product.description || ''),
      price_inr: Number.isFinite(Number(product.price_inr)) ? Number(product.price_inr) : null,
      currency: 'INR',
      url: String(product.artifact_url),
      category: String(product.category || 'general')
    },
    requested_at: new Date().toISOString(),
    mode: enabled ? 'live' : 'dry-run'
  };

  if (!enabled) {
    console.log(JSON.stringify({ ok: true, mode: 'dry-run', dispatched: false, reason: 'DISPATCH_ENABLED_not_true', payload }, null, 2));
    return;
  }
  let webhookUrl;
  try { webhookUrl = new URL(webhook); } catch { return fail('MAKE_WEBHOOK_URL must be a valid Make.com webhook URL'); }
  const allowedHost = webhookUrl.hostname === 'hook.make.com' || /^hook\\.[a-z0-9-]+\\.make\\.com$/i.test(webhookUrl.hostname);
  if (webhookUrl.protocol !== 'https:' || !allowedHost || webhookUrl.username || webhookUrl.password || (webhookUrl.port && webhookUrl.port !== '443')) {
    return fail('MAKE_WEBHOOK_URL must use HTTPS and an official hook.make.com or hook.<region>.make.com host');
  }

  fetch(webhookUrl.toString(), {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'idempotency-key': payload.idempotency_key },
    body: JSON.stringify(payload),
    signal: AbortSignal.timeout(15000)
  }).then(async response => {
    const responseText = (await response.text()).slice(0, 1000);
    if (!response.ok) return fail('Webhook returned HTTP ' + response.status + ': ' + responseText);
    console.log(JSON.stringify({ ok: true, mode: 'live', dispatched: true, product_id: product.id, idempotency_key: payload.idempotency_key, webhook_status: response.status, note: 'Webhook accepted the request; downstream platform publication must be independently verified.' }));
  }).catch(error => fail('Webhook request failed: ' + error.message));
}

main();
