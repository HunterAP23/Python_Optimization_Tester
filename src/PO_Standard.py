#!/usr/bin/env python
import sys
import time
from datetime import timedelta

import psutil


def ValueError_Handler(var, exp, var_type):
    val_exp = None
    val_var = None
    if "<class 'type'>" == str(type(var_type)):
        try:
            val_exp = var_type(var)
        except ValueError:
            print("ERROR: Could not cast value of '{0}' to type '{1}'.".format(var, var_type))
            return None

        try:
            val_var = var_type(exp)
        except ValueError:
            print("ERROR: Could not cast value of '{0}' to type '{1}'.".format(exp, var_type))
            return None

        if val_var == val_exp:
            return True
        else:
            return False
    else:
        print("ERROR: '{0}' is a not a type class.")
        return None


# def bytes2human(
#     n,
#     format="%(value).1f%(symbol)s",
# ):
#     """Used by various scripts. See:
#     http://goo.gl/zeJZl
#     >>> bytes2human(10000)
#     '9.8K'
#     >>> bytes2human(100001221)
#     '95.4M'
#     """
#     symbols = ("B", "K", "M", "G", "T", "P", "E", "Z", "Y")
#     prefix = {}
#     for i, s in enumerate(symbols[1:]):
#         prefix[s] = 1 << (i + 1) * 10
#     for symbol in reversed(symbols[1:]):
#         if n >= prefix[symbol]:
#             value = float(n) / prefix[symbol]
#             return format % locals()
#     return format % dict(symbol=symbols[0], value=n)


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def measure_resources(func):
    def wrapper(*args, **kwargs):
        mem_before = psutil.Process().memory_info().rss
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        mem_after = (
            psutil.Process().memory_info().rss - sys.getsizeof(start) - sys.getsizeof(end) - sys.getsizeof(mem_before)
        )
        return result, {
            "time_seconds": end - start,
            "time_formatted": str(timedelta(seconds=end - start)),
            "memory_bytes": mem_after - mem_before - sys.getsizeof(mem_after),
            "memory_formatted": sizeof_fmt(mem_after - mem_before),
        }

    return wrapper


def measure(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result, {}

    return wrapper


def measure_memory(func):
    def wrapper(*args, **kwargs):
        proc = psutil.Process()
        mem_before = proc.memory_info().rss
        result, stats = func(*args, **kwargs)
        mem_after = proc.memory_info().rss
        return result, stats | {
            "memory_bytes": mem_after - mem_before,
            "memory_formatted": sizeof_fmt(mem_after - mem_before),
        }

    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result, stats = func(*args, **kwargs)
        end = time.perf_counter()
        return result, stats | {
            "time_seconds": end - start,
            "time_formatted": str(timedelta(seconds=end - start)),
        }

    return wrapper


class Resource_Measurer:
    def __init__(self):
        self._time_start = time.perf_counter()
        self._mem_before = psutil.Process().memory_info().rss

    def finish(self):
        self._time_end = time.perf_counter()
        self._after = psutil.Process().memory_info().rss - sys.getsizeof(self)

    def result(self):
        return {
            "time_seconds": self._end - self._start,
            "time_formatted": str(timedelta(seconds=self.end - self.start)),
            "memory_bytes": self._after - self._before,
            "memory_formatted": sizeof_fmt(self._after - self._before),
        }
