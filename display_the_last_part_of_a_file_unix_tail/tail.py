def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines"""
    with open(filepath) as file:
        lines = [line.strip("\n") for line in file.readlines()]
    return lines[-n:]
