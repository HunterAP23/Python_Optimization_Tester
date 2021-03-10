import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n: int, table: tuple):
    return (n % i for i in table if i < n)


def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    return (n % i for i in table if i <= boundary)


def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    return (n % i for i in table if i <= boundary)
