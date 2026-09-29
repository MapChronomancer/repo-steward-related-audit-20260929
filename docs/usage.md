# Usage

This document describes how to use **repo-steward-related-audit-20260929**.

## Install

```bash
pip install -e .
```

## Basic example

```python
from repo_steward_related_audit_20260929.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
repo_steward_related_audit_20260929 alpha beta -v
```

## Theme

This project is oriented around: Harmless starter example for functional auditing.
