import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    list_of_args = [arg for arg in args if arg]
    if not list_of_args:
        return set()
    return set.intersection(*map(set, list_of_args))
