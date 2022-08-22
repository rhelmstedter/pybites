from math import ceil, floor


def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    values_sorted = dict(sorted(d.items(), key=lambda t: t[0]))
    midpoint = sum(values_sorted.values()) / 2

    if midpoint.is_integer():
        even = True
    else:
        even = False

    below_lower_bound = True

    for value, occurences in values_sorted.items():
        midpoint -= occurences
        if midpoint < 0 and below_lower_bound:
            median_manual = value
            break
        elif midpoint == 0 and even is True:
            median_manual = value / 2
            below_lower_bound = False
        elif midpoint < 0 and below_lower_bound is False:
            median_manual += value / 2
            break
    return median_manual
