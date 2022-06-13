import functools as ft
import math
cimport cython


@cython.cfunc
@cython.locals(n=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_default(int n, tuple table):
    cdef list ret
    ret = [n % i for i in table]
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(int n, tuple table):
    boundary = math.floor(n / 2)
    cdef list ret
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(int n, tuple table):
    boundary = math.floor(math.sqrt(n))
    cdef list ret
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)
