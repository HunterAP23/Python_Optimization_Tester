import datetime as dt
import decimal
import functools as ft
import math
import numbers
import time

table = []
table2 = []
table3 = []


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(num):
    global table
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        for i in range(len(table)):
            checks = checks + 1
            if num % table[i] == 0:
                return [False, checks]
            else:
                continue
        table.append(num)
        return [True, checks]


@ft.lru_cache(maxsize=None)
def is_prime_half(num):
    global table2
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = math.floor(num / 2)
        for i in range(len(table2)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return [False, checks]
                else:
                    continue
        table2.append(num)
        return [True, checks]


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(num):
    global table3
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = int(math.floor(math.sqrt(num)))
        for i in range(len(table3)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return [False, checks]
                else:
                    continue
        table3.append(num)
        return [True, checks]


def Main_Default(value_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Default LRU started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_default_lru_time.txt"
    my_file2 = "files_runs/normal_default_lru_divisions.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(value_max):
            tmp = is_prime_default(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default LRU Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default LRU finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Normal is_prime.cache_info(): {0}".format(is_prime.cache_info())

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} normal default LRU passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()


def Main_Half(value_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Half LRU started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_lru_time.txt"
    my_file2 = "files_runs/normal_half_lru_division.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(value_max):
            tmp = is_prime_half(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half LRU Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half LRU finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Normal is_prime.cache_info(): {0}".format(is_prime.cache_info())

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} normal half LRU passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()


def Main_Sqrt(value_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt LRU started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_sqrt_lru_time.txt"
    my_file2 = "files_runs/normal_sqrt_lru_divisions.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(value_max):
            tmp = is_prime_sqrt(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Sqrt LRU Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt LRU finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    # msg += "Normal is_prime.cache_info(): {0}".format(is_prime.cache_info())

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} normal sqrt-bound LRU passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()
