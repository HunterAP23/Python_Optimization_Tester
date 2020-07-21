import functools as ft
import math
cimport cython


cdef void print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@cython.cfunc
@cython.locals(n=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_default(int n, list table):
    cdef list ret
    ret = [n % i for i in table]
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(int n, list table):
    boundary = math.floor(n / 2)
    cdef list ret
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(int n, list table):
    boundary = math.floor(math.sqrt(n))
    cdef list ret
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)
