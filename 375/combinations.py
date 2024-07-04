from itertools import product

DIGIT_MAP = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    if len(digits) > 4:
        raise ValueError
    try:
        mapped_digits = [DIGIT_MAP[int(d)] for d in digits]
    except TypeError:
        raise ValueError
    return ["".join(comb) for comb in sorted(product(*mapped_digits))]


if __name__ == "__main__":
    print(generate_letter_combinations("232"))
