from PO_Standard import measure_resources


@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append((lambda j: n % j)(i))
        else:
            break
    return ret
