def round_even(number):
    """Takes a number and returns it rounded even"""
    if not (number + 0.5) % 2:
        return round(number + 0.5)
    elif not (number - 0.5) % 2:
        return round(number - 0.5)
    else:
        return round(number)
