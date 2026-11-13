import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

const migration = fs.readFileSync(new URL("../sql/migrations/20261113_central_records_email_ledger.sql", import.meta.url), "utf8");
const docs = fs.readFileSync(new URL("../../docs/CENTRAL-RECORDS-EMAIL-LEDGER.md", import.meta.url), "utf8");

test("central records migration is additive and safe to re-run", () => {
  assert.match(migration, /create extension if not exists pgcrypto/i);
  for (const table of ["communication_messages", "communication_attachments", "record_links", "audit_checkpoints"]) {
    assert.match(migration, new RegExp("create table if not exists " + table, "i"));
  }
  assert.match(migration, /create index if not exists communication_messages_thread_idx/i);
  assert.match(migration, /unique\s*\(provider,\s*mailbox,\s*provider_message_id\)/i);
  assert.doesNotMatch(migration, /\bdrop\s+(table|column|schema)\b/i);
  assert.doesNotMatch(migration, /\btruncate\b/i);
  assert.match(migration, /references accounts\(id\)/i);
});

test("email archive schema encodes privacy and integrity guardrails", () => {
  assert.match(migration, /encrypted_content bytea/i);
  assert.match(migration, /check \(encrypted = true\)/i);
  assert.match(migration, /jsonb_typeof\(to_addresses\) = 'array'/i);
  assert.match(migration, /jsonb_typeof\(metadata\) = 'object'/i);
  assert.match(migration, /content_sha256 char\(64\)/i);
  assert.match(docs, /Never store passwords, OTPs, payment PINs/i);
  assert.match(docs, /Not applied to any database/i);
});

test("rollout documentation does not represent mailbox sync as live", () => {
  assert.match(docs, /No mailbox connected, no email imported, no production route enabled/i);
  assert.match(docs, /Gmail\/SMTP provider connection authorized by the account owner/i);
});
