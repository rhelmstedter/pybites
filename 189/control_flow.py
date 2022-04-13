IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: list[str]) -> list[str]:
    filtered = []
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        elif not name.isalpha():
            continue
        elif name.startswith(QUIT_CHAR):
            break
        elif len(filtered) == MAX_NAMES:
            break
        else:
            filtered.append(name)
    return filtered
