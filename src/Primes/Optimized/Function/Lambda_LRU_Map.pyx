import functools as ft
import math
cimport cython


cdef void print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@cython.cfunc
@cython.returns((cython.bint, cython.int))
@cython.locals(n=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: tuple):
    my_lam = lambda y: n % y
    cdef list ret = list(map(ft.lru_cache(maxsize=None)(my_lam), table))
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.returns((cython.bint, cython.int))
@cython.locals(n=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: tuple):
    cdef int boundary = math.floor(n / 2)
    my_lam = lambda y: n % y if y <= boundary else 1
    cdef list ret = list(map(ft.lru_cache(maxsize=None)(my_lam), table))
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.returns((cython.bint, cython.int))
@cython.locals(n=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: tuple):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y if y <= boundary else 1
    cdef list ret = list(map(ft.lru_cache(maxsize=None)(my_lam), table))
    return (all(ret), sum(ret),)
