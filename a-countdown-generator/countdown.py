def countdown():
    """Write a generator that counts from 100 to 1"""
    for number in range(100, 0, -1):
        yield number
