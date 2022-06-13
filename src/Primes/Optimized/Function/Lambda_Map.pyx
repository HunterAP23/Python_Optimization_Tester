import math

cimport cython


def is_prime_default(int n, tuple table):
    my_lam = lambda y: n % y
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_half(int n, tuple table):
    cdef int boundary = math.floor(n / 2)
    my_lam = lambda y: n % y if y <= boundary else 1
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)


def is_prime_sqrt(int n, tuple table):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y if y <= boundary else 1
    ret = list(map(my_lam, table))
    return (all(ret), sum(ret),)
