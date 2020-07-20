import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef is_prime__default(int n, list table):
    cdef int checks = 0

    cdef int i
    for i in range(len(table)):
        if n % table[i] == 0:
            return (False, 1)
        else:
            checks += 1
    return (True, checks)


cdef is_prime__half(int n, list table):
    cdef int checks = 0

    cdef int boundary = math.floor(n / 2)
    cdef int i
    for i in range(len(table)):
        if table[i] <= boundary:
            if n % table[i] == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)


cdef is_prime__sqrt(int n, list table):
    cdef int checks = 0

    cdef int boundary = math.floor(math.sqrt(n))
    cdef int i
    for i in range(len(table)):
        if table[i] <= boundary:
            if n % table[i] == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)
