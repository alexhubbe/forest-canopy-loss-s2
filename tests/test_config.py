from fcl.config import load_config


def test_default_config_loads():
    cfg = load_config()
    assert cfg["name"] == "frankenwald"
    min_lon, min_lat, max_lon, max_lat = cfg["bbox"]
    assert min_lon < max_lon and min_lat < max_lat
    assert cfg["sentinel2"]["collection"] == "sentinel-2-l2a"
