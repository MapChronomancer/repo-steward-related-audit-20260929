// Entry point for study-notes.
import { run } from "./core.js";

const cfg = { verbose: true, targets: process.argv.slice(2) };
process.exit(run(cfg));
