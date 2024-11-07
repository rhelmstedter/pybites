# tests are hidden for this Bite
from fizzbuzz import fizzbuzz


def test_mult_of_both():
    result = fizzbuzz(15)
    large_num = fizzbuzz(1005)
    assert result == "Fizz Buzz"
    assert large_num == "Fizz Buzz"


def test_mult_of_5():
    small_num = fizzbuzz(10)
    large_num = fizzbuzz(1105)

    assert small_num == "Buzz"
    assert large_num == "Buzz"


def test_mult_of_3():
    small_num = fizzbuzz(9)
    large_num = fizzbuzz(1503)

    assert small_num == "Fizz"
    assert large_num == "Fizz"


def test_neither():
    small_num = fizzbuzz(8)
    large_num = fizzbuzz(1502)

    assert small_num == 8
    assert large_num == 1502
