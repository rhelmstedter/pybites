from typing import get_type_hints

from annotations import sum_numbers


def test_sum_numbers():
    type_hints = get_type_hints(sum_numbers)
    assert type_hints['numbers'] == list[int]
    assert type_hints['return'] == int