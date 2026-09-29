"""Command line interface for pkg_class."""

from __future__ import annotations

import argparse
import sys

from .core import Config, run


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="pkg_class", description="pkg_class cli")
    p.add_argument("targets", nargs="*", help="targets to process")
    p.add_argument("-v", "--verbose", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = Config(verbose=args.verbose, targets=list(args.targets))
    return run(cfg)


if __name__ == "__main__":
    sys.exit(main())
