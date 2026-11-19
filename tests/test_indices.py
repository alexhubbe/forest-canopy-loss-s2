import numpy as np

from fcl.indices import ndmi, ndvi, normalized_difference, to_reflectance


def test_normalized_difference_basic():
    assert np.isclose(normalized_difference(0.6, 0.2), 0.5)


def test_zero_denominator_gives_nan():
    assert np.isnan(normalized_difference(np.array([0.0]), np.array([0.0])))[0]


def test_ndvi_range_for_vegetation_and_water():
    # dense vegetation: high NIR, low red -> positive; water: NIR < red -> negative
    assert ndvi(0.45, 0.05) > 0.7
    assert ndvi(0.02, 0.05) < 0


def test_ndmi_drops_when_canopy_dries():
    healthy = ndmi(0.40, 0.15)
    stressed = ndmi(0.30, 0.22)
    assert stressed < healthy


def test_to_reflectance_with_offset():
    assert np.isclose(to_reflectance(2000, offset=-0.1), 0.1)
