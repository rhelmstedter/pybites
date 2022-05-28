import unicodedata
from string import ascii_letters


def filter_accents(text):
    """Return a sequence of accented characters found in
    the passed in lowercased text string
    """
    return [
        c
        for c in text.lower()
        if unicodedata.category(c) == "Ll" and c not in ascii_letters
    ]
