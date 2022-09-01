import math
import time
from typing import Literal


def is_prime(
    value_max: int,
    num_loops: int,
    bounding: Literal["Default", "Half", "Sqrt"],
    **kwargs,
):
    data = {
        "divisions": dict(),
        "primes": dict(),
        "times": dict(),
    }

    for i in range(num_loops):
        data["divisions"][i] = dict()
        data["times"][i] = []
        data["primes"][i] = []
        data["primes"][i].append(2)

        for n in range(3, value_max, 2):
            tmp_time_start = time.perf_counter()
            boundary = n
            if bounding == "Half":
                boundary = math.floor(n / 2)
            elif bounding == "Sqrt":
                boundary = math.floor(math.sqrt(n))
            ret = [lambda j: n % j for j in data["primes"][i] if j <= boundary]
            tmp_time_end = time.perf_counter()
            data["times"][i].append(tmp_time_end - tmp_time_start)

            data["divisions"][i][n] = len(ret)
            if all(ret):
                data["primes"][i].append(n)

    return data
