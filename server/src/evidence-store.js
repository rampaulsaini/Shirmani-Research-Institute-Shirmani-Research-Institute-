/**
 * Provider-neutral contract for private evidence storage.
 *
 * This module deliberately contains no storage provider, credentials, network
 * calls, filesystem persistence, or production adapter. A future adapter must
 * be reviewed and tested before it is configured in a deployment.
 *
 * Contract:
 *   put(readable, metadata) -> { key, sha256, sizeBytes, contentType }
 *   head(key)              -> metadata | null
 *   get(key)               -> readable | null
 *   delete(key)            -> boolean
 *
 * The adapter owns stream handling, object integrity, access controls, and
 * provider-specific error translation. Callers must never treat a key alone
 * as proof that an object exists.
 */

const REQUIRED_METHODS = Object.freeze(["put", "head", "get", "delete"]);

export function createEvidenceStore(adapter) {
  if (!adapter || typeof adapter !== "object") {
    throw new TypeError("EVIDENCE_STORE_ADAPTER_REQUIRED");
  }

  for (const method of REQUIRED_METHODS) {
    if (typeof adapter[method] !== "function") {
      throw new TypeError(`EVIDENCE_STORE_METHOD_REQUIRED:${method}`);
    }
  }

  return Object.freeze({
    put(readable, metadata) {
      if (!readable || typeof readable.pipe !== "function" &&
          typeof readable[Symbol.asyncIterator] !== "function") {
        throw new TypeError("EVIDENCE_STREAM_REQUIRED");
      }
      if (!metadata || typeof metadata !== "object" || Array.isArray(metadata)) {
        throw new TypeError("EVIDENCE_METADATA_REQUIRED");
      }
      return adapter.put(readable, Object.freeze({ ...metadata }));
    },

    head(key) {
      if (typeof key !== "string" || !key.trim()) {
        throw new TypeError("EVIDENCE_KEY_REQUIRED");
      }
      return adapter.head(key);
    },

    get(key) {
      if (typeof key !== "string" || !key.trim()) {
        throw new TypeError("EVIDENCE_KEY_REQUIRED");
      }
      return adapter.get(key);
    },

    delete(key) {
      if (typeof key !== "string" || !key.trim()) {
        throw new TypeError("EVIDENCE_KEY_REQUIRED");
      }
      return adapter.delete(key);
    }
  });
}
