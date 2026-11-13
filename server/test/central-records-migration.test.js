import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

const migration = fs.readFileSync(new URL("../sql/migrations/20261113_central_records_email_ledger.sql", import.meta.url), "utf8");
const docs = fs.readFileSync(new URL("../../docs/CENTRAL-RECORDS-EMAIL-LEDGER.md", import.meta.url), "utf8");

test("central records migration is additive and contains each table once", () => {
  assert.match(migration, /create extension if not exists pgcrypto/i);
  for (const table of ["communication_messages", "communication_attachments", "record_links", "audit_checkpoints"]) {
    const matches = migration.match(new RegExp("create table if not exists " + table, "ig")) ?? [];
    assert.equal(matches.length, 1, table + " must be declared exactly once");
  }
  assert.match(migration, /create index if not exists communication_messages_thread_idx/i);
  assert.match(migration, /unique\s*\(provider,\s*mailbox,\s*provider_message_id\)/i);
  assert.doesNotMatch(migration, /\bdrop\s+(table|column|schema)\b/i);
  assert.doesNotMatch(migration, /\btruncate\b/i);
  assert.match(migration, /references accounts\(id\)/i);
  assert.equal((migration.match(/metadata jsonb not null/gi) ?? []).length, 1);
  assert.equal((migration.match(/encrypted boolean not null/gi) ?? []).length, 1);
});

test("email archive schema encodes privacy and integrity guardrails", () => {
  assert.match(migration, /encrypted_content bytea/i);
  assert.match(migration, /check \(encrypted = true\)/i);
  assert.match(migration, /jsonb_typeof\(to_addresses\) = 'array'/i);
  assert.match(migration, /jsonb_typeof\(metadata\) = 'object'/i);
  assert.match(migration, /content_sha256 char\(64\)/i);
  assert.match(migration, /\^\[0-9a-f\]\{64\}\$/i);
  assert.match(docs, /Never store passwords, OTPs, payment PINs/i);
  assert.match(docs, /migration has been tested on a temporary Neon branch only/i);\n  assert.match(docs, /has not been applied to production/i);
});

test("rollout documentation does not represent mailbox sync as live", () => {
  assert.match(docs, /No mailbox is connected and no email has been imported/i);\n  assert.match(docs, /Production routes are unchanged/i);
  assert.match(docs, /Gmail\/SMTP provider connection authorized by the account owner/i);
});
