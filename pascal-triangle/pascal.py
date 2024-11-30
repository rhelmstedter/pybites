from typing import List
from itertools import pairwise


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 0:
        return []
    elif N == 1:
        return [1]
    else:
        return [1] + [sum(pair) for pair in pairwise(pascal(N - 1))] + [1]
