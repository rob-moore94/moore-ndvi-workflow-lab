"""Tests for ndvi_workflow/indices.py.

This file is a worked example. Each test checks one thing we know must be
true about the science or the data, not just that the code runs. Use it as a
model for the tests you write in Part 3 of the lab.
"""

import numpy as np
import pytest
import xarray as xr

from ndvi_workflow.indices import normalized_diff


def test_known_values():
    nir = np.array([[0.5, 0.4]])
    red = np.array([[0.1, 0.4]])
    np.testing.assert_allclose(normalized_diff(nir, red), [[0.4 / 0.6, 0.0]])


def test_different_shapes_raise_value_error():
    with pytest.raises(ValueError):
        normalized_diff(np.ones((2, 5)), np.ones((1, 2, 5)))


def test_uint16_input_does_not_wrap_around():
    nir = np.array([3000], dtype="uint16")
    red = np.array([5000], dtype="uint16")
    np.testing.assert_allclose(normalized_diff(nir, red), [-0.25])


def test_zero_denominator_gives_nan_with_warning():
    nir = np.array([-15.0, 10.0])
    red = np.array([15.0, 5.0])
    with pytest.warns(RuntimeWarning):
        result = normalized_diff(nir, red)
    assert np.isnan(result[0])
    assert result[1] == pytest.approx(5 / 15)


def test_nodata_zeros_give_nan():
    result = normalized_diff(np.array([0.0]), np.array([0.0]))
    assert np.isnan(result[0])


def test_works_with_xarray_and_keeps_coords():
    nir = xr.DataArray(np.array([[0.5, 0.0]]), dims=("y", "x"), coords={"x": [10, 20]})
    red = xr.DataArray(np.array([[0.1, 0.0]]), dims=("y", "x"), coords={"x": [10, 20]})
    result = normalized_diff(nir, red)
    assert isinstance(result, xr.DataArray)
    assert list(result["x"].values) == [10, 20]
    assert np.isnan(result.values[0, 1])
