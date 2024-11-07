chars1 = [
    "A",
    "f",
    ".",
    "Q",
    2,
]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
chars2 = [
    ".",
    "{",
    " ^",
    "%",
    "a",
]  # returns index 4 ('a' is alphanumeric among non-alphanumerics)


def get_index_different_char(chars):
    mask = [str(word).isalnum() for word in chars]
    return mask.index(min(set(mask), key=mask.count))
