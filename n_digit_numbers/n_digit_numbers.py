from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    power_of_ten = 10 ** (n - 1)
    nums = []
    for num in numbers:
        if abs(int(num)) < power_of_ten:
            nums.append(int(num * power_of_ten))
        elif len(str(abs(num))) == len(str(power_of_ten)):
            nums.append(num)
        else:
            nums.append(int((num / 10 ** (len(str(abs(num))) - 1)) * power_of_ten))
    return nums
