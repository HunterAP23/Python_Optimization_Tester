import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def Main_Default(
    value_max: int, num_loops: int, rlock, runtime: str, compilation: str, call_type: str, subcall: str, case: str
):
    group = " ".join([runtime, compilation, call_type, subcall])
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "{0} {1} started at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        overall_start.year,
        overall_start.month,
        overall_start.day,
        overall_start.hour,
        overall_start.minute,
        overall_start.second,
        overall_start.microsecond,
    )
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.perf_counter()
        for n in range(3, value_max, 2):
            ret = list(map(lambda y: n % y, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.perf_counter() - tmp_time_start

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
    msg += "{0} {1} finished at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        time_now.year,
        time_now.month,
        time_now.day,
        time_now.hour,
        time_now.minute,
        time_now.second,
        time_now.microsecond,
    )
    print_lock(msg, rlock)

    # average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    average_time = math.fsum(time_list)
    msg = "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(
        num_loops, group, case, average_time
    )
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Half(
    value_max: int, num_loops: int, rlock, runtime: str, compilation: str, call_type: str, subcall: str, case: str
):
    group = " ".join([runtime, compilation, call_type, subcall])
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "{0} {1} started at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        overall_start.year,
        overall_start.month,
        overall_start.day,
        overall_start.hour,
        overall_start.minute,
        overall_start.second,
        overall_start.microsecond,
    )
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.perf_counter()
        for n in range(3, value_max, 2):
            boundary = math.floor(n / 2)
            ret = list(map(lambda y: n % y if y <= boundary else 1, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.perf_counter() - tmp_time_start

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
    msg += "{0} {1} finished at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        time_now.year,
        time_now.month,
        time_now.day,
        time_now.hour,
        time_now.minute,
        time_now.second,
        time_now.microsecond,
    )
    print_lock(msg, rlock)

    # average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    average_time = math.fsum(time_list)
    msg = "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(
        num_loops, group, case, average_time
    )
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def Main_Sqrt(
    value_max: int, num_loops: int, rlock, runtime: str, compilation: str, call_type: str, subcall: str, case: str
):
    group = " ".join([runtime, compilation, call_type, subcall])
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "{0} {1} started at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        overall_start.year,
        overall_start.month,
        overall_start.day,
        overall_start.hour,
        overall_start.minute,
        overall_start.second,
        overall_start.microsecond,
    )
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.perf_counter()
        for n in range(3, value_max, 2):
            boundary = math.floor(math.sqrt(n))
            ret = list(map(lambda y: n % y if y <= boundary else 1, primes_list))

            if all(ret):
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, sum(ret)))
                primes_list.append(n)

        tmp_time_total = time.perf_counter() - tmp_time_start

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
    msg += "{0} {1} finished at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(
        group,
        case,
        time_now.year,
        time_now.month,
        time_now.day,
        time_now.hour,
        time_now.minute,
        time_now.second,
        time_now.microsecond,
    )
    print_lock(msg, rlock)

    # average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    average_time = math.fsum(time_list)
    msg = "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(
        num_loops, group, case, average_time
    )
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()
