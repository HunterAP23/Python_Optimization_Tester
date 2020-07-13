cimport cython
import datetime as dt
import functools as ft
import math
import time


cdef list table = []
cdef list table2 = []
cdef list table3 = []


cdef void print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime(num):
    global table
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        for i in range(2, len(table)):
            checks = checks + 1
            if num % table[i] == 0:
                return (False, checks)
            else:
                continue
        table.append(num)
        return (True, checks)


@ft.lru_cache(maxsize=None)
def is_prime_half(num):
    global table2
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        boundary = math.floor(num / 2)
        for i in range(len(table2)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return (False, checks)
                else:
                    continue
        table2.append(num)
        return (True, checks)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(num):
    global table3
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        boundary = math.floor(math.sqrt(num))
        for i in range(len(table3)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return (False, checks)
                else:
                    continue
        table3.append(num)
        return (True, checks)


cdef void Main_Default(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default LRU started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_default_LRU_main_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/optimized_default_LRU_main_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/optimized_default_LRU_main_primes.txt"
    txt_output3 = open(my_file3, "a")

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for i in range(num_loops):
        global table
        table = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime(j)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Default LRU Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default LRU Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Optimized is_prime.cache_info(): {0}".format(is_prime.cache_info())
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} optimized LRU normal passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


cdef void Main_Half(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_half_LRU_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/optimized_half_LRU_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/optimized_half_LRU_primes.txt"
    txt_output3 = open(my_file3, "a")

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for i in range(num_loops):
        global table2
        table2 = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_half(j)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Half LRU  Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half LRU Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Optimized is_prime_half.cache_info(): {0}".format(is_prime_half.cache_info())
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} optimized half LRU passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


cdef void Main_Sqrt(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt LRU started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_sqrt_LRU_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/optimized_sqrt_LRU_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/optimized_sqrt_LRU_primes.txt"
    txt_output3 = open(my_file3, "a")

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for i in range(num_loops):
        global table3
        table3 = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_sqrt(j)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Sqrt LRU Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt LRU Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Optimized is_prime_sqrt.cache_info(): {0}".format(is_prime_sqrt.cache_info())
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} optimized LRU sqrt-bound passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()
