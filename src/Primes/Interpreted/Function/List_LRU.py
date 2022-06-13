import functools as ft
import math


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    return [n % i for i in table]


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    return [n % i for i in table if i <= boundary]


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    return [n % i for i in table if i <= boundary]
