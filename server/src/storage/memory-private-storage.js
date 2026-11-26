import { createHash, createHmac, randomBytes, timingSafeEqual } from "node:crypto";

const DEFAULT_MIME_TYPES = [
  "application/pdf",
  "image/jpeg",
  "image/png",
  "image/webp",
  "audio/mpeg",
  "audio/mp4",
  "video/mp4",
  "text/plain"
];

const cleanId = (value, field) => {
  if (typeof value !== "string" || !value.trim() || value.length > 200) {
    throw new TypeError(`${field} is required`);
  }
  return value.trim();
};

const sha256 = value => createHash("sha256").update(value).digest("hex");

/**
 * In-memory, test-only implementation of the private object-storage contract.
 * It is deliberately not wired to HTTP routes or production configuration.
 * Grants are opaque bearer tokens for tests, not signed URLs.
 */
export function createMemoryPrivateStorageAdapter({
  clock = () => Date.now(),
  maxBytes = 5 * 1024 * 1024,
  allowedMimeTypes = DEFAULT_MIME_TYPES,
  grantTtlMs = 60_000,
  grantSecret = randomBytes(32)
} = {}) {
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) throw new TypeError("maxBytes must be a positive safe integer");
  if (!Number.isSafeInteger(grantTtlMs) || grantTtlMs < 1 || grantTtlMs > 300_000) {
    throw new TypeError("grantTtlMs must be between 1 and 300000");
  }
  const secret = Buffer.isBuffer(grantSecret) ? grantSecret : Buffer.from(String(grantSecret));
  if (secret.length < 32) throw new TypeError("grantSecret must contain at least 32 bytes");

  const mimeAllowlist = new Set(allowedMimeTypes);
  const objects = new Map();
  const consumedGrants = new Set();
  const audit = [];

  const storageId = (ownerId, objectKey) => `${cleanId(ownerId, "ownerId")}\u0000${cleanId(objectKey, "objectKey")}`;
  const record = (actorId, action, objectKey, details = {}) => {
    audit.push(Object.freeze({
      actor_id: actorId,
      action,
      object_key: objectKey,
      at: new Date(clock()).toISOString(),
      ...details
    }));
  };
  const sign = payload => createHmac("sha256", secret).update(payload).digest("base64url");

  function put({ ownerId, objectKey, body, mimeType, expectedSha256 }) {
    const normalizedOwnerId = cleanId(ownerId, "ownerId");
    const normalizedObjectKey = cleanId(objectKey, "objectKey");
    const id = storageId(normalizedOwnerId, normalizedObjectKey);
    if (!Buffer.isBuffer(body) && !(body instanceof Uint8Array)) throw new TypeError("body must be bytes");
    const bytes = Buffer.from(body);
    if (bytes.length < 1 || bytes.length > maxBytes) throw new RangeError("OBJECT_SIZE_NOT_ALLOWED");
    if (typeof mimeType !== "string" || !mimeAllowlist.has(mimeType)) throw new TypeError("MIME_TYPE_NOT_ALLOWED");
    const digest = sha256(bytes);
    if (expectedSha256 !== undefined && expectedSha256 !== digest) throw new Error("SHA256_MISMATCH");
    if (objects.has(id)) throw new Error("OBJECT_ALREADY_EXISTS");

    const createdAt = new Date(clock()).toISOString();
    const metadata = Object.freeze({
      owner_id: normalizedOwnerId,
      object_key: normalizedObjectKey,
      mime_type: mimeType,
      byte_size: bytes.length,
      sha256: digest,
      status: "ready",
      created_at: createdAt
    });
    objects.set(id, { metadata, body: Buffer.from(bytes) });
    record(normalizedOwnerId, "object.created", normalizedObjectKey, { sha256: digest, byte_size: bytes.length });
    return metadata;
  }

  function head({ ownerId, objectKey }) {
    const id = storageId(ownerId, objectKey);
    const entry = objects.get(id);
    if (!entry) return null;
    record(ownerId, "object.metadata_read", objectKey);
    return entry.metadata;
  }

  function get({ ownerId, objectKey }) {
    const id = storageId(ownerId, objectKey);
    const entry = objects.get(id);
    if (!entry) return null;
    record(ownerId, "object.read", objectKey);
    return Buffer.from(entry.body);
  }

  function issueReadGrant({ ownerId, objectKey, ttlMs = grantTtlMs }) {
    const id = storageId(ownerId, objectKey);
    if (!objects.has(id)) throw new Error("OBJECT_NOT_FOUND");
    if (!Number.isSafeInteger(ttlMs) || ttlMs < 1 || ttlMs > grantTtlMs) throw new RangeError("GRANT_TTL_NOT_ALLOWED");
    const payload = Buffer.from(JSON.stringify({
      owner_id: ownerId,
      object_key: objectKey,
      expires_at: clock() + ttlMs,
      nonce: randomBytes(16).toString("hex")
    })).toString("base64url");
    const grant = `${payload}.${sign(payload)}`;
    record(ownerId, "object.read_grant_issued", objectKey, { expires_in_ms: ttlMs });
    return grant;
  }

  function redeemReadGrant({ grant }) {
    if (typeof grant !== "string") throw new TypeError("grant is required");
    const [payload, signature, extra] = grant.split(".");
    if (!payload || !signature || extra !== undefined) throw new Error("INVALID_GRANT");
    const expected = Buffer.from(sign(payload));
    const supplied = Buffer.from(signature);
    if (expected.length !== supplied.length || !timingSafeEqual(expected, supplied)) throw new Error("INVALID_GRANT");
    let claims;
    try { claims = JSON.parse(Buffer.from(payload, "base64url").toString("utf8")); }
    catch { throw new Error("INVALID_GRANT"); }
    if (!Number.isFinite(claims.expires_at) || claims.expires_at <= clock()) throw new Error("GRANT_EXPIRED");
    if (consumedGrants.has(claims.nonce)) throw new Error("GRANT_ALREADY_USED");
    const id = storageId(claims.owner_id, claims.object_key);
    const entry = objects.get(id);
    if (!entry) throw new Error("OBJECT_NOT_FOUND");
    consumedGrants.add(claims.nonce);
    record("grant", "object.read_grant_redeemed", claims.object_key);
    return { metadata: entry.metadata, body: Buffer.from(entry.body) };
  }

  function remove({ ownerId, objectKey }) {
    const id = storageId(ownerId, objectKey);
    const entry = objects.get(id);
    if (!entry) return false;
    objects.delete(id);
    record(ownerId, "object.deleted", objectKey, { sha256: entry.metadata.sha256 });
    return true;
  }

  function listAudit() {
    return audit.map(entry => ({ ...entry }));
  }

  return Object.freeze({ put, head, get, issueReadGrant, redeemReadGrant, remove, listAudit });
}

export { DEFAULT_MIME_TYPES };
