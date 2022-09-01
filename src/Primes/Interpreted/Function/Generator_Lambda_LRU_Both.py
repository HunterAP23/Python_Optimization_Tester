import functools as ft


@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int):
    for i in primes:
        if i < boundary:
            yield ft.lru_cache(maxsize=None)(lambda i: n % i)
        else:
            break
