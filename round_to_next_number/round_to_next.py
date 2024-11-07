def round_to_next(number: int, multiple: int):
    if number % multiple:
        difference = multiple - (number % multiple)
        if multiple > 0:
            return number + difference
        elif multiple < 0 and number < 0:
            return number + difference
        elif multiple < 0:
            return number - difference
    return number
