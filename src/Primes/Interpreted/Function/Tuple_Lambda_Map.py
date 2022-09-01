def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return list(map(lambda y: n % y if y <= boundary else 1, primes))
