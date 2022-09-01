cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> list:
    return list(map(lambda i: n % i if i <= boundary else 1, primes))
