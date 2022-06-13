import math


def is_prime_default(n: int, table: tuple):
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        yield my_lam(i)


def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        if i <= boundary:
            yield my_lam(i)
        else:
            break


def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        if i <= boundary:
            yield my_lam(i)
        else:
            break
