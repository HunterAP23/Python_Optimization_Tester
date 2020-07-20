import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n: int, table: list):
    my_lam = lambda y: n % y
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    my_lam = lambda y: n % y if y <= boundary else 0
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y if y <= boundary else 0
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)
