VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
    VOWELS. Match is case insensitive."""
    return all(c.lower() in VOWELS for c in input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
    chars are in it. Match is case insensitive."""
    return any(c in input_str.lower() for c in PYTHON)


def contains_digits(input_str):
    """Receives input string and checks if it contains
    one or more digits."""
    return any(c.isdigit() for c in input_str)
