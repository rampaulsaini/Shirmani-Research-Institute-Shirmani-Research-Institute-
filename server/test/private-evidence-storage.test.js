import assert from "node:assert/strict";
import test from "node:test";
import {
  createMemoryPrivateObjectAdapter,
  createPrivateEvidenceStorage
} from "../src/private-evidence-storage.js";

function setup(options = {}) {
  let time = 1_800_000_000_000;
  const events = [];
  const adapter = createMemoryPrivateObjectAdapter();
  const storage = createPrivateEvidenceStorage({
    adapter,
    maxBytes: 8,
    grantTtlMs: 1_000,
    now: () => time,
    audit: async event => { events.push(event); },
    ...options
  });
  return { adapter, storage, events, advance: ms => { time += ms; } };
}

test("stores private bytes with generated key, exact size and SHA-256", async () => {
  const { adapter, storage, events } = setup();
  const result = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("hello"), mimeType: "text/plain" });
  assert.match(result.key, /^private-evidence\/[0-9a-f-]{36}$/);
  assert.equal(result.byteSize, 5);
  assert.equal(result.sha256, "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824");
  assert.deepEqual(await adapter.inspect(result.key), {
    metadata: { contentType: "text/plain", private: true, sha256: result.sha256 },
    byteSize: 5
  });
  assert.equal(events[0].event_type, "private_evidence.stored");
});

test("rejects another actor and unsupported MIME types", async () => {
  const { storage } = setup();
  await assert.rejects(storage.store({ actorId: "intruder", ownerId: "owner-1", bytes: Buffer.from("x"), mimeType: "text/plain" }), { code: "PRIVATE_EVIDENCE_ACCESS_DENIED" });
  await assert.rejects(storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("x"), mimeType: "text/html" }), /MIME_TYPE_NOT_ALLOWED/);
});

test("rejects empty, oversized and non-byte payloads", async () => {
  const { storage } = setup();
  const base = { actorId: "owner-1", ownerId: "owner-1", mimeType: "text/plain" };
  await assert.rejects(storage.store({ ...base, bytes: Buffer.alloc(0) }), /EVIDENCE_SIZE_OUT_OF_RANGE/);
  await assert.rejects(storage.store({ ...base, bytes: Buffer.alloc(9) }), /EVIDENCE_SIZE_OUT_OF_RANGE/);
  await assert.rejects(storage.store({ ...base, bytes: "not bytes" }), /BYTES_REQUIRED/);
});

test("allows only the owner to retrieve evidence; no public URL is exposed", async () => {
  const { storage } = setup();
  const stored = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("private"), mimeType: "text/plain" });
  await assert.rejects(storage.read({ actorId: "other", ownerId: "owner-1", key: stored.key }), { code: "PRIVATE_EVIDENCE_ACCESS_DENIED" });
  const read = await storage.read({ actorId: "owner-1", ownerId: "owner-1", key: stored.key });
  assert.equal(read.bytes.toString(), "private");
  assert.equal("url" in read, false);
});

test("issues expiring single-use read grants", async () => {
  const { storage, advance } = setup();
  const stored = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("grant"), mimeType: "text/plain" });
  const grant = await storage.issueReadGrant({ actorId: "owner-1", ownerId: "owner-1", key: stored.key });
  assert.equal((await storage.readWithGrant({ token: grant.token })).bytes.toString(), "grant");
  await assert.rejects(storage.readWithGrant({ token: grant.token }), { code: "READ_GRANT_INVALID_OR_USED" });

  const expiring = await storage.issueReadGrant({ actorId: "owner-1", ownerId: "owner-1", key: stored.key });
  advance(1_001);
  await assert.rejects(storage.readWithGrant({ token: expiring.token }), { code: "READ_GRANT_EXPIRED" });
});

test("deletes evidence and revokes outstanding grants", async () => {
  const { storage, adapter } = setup();
  const stored = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("delete"), mimeType: "text/plain" });
  const grant = await storage.issueReadGrant({ actorId: "owner-1", ownerId: "owner-1", key: stored.key });
  await storage.delete({ actorId: "owner-1", ownerId: "owner-1", key: stored.key });
  assert.equal(await adapter.has(stored.key), false);
  await assert.rejects(storage.readWithGrant({ token: grant.token }), { code: "READ_GRANT_INVALID_OR_USED" });
});

test("retention deletion removes only the owner's records older than the cutoff", async () => {
  const { storage, advance, adapter } = setup();
  const old = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("old"), mimeType: "text/plain" });
  advance(500);
  const recent = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("new"), mimeType: "text/plain" });
  const other = await storage.store({ actorId: "owner-2", ownerId: "owner-2", bytes: Buffer.from("theirs"), mimeType: "text/plain" });
  advance(501);
  const result = await storage.deleteExpired({ actorId: "owner-1", ownerId: "owner-1", retentionMs: 1_000 });
  assert.deepEqual(result.deleted, [old.key]);
  assert.equal(await adapter.has(old.key), false);
  assert.equal(await adapter.has(recent.key), true);
  assert.equal(await adapter.has(other.key), true);
});

test("rolls back stored object if audit persistence fails", async () => {
  const adapter = createMemoryPrivateObjectAdapter();
  const storage = createPrivateEvidenceStorage({ adapter, audit: async () => { throw new Error("audit unavailable"); } });
  await assert.rejects(storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("audit"), mimeType: "text/plain" }), /audit unavailable/);
});

test("rejects tampered object bytes instead of returning unverified evidence", async () => {
  const backing = createMemoryPrivateObjectAdapter();
  const adapter = {
    put: (...args) => backing.put(...args),
    get: async key => {
      const bytes = await backing.get(key);
      return bytes ? Buffer.from("tampered") : null;
    },
    delete: (...args) => backing.delete(...args)
  };
  const storage = createPrivateEvidenceStorage({ adapter });
  const stored = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("original"), mimeType: "text/plain" });
  await assert.rejects(storage.read({ actorId: "owner-1", ownerId: "owner-1", key: stored.key }), { code: "PRIVATE_EVIDENCE_INTEGRITY_MISMATCH" });
});

test("does not leave a usable read grant when grant audit persistence fails", async () => {
  const adapter = createMemoryPrivateObjectAdapter();
  let failGrantAudit = false;
  const storage = createPrivateEvidenceStorage({
    adapter,
    audit: async event => {
      if (failGrantAudit && event.event_type === "private_evidence.read_grant_issued") throw new Error("audit unavailable");
    }
  });
  const stored = await storage.store({ actorId: "owner-1", ownerId: "owner-1", bytes: Buffer.from("grant"), mimeType: "text/plain" });
  failGrantAudit = true;
  await assert.rejects(storage.issueReadGrant({ actorId: "owner-1", ownerId: "owner-1", key: stored.key }), /audit unavailable/);
});
