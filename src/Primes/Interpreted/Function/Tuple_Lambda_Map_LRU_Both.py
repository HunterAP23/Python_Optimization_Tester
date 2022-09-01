import functools as ft


@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int) -> tuple:
    return tuple(map(ft.lru_cache(maxsize=None)(lambda y: n % y if y <= boundary else 1), primes))
