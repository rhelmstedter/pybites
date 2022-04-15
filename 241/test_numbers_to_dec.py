import pytest

from numbers_to_dec import list_to_decimal


def test_good_vales():
    result = list_to_decimal([0, 4, 2, 8])
    assert result == 428


def test_outside_range():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])


def test_non_ints():
    with pytest.raises(TypeError):
        list_to_decimal(["4", 5, 3, 1])
        list_to_decimal([3.6, 4, 1])
        list_to_decimal([6, 2, True])
