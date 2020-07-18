"""Interpeted Function Lambda."""

import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    """Lock print capabilities until a message is sent."""
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime_default(n: int, table):
    """Interpeted Function Lambda Default."""
    my_lam = lambda y: n % y
    ret = []
    for i in range(len(table)):
        ret.append(my_lam(table[i]))
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


def is_prime_half(n: int, table):
    """Interpeted Function Lambda Half."""
    boundary = math.floor(n / 2)
    my_lam = lambda y: n % y
    ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


def is_prime_sqrt(n: int, table):
    """Interpeted Function Lambda Square Root."""
    boundary = math.floor(math.sqrt(n))
    my_lam = lambda y: n % y
    ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


def Main(value_max: int, num_loops: int, rlock, runtime, compilation, call_type, subcall, case):
    """Interpeted Function Lambda Main."""
    group = " ".join([runtime, compilation, call_type, subcall])
    print_lock(group, rlock)
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "{0} {1} started at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(group, case, overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w")

    func = globals()["is_prime_{0}".format(case.lower())]

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, value_max, 2):
            ret = func(n, tuple(primes_list))

            if ret[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, ret[1]))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("{0} {1} Pass {2} took {3} seconds.\n\n".format(group, case, i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/{0}/divisions_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/{0}/primes_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "{0} {1} finished at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(group, case, time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(num_loops, group, case, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


# def Main_Default(value_max, num_loops, rlock, runtime, compilation, call_type, subcall, case):
#     msg = ("-" * 80) + "\n"
#     overall_start = dt.datetime.now()
#     msg += "CPython Interpreted (Function Lambda) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
#     print_lock(msg, rlock)
#
#     time_list = []
#     div_list = []
#     primes_list = []
#
#     time_output = open("files_runs/cpython_interpreted_function_lambda/default_time.txt", "w")
#
#     for i in range(num_loops):
#         # Clear the lists before a run
#         time_list = []
#         div_list = []
#         primes_list = []
#         primes_list.append(2)
#
#         tmp_time_start = time.time()
#         for n in range(3, value_max, 2):
#             tmp = is_prime_default(n, tuple(primes_list))
#             if tmp[0]:
#                 div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
#                 primes_list.append(n)
#
#         tmp_time_total = time.time() - tmp_time_start
#
#         time_output.write("CPython Interpreted (Function Lambda) Pass {0} took {1} seconds.\n\n".format(i + 1, tmp_time_total))
#         time_list.append(tmp_time_total)
#
#     with open("files_runs/cpython_interpreted_function_lambda/default_divisions.txt", "w") as div_output:
#         for div in div_list:
#             div_output.write(div)
#
#     with open("files_runs/cpython_interpreted_function_lambda/default_primes.txt", "w") as primes_output:
#         for prime in primes_list:
#             primes_output.write("{0}\n".format(prime))
#
#     time_now = dt.datetime.now()
#     msg = ("-" * 80) + "\n"
#     msg += "CPython Interpreted (Function Lambda) finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
#     print_lock(msg, rlock)
#
#     average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
#     msg = "Average time it took to calculate {0} normal default (Function Lambda) passes was {1} seconds.".format(num_loops, average_time)
#     time_output.write(msg)
#     print_lock(msg, rlock)
#     time_output.close()
#
#
# def Main_Half(value_max, num_loops, rlock, runtime, compilation, call_type, subcall, case):
#     msg = ("-" * 80) + "\n"
#     overall_start = dt.datetime.now()
#     msg += "Normal Half (Function Lambda) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
#     print_lock(msg, rlock)
#
#     time_list = []
#     div_list = []
#     primes_list = []
#
#     time_output = open("files_runs/cpython_interpreted_function_lambda/half_time.txt", "w")
#
#     for i in range(num_loops):
#         # Clear the lists before a run
#         time_list = []
#         div_list = []
#         primes_list = []
#         primes_list.append(2)
#
#         tmp_time_start = time.time()
#         for n in range(3, value_max, 2):
#             tmp = is_prime_half(n, tuple(primes_list))
#             if tmp[0]:
#                 div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
#                 primes_list.append(n)
#
#         tmp_time_total = time.time() - tmp_time_start
#
#         time_output.write("Normal Half (Function Lambda) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
#         time_list.append(tmp_time_total)
#
#     with open("files_runs/cpython_interpreted_function_lambda/half_divisions.txt", "w") as div_output:
#         for div in div_list:
#             div_output.write(div)
#
#     with open("files_runs/cpython_interpreted_function_lambda/half_primes.txt", "w") as primes_output:
#         for prime in primes_list:
#             primes_output.write("{0}\n".format(prime))
#
#     time_now = dt.datetime.now()
#     msg = ("-" * 80) + "\n"
#     msg += "Normal Half (Function Lambda) finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
#     print_lock(msg, rlock)
#
#     average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
#     msg = "Average time it took to calculate {0} normal half-bound (Function Lambda) passes was {1} seconds.".format(num_loops, average_time)
#     time_output.write(msg)
#     print_lock(msg, rlock)
#     time_output.close()
#
#
# def Main_Sqrt(value_max, num_loops, rlock, runtime, compilation, call_type, subcall, case):
#     msg = ("-" * 80) + "\n"
#     overall_start = dt.datetime.now()
#     msg += "Normal Sqrt (Function Lambda) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
#     print_lock(msg, rlock)
#
#     time_list = []
#     div_list = []
#     primes_list = []
#
#     time_output = open("files_runs/cpython_interpreted_function_lambda/sqrt_time.txt", "w")
#
#     for i in range(num_loops):
#         # Clear the lists before a run
#         time_list = []
#         div_list = []
#         primes_list = []
#         primes_list.append(2)
#
#         tmp_time_start = time.time()
#         for n in range(3, value_max, 2):
#             tmp = is_prime_sqrt(n, tuple(primes_list))
#             if tmp[0]:
#                 div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
#                 primes_list.append(n)
#
#         tmp_time_total = time.time() - tmp_time_start
#
#         time_output.write("Normal Sqrt (Function Lambda) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
#         time_list.append(tmp_time_total)
#
#     with open("files_runs/cpython_interpreted_function_lambda/sqrt_divisions.txt", "w") as div_output:
#         for div in div_list:
#             div_output.write(div)
#
#     with open("files_runs/cpython_interpreted_function_lambda/sqrt_primes.txt", "w") as primes_output:
#         for prime in primes_list:
#             primes_output.write("{0}\n".format(prime))
#
#     time_now = dt.datetime.now()
#     msg = ("-" * 80) + "\n"
#     msg += "Normal Sqrt (Function Lambda) finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
#     print_lock(msg, rlock)
#
#     average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
#     msg = "Average time it took to calculate {0} normal sqrt-bound (Function Lambda) passes was {1} seconds.".format(num_loops, average_time)
#     time_output.write(msg)
#     print_lock(msg, rlock)
#     time_output.close()
