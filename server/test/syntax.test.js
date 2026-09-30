import test from "node:test";
import assert from "node:assert/strict";
import { spawn } from "node:child_process";

test("server source passes Node syntax validation", async () => {
  const child = spawn(process.execPath, ["--check", "src/index.js"], { cwd: new URL("..", import.meta.url).pathname });
  const code = await new Promise(resolve => child.on("close", resolve));
  assert.equal(code, 0);
});
