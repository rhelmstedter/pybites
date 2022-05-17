from string import printable


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii = []
    for word in text.split():
        is_not_ascii = False
        for letter in word:
            if letter not in printable:
                is_not_ascii = True
                break
        if is_not_ascii:
            non_ascii.append(word)
    return non_ascii
