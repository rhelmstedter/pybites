from typing import List


def minimum_number(digits: List[int]) -> int:
    if not digits:
        return 0
    return int(''.join(map(str, sorted(set(digits)))))
