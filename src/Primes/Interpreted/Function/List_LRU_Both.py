import functools as ft


@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return [ft.lru_cache(maxsize=None)(n % i for i in primes if i <= boundary)]
