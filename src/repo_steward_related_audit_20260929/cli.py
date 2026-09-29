"""Command line interface for repo_steward_related_audit_20260929."""

from __future__ import annotations

import argparse
import sys

from .core import Config, run


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="repo_steward_related_audit_20260929", description="repo_steward_related_audit_20260929 cli")
    p.add_argument("targets", nargs="*", help="targets to process")
    p.add_argument("-v", "--verbose", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = Config(verbose=args.verbose, targets=list(args.targets))
    return run(cfg)


if __name__ == "__main__":
    sys.exit(main())
