"""Helpers for building small synthetic Landsat-like arrays for tests.

pytest loads this file automatically. In a test file you can use:

- `to_dn(reflectance)`: convert reflectance to Landsat Collection 2 Level-2
  digital numbers, the way they are stored in the files.
- `QA_CLEAR`, `QA_FILL`, `QA_CLOUD`, `QA_SHADOW`, `QA_SNOW`: QA_PIXEL values
  for a clear pixel, a fill pixel, a cloud, a cloud shadow and snow.
- `make_stack(...)`, or the `stack_factory` fixture: build an array shaped like
  the output of `stackstac.stack`, with dims (time, band, y, x).

Import the helpers with, for example:
    from conftest import QA_CLEAR, QA_CLOUD, to_dn
"""

import numpy as np
import pandas as pd
import pytest
import xarray as xr

# Typical QA_PIXEL value for a clear land pixel in Landsat 8/9 Collection 2
QA_CLEAR = 21824
QA_FILL = 1
QA_CLOUD = QA_CLEAR | (1 << 3)
QA_SHADOW = QA_CLEAR | (1 << 4)
QA_SNOW = QA_CLEAR | (1 << 5)


def to_dn(reflectance):
    """Convert reflectance to Collection 2 Level-2 digital numbers (uint16)."""
    return np.round((np.asarray(reflectance, dtype="float64") + 0.2) / 0.0000275).astype("uint16")


def make_stack(red, nir, qa, dates, ids=None):
    """
    Build a stackstac-like DataArray with dims (time, band, y, x).

    red, nir: reflectance arrays of shape (time, y, x); qa: QA_PIXEL values.
    Values are stored as float64 digital numbers, like stackstac returns them.
    """
    red_dn, nir_dn = to_dn(red), to_dn(nir)
    qa = np.asarray(qa, dtype="float64")
    values = np.stack([red_dn, nir_dn, qa], axis=1).astype("float64")
    ntime, _, ny, nx = values.shape
    ids = ids or [f"scene_{i}" for i in range(ntime)]
    return xr.DataArray(
        values,
        dims=("time", "band", "y", "x"),
        coords={
            "time": pd.to_datetime(dates),
            "band": ["red", "nir08", "qa_pixel"],
            "y": np.arange(ny) * -30.0,
            "x": np.arange(nx) * 30.0,
            "id": ("time", ids),
        },
    )


@pytest.fixture
def stack_factory():
    return make_stack
