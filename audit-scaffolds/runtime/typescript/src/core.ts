// Core starter for study-notes — theme label: Harmless documentation fixture \"quoted\".\nSecond line C:\\notes\u2028No AI execution..
export interface Config { verbose: boolean; targets: string[]; }

export function run(config: Config): number {
  if (config.verbose) console.log(`[study-notes] ${config.targets.length} targets`);
  for (const t of config.targets) process(t, config.verbose);
  return 0;
}

function process(name: string, verbose: boolean): void {
  if (verbose) console.log(`  -> ${name}`);
}
