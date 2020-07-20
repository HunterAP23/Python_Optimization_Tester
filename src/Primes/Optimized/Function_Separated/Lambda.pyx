import functools as ft
import math
cimport cython


cdef print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef is_prime__default(int n, list table):
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in range(len(table)):
        ret.append(my_lam(table[i]))
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


cdef is_prime__half(int n, list table):
    cdef int boundary = math.floor(n / 2)
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


cdef is_prime__sqrt(int n, list table):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y
    cdef list ret = []
    cdef int i
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)
