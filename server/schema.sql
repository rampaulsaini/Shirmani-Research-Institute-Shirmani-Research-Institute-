create extension if not exists pgcrypto;
create table if not exists accounts (
  id uuid primary key default gen_random_uuid(), email varchar(320) not null unique,
  password_hash text not null, role varchar(24) not null default 'user' check (role in ('user','moderator','admin')), created_at timestamptz not null default now()
);
create table if not exists profiles (
  id uuid primary key references accounts(id) on delete cascade,
  display_name varchar(80) not null default '', bio varchar(1000) not null default '',
  language varchar(32) not null default 'हिंदी', created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create table if not exists posts (
  id uuid primary key default gen_random_uuid(), author_id uuid not null references profiles(id) on delete cascade,
  text varchar(5000) not null, type varchar(32) not null default 'विचार',
  created_at timestamptz not null default now()
);
create table if not exists self_interviews (
  id uuid primary key default gen_random_uuid(), profile_id uuid not null references profiles(id) on delete cascade,
  question varchar(1000) not null, answer varchar(5000) not null, created_at timestamptz not null default now()
);
create table if not exists marketplace_listings (
  id uuid primary key default gen_random_uuid(), owner_id uuid not null references profiles(id) on delete cascade,
  kind varchar(32) not null check (kind in ('product','service','course','music','audio','job')),
  title varchar(160) not null, description varchar(5000) not null default '',
  price_minor bigint not null default 0 check (price_minor >= 0), currency char(3) not null default 'INR',
  status varchar(24) not null default 'draft' check (status in ('draft','published','paused','archived')),
  created_at timestamptz not null default now()
);
create table if not exists transactions (
  id uuid primary key default gen_random_uuid(), buyer_id uuid not null references accounts(id),
  seller_id uuid not null references accounts(id), listing_id uuid not null references marketplace_listings(id),
  amount_minor bigint not null check (amount_minor >= 0), currency char(3) not null,
  provider varchar(40), provider_reference varchar(200), status varchar(24) not null default 'created'
    check (status in ('created','pending','paid','failed','refunded','cancelled')),
  created_at timestamptz not null default now(), updated_at timestamptz not null default now()
);
create table if not exists reports (
  id uuid primary key default gen_random_uuid(), reporter_id uuid not null references accounts(id),
  target_type varchar(32) not null, target_id uuid not null, reason varchar(100) not null,
  details varchar(3000) not null default '', status varchar(24) not null default 'open'
    check (status in ('open','reviewing','resolved','dismissed','appealed')),
  created_at timestamptz not null default now(), resolved_at timestamptz
);
create table if not exists audit_events (
  id uuid primary key default gen_random_uuid(), actor_id uuid references accounts(id),
  event_type varchar(64) not null, target_type varchar(32), target_id uuid,
  metadata jsonb not null default '{}'::jsonb, created_at timestamptz not null default now()
);
create table if not exists ai_tasks (
  id uuid primary key default gen_random_uuid(), owner_id uuid references accounts(id),
  task_type varchar(64) not null, input jsonb not null default '{}'::jsonb,
  status varchar(24) not null default 'queued'
    check (status in ('queued','running','succeeded','failed','needs_human_review','cancelled')),
  result jsonb, created_at timestamptz not null default now(), updated_at timestamptz not null default now()
);
create index if not exists posts_created_at_idx on posts(created_at desc);
create index if not exists interviews_profile_idx on self_interviews(profile_id, created_at desc);
create index if not exists marketplace_listings_created_idx on marketplace_listings(created_at desc);
create index if not exists marketplace_listings_kind_idx on marketplace_listings(kind, created_at desc);
create index if not exists transactions_buyer_idx on transactions(buyer_id, created_at desc);
create index if not exists transactions_seller_idx on transactions(seller_id, created_at desc);
create index if not exists reports_status_idx on reports(status, created_at desc);
create index if not exists audit_events_target_idx on audit_events(target_type, target_id, created_at desc);
create index if not exists ai_tasks_status_idx on ai_tasks(status, created_at desc);


create index if not exists reports_target_idx on reports(target_type, target_id, created_at desc);
create index if not exists ai_tasks_owner_idx on ai_tasks(owner_id, created_at desc);
