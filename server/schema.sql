create extension if not exists pgcrypto;
create table if not exists accounts (
  id uuid primary key default gen_random_uuid(),
  email varchar(320) not null unique,
  password_hash text not null,
  created_at timestamptz not null default now()
);
create table if not exists profiles (
  id uuid primary key references accounts(id) on delete cascade,
  display_name varchar(80) not null default '',
  bio varchar(1000) not null default '',
  language varchar(32) not null default 'हिंदी',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create table if not exists posts (
  id uuid primary key default gen_random_uuid(),
  author_id uuid not null references profiles(id) on delete cascade,
  text varchar(5000) not null,
  type varchar(32) not null default 'विचार',
  created_at timestamptz not null default now()
);
create table if not exists self_interviews (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null references profiles(id) on delete cascade,
  question varchar(1000) not null,
  answer varchar(5000) not null,
  created_at timestamptz not null default now()
);
create index if not exists posts_created_at_idx on posts(created_at desc);
create index if not exists interviews_profile_idx on self_interviews(profile_id, created_at desc);


create table if not exists marketplace_listings (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references profiles(id) on delete cascade,
  kind varchar(32) not null check (kind in ('product','service','course','music','audio','job')),
  title varchar(160) not null,
  description varchar(5000) not null default '',
  price_minor bigint not null default 0 check (price_minor >= 0),
  currency char(3) not null default 'INR',
  status varchar(24) not null default 'draft' check (status in ('draft','published','paused','archived')),
  created_at timestamptz not null default now()
);
create index if not exists marketplace_listings_created_idx on marketplace_listings(created_at desc);
create index if not exists marketplace_listings_kind_idx on marketplace_listings(kind, created_at desc);
