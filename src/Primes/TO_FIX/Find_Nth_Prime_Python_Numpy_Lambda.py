import datetime as dt
import functools as ft
import math
import numpy as np
import time


# def split(arr, cond):
#   # return [arr[cond], arr[~cond]]
#   return arr[cond]


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, n, 2))


def is_prime_half(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, math.floor(n / 2), 2))


def is_prime_sqrt(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, math.floor(math.sqrt(n)), 2))


def Main_Default(value_max: int, num_loops: int, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_default_numpy_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_default_numpy_divisions.txt"
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []
    primes = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, value_max)
        foo = np.vectorize(is_prime)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default Numpy Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Numpy finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default numpy passes was {1} seconds.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()


def Main_Half(value_max: int, num_loops: int, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_numpy_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_half_numpy_divisions.txt"
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []
    primes = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, value_max)
        foo = np.vectorize(is_prime_half)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start
        txt_output.write("Normal Half Numpy Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Numpy finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half numpy passes was {1} seconds.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()


def Main_Sqrt(value_max: int, num_loops: int, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_sqrt_numpy_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_sqrt_numpy_divisions.txt"
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []
    primes = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, value_max)
        foo = np.vectorize(is_prime_sqrt)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start
        txt_output.write("Normal Sqrt Numpy Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Numpy finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound numpy passes was {1} seconds.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()
