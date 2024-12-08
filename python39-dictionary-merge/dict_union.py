def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return  new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      Values of any shared keys are summed.
    """
    try:
        total_keys = list(a.keys() | b.keys())
        new_dict = {}
        for k in total_keys:
            new_dict[k] = a.get(k, 0) + b.get(k, 0)
        return new_dict
    except AttributeError:
        raise TypeError("Can only combine two dictionaries")


if __name__ == "__main__":
    fruit = {"apple": 3, "banana": 2, "orange": 1}
    veggies = {"radish": 5, "artichoke": 2, "chard": 1}
    combine_and_count(fruit, veggies)
