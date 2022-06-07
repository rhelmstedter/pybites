from operator import add, mul, sub, truediv


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

    Examples - input -> output:
    '2 * 3' -> 6
    '2 + 6' -> 8

    Support +, -, * and /, use "true" division (so 2/3 is .66
    rather than 0)

    Make sure you convert both numbers to ints.
    If bad data is passed in, raise a ValueError.
    """
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
    }
    try:
        a1, op, a2 = calculation.split()
        return operations[op](float(a1), float(a2))
    except KeyError or ZeroDivisionError:
        raise ValueError
    except ZeroDivisionError:
        raise ValueError
