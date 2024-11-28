from functools import lru_cache


@lru_cache()
def cached_fib(n):
    if n <= 1:
        return n
    return n + cached_fib(n - 1)
