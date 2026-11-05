"""Spectral index calculations."""

import warnings

import numpy as np
import xarray as xr


def normalized_diff(b1, b2):
    """
    Calculate the normalized difference of two arrays of the same shape.

    Math will be calculated (b1 - b2) / (b1 + b2). For example, NDVI is
    normalized_diff(nir, red).

    Parameters
    ----------
    b1, b2 : numpy arrays or xarray DataArrays
        Two arrays of the same shape. Integer arrays (e.g. uint16 Landsat
        bands) are converted to float before the calculation.

    Returns
    -------
    n_diff : numpy array or xarray DataArray (same type as the inputs)
        The element-wise result of (b1 - b2) / (b1 + b2) as a float array.
        Infinity values (from dividing by zero) are replaced with nan, and
        0/0 (e.g. nodata in both bands) also gives nan.

    Raises
    ------
    ValueError
        If the two arrays do not have the same shape.
    """
    if b1.shape != b2.shape:
        raise ValueError("Input arrays should have the same shape")

    # Convert to float to avoid wraparound errors with unsigned integers (uint16)
    b1 = b1.astype("float64")
    b2 = b2.astype("float64")

    # Ignore numpy's own warnings for division by zero, since we handle these below
    with np.errstate(divide="ignore", invalid="ignore"):
        n_diff = (b1 - b2) / (b1 + b2)

    is_inf = np.isinf(n_diff)
    if is_inf.any():
        warnings.warn(
            "Divide by zero produced infinity values that will be replaced with nan values",
            RuntimeWarning,
        )
        if isinstance(n_diff, xr.DataArray):
            n_diff = n_diff.where(~is_inf)
        else:
            n_diff = np.where(is_inf, np.nan, n_diff)

    return n_diff
