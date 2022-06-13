import math


def is_prime_default(n: int, table: tuple):
    my_lam = lambda y: n % y
    return list(map(my_lam, table))


def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    my_lam = lambda y: n % y if y <= boundary else 1
    return list(map(my_lam, table))


def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y if y <= boundary else 1
    return list(map(my_lam, table))
