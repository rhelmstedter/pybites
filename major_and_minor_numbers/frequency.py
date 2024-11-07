from collections import Counter


def major_n_minor(numbers: list[int]) -> tuple[int]:
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counts = Counter(numbers).most_common()
    major = counts[0][0]
    minor = counts[-1][0]
    return major, minor
