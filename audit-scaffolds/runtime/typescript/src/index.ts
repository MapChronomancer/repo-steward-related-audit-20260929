// Entry point for study-notes.
import { run } from "./core.js";
import type { Config } from "./core.js";

const cfg: Config = { verbose: true, targets: process.argv.slice(2) };
process.exit(run(cfg));
