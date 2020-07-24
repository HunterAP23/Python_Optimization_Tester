import functools as ft
import math
cimport cython


cdef void print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef(bint, int) is_prime_default(int n, tuple table):
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in table:
        ret.append(my_lam(i))
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_half(int n, tuple table):
    cdef int boundary = math.floor(n / 2)
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_sqrt(int n, tuple table):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)
