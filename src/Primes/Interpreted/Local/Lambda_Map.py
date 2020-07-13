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
    msg += "Normal Default (Local Lambda Map) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_lambda_map/default_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            ret = list(map(lambda y: n % y, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Default (Local Lambda Map) Pass {0} took {1} seconds.\n\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_lambda_map/default_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_lambda_map/default_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default (Local Lambda Map) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default (Local Lambda Map) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half (Local Lambda Map) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_lambda_map/half_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            boundary = math.floor(n / 2)
            ret = list(map(lambda y: n % y if y <= boundary else 0, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Half (Local Lambda Map) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_lambda_map/half_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_lambda_map/half_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half (Local Lambda Map) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half-bound (Local Lambda Map) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Sqrt (Local Lambda Map) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/cpython_interpreted_local_lambda_map/sqrt_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            boundary = math.floor(math.sqrt(n))
            ret = list(map(lambda y: n % y if y <= boundary else 0, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Sqrt (Local Lambda Map) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/cpython_interpreted_local_lambda_map/sqrt_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/cpython_interpreted_local_lambda_map/sqrt_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt (Local Lambda Map) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound (Local Lambda Map) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()
