import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    return (my_lam(i) for i in table)


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    return (my_lam(i) for i in table if i <= boundary)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    return (my_lam(i) for i in table if i <= boundary)
