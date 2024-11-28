from itertools import product

DIGIT_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
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
    if len(digits) > 4 or not digits.isdigit():
        raise ValueError(
            "`digits` string contains non-digit characters or has more than four digits."
        )
    mapped_digits = [DIGIT_MAP[digit] for digit in digits]
    return ["".join(comb) for comb in product(*mapped_digits)]
