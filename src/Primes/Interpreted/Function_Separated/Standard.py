import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n: int, table: list):
    checks = 0

    for i in table:
        if n % i == 0:
            return (False, 1)
        else:
            checks += 1
    return (True, checks)


def is_prime_half(n: int, table: list):
    checks = 0

    boundary = math.floor(n / 2)
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)


def is_prime_sqrt(n: int, table: list):
    checks = 0

    boundary = math.floor(math.sqrt(n))
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)
