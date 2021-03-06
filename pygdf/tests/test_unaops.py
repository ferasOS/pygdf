from __future__ import division

import pytest

import numpy as np

from pygdf.dataframe import Series

from . import utils


def test_series_ceil():
    arr = np.random.random(100) * 100
    sr = Series.from_any(arr)
    np.testing.assert_equal(sr.ceil().to_array(), np.ceil(arr))


def test_series_floor():
    arr = np.random.random(100) * 100
    sr = Series.from_any(arr)
    np.testing.assert_equal(sr.floor().to_array(), np.floor(arr))


@pytest.mark.parametrize('nelem', [1, 7, 8, 9, 32, 64, 128])
def test_validity_ceil(nelem):
    # Data
    data = np.random.random(nelem) * 100
    mask = utils.random_bitmask(nelem)
    bitmask = utils.expand_bits_to_bytes(mask)
    null_count = utils.count_zero(bitmask)
    sr = Series.from_masked_array(data, mask, null_count)

    # Result
    res = sr.ceil()

    na_value = -100000
    got = res.fillna(na_value).to_array()
    res_mask = np.asarray(bitmask, dtype=np.bool_)[:data.size]

    expect = np.ceil(data)
    expect[~res_mask] = na_value

    # Check
    print('expect')
    print(expect)
    print('got')
    print(got)

    np.testing.assert_array_equal(expect, got)
