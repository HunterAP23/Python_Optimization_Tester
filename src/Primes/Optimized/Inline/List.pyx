import math
import time

cimport cython  # noqa: E999


@cython.ccall
def is_prime(value_max: cython.int, num_loops: cython.int, bounding: str, Resource_Measurer, kwargs) -> dict:
    return is_prime_cython(value_max, num_loops, bounding, Resource_Measurer, kwargs)


@cython.cfunc
@cython.returns(dict)
@cython.locals(i=cython.int, ret=list, j=cython.int)
def is_prime_cython(value_max: cython.int, num_loops: cython.int, bounding: str, Resource_Measurer, kwargs) -> dict:
    cdef dict data = {
        "divisions": dict(),
        "primes": dict(),
        "times": dict(),
    }
    cdef int n
    cdef int boundary

    for i in range(num_loops):
        data["divisions"][i] = dict()
        data["times"][i] = []
        data["primes"][i] = []
        data["primes"][i].append(2)
        for n in range(3, value_max, 2):
            measurer = Resource_Measurer()
            boundary = n
            if bounding == "Half":
                boundary = math.floor(n / 2)
            elif bounding == "Sqrt":
                boundary = math.floor(math.sqrt(n))
            ret = [n % j for j in data["primes"] if j <= boundary]
            tmp_time_end = time.perf_counter()
            data["times"][i].append(tmp_time_end - tmp_time_start)

            data["divisions"][i][n] = len(ret)
            if all(ret):
                data["primes"][i].append(n)

    return data