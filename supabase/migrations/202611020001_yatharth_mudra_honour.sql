-- Yatharth Mudra is a non-monetary honour record, not a token or payment instrument.
-- Apply manually after reviewing the target Supabase project and migration history.
create table if not exists public.yatharth_mudra_honour (
  id uuid primary key default gen_random_uuid(),
  application_id text not null unique,
  subject_display_name text,
  status text not null default 'DRAFT_NOT_ISSUED'
    check (status in ('DRAFT_NOT_ISSUED','UNDER_REVIEW','APPROVED_PENDING_APPEAL','ISSUED','REVOKED')),
  philosophy jsonb not null,
  assessment jsonb not null,
  observation jsonb not null default '{}'::jsonb,
  reviewer_decisions jsonb not null default '[]'::jsonb,
  evidence_refs jsonb not null default '[]'::jsonb,
  certificate_payload_hash text
    check (certificate_payload_hash is null or certificate_payload_hash ~ '^[a-fA-F0-9]{64}$'),
  hash_algorithm text not null default 'SHA-256' check (hash_algorithm = 'SHA-256'),
  issued_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint issued_requires_hash check (status <> 'ISSUED' or certificate_payload_hash is not null)
);

comment on table public.yatharth_mudra_honour is
  'Private evidence and review ledger for a creator-defined non-monetary honour. Not legal tender, an investment, or proof of metaphysical claims.';

alter table public.yatharth_mudra_honour enable row level security;

-- No anon/authenticated policies are created intentionally: records remain private.
-- Access must be mediated by a trusted server using the Supabase service role,
-- with reviewer authorization, consent checks, audit logging, and least privilege.
-- Never expose the service-role key in browser code.
