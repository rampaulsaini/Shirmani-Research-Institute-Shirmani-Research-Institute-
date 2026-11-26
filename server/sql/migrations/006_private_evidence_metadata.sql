-- Durable metadata for private evidence objects.
-- Binary objects remain in a separately configured private object store.
create table if not exists private_evidence_objects (
  object_key text primary key
    check (object_key ~ '^private-evidence/[0-9a-f-]{36}$'),
  owner_id uuid not null references accounts(id) on delete restrict,
  mime_type text not null
    check (mime_type in ('application/pdf','image/jpeg','image/png','image/webp','text/plain')),
  byte_size bigint not null check (byte_size between 1 and 10485760),
  sha256 char(64) not null check (sha256 ~ '^[0-9a-f]{64}$'),
  created_at timestamptz not null default now()
);

create index if not exists private_evidence_objects_owner_created_idx
  on private_evidence_objects(owner_id, created_at asc, object_key asc);

comment on table private_evidence_objects is
'Private evidence object metadata only; bytes live in a separately configured private object store. No public URL is stored.';
