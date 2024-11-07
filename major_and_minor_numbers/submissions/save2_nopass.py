from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    counts = Counter()
    for num in numbers:
        counts[num] += 1
    major = counts.most_common()[0][1]
    minor = counts.most_common(1)[-1][1]
    return major, minor