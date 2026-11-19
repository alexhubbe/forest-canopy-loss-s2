"""Load the project configuration (area of interest, time range, collections)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "configs" / "aoi.yaml"


def load_config(path: str | Path = DEFAULT_CONFIG) -> dict[str, Any]:
    """Read a YAML config file and return it as a dict."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
