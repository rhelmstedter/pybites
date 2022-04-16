from pprint import pformat
from typing import Any


def pretty_string(obj: Any) -> str:
    return pformat(obj, depth=2, width=60)
