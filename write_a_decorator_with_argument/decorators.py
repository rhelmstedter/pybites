from functools import wraps

"""I hope this works"""


def make_html(element):
    def decorater(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{element}>{func()}</{element}>"

        return wrapper

    return decorater
