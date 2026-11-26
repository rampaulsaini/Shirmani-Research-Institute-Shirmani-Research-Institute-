import { createHash, randomBytes, randomUUID } from "node:crypto";

const DEFAULT_MIME_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "image/webp",
  "text/plain"
]);

function requireIdentity(actorId, ownerId) {
  if (typeof actorId !== "string" || !actorId || typeof ownerId !== "string" || !ownerId) {
    throw new TypeError("ACTOR_AND_OWNER_REQUIRED");
  }
  if (actorId !== ownerId) {
    const error = new Error("PRIVATE_EVIDENCE_ACCESS_DENIED");
    error.code = "PRIVATE_EVIDENCE_ACCESS_DENIED";
    throw error;
  }
}

/**
 * Provider-neutral private evidence service.
 *
 * An adapter must implement put(key, bytes, metadata), get(key), and delete(key).
 * The adapter is responsible for private-at-rest storage and must never expose
 * public object URLs. This service deliberately returns no provider URL.
 */
export function createPrivateEvidenceStorage({
  adapter,
  allowedMimeTypes = DEFAULT_MIME_TYPES,
  maxBytes = 10 * 1024 * 1024,
  grantTtlMs = 60_000,
  now = Date.now,
  audit = async () => {}
} = {}) {
  if (!adapter || !["put", "get", "delete"].every(name => typeof adapter[name] === "function")) {
    throw new TypeError("PRIVATE_STORAGE_ADAPTER_REQUIRES_PUT_GET_DELETE");
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) throw new TypeError("INVALID_MAX_BYTES");
  if (!Number.isSafeInteger(grantTtlMs) || grantTtlMs < 1 || grantTtlMs > 7 * 24 * 60 * 60 * 1000) {
    throw new TypeError("INVALID_GRANT_TTL");
  }

  const mimeAllowlist = new Set(allowedMimeTypes);
  const records = new Map();
  const grants = new Map();

  async function readVerifiedObject(record) {
    const bytes = await adapter.get(record.key);
    if (!bytes) {
      const error = new Error("PRIVATE_EVIDENCE_OBJECT_MISSING");
      error.code = "PRIVATE_EVIDENCE_OBJECT_MISSING";
      throw error;
    }
    const body = Buffer.from(bytes);
    const actualHash = createHash("sha256").update(body).digest("hex");
    if (body.length !== record.byteSize || actualHash !== record.sha256) {
      const error = new Error("PRIVATE_EVIDENCE_INTEGRITY_MISMATCH");
      error.code = "PRIVATE_EVIDENCE_INTEGRITY_MISMATCH";
      throw error;
    }
    return body;
  }

  async function removeRecord(key, record, eventType) {
    await adapter.delete(key);
    records.delete(key);
    for (const [token, grant] of grants) if (grant.key === key) grants.delete(token);
    await audit({ event_type: eventType, actor_id: record.ownerId, target_type: "private_evidence", target_id: key });
  }

  return Object.freeze({
    async store({ actorId, ownerId, bytes, mimeType }) {
      requireIdentity(actorId, ownerId);
      if (!mimeAllowlist.has(mimeType)) throw new TypeError("MIME_TYPE_NOT_ALLOWED");
      if (!(Buffer.isBuffer(bytes) || bytes instanceof Uint8Array)) throw new TypeError("BYTES_REQUIRED");
      const body = Buffer.from(bytes);
      if (body.length < 1 || body.length > maxBytes) throw new RangeError("EVIDENCE_SIZE_OUT_OF_RANGE");

      const key = `private-evidence/${randomUUID()}`;
      const sha256 = createHash("sha256").update(body).digest("hex");
      const record = { key, ownerId, mimeType, byteSize: body.length, sha256, createdAt: now() };
      await adapter.put(key, body, { contentType: mimeType, private: true, sha256 });
      records.set(key, record);
      try {
        await audit({ event_type: "private_evidence.stored", actor_id: actorId, target_type: "private_evidence", target_id: key, metadata: { mime_type: mimeType, byte_size: body.length, sha256 } });
      } catch (error) {
        await adapter.delete(key);
        records.delete(key);
        throw error;
      }
      return Object.freeze({ ...record });
    },

    async read({ actorId, ownerId, key }) {
      requireIdentity(actorId, ownerId);
      const record = records.get(key);
      if (!record || record.ownerId !== ownerId) {
        const error = new Error("PRIVATE_EVIDENCE_NOT_FOUND");
        error.code = "PRIVATE_EVIDENCE_NOT_FOUND";
        throw error;
      }
      const bytes = await readVerifiedObject(record);
      return { metadata: Object.freeze({ ...record }), bytes };
    },

    async issueReadGrant({ actorId, ownerId, key }) {
      requireIdentity(actorId, ownerId);
      const record = records.get(key);
      if (!record || record.ownerId !== ownerId) {
        const error = new Error("PRIVATE_EVIDENCE_NOT_FOUND");
        error.code = "PRIVATE_EVIDENCE_NOT_FOUND";
        throw error;
      }
      const token = randomBytes(32).toString("base64url");
      const expiresAt = now() + grantTtlMs;
      grants.set(token, { key, ownerId, expiresAt });
      try {
        await audit({ event_type: "private_evidence.read_grant_issued", actor_id: actorId, target_type: "private_evidence", target_id: key, metadata: { expires_at: new Date(expiresAt).toISOString(), single_use: true } });
      } catch (error) {
        grants.delete(token);
        throw error;
      }
      return Object.freeze({ token, expiresAt });
    },

    async readWithGrant({ token }) {
      if (typeof token !== "string" || !token) throw new TypeError("READ_GRANT_REQUIRED");
      const grant = grants.get(token);
      if (!grant) {
        const error = new Error("READ_GRANT_INVALID_OR_USED");
        error.code = "READ_GRANT_INVALID_OR_USED";
        throw error;
      }
      grants.delete(token);
      if (grant.expiresAt <= now()) {
        const error = new Error("READ_GRANT_EXPIRED");
        error.code = "READ_GRANT_EXPIRED";
        throw error;
      }
      const record = records.get(grant.key);
      if (!record || record.ownerId !== grant.ownerId) {
        const error = new Error("PRIVATE_EVIDENCE_NOT_FOUND");
        error.code = "PRIVATE_EVIDENCE_NOT_FOUND";
        throw error;
      }
      const bytes = await readVerifiedObject(record);
      await audit({ event_type: "private_evidence.read", actor_id: grant.ownerId, target_type: "private_evidence", target_id: grant.key });
      return { metadata: Object.freeze({ ...record }), bytes };
    },

    async delete({ actorId, ownerId, key }) {
      requireIdentity(actorId, ownerId);
      const record = records.get(key);
      if (!record || record.ownerId !== ownerId) {
        const error = new Error("PRIVATE_EVIDENCE_NOT_FOUND");
        error.code = "PRIVATE_EVIDENCE_NOT_FOUND";
        throw error;
      }
      await removeRecord(key, record, "private_evidence.deleted");
      return { deleted: true, key };
    },

    async deleteExpired({ actorId, ownerId, retentionMs }) {
      requireIdentity(actorId, ownerId);
      if (!Number.isSafeInteger(retentionMs) || retentionMs < 1) throw new TypeError("INVALID_RETENTION_MS");
      const cutoff = now() - retentionMs;
      const deleted = [];
      for (const [key, record] of records) {
        if (record.ownerId === ownerId && record.createdAt <= cutoff) {
          await removeRecord(key, record, "private_evidence.retention_deleted");
          deleted.push(key);
        }
      }
      return { deleted };
    }
  });
}

/**
 * Deterministic in-memory adapter for tests only. It is not durable storage.
 */
export function createMemoryPrivateObjectAdapter() {
  const objects = new Map();
  return Object.freeze({
    async put(key, bytes, metadata) {
      if (metadata?.private !== true) throw new Error("OBJECT_MUST_BE_PRIVATE");
      objects.set(key, { bytes: Buffer.from(bytes), metadata: { ...metadata } });
    },
    async get(key) {
      const object = objects.get(key);
      return object ? Buffer.from(object.bytes) : null;
    },
    async delete(key) {
      objects.delete(key);
    },
    async has(key) {
      return objects.has(key);
    },
    async inspect(key) {
      const object = objects.get(key);
      return object ? { metadata: { ...object.metadata }, byteSize: object.bytes.length } : null;
    }
  });
}
