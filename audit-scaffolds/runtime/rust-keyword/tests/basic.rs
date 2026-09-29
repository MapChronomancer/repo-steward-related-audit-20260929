use pkg_fn::{run, Config};

#[test]
fn run_empty_is_zero() {
    let cfg = Config { verbose: false, targets: vec![] };
    assert_eq!(run(&cfg), 0);
}
