import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@cython.cfunc
@cython.locals(n=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_default(int n, list table):
    cdef list ret
    ret = [n % table[i] for i in range(len(table))]
    return (all(ret), sum([bool(i) for i in ret]))


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(int n, list table):
    boundary = math.floor(n / 2)
    cdef list ret
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(int n, list table):
    boundary = math.floor(math.sqrt(n))
    cdef list ret
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))
