"""Helpers for the DLR Forest Canopy Cover Loss (FCCL) labels.

FCCL_DE_P1M.tif encoding:
    NaN   -> non-forest
    0     -> intact forest
    1..98 -> month of canopy loss (1 = Sep 2017, ..., 98 = Oct 2025)

FCCL_DE_P1M_MASK.tif: 1 = consistent loss, 2-4 = temporary disturbance.
"""

from __future__ import annotations

import numpy as np

FIRST_YEAR = 2017
FIRST_MONTH = 9  # index 1 = September 2017
MAX_INDEX = 98   # October 2025


def index_to_year_month(index: np.ndarray | int) -> tuple[np.ndarray, np.ndarray]:
    """Convert FCCL month indices (1..98) to (year, month).

    Values outside 1..MAX_INDEX (0 = intact, NaN = non-forest) return year = month = 0.
    """
    idx = np.asarray(index, dtype="float64")
    valid = np.isfinite(idx) & (idx >= 1) & (idx <= MAX_INDEX)
    months_since_jan_first_year = np.where(valid, idx, 1).astype("int64") - 1 + (FIRST_MONTH - 1)
    year = np.where(valid, FIRST_YEAR + months_since_jan_first_year // 12, 0)
    month = np.where(valid, months_since_jan_first_year % 12 + 1, 0)
    return year, month


def year_month_to_index(year: int, month: int) -> int:
    """Inverse of :func:`index_to_year_month` for a single date."""
    index = (year - FIRST_YEAR) * 12 + (month - FIRST_MONTH) + 1
    if not 1 <= index <= MAX_INDEX:
        raise ValueError(f"{year}-{month:02d} is outside the FCCL period (Sep 2017 - Oct 2025)")
    return index


def consistent_loss(loss_index: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Boolean array: pixels with a loss date AND flagged as consistent loss (mask == 1)."""
    idx = np.asarray(loss_index, dtype="float64")
    has_loss = np.isfinite(idx) & (idx >= 1) & (idx <= MAX_INDEX)
    return has_loss & (np.asarray(mask) == 1)
