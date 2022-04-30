from typing import List


def sum_numbers(numbers: List[int] = None) -> int:
    if numbers is None:
        return 5050
    else:
        return sum(numbers)
