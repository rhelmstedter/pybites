decimal_to_roman = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError
    elif not 0 < decimal_number < 4000:
        raise ValueError
    roman_numeral = ""
    while decimal_number:
        for dec, rom in decimal_to_roman.items():
            if decimal_number >= dec:
                quotient, remainder = divmod(decimal_number, dec)
                roman_numeral += rom * quotient
                decimal_number = remainder
    return roman_numeral


if __name__ == "__main__":
    print(romanize(999))
