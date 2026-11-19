"""Search Sentinel-1/2 scenes on the Microsoft Planetary Computer STAC API."""

from __future__ import annotations

from typing import Any

PC_STAC_URL = "https://planetarycomputer.microsoft.com/api/stac/v1"


def open_catalog():
    """Open the Planetary Computer STAC catalog with automatic URL signing."""
    import planetary_computer
    import pystac_client

    return pystac_client.Client.open(PC_STAC_URL, modifier=planetary_computer.sign_inplace)


def search_s2(cfg: dict[str, Any], start: str | None = None, end: str | None = None,
              max_cloud: float | None = None):
    """Return the Sentinel-2 L2A items covering the AOI in the config."""
    s2 = cfg["sentinel2"]
    start = start or cfg["time"]["start"]
    end = end or cfg["time"]["end"]
    max_cloud = s2["max_cloud_cover"] if max_cloud is None else max_cloud
    return open_catalog().search(
        collections=[s2["collection"]],
        bbox=cfg["bbox"],
        datetime=f"{start}/{end}",
        query={"eo:cloud_cover": {"lt": max_cloud}},
    ).item_collection()


def search_s1(cfg: dict[str, Any], start: str | None = None, end: str | None = None):
    """Return the Sentinel-1 RTC items covering the AOI in the config."""
    start = start or cfg["time"]["start"]
    end = end or cfg["time"]["end"]
    return open_catalog().search(
        collections=[cfg["sentinel1"]["collection"]],
        bbox=cfg["bbox"],
        datetime=f"{start}/{end}",
    ).item_collection()
