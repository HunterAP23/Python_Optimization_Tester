import functools as ft


@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int) -> tuple:
    return tuple(n % i for i in primes if i <= boundary)
