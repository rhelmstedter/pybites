"""pybite challenge 1."""


def sum_numbers(numbers: list = None) -> int:
    """Calculate sum of integers up to numbers."""
    if numbers is None:
        return 5050
    else:
        return sum(numbers)
