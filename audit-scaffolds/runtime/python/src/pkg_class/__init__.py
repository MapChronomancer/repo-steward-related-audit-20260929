"""pkg_class package."""

__version__ = "0.1.0"
from .core import Config, run  # noqa: F401

__all__ = ["Config", "run", "__version__"]
