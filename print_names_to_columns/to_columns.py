from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i, name in enumerate(names, 1):
        if not i % cols:
            print(f"| {name:<10}\n", end='')
        else:
            print(f"| {name:<10}", end='')
