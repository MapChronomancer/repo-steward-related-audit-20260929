use pkg_fn::{run, Config};

fn main() {
    let cfg = Config { verbose: true, targets: std::env::args().skip(1).collect() };
    std::process::exit(run(&cfg));
}
