def is_prime(n: int, primes: tuple, boundary: int):
    for i in primes:
        if i < boundary:
            yield lambda i: n % i
        else:
            break
