import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(n):
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


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Default started."
    print_lock(msg, rlock)

    global table

    my_file = "files_runs/normal_default_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_default_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/normal_default_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

        table = []

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal default passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Half started."
    print_lock(msg, rlock)

    global table2

    my_file = "files_runs/normal_half_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_half_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/normal_half_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_half(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

        table2 = []

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal half passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt started."
    print_lock(msg, rlock)

    global table3

    my_file = "files_runs/normal_sqrt_time.txt"
    txt_output = open(my_file, 'a')
    my_file2 = "files_runs/normal_sqrt_divisions.txt"
    txt_output2 = open(my_file2, 'a')
    my_file3 = "files_runs/normal_sqrt_primes.txt"
    txt_output3 = open(my_file3, 'a')
    time_list = []
    divisions_list = []
    primes = []

    for j in range(num_loops):
        tmp_time_start = time.time()
        for i in range(my_max):
            tmp = is_prime_sqrt(i)
            if tmp[0]:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
                primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Sqrt Pass {0} took {1} seconds.\n".format(j + 1, tmp_time_total))
        time_list.append(tmp_time_total)

        table3 = []

    for item in list(set(divisions_list)):
        txt_output2.write(item)
    txt_output2.close()

    for prime in list(set(primes)):
        txt_output3.write(prime)
    txt_output3.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "The average time it took to calculate {0} normal square root passes was {1}.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()
