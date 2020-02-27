import datetime as dt
import functools as ft
import math
import numpy as np
import time


# def split(arr, cond):
#   # return [arr[cond], arr[~cond]]
#   return arr[cond]


table = np.empty((1,))


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(num):
    global table
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        for j in range(len(table)):
            checks = checks + 1
            if num % table[j] == 0:
                return [False, checks]
            else:
                continue
        table.append(num)
        return [True, checks]


def is_prime_half(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, math.floor(n / 2), 2))


def is_prime_sqrt(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, math.floor(math.sqrt(n)), 2))


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_default_numpy_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_default_numpy_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    time_list = []
    divisions_list = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, my_max)
        foo = np.vectorize(is_prime)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default Numpy Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Numpy Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal default numpy passes was {1}.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_numpy_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_half_numpy_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, my_max)
        foo = np.vectorize(is_prime_half)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start
        txt_output.write("Normal Half Numpy Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Numpy Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal half numpy passes was {1}.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Numpy started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_sqrt_numpy_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_sqrt_numpy_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        vals = np.arange(1, my_max)
        foo = np.vectorize(is_prime_sqrt)
        pbools = foo(vals)
        primes = np.extract(pbools, vals)
        for prime in primes:
            divisions_list.append("{0}\n".format(prime))

        tmp_time_total = time.time() - tmp_time_start
        txt_output.write("Normal Sqrt Numpy Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    # for prime in list(set(primes)):
    #     txt_output3.write(prime)
    # txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Numpy Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal square root numpy passes was {1}.".format(num_loops, average_time)
    print_lock(msg, rlock)
    txt_output.write(msg)
    txt_output.close()
