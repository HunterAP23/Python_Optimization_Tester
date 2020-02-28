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


cdef (bint, int) is_prime(int num):
    global table
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        for j in range(len(table)):
            checks = checks + 1
            if num % table[j] == 0:
                return (False, checks)
            else:
                continue
        table.append(num)
        return (True, checks)


cdef (bint, int) is_prime_half(int num):
    global table2
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        boundary = math.floor(num / 2)
        for j in range(len(table2)):
            if table2[j] <= boundary:
                checks = checks + 1
                if num % table2[j] == 0:
                    return (False, checks)
                else:
                    continue
        table2.append(num)
        return (True, checks)


cdef (bint, int) is_prime_sqrt(int num):
    global table3
    cdef int checks = 0

    if num <= 1:
        return (False, 0)
    else:
        checks = checks + 1
        boundary = math.floor(math.sqrt(num))
        for j in range(len(table3)):
            if table3[j] <= boundary:
                checks = checks + 1
                if num % table3[j] == 0:
                    return (False, checks)
                else:
                    continue
        table3.append(num)
        return (True, checks)


cdef void main_def(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_default_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/optimized_default_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/optimized_default_primes.txt"
    txt_output3 = open(my_file3, 'a')

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for j in range(num_loops):
        global table
        table = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Default Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} optimized normal passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


cdef void main_half(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_half_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/optimized_half_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/optimized_half_primes.txt"
    txt_output3 = open(my_file3, 'a')

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for j in range(num_loops):
        global table2
        table2 = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_half(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Half Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} optimized half passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


cdef void main_sqrt(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_sqrt_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/optimized_sqrt_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/optimized_sqrt_primes.txt"
    txt_output3 = open(my_file3, 'a')

    cdef list time_list = []
    cdef list divisions_list = []
    cdef list primes = []

    for j in range(num_loops):
        global table3
        table3 = []
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_sqrt(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Sqrt Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)


    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    cdef double average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} optimized square root passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()
