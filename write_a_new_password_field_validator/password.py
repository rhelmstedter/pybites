import string
import re

PUNCTUATION_CHARS = string.punctuation

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    pattern = r".*\d+.*[A-Z]+.*[a-z]{2,}"
    mo = re.match(pattern, "".join(sorted(password)))
    good_punc = False
    for c in password:
        if c in PUNCTUATION_CHARS:
            good_punc = True
            break
    if not good_punc:
        return False
    elif password in used_passwords:
        return False
    elif not 6 <= len(password) <= 12:
        return False
    elif mo:
        used_passwords.add(password)
        return True
