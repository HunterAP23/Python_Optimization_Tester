import functools as ft


def is_prime(n: int, primes: tuple, boundary: int) -> tuple:
    return tuple(ft.lru_cache(maxsize=None)(n % i for i in primes if i <= boundary))
