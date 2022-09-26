import functools as ft

from PO_Standard import measure_resources


@ft.lru_cache(maxsize=None)
@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> tuple:
    return tuple(ft.lru_cache(maxsize=None)(n % i for i in primes if i <= boundary))
