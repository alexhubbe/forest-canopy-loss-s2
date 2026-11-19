import numpy as np
import pytest

from fcl.labels import consistent_loss, index_to_year_month, year_month_to_index


def test_first_and_last_index():
    year, month = index_to_year_month(np.array([1, 98]))
    assert year.tolist() == [2017, 2025]
    assert month.tolist() == [9, 10]


def test_year_boundary():
    # index 4 = Dec 2017, index 5 = Jan 2018
    year, month = index_to_year_month(np.array([4, 5]))
    assert year.tolist() == [2017, 2018]
    assert month.tolist() == [12, 1]


def test_non_loss_values_map_to_zero():
    year, month = index_to_year_month(np.array([0, np.nan, 99]))
    assert year.tolist() == [0, 0, 0]
    assert month.tolist() == [0, 0, 0]


@pytest.mark.parametrize("idx", [1, 5, 50, 98])
def test_round_trip(idx):
    year, month = index_to_year_month(idx)
    assert year_month_to_index(int(year), int(month)) == idx


def test_out_of_range_date_raises():
    with pytest.raises(ValueError):
        year_month_to_index(2017, 8)


def test_consistent_loss():
    loss = np.array([0, 12, 30, np.nan, 40])
    mask = np.array([1, 1, 2, 1, 1])
    assert consistent_loss(loss, mask).tolist() == [False, True, False, False, True]
