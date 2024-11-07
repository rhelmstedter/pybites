def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum([d ** len(str(n)) for d in digits]) == n
