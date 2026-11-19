"""Spectral indices for Sentinel-2 surface reflectance (0-1 scale).

Band names follow Sentinel-2 L2A: B04 = red, B05 = red edge 1, B08 = NIR (10 m),
B8A = narrow NIR (20 m), B11 = SWIR 1.6 um, B12 = SWIR 2.2 um.
Works with numpy arrays and xarray DataArrays alike.
"""

from __future__ import annotations

import numpy as np


def normalized_difference(a, b):
    """(a - b) / (a + b); returns NaN where a + b == 0."""
    with np.errstate(divide="ignore", invalid="ignore"):
        denom = a + b
        return (a - b) / np.where(denom == 0, np.nan, denom)


def ndvi(nir, red):
    """Normalized Difference Vegetation Index: vegetation greenness."""
    return normalized_difference(nir, red)


def ndmi(nir, swir1):
    """Normalized Difference Moisture Index (NIR vs SWIR 1.6 um): canopy water content."""
    return normalized_difference(nir, swir1)


def nbr(nir, swir2):
    """Normalized Burn Ratio (NIR vs SWIR 2.2 um): sensitive to canopy disturbance."""
    return normalized_difference(nir, swir2)


def ndre(nir, red_edge):
    """Normalized Difference Red Edge (e.g. B8A vs B05): sensitive to chlorophyll / early stress."""
    return normalized_difference(nir, red_edge)


def to_reflectance(dn, scale: float = 1e-4, offset: float = 0.0):
    """Convert stored integers to reflectance: dn * scale + offset.

    Note: Sentinel-2 L2A from processing baseline 04.00 (Jan 2022) onwards carries
    an offset of -1000 in DN (i.e. offset = -0.1 after scaling). Check item metadata.
    """
    return dn * scale + offset
