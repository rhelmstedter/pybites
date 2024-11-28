import argparse
from functools import reduce
from operator import sub, mul, truediv


def calculator(operation, numbers):
    """TODO 1:
    Create a calculator that takes an operation and list of numbers.
    Perform the operation returning the result rounded to 2 decimals"""
    numbers = [float(num) for num in numbers]
    if not numbers:
        raise SystemExit
    elif operation == "add":
        return round(sum(numbers), 2)
    elif operation == "sub":
        return round(reduce(sub, numbers), 2)
    elif operation == "mul":
        return round(reduce(mul, numbers), 2)
    elif operation == "div":
        return round(reduce(truediv, numbers), 2)


def create_parser():
    """TODO 2:
    Create an ArgumentParser object:
    - have one operation argument,
    - have one or more integers that can be operated on.
    Returns a argparse.ArgumentParser object.

    Note that type=float times out here so do the casting in the calculator
    function above!"""
    parser = argparse.ArgumentParser(
        description="a simple calculator",
    )
    operations = [
        ("-a", "--add", "add"),
        ("-s", "--sub", "sub"),
        ("-m", "--mul", "mul"),
        ("-d", "--div", "div"),
    ]
    for short, long, constant in operations:
        parser.add_argument(
            short,
            long,
            nargs="+",
        )
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
    Calls calculator with provided args object.
    If args are not provided get them via create_parser,
    if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == "__main__":
    call_calculator(stdout=True)
