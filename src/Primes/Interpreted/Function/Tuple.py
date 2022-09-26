from PO_Standard import measure_resources


@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> tuple:
    return tuple(n % i for i in primes if i <= boundary)
