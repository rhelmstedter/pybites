from collections import Counter
from itertools import product


def original_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die."""
    sides = range(1, n + 1)
    return sum(n for n in sides) / n


def new_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die when the player simulaneously rolls
    two dice and chooses the larger value.
    """
    sides = range(1, n + 1)
    counts = Counter(max(n) for n in product(sides, sides))
    return round(sum(value * count for value, count in counts.items()) / n**2, 3)
