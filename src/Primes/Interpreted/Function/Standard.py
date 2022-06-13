import math


def is_prime_default(n: int, table: tuple):
    ret = []

    for i in table:
        if n % i == 0:
            return ret
        else:
            ret.append(i)
    return ret


def is_prime_half(n: int, table: tuple):
    ret = []

    boundary = math.floor(n / 2)
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return ret
            else:
                ret.append(i)
        else:
            break
    return ret


def is_prime_sqrt(n: int, table: tuple):
    ret = []

    boundary = math.floor(math.sqrt(n))
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return ret
            else:
                ret.append(i)
        else:
            break
    return ret
