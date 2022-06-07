import math
cimport cython


cdef void print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef(bint, int) is_prime_default(int n, tuple table):
    cdef list ret
    cdef int i
    ret = [n % i for i in table]
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_half(int n, tuple table):
    cdef int boundary = math.floor(n / 2)
    cdef list ret
    cdef int i
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_sqrt(int n, tuple table):
    cdef int boundary = math.floor(math.sqrt(n))
    cdef list ret
    cdef int i
    ret = [n % i for i in table if i <= boundary]
    return (all(ret), sum(ret),)
