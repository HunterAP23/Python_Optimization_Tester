import functools as ft

cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> tuple:
    return tuple(map(ft.lru_cache(maxsize=None)(lambda i: n % i if i <= boundary else 1), primes))
