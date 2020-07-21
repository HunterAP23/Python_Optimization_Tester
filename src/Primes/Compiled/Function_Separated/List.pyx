import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n: int, table: list):
    ret = [n % i for i in table]
    return (all(ret), sum(ret),)


def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)


def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)
