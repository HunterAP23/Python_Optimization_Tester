import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: list):
    ret = [n % table[i] for i in range(len(table))]
    return (all(ret), sum([bool(i) for i in ret]))


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))
