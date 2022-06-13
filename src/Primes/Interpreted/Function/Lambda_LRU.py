import math


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        ret.append(my_lam(i))
    return ret


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return ret


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    ret = []
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return ret
