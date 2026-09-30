-- Shirmani / Yatharth public-platform PostgreSQL baseline schema.
-- Apply with: psql "$DATABASE_URL" -f server/sql/schema.sql
create extension if not exists pgcrypto;

create table if not exists accounts (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  password_hash text not null,
  created_at timestamptz not null default now()
);

create table if not exists profiles (
  id uuid primary key references accounts(id) on delete cascade,
  display_name text not null default '',
  bio text not null default '',
  language text not null default 'हिंदी',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists posts (
  id uuid primary key default gen_random_uuid(),
  author_id uuid not null references accounts(id) on delete cascade,
  text text not null,
  type text not null default 'विचार',
  created_at timestamptz not null default now()
);
create index if not exists posts_created_at_idx on posts(created_at desc);

create table if not exists self_interviews (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null references accounts(id) on delete cascade,
  question text not null,
  answer text not null,
  created_at timestamptz not null default now()
);

create table if not exists marketplace_listings (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references accounts(id) on delete cascade,
  kind text not null check (kind in ('product','service','course','music','audio','job')),
  title text not null,
  description text not null default '',
  price_minor bigint not null default 0 check (price_minor >= 0),
  currency char(3) not null default 'INR',
  status text not null default 'draft' check (status in ('draft','published','paused','archived')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists marketplace_listings_public_idx on marketplace_listings(status,created_at desc);

create table if not exists ai_tasks (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references accounts(id) on delete cascade,
  task_type text not null,
  input jsonb not null default '{}'::jsonb,
  status text not null default 'queued' check (status in ('queued','running','completed','failed','cancelled')),
  result jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists reports (
  id uuid primary key default gen_random_uuid(),
  reporter_id uuid not null references accounts(id) on delete cascade,
  target_type text not null,
  target_id text not null,
  reason text not null,
  details text not null default '',
  status text not null default 'open' check (status in ('open','under_review','resolved','dismissed')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists audit_events (
  id uuid primary key default gen_random_uuid(),
  actor_id uuid references accounts(id) on delete set null,
  event_type text not null,
  target_type text not null,
  target_id text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);
create index if not exists audit_events_actor_idx on audit_events(actor_id,created_at desc);

create table if not exists transactions (
  id uuid primary key default gen_random_uuid(),
  buyer_id uuid not null references accounts(id) on delete restrict,
  seller_id uuid not null references accounts(id) on delete restrict,
  listing_id uuid not null references marketplace_listings(id) on delete restrict,
  amount_minor bigint not null check (amount_minor >= 0),
  currency char(3) not null,
  status text not null default 'intent' check (status in ('intent','pending','paid','failed','refunded','cancelled')),
  provider text,
  provider_reference text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists transactions_participant_idx on transactions(buyer_id,seller_id,created_at desc);

-- Marketplace order intent/lifecycle. Payment provider integration remains deployment-gated.
create table if not exists orders (
  id uuid primary key default gen_random_uuid(),
  buyer_id uuid not null references accounts(id) on delete restrict,
  seller_id uuid not null references accounts(id) on delete restrict,
  listing_id uuid not null references marketplace_listings(id) on delete restrict,
  quantity integer not null default 1 check (quantity between 1 and 100),
  unit_amount_minor bigint not null check (unit_amount_minor >= 0),
  total_amount_minor bigint not null check (total_amount_minor >= 0),
  currency char(3) not null,
  status text not null default 'intent' check (status in ('intent','pending','paid','fulfilled','completed','failed','refunded','cancelled')),
  provider text,
  provider_reference text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists orders_participant_idx on orders(buyer_id,seller_id,created_at desc);


-- Social interaction primitives.
create table if not exists follows (
  follower_id uuid not null references accounts(id) on delete cascade,
  followed_id uuid not null references accounts(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (follower_id, followed_id),
  check (follower_id <> followed_id)
);

create table if not exists comments (
  id uuid primary key default gen_random_uuid(),
  post_id uuid not null references posts(id) on delete cascade,
  author_id uuid not null references accounts(id) on delete cascade,
  text text not null,
  created_at timestamptz not null default now()
);

create table if not exists reactions (
  post_id uuid not null references posts(id) on delete cascade,
  user_id uuid not null references accounts(id) on delete cascade,
  reaction text not null,
  created_at timestamptz not null default now(),
  primary key (post_id,user_id)
);

create table if not exists notifications (
  id uuid primary key default gen_random_uuid(),
  recipient_id uuid not null references accounts(id) on delete cascade,
  actor_id uuid references accounts(id) on delete set null,
  kind text not null,
  target_type text,
  target_id text,
  payload jsonb not null default '{}'::jsonb,
  read_at timestamptz,
  created_at timestamptz not null default now()
);
create index if not exists notifications_recipient_idx on notifications(recipient_id,created_at desc);

-- Media is metadata only; binary storage must be supplied by a production object-storage provider.
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

-- Bounded Automission/privacy/evidence hardening primitives.
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
create table if not exists privacy_requests (
  id uuid primary key default gen_random_uuid(),
  account_id uuid not null references accounts(id) on delete cascade,
  request_type text not null check (request_type in ('export','delete','correction')),
  status text not null default 'requested' check (status in ('requested','processing','completed','rejected')),
  details text not null default '',
  created_at timestamptz not null default now(),
  completed_at timestamptz
);
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
create index if not exists ai_task_events_task_idx on ai_task_events(task_id,created_at asc);
create index if not exists privacy_requests_account_idx on privacy_requests(account_id,created_at desc);
create index if not exists verification_evidence_claim_idx on verification_evidence(claim_id,created_at desc);

insert into ai_agents(agent_key,display_name,scope,requires_human_review) values
('research-organizer','Research Organizer','classify, deduplicate and structure research records',true),
('evidence-indexer','Evidence Indexer','index sources and counter-evidence without declaring truth',true),
('translation-assist','Translation Assist','translate while preserving source provenance',false),
('platform-health','Platform Health','observe service/workflow health and prepare recovery actions',true)
on conflict(agent_key) do nothing;

-- Learning/work/dispute primitives; workflows remain deployment-gated.
create table if not exists course_enrollments (
  id uuid primary key default gen_random_uuid(),
  course_listing_id uuid not null references marketplace_listings(id) on delete restrict,
  learner_id uuid not null references accounts(id) on delete cascade,
  status text not null default 'active' check (status in ('active','completed','cancelled')),
  created_at timestamptz not null default now(),
  unique(course_listing_id,learner_id)
);

create table if not exists work_orders (
  id uuid primary key default gen_random_uuid(),
  listing_id uuid references marketplace_listings(id) on delete restrict,
  client_id uuid not null references accounts(id) on delete restrict,
  worker_id uuid references accounts(id) on delete restrict,
  status text not null default 'requested' check (status in ('requested','accepted','in_progress','delivered','completed','cancelled','disputed')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists disputes (
  id uuid primary key default gen_random_uuid(),
  opened_by uuid not null references accounts(id) on delete restrict,
  target_type text not null,
  target_id text not null,
  reason text not null,
  status text not null default 'open' check (status in ('open','under_review','resolved','appealed','closed')),
  resolution text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists verification_reviews (
  id uuid primary key default gen_random_uuid(),
  claim_id text not null,
  reviewer_type text not null check (reviewer_type in ('independent_human','source','automated_assist')),
  reviewer_reference text,
  evidence jsonb not null default '{}'::jsonb,
  decision text not null default 'inconclusive' check (decision in ('verified','partially_supported','inconclusive','not_verified')),
  notes text not null default '',
  created_at timestamptz not null default now()
);
