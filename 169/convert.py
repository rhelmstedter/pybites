def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if "in" in fmt.lower():
        return round(value / 2.54, 4)
    elif "cm" in fmt.lower():
        return round(value * 2.54, 4)
    else:
        raise ValueError
