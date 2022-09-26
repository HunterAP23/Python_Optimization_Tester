cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> list:
    return list(map(lambda j: n % j if j <= boundary else 1, primes))
