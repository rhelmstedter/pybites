decimal_to_roman = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError
    elif not 0 < decimal_number < 4000:
        raise ValueError
    roman_numeral = ""
    while decimal_number:
        for dec, rom in sorted(decimal_to_roman.items(), reverse=True):
            if decimal_number >= dec:
                quotient, remainder = divmod(decimal_number, dec)
                roman_numeral += rom * quotient
                decimal_number = remainder
    return roman_numeral


if __name__ == "__main__":
    print(romanize(999))
