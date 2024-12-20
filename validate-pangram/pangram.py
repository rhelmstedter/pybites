from string import ascii_lowercase


def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    return all(c in sentence.lower() for c in ascii_lowercase)


if __name__ == "__main__":
    validate_pangram()
