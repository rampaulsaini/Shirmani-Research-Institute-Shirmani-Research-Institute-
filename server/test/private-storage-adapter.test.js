import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { createPrivateStorageAdapter } from "../src/storage/private-storage-adapter.js";

function createFakeProvider({ now = () => Date.now(), grantTtlAdjustment = 0 } = {}) {
  const objects = new Map();
  const calls = [];
  return {
    objects,
    calls,
    async putObject(input) {
      calls.push({ method: "putObject", private: input.private, ifAbsent: input.ifAbsent });
      if (input.ifAbsent && objects.has(input.key)) throw new Error("OBJECT_ALREADY_EXISTS");
      objects.set(input.key, {
        body: Buffer.from(input.body),
        mimeType: input.mimeType,
        metadata: input.metadata,
        private: input.private
      });
    },
    async headObject({ key }) {
      const object = objects.get(key);
      if (!object) return null;
      return { mimeType: object.mimeType, byteSize: object.body.byteLength, ...object.metadata };
    },
    async getObject({ key }) {
      const object = objects.get(key);
      return object ? Buffer.from(object.body) : null;
    },
    async deleteObject({ key }) {
      return objects.delete(key);
    },
    async createReadGrant({ key, expiresInSeconds }) {
      if (!objects.has(key)) throw new Error("OBJECT_NOT_FOUND");
      return {
        url: "https://private.example.invalid/object/" + key,
        expiresAt: Math.floor(now() / 1000) + expiresInSeconds + grantTtlAdjustment
      };
    }
  };
}

const fixedNow = () => 1_800_000_000_000;
const allowed = async ({ actorId }) => actorId === "owner-1";

test("private adapter stores bytes with SHA-256, owner metadata and create-only semantics", async () => {
  const provider = createFakeProvider();
  const adapter = createPrivateStorageAdapter({ provider, authorize: allowed, now: fixedNow });
  const body = Buffer.from("private evidence");
  const result = await adapter.putObject({
    key: "orders/order-1/evidence.pdf",
    body,
    mimeType: "application/pdf",
    ownerId: "owner-1", actorId: "owner-1"
  });

  assert.equal(result.storage, "private");
  assert.equal(result.ownerId, "owner-1");
  assert.equal(result.byteSize, body.length);
  assert.equal(result.sha256, createHash("sha256").update(body).digest("hex"));
  assert.equal(provider.calls[0].private, true);
  assert.equal(provider.calls[0].ifAbsent, true);
  assert.deepEqual(await adapter.getObject({ key: result.key, actorId: "owner-1" }), body);
  await assert.rejects(
    adapter.putObject({ key: result.key, body, mimeType: "application/pdf", ownerId: "owner-1", actorId: "owner-1" }),
    /OBJECT_ALREADY_EXISTS/
  );
});

test("invalid keys, MIME types, bodies and oversized objects fail before provider writes", async () => {
  const provider = createFakeProvider();
  const adapter = createPrivateStorageAdapter({
    provider, authorize: allowed, maxObjectBytes: 8, now: fixedNow
  });
  const validBody = Buffer.from("12345678");

  for (const key of ["../secret", "/absolute", "orders//item", "orders/./item", "orders\\\\item"]) {
    await assert.rejects(adapter.putObject({
      key, body: Buffer.from("ok"), mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
    }), /INVALID_STORAGE_KEY/);
  }
  await assert.rejects(adapter.putObject({
    key: "orders/item", body: Buffer.from("ok"), mimeType: "text/html", ownerId: "owner-1", actorId: "owner-1"
  }), /UNSUPPORTED_MIME_TYPE/);
  await assert.rejects(adapter.putObject({
    key: "orders/item", body: Buffer.from("123456789"), mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
  }), /OBJECT_SIZE_OUT_OF_RANGE/);
  await assert.rejects(adapter.putObject({
    key: "orders/item", body: "not bytes", mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
  }), /INVALID_OBJECT_BODY/);
  assert.equal(provider.objects.size, 0);
  assert.equal(validBody.length, 8);
});

test("every private read, metadata lookup, delete and grant is authorization-gated", async () => {
  const provider = createFakeProvider();
  const adapter = createPrivateStorageAdapter({ provider, authorize: allowed, now: fixedNow });
  await adapter.putObject({
    key: "orders/order-1/file.txt", body: Buffer.from("secret"),
    mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
  });

  for (const operation of [
    () => adapter.putObject({ key: "orders/order-1/forged.txt", body: Buffer.from("x"), mimeType: "text/plain", ownerId: "owner-1", actorId: "intruder" }),
    () => adapter.headObject({ key: "orders/order-1/file.txt", actorId: "intruder" }),
    () => adapter.getObject({ key: "orders/order-1/file.txt", actorId: "intruder" }),
    () => adapter.deleteObject({ key: "orders/order-1/file.txt", actorId: "intruder" }),
    () => adapter.createReadGrant({ key: "orders/order-1/file.txt", actorId: "intruder" })
  ]) {
    await assert.rejects(operation, error => error.code === "STORAGE_ACCESS_DENIED");
  }

  assert.equal(provider.objects.size, 1);
  assert.equal(provider.calls.filter(call => call.method === "putObject").length, 1);
});

test("read grants are HTTPS-only and cannot exceed the configured short TTL", async () => {
  const provider = createFakeProvider({ now: fixedNow });
  const adapter = createPrivateStorageAdapter({
    provider, authorize: allowed, maxReadGrantSeconds: 120, now: fixedNow
  });
  await adapter.putObject({
    key: "orders/order-1/file.txt", body: Buffer.from("secret"),
    mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
  });

  const grant = await adapter.createReadGrant({
    key: "orders/order-1/file.txt", actorId: "owner-1", expiresInSeconds: 60
  });
  assert.equal(grant.access, "temporary_bearer_grant");
  assert.equal(grant.expiresAt, Math.floor(fixedNow() / 1000) + 60);

  await assert.rejects(adapter.createReadGrant({
    key: "orders/order-1/file.txt", actorId: "owner-1", expiresInSeconds: 121
  }), /READ_GRANT_TTL_OUT_OF_RANGE/);
});

test("adapter rejects provider grants that are expired or longer-lived than requested", async () => {
  const provider = createFakeProvider({ now: fixedNow, grantTtlAdjustment: 1 });
  const adapter = createPrivateStorageAdapter({ provider, authorize: allowed, now: fixedNow });
  await adapter.putObject({
    key: "orders/order-1/file.txt", body: Buffer.from("secret"),
    mimeType: "text/plain", ownerId: "owner-1", actorId: "owner-1"
  });
  await assert.rejects(adapter.createReadGrant({
    key: "orders/order-1/file.txt", actorId: "owner-1", expiresInSeconds: 60
  }), /INVALID_PROVIDER_READ_GRANT/);
});

test("provider and authorization configuration fail closed", () => {
  assert.throws(() => createPrivateStorageAdapter({ provider: {}, authorize: allowed }), /INVALID_STORAGE_PROVIDER/);
  assert.throws(() => createPrivateStorageAdapter({ provider: createFakeProvider() }), /AUTHORIZATION_CALLBACK_REQUIRED/);
});
