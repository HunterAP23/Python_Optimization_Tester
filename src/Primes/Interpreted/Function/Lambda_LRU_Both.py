import functools as ft

from PO_Standard import measure_resources


@ft.lru_cache(maxsize=None)
@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append(ft.lru_cache(maxsize=None)(lambda j: n % j)(i))
        else:
            break
    return ret
