import functools as ft
import math
from typing import Literal


def is_prime(
    value_max: int,
    num_loops: int,
    bounding: Literal["Default", "Half", "Sqrt"],
    Resource_Measurer,
    **kwargs,
):
    def is_prime_mapped(n, y):
        return n % y

    data = {
        "divisions": dict(),
        "primes": dict(),
        "times": dict(),
        "memory_usage": dict(),
    }

    for i in range(num_loops):
        data["divisions"][i] = dict()
        data["times"][i] = []
        data["primes"][i] = []
        data["primes"][i].append(2)

        for n in range(3, value_max, 2):
            measurer = Resource_Measurer()
            boundary = n
            if bounding == "Half":
                boundary = math.floor(n / 2)
            elif bounding == "Sqrt":
                boundary = math.floor(math.sqrt(n))
            ret = tuple(map(ft.partial(is_prime_mapped, n), [j for j in data["primes"][i] if j <= boundary]))
            measurer.finish()
            resources = measurer.result()
            del measurer
            data["times"][i].append(resources["time_seconds"])
            data["memory_usage"][i].append(resources["memory_bytes"])

            data["divisions"][i][n] = len(ret)
            if all(ret):
                data["primes"][i].append(n)

    return data
