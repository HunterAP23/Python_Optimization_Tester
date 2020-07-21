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
def is_prime_default(n: int, table: list):
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    for i in range(len(table)):
        ret.append(my_lam(table[i]))
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: list):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


@cython.cfunc
@cython.locals(n=cython.int, boundary=cython.int, i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: list):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)
