cimport cython
import datetime as dt
import functools as ft
import math
import time

table = []
table2 = []
table3 = []


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


def is_prime_half(num):
    global table2
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = math.floor(num / 2)
        for j in range(len(table2)):
            if table2[j] <= boundary:
                checks = checks + 1
                if num % table2[j] == 0:
                    return [False, checks]
                else:
                    continue
        table2.append(num)
        return [True, checks]


def is_prime_sqrt(num):
    global table3
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = math.floor(math.sqrt(num))
        for j in range(len(table3)):
            if table3[j] <= boundary:
                checks = checks + 1
                if num % table3[j] == 0:
                    return [False, checks]
                else:
                    continue
        table3.append(num)
        return [True, checks]


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Compiled Default started."
    print_lock(msg, rlock)

    my_file = "files_runs/compiled_default_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/compiled_default_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/compiled_default_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Compiled Default Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Compiled Default Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} compiled default passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Compiled Half started."
    print_lock(msg, rlock)

    my_file = "files_runs/compiled_half_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/compiled_half_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/compiled_half_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime_half(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Compiled Half Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Compiled Half Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} compiled half passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Compiled Sqrt started."
    print_lock(msg, rlock)

    my_file = "files_runs/compiled_sqrt_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/compiled_sqrt_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/compiled_sqrt_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime_sqrt(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Compiled Sqrt Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Compiled Sqrt Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} compiled square root passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()
