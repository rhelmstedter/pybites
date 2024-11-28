
def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    half_num_items = sum(d.values()) / 2
    lower_median = None
    current_location = 0

    for num, occurrences in sorted(d.items()):
        current_location += occurrences
        if current_location == half_num_items:
            lower_median = num
        if current_location > half_num_items:
            if lower_median:
                median = (lower_median + num) / 2
            else:
                median = num
            return median
