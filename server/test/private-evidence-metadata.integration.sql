begin;

do $$
declare
  test_owner uuid;
  test_key text := 'private-evidence/123e4567-e89b-12d3-a456-426614174099';
begin
  if to_regclass('public.private_evidence_objects') is null then
    raise exception 'private_evidence_objects table missing';
  end if;

  insert into accounts(email, password_hash)
  values ('private-evidence-migration-test@example.invalid', 'test-only')
  returning id into test_owner;

  insert into private_evidence_objects(object_key, owner_id, mime_type, byte_size, sha256)
  values (test_key, test_owner, 'text/plain', 4, repeat('a', 64));

  if not exists (
    select 1 from private_evidence_objects
    where object_key = test_key and owner_id = test_owner and byte_size = 4
  ) then
    raise exception 'valid private evidence metadata insert failed';
  end if;

  begin
    insert into private_evidence_objects(object_key, owner_id, mime_type, byte_size, sha256)
    values ('private-evidence/123e4567-e89b-12d3-a456-426614174098', test_owner, 'text/html', 4, repeat('a', 64));
    raise exception 'unsupported MIME type unexpectedly accepted';
  exception when check_violation then
    null;
  end;

  begin
    insert into private_evidence_objects(object_key, owner_id, mime_type, byte_size, sha256)
    values ('private-evidence/123e4567-e89b-12d3-a456-426614174097', test_owner, 'text/plain', 0, repeat('a', 64));
    raise exception 'zero-byte evidence unexpectedly accepted';
  exception when check_violation then
    null;
  end;

  delete from private_evidence_objects where object_key = test_key;
  delete from accounts where id = test_owner;
end;
$$;

rollback;
