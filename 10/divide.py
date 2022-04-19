def positive_divide(numerator, denominator):
    try:
        quotient = numerator / denominator
        if quotient < 0:
            raise ValueError
        return quotient
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError
