"""Tests for repo_steward_related_audit_20260929.core."""

from repo_steward_related_audit_20260929.core import Config, run


def test_run_returns_zero_for_empty_config() -> None:
    assert run(Config()) == 0


def test_config_from_args_collects_targets() -> None:
    cfg = Config.from_args(["a", "b", "c"])
    assert cfg.targets == ["a", "b", "c"]
