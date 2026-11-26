import assert from "node:assert/strict";
import test from "node:test";
import { createPostgresPrivateMetadataStore } from "../src/postgres-private-evidence-metadata.js";

function fakePool(rows = []) {
  const calls = [];
  return {
    calls,
    async query(sql, values = []) {
      calls.push({ sql, values });
      if (/^select/i.test(sql.trim())) return { rows };
      return { rows: [], rowCount: 1 };
    }
  };
}

test("PostgreSQL metadata adapter uses parameterized queries", async () => {
  const pool = fakePool();
  const store = createPostgresPrivateMetadataStore(pool);
  const record = {
    key: "private-evidence/123e4567-e89b-12d3-a456-426614174000",
    ownerId: "123e4567-e89b-12d3-a456-426614174001",
    mimeType: "text/plain",
    byteSize: 12,
    sha256: "a".repeat(64),
    createdAt: 1_800_000_000_000
  };
  await store.put(record);
  await store.get(record.key);
  await store.delete(record.key);
  await store.listByOwner(record.ownerId);

  assert.equal(pool.calls.length, 4);
  for (const call of pool.calls) assert.match(call.sql, /\$1/);
  assert.deepEqual(pool.calls[0].values, [
    record.key, record.ownerId, record.mimeType, record.byteSize, record.sha256, record.createdAt
  ]);
  assert.deepEqual(pool.calls[1].values, [record.key]);
  assert.deepEqual(pool.calls[2].values, [record.key]);
  assert.deepEqual(pool.calls[3].values, [record.ownerId]);
});

test("maps PostgreSQL metadata rows to the service record shape", async () => {
  const pool = fakePool([{
    object_key: "private-evidence/123e4567-e89b-12d3-a456-426614174000",
    owner_id: "123e4567-e89b-12d3-a456-426614174001",
    mime_type: "image/png",
    byte_size: "2048",
    sha256: "b".repeat(64),
    created_at: "2026-11-26T12:00:00.000Z"
  }]);
  const record = await createPostgresPrivateMetadataStore(pool).get("private-evidence/123e4567-e89b-12d3-a456-426614174000");
  assert.equal(record.ownerId, "123e4567-e89b-12d3-a456-426614174001");
  assert.equal(record.byteSize, 2048);
  assert.equal(record.mimeType, "image/png");
  assert.equal(record.createdAt, Date.parse("2026-11-26T12:00:00.000Z"));
});

test("rejects unsafe byte-size values returned by PostgreSQL", async () => {
  const pool = fakePool([{
    object_key: "private-evidence/123e4567-e89b-12d3-a456-426614174000",
    owner_id: "123e4567-e89b-12d3-a456-426614174001",
    mime_type: "text/plain",
    byte_size: "9007199254740993",
    sha256: "c".repeat(64),
    created_at: "2026-11-26T12:00:00.000Z"
  }]);
  await assert.rejects(
    createPostgresPrivateMetadataStore(pool).get("private-evidence/123e4567-e89b-12d3-a456-426614174000"),
    /PRIVATE_EVIDENCE_BYTE_SIZE_INVALID/
  );
});
