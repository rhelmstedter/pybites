import inspect

import pytest
import numbers_to_dec
from numbers_to_dec import list_to_decimal


def test_good_vales():
    result = list_to_decimal([0, 4, 2, 8])
    assert result == 428


def test_outside_range():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])
        list_to_decimal([-3, 10])


def test_str():
    with pytest.raises(TypeError):
        list_to_decimal(["4", 5, 3, 1])


def test_float():
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 4, 1])


def test_boo():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])


def test_range():
    line = [line for line in inspect.getsourcelines(numbers_to_dec)[0] if 'range' in line][1]
    assert "range(0, 10)" in line
