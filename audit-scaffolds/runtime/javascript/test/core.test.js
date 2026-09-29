import { test } from "node:test";
import assert from "node:assert";
import { run } from "../src/core.js";

test("run returns zero for empty config", () => {
  assert.strictEqual(run({ verbose: false, targets: [] }), 0);
});
