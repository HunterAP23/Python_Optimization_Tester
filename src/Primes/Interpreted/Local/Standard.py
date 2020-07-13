import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def Main_Default(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Default (Local) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_standard/default_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            checks = 0

            for j in range(len(primes_list)):
                if n % primes_list[j] == 0:
                    continue
                else:
                    checks += 1
            div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, checks))
            primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Default (Local) Pass {0} took {1} seconds.\n\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_standard/default_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_standard/default_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default (Local) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default (Local) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half (Local) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_standard/half_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            checks = 0

            boundary = math.floor(n / 2)
            for j in range(len(primes_list)):
                if primes_list[j] <= boundary:
                    if n % primes_list[j] == 0:
                        continue
                    else:
                        checks += 1
                else:
                    break
            div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, checks))
            primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Half (Local) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_standard/half_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_standard/half_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half (Local) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half-bound (Local) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Sqrt (Local) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_standard/sqrt_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            checks = 0

            boundary = math.floor(math.sqrt(n))
            for j in range(len(primes_list)):
                if primes_list[j] <= boundary:
                    if n % primes_list[j] == 0:
                        continue
                    else:
                        checks += 1
                else:
                    break
            div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, checks))
            primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Sqrt (Local) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_standard/sqrt_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_standard/sqrt_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt (Local) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound (Local) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()