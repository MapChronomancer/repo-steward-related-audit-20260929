# Usage

This is a starter scaffold for **class**, not a finished implementation of the supplied project theme. The example CLI reports its targets.

## Install

```bash
pip install -e .
```

## Basic example

```python
from pkg_class.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
pkg_class alpha beta -v
```

## Tests

```bash
pytest
```

## Theme

Project theme label: Harmless documentation fixture "quoted".
Second line C:\notes No AI execution..
