-- SRI Central Records & Email Ledger — additive, deployment-gated migration.
-- Encrypt message bodies and attachment bytes in the application before storage.
-- Never store passwords, OTPs, payment PINs, access tokens, or payment credentials.
-- Run only after server/sql/schema.sql has created the accounts table.
create extension if not exists pgcrypto;

create table if not exists communication_messages (
  id uuid primary key default gen_random_uuid(),
  provider text not null check (provider in ('gmail','smtp','imap','manual','other')),
  provider_message_id text,
  provider_thread_id text,
  direction text not null check (direction in ('inbound','outbound')),
  mailbox text not null,
  from_address text,
  to_addresses jsonb not null default '[]'::jsonb check (jsonb_typeof(to_addresses) = 'array'),
  cc_addresses jsonb not null default '[]'::jsonb check (jsonb_typeof(cc_addresses) = 'array'),
  subject text not null default '',
  sent_at timestamptz,
  received_at timestamptz,
  delivery_status text not null default 'unknown'
    check (delivery_status in ('unknown','queued','sent','delivered','bounced','failed')),
  encrypted_content bytea not null,
  content_key_version text not null,
  content_sha256 char(64) not null check (content_sha256 ~ '^[0-9a-f]{64}$'),
  metadata jsonb not null default '{}'::jsonb
    check (jsonb_typeof(metadata) = 'object'),
  created_at timestamptz not null default now(),
  unique (provider, mailbox, provider_message_id)
);
create index if not exists communication_messages_thread_idx
  on communication_messages(provider, mailbox, provider_thread_id, coalesce(sent_at, received_at, created_at) desc);
create index if not exists communication_messages_created_idx
  on communication_messages(created_at desc);

create table if not exists communication_attachments (
  id uuid primary key default gen_random_uuid(),
  message_id uuid not null references communication_messages(id) on delete restrict,
  file_name text not null,
  mime_type text not null,
  byte_size bigint not null check (byte_size >= 0),
  storage_key text not null,
  sha256 char(64) check (sha256 is null or sha256 ~ '^[0-9a-f]{64}$'),
  encrypted boolean not null default true check (encrypted = true),
  created_at timestamptz not null default now()
);
create index if not exists communication_attachments_message_idx
  on communication_attachments(message_id);

create table if not exists record_links (
  id uuid primary key default gen_random_uuid(),
  source_type text not null,
  source_id text not null,
  target_type text not null,
  target_id text not null,
  relation text not null,
  created_by uuid references accounts(id) on delete set null,
  created_at timestamptz not null default now(),
  unique (source_type, source_id, target_type, target_id, relation)
);
create index if not exists record_links_target_idx
  on record_links(target_type, target_id);

-- Application APIs must insert audit events only. DB-owner tampering still
-- requires periodic off-site exports/checkpoints for independent detection.
create table if not exists audit_checkpoints (
  id uuid primary key default gen_random_uuid(),
  range_start timestamptz not null,
  range_end timestamptz not null,
  event_count bigint not null check (event_count >= 0),
  digest_sha256 char(64) not null check (digest_sha256 ~ '^[0-9a-f]{64}$'),
  exported_uri text,
  created_at timestamptz not null default now(),
  check (range_end >= range_start)
);
create index if not exists audit_checkpoints_created_idx
  on audit_checkpoints(created_at desc);
