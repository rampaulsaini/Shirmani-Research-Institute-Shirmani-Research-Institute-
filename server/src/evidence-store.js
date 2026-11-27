/**
 * Provider-neutral private evidence storage contract.
 *
 * This module deliberately contains no cloud SDK, local filesystem fallback,
 * credentials, upload route, or production adapter. A real adapter must be
 * selected and reviewed separately before it can be wired into HTTP routes.
 */

export const EVIDENCE_PURPOSES = Object.freeze([
  "written_acceptance",
  "payment_proof",
  "customer_consent",
  "delivery",
  "customer_acceptance"
]);

export const EVIDENCE_CONTENT_TYPES = Object.freeze([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);

export const DEFAULT_MAX_EVIDENCE_BYTES = 10 * 1024 * 1024;

export function validateEvidenceMetadata(metadata, {
  maxBytes = DEFAULT_MAX_EVIDENCE_BYTES
} = {}) {
  if (!metadata || typeof metadata !== "object" || Array.isArray(metadata)) {
    throw new TypeError("EVIDENCE_METADATA_REQUIRED");
  }
  if (!EVIDENCE_PURPOSES.includes(metadata.purpose)) {
    throw new TypeError("EVIDENCE_PURPOSE_INVALID");
  }
  if (typeof metadata.contentType !== "string" ||
      !EVIDENCE_CONTENT_TYPES.includes(metadata.contentType)) {
    throw new TypeError("EVIDENCE_CONTENT_TYPE_NOT_ALLOWED");
  }
  if (typeof metadata.uploaderId !== "string" ||
      !metadata.uploaderId.trim() || metadata.uploaderId.length > 200) {
    throw new TypeError("EVIDENCE_UPLOADER_REQUIRED");
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw new TypeError("EVIDENCE_MAX_BYTES_INVALID");
  }
  return Object.freeze({
    purpose: metadata.purpose,
    contentType: metadata.contentType,
    uploaderId: metadata.uploaderId.trim(),
    maxBytes
  });
}

/**
 * Implementations must:
 * - generate opaque server-side object keys (never accept client paths);
 * - keep objects private and enforce authorization outside this interface;
 * - stream with a hard byte limit and compute SHA-256 while writing;
 * - verify object existence and metadata in head/get;
 * - make delete idempotent and preserve an audit trail at the caller.
 *
 * put(source, metadata) accepts an AsyncIterable<Uint8Array> and returns
 * { key, checksumSha256, byteSize, contentType, purpose }.
 * head(key) returns metadata or null; get(key) returns an async byte stream
 * or null; delete(key) returns true when absent or deleted.
 */
export class EvidenceStore {
  async put(_source, _metadata) {
    throw new Error("EVIDENCE_STORE_PUT_NOT_IMPLEMENTED");
  }

  async head(_key) {
    throw new Error("EVIDENCE_STORE_HEAD_NOT_IMPLEMENTED");
  }

  async get(_key) {
    throw new Error("EVIDENCE_STORE_GET_NOT_IMPLEMENTED");
  }

  async delete(_key) {
    throw new Error("EVIDENCE_STORE_DELETE_NOT_IMPLEMENTED");
  }
}
