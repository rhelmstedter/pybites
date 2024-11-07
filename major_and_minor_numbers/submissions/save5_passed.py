from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    counts = Counter(numbers)
    major = counts.most_common()[0][0]
    minor = counts.most_common()[-1][0]
    return major, minor