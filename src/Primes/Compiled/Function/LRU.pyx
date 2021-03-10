import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    checks = []

    for i in table:
        if n % i == 0:
            checks.append(False)
            return checks
        else:
            checks.append(True)
    return checks


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    checks = []

    boundary = math.floor(n / 2)
    for i in table:
        if i <= boundary:
            if n % i == 0:
                checks.append(False)
                return checks
            else:
                checks.append(True)
        else:
            break
    return checks


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    checks = []

    boundary = math.floor(math.sqrt(n))
    for i in table:
        if i <= boundary:
            if n % i == 0:
                checks.append(False)
                return checks
            else:
                checks.append(True)
        else:
            break
    return checks
