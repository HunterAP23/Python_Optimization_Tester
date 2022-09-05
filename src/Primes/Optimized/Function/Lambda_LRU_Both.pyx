import functools as ft

cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int, ret=list)
@ft.lru_cache(maxsize=None)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append(ft.lru_cache(maxsize=None)(lambda y: n % y)(i))
        else:
            break
    return ret
