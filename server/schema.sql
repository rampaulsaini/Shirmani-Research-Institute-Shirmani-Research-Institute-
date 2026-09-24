create table if not exists profiles (
  id uuid primary key,
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
