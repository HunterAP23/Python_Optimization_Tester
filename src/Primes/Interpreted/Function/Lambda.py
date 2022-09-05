def is_prime(n: int, primes: tuple, boundary: int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append((lambda y: n % y)(i))
        else:
            break
    return ret
