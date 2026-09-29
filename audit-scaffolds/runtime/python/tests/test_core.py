"""Tests for pkg_class.core."""

from pkg_class.core import Config, run


def test_run_returns_zero_for_empty_config() -> None:
    assert run(Config()) == 0


def test_config_from_args_collects_targets() -> None:
    cfg = Config.from_args(["a", "b", "c"])
    assert cfg.targets == ["a", "b", "c"]
