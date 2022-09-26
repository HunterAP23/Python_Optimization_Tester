import functools as ft
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
            ret = []
            measurer = Resource_Measurer()
            boundary = n
            if bounding == "Half":
                boundary = math.floor(n / 2)
            elif bounding == "Sqrt":
                boundary = math.floor(math.sqrt(n))
            for j in data["primes"][i]:
                if j <= boundary:
                    ret.append(ft.lru_cache(maxsize=None)(lambda j: n % j))
            measurer.finish()
            resources = measurer.result()
            del measurer
            data["times"][i].append(resources["time_seconds"])
            data["memory_usage"][i].append(resources["memory_bytes"])

            data["divisions"][i][n] = len(ret)
            if all(list(ret)):
                data["primes"][i].append(n)

    return data