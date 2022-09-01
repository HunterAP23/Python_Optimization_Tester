cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int, ret=list)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append(lambda i: n % i)
        else:
            break
    return ret