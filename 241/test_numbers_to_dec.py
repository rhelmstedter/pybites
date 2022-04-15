import pytest

from numbers_to_dec import list_to_decimal


def test_good_vales():
    result = list_to_decimal([0, 4, 2, 8])
    assert result == 428


def test_negatives():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])


def test_bad_types():
    with pytest.raises(TypeError):
        list_to_decimal(["2", 3, 12])

