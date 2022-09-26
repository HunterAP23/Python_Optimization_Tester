import functools as ft

from PO_Standard import measure_resources


@ft.lru_cache(maxsize=None)
@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return list(map(lambda j: n % j if j <= boundary else 1), primes)
