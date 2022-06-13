import math
cimport cython

cdef(bint, int) is_prime_default(int n, tuple table):
    cdef int checks = 0

    cdef int i
    for i in table:
        if n % i == 0:
            return (False, 1)
        else:
            checks += 1
    return (True, checks)


cdef(bint, int) is_prime_half(int n, tuple table):
    cdef int checks = 0

    cdef int boundary = math.floor(n / 2)
    cdef int i
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)


cdef(bint, int) is_prime_sqrt(int n, tuple table):
    cdef int checks = 0

    cdef int boundary = math.floor(math.sqrt(n))
    cdef int i
    for i in table:
        if i <= boundary:
            if n % i == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)
