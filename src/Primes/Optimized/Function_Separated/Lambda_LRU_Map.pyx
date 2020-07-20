import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@cython.cfunc
@cython.locals(n=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: list):
    my_lam = ft.lru_cache()(lambda y: n % y)
    cdef list ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache()(lambda y: n % y if y <= boundary else 0)
    cdef list ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache()(lambda y: n % y if y <= boundary else 0)
    cdef list ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)
