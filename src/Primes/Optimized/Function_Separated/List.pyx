import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef is_prime__default(int n, list table):
    cdef list ret
    cdef int i
    ret = [n % table[i] for i in range(len(table))]
    return (all(ret), sum([bool(i) for i in ret]))


cdef is_prime__half(int n, list table):
    cdef int boundary = math.floor(n / 2)
    cdef list ret
    cdef int i
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))


cdef is_prime__sqrt(int n, list table):
    cdef int boundary = math.floor(math.sqrt(n))
    cdef list ret
    cdef int i
    ret = [n % table[i] for i in range(len(table)) if table[i] <= boundary]
    return (all(ret), sum([bool(i) for i in ret]))
