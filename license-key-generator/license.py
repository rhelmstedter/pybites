from secrets import choice
from string import ascii_uppercase, digits

CHARS = ascii_uppercase + digits


def gen_key(parts=4, chars_per_part=8):
    parts_ = []
    for part in range(parts):
        part = "".join([choice(CHARS) for _ in range(chars_per_part)])
        parts_.append(part)
    return "-".join(parts_)
