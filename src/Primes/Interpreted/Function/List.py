from PO_Standard import measure_resources


@measure_resources
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return [n % i for i in primes if i <= boundary]
