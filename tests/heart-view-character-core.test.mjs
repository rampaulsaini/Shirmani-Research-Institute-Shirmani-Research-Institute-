import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
const source = await readFile(new URL("../showroom/heart-view-character-core.js", import.meta.url), "utf8");
const core = await import("data:text/javascript;base64," + Buffer.from(source).toString("base64"));
const { VERSIONS, EVIDENCE_RULES, DEFAULT_PROFILE, buildBrief, runSelfChecks } = core;

test("exactly four versions exist", () => assert.deepEqual(Object.keys(VERSIONS), ["V1", "V2", "V3", "V4"]));
test("all versions have release gates", () => Object.values(VERSIONS).forEach(v => assert.ok(v.required.length >= 4)));
test("insufficient evidence uses required Hindi wording", () => assert.match(EVIDENCE_RULES["INSUFFICIENT EVIDENCE"], /अभी पर्याप्त प्रमाण उपलब्ध नहीं है/));
test("philosophy is not framed as verified science", () => assert.match(EVIDENCE_RULES["PHILOSOPHICAL / IDENTITY"], /वैज्ञानिक तथ्य/));
test("each brief discloses unconnected integrations", () => Object.keys(VERSIONS).forEach(version => { const b=buildBrief({version}); assert.ok(b.includes("VERSION: "+version)); assert.match(b,/NOT_CONNECTED/); assert.match(b,/NOT PRODUCTION VERIFIED/); }));
test("V4 requires end-to-end testing", () => assert.ok(VERSIONS.V4.required.some(g => g.includes("end-to-end"))));
test("media status is honestly pending", () => { const b=buildBrief(DEFAULT_PROFILE); assert.match(b,/RECORDING_PENDING/); assert.match(b,/QR URL: PENDING/); });
test("self-check suite passes", () => assert.ok(runSelfChecks().every(c => c.pass)));
