import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(int n, list table):
    my_lam = lambda y: n % y
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_half(int n, list table):
    cdef int boundary = math.floor(n / 2)
    my_lam = lambda y: n % y if y <= boundary else 1
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_sqrt(int n, list table):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y if y <= boundary else 1
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)
