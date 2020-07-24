import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    ret = [n % i for i in table]
    return (all(ret), sum(ret),)


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)
