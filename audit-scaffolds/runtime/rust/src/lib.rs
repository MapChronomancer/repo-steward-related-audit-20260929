//! Core starter for study-notes — theme label: Harmless documentation fixture \"quoted\".\nSecond line C:\\notes\u2028No AI execution..

pub struct Config {
    pub verbose: bool,
    pub targets: Vec<String>,
}

/// Execute over the configured targets, returning an exit code.
pub fn run(cfg: &Config) -> i32 {
    if cfg.verbose {
        println!("[study-notes] {} targets", cfg.targets.len());
    }
    for t in &cfg.targets {
        process(t, cfg.verbose);
    }
    0
}

fn process(name: &str, verbose: bool) {
    if verbose {
        println!("  -> {}", name);
    }
}
