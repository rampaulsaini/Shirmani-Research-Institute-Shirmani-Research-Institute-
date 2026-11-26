import { createHash, randomUUID } from "node:crypto";

const DEFAULT_MAX_BYTES = 10 * 1024 * 1024;
const DEFAULT_ALLOWED_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);

export class EvidenceError extends Error {
  constructor(code, status = 400) {
    super(code);
    this.name = "EvidenceError";
    this.code = code;
    this.status = status;
  }
}

const requiredString = (value, code) => {
  if (typeof value !== "string" || !value.trim()) throw new EvidenceError(code);
  return value.trim();
};

const validSha256 = value => typeof value === "string" && /^[a-f0-9]{64}$/i.test(value);

const assertAdapter = storage => {
  if (!storage || typeof storage.createUploadIntent !== "function" ||
      typeof storage.headObject !== "function" ||
      typeof storage.createSignedDownload !== "function" ||
      typeof storage.deleteObject !== "function") {
    throw new EvidenceError("EVIDENCE_STORAGE_NOT_CONFIGURED", 503);
  }
};

/**
 * Provider-neutral private evidence boundary.
 *
 * The adapter must keep objects private and implement the four methods below.
 * This module does not provide a provider implementation or expose public URLs.
 * Callers must persist the returned objectKey against the order/purpose and must
 * supply a database-backed authorization callback for every download.
 */
export function createPrivateEvidenceService({
  storage,
  maxBytes = DEFAULT_MAX_BYTES,
  allowedMimeTypes = DEFAULT_ALLOWED_TYPES,
  clock = () => Date.now()
} = {}) {
  const configured = () => {
    assertAdapter(storage);
    return storage;
  };

  const createUploadIntent = async ({
    actorId,
    orderId,
    purpose,
    contentType,
    byteLength,
    sha256
  } = {}) => {
    const adapter = configured();
    const owner = requiredString(actorId, "ACTOR_REQUIRED");
    const order = requiredString(orderId, "ORDER_REQUIRED");
    const evidencePurpose = requiredString(purpose, "EVIDENCE_PURPOSE_REQUIRED");
    const mime = requiredString(contentType, "CONTENT_TYPE_REQUIRED").toLowerCase();

    if (!allowedMimeTypes.has(mime)) throw new EvidenceError("EVIDENCE_CONTENT_TYPE_NOT_ALLOWED");
    if (!Number.isSafeInteger(byteLength) || byteLength < 1 || byteLength > maxBytes) {
      throw new EvidenceError("EVIDENCE_SIZE_NOT_ALLOWED");
    }
    if (!validSha256(sha256)) throw new EvidenceError("EVIDENCE_SHA256_REQUIRED");

    const objectKey = `private-evidence/${randomUUID()}`;
    const expiresAt = new Date(clock() + 5 * 60_000).toISOString();
    const result = await adapter.createUploadIntent({
      objectKey,
      contentType: mime,
      byteLength,
      metadata: {
        actorId: owner,
        orderId: order,
        purpose: evidencePurpose,
        sha256: sha256.toLowerCase()
      },
      expiresAt
    });

    if (!result || typeof result.uploadUrl !== "string" || !result.uploadUrl.startsWith("https://")) {
      throw new EvidenceError("EVIDENCE_UPLOAD_INTENT_INVALID", 503);
    }

    return { objectKey, uploadUrl: result.uploadUrl, expiresAt };
  };

  const finalizeUpload = async ({
    actorId,
    orderId,
    purpose,
    objectKey,
    expectedSha256
  } = {}) => {
    const adapter = configured();
    const owner = requiredString(actorId, "ACTOR_REQUIRED");
    const order = requiredString(orderId, "ORDER_REQUIRED");
    const evidencePurpose = requiredString(purpose, "EVIDENCE_PURPOSE_REQUIRED");
    const key = requiredString(objectKey, "EVIDENCE_OBJECT_KEY_REQUIRED");
    if (!/^private-evidence\/[0-9a-f-]{36}$/i.test(key)) throw new EvidenceError("EVIDENCE_OBJECT_KEY_INVALID");
    if (!validSha256(expectedSha256)) throw new EvidenceError("EVIDENCE_SHA256_REQUIRED");

    const object = await adapter.headObject(key);
    if (!object) throw new EvidenceError("EVIDENCE_OBJECT_NOT_FOUND", 404);
    const metadata = object.metadata || {};
    if (metadata.actorId !== owner || metadata.orderId !== order || metadata.purpose !== evidencePurpose) {
      throw new EvidenceError("EVIDENCE_METADATA_MISMATCH", 403);
    }
    if (!validSha256(object.sha256) || object.sha256.toLowerCase() !== expectedSha256.toLowerCase() ||
        metadata.sha256?.toLowerCase() !== expectedSha256.toLowerCase()) {
      throw new EvidenceError("EVIDENCE_HASH_MISMATCH", 422);
    }
    if (!Number.isSafeInteger(object.byteLength) || object.byteLength < 1 || object.byteLength > maxBytes) {
      throw new EvidenceError("EVIDENCE_SIZE_NOT_ALLOWED", 422);
    }
    if (!allowedMimeTypes.has(object.contentType)) throw new EvidenceError("EVIDENCE_CONTENT_TYPE_NOT_ALLOWED", 422);

    return {
      objectKey: key,
      sha256: object.sha256.toLowerCase(),
      byteLength: object.byteLength,
      contentType: object.contentType,
      verified: true
    };
  };

  const getAuthorizedDownload = async ({ actorId, objectKey, authorize } = {}) => {
    const adapter = configured();
    const owner = requiredString(actorId, "ACTOR_REQUIRED");
    const key = requiredString(objectKey, "EVIDENCE_OBJECT_KEY_REQUIRED");
    if (!/^private-evidence\/[0-9a-f-]{36}$/i.test(key)) throw new EvidenceError("EVIDENCE_OBJECT_KEY_INVALID");
    if (typeof authorize !== "function" || await authorize({ actorId: owner, objectKey: key }) !== true) {
      throw new EvidenceError("EVIDENCE_ACCESS_DENIED", 403);
    }

    const result = await adapter.createSignedDownload({ objectKey: key, expiresInSeconds: 60 });
    if (!result || typeof result.url !== "string" || !result.url.startsWith("https://")) {
      throw new EvidenceError("EVIDENCE_DOWNLOAD_UNAVAILABLE", 503);
    }
    return { url: result.url, expiresInSeconds: 60 };
  };

  const deleteEvidence = async ({ actorId, objectKey, authorize } = {}) => {
    const adapter = configured();
    const owner = requiredString(actorId, "ACTOR_REQUIRED");
    const key = requiredString(objectKey, "EVIDENCE_OBJECT_KEY_REQUIRED");
    if (!/^private-evidence\/[0-9a-f-]{36}$/i.test(key)) throw new EvidenceError("EVIDENCE_OBJECT_KEY_INVALID");
    if (typeof authorize !== "function" || await authorize({ actorId: owner, objectKey: key }) !== true) {
      throw new EvidenceError("EVIDENCE_ACCESS_DENIED", 403);
    }
    await adapter.deleteObject({ objectKey: key });
    return { deleted: true };
  };

  return Object.freeze({ createUploadIntent, finalizeUpload, getAuthorizedDownload, deleteEvidence });
}

export function sha256Hex(buffer) {
  if (!Buffer.isBuffer(buffer)) throw new TypeError("BUFFER_REQUIRED");
  return createHash("sha256").update(buffer).digest("hex");
}
