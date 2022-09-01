import functools as ft


def is_prime(n: int, primes: tuple, boundary: int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append(ft.lru_cache(maxsize=None)(lambda i: n % i))
        else:
            break
    return ret
