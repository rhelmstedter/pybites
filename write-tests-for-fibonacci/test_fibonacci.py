from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_


def test_negatives():
    with pytest.raises(ValueError):
        fib(-9)


def test_initial_values():
    result_zero = fib(0)
    result_one = fib(1)

    assert result_zero == 0
    assert result_one == 1


def test_values():
    result = fib(9)
    assert result == 34
