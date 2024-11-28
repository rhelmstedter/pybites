
def sum_numbers(numbers: list[int] | None = None) -> int:
    """Takes in a list of numbers and returns the sum.
    If numbers is None, returns the sum from 1 to 100.
    """
    if numbers is None:
        return 5050
    return sum(numbers)
