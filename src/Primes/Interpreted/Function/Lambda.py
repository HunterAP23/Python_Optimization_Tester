import math


def is_prime_default(n: int, table: tuple):
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        ret.append(my_lam(i))
    return ret


def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return ret


def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return ret
