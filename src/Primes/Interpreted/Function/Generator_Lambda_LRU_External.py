import functools as ft

from PO_Standard import measure_resources


@measure_resources
@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int):
    for i in primes:
        if i < boundary:
            yield (lambda j: n % j)(i)
        else:
            break
