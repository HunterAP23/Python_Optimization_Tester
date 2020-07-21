import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: list):
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        ret.append(my_lam(i))
    return (all(ret), sum(ret),)


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)
