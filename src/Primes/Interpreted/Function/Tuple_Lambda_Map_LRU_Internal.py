import functools as ft

from PO_Standard import measure_resources


@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return list(map(ft.lru_cache(maxsize=None)(lambda j: n % j if j <= boundary else 1), primes))
