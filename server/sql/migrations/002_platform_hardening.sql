-- Yatharth Global Platform hardening migration 002.
-- Deployment-gated: apply only to managed PostgreSQL after review.
-- Adds media metadata, bounded AI/Automission work, privacy lifecycle, and evidence-aware verification.
-- It does not create payment, currency, employment, or independent-verification claims.

create table if not exists media_assets (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references accounts(id) on delete cascade,
  media_type text not null check (media_type in ('image','video','audio','document')),
  storage_key text not null,
  mime_type text not null,
  byte_size bigint not null check (byte_size >= 0),
  status text not null default 'pending' check (status in ('pending','ready','blocked','deleted')),
  created_at timestamptz not null default now()
);
create index if not exists media_assets_owner_idx on media_assets(owner_id, created_at desc);

create table if not exists ai_agents (
  id uuid primary key default gen_random_uuid(),
  agent_key text not null unique,
  display_name text not null,
  scope text not null,
  status text not null default 'enabled' check (status in ('enabled','paused','retired')),
  requires_human_review boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists ai_task_events (
  id uuid primary key default gen_random_uuid(),
  task_id uuid not null references ai_tasks(id) on delete cascade,
  agent_id uuid references ai_agents(id) on delete set null,
  event_type text not null,
  payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);
create index if not exists ai_task_events_task_idx on ai_task_events(task_id, created_at asc);

create table if not exists privacy_requests (
  id uuid primary key default gen_random_uuid(),
  account_id uuid not null references accounts(id) on delete cascade,
  request_type text not null check (request_type in ('export','delete','correction')),
  status text not null default 'requested' check (status in ('requested','processing','completed','rejected')),
  details text not null default '',
  created_at timestamptz not null default now(),
  completed_at timestamptz
);
create index if not exists privacy_requests_account_idx on privacy_requests(account_id, created_at desc);

create table if not exists verification_evidence (
  id uuid primary key default gen_random_uuid(),
  claim_id text not null,
  evidence_type text not null check (evidence_type in ('primary_source','secondary_source','counter_evidence','reproducible_test','human_review')),
  source_reference text,
  content_hash text,
  summary text not null default '',
  independent boolean not null default false,
  created_at timestamptz not null default now()
);
create index if not exists verification_evidence_claim_idx on verification_evidence(claim_id, created_at desc);

insert into ai_agents(agent_key,display_name,scope,requires_human_review)
values
 ('research-organizer','Research Organizer','classify, deduplicate and structure research records',true),
 ('evidence-indexer','Evidence Indexer','index sources and counter-evidence without declaring truth',true),
 ('translation-assist','Translation Assist','translate while preserving source provenance',false),
 ('platform-health','Platform Health','observe service/workflow health and prepare recovery actions',true)
on conflict (agent_key) do nothing;

comment on table verification_evidence is
'Supporting evidence records only. Evidence presence never changes a claim to independently verified.';
comment on table ai_agents is
'Bounded automation registry. Agents cannot independently certify philosophical or scientific truth.';


-- Payment-provider and other system-originated audit events may have no user actor.
-- The canonical schema uses a nullable actor_id for this bounded system-event case.
alter table if exists audit_events alter column actor_id drop not null;
