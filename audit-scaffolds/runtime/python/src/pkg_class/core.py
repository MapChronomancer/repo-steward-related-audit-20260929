'Core starter for pkg_class.\n\nExample executor template. Theme: Harmless documentation fixture "quoted".\nSecond line C:\\notes\u2028No AI execution..\n'

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


__all__ = ["Config", "run"]


@dataclass
class Config:
    """Runtime configuration."""
    verbose: bool = False
    targets: list[str] = field(default_factory=list)

    @classmethod
    def from_args(cls, items: Iterable[str]) -> "Config":
        cfg = cls()
        for it in items:
            cfg.targets.append(str(it))
        return cfg


def run(config: Config) -> int:
    """Entrypoint. Returns process exit code."""
    if config.verbose:
        print(f"[pkg_class] starting with {len(config.targets)} targets")
    for t in config.targets:
        _process_target(t, verbose=config.verbose)
    return 0


def _process_target(name: str, *, verbose: bool = False) -> None:
    if verbose:
        print(f"  -> {name}")
