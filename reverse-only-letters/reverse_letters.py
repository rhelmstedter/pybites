def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    non_letters = [(i, char) for i, char in enumerate(string) if not char.isalpha()]
    reversed_chars = [char for char in string[::-1] if char.isalpha()]
    for i, char in non_letters:
        reversed_chars.insert(i, char)
    return "".join(reversed_chars)


if __name__ == "__main__":
    reverse_letters()
