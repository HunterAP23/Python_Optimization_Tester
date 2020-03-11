import datetime as dt
import functools as ft
from math import sqrt, floor
import time

def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(n, table):
    if n % 2 == 0 and n > 2:
        return False
    else:
        if len(table) == 0:
            if all(n % i for i in range(2, n)):
                return True
        elif all(n % i for i in table):
            return True


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Default Lambda started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_default_lambda_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_default_lambda_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_default_lambda_primes.txt"
    txt_output3 = open(my_file3, "a")

    time_list = []
    divisions_list = []
    table = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table) == 0:
                    if all(n % i for i in range(2, n)):
                        table.append(n)
                elif all(n % i for i in table):
                    table.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default Lambda Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Lambda Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default lambda passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_def2(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Default Lambda2 started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_default2_lambda_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_default2_lambda_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_default2_lambda_primes.txt"
    txt_output3 = open(my_file3, "a")

    time_list = []
    divisions_list = []
    table = []

    for i in range(num_loops):
        table = []
        table.append(2)
        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            if all(n % i for i in table):
                table.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Default Lambda2 Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default Lambda2 Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default lambda2 passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half Lambda started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_lambda_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_half_lambda_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_half_lambda_primes.txt"
    txt_output3 = open(my_file3, "a")
    time_list = []
    divisions_list = []
    table2 = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table2) == 0:
                    if all(n % i for i in range(2, int(n / 2))):
                        table2.append(n)
                else:
                    point = int(len(table2) / 2)
                    if all(n % i for i in table2[:point]):
                        table2.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
            # primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half Lambda Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table2)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Lambda Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half lambda passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half2(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half Lambda Floor started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_lambda_floor_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_half_lambda_floor_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_half_lambda_floor_primes.txt"
    txt_output3 = open(my_file3, "a")
    time_list = []
    divisions_list = []
    table2 = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table2) == 0:
                    if all(n % i for i in range(2, floor(n / 2))):
                        table2.append(n)
                else:
                    point = floor(len(table2) / 2)
                    if all(n % i for i in table2[:point]):
                        table2.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
            # primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half Lambda Floor Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table2)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Lambda Floor Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half lambda floor passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half3(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half Lambda FloorDiv started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_lambda_floordiv_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_half_lambda_floordiv_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_half_lambda_floordiv_primes.txt"
    txt_output3 = open(my_file3, "a")
    time_list = []
    divisions_list = []
    table2 = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table2) == 0:
                    if all(n % i for i in range(2, n // 2)):
                        table2.append(n)
                else:
                    point = len(table2) // 2
                    if all(n % i for i in table2[:point]):
                        table2.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
            # primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half Lambda FloorDiv Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table2)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Lambda FloorDiv Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half lambda floordiv passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_half4(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half Lambda RShift started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    my_file = "files_runs/normal_half_lambda_rshift_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_half_lambda_rshift_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_half_lambda_rshift_primes.txt"
    txt_output3 = open(my_file3, "a")
    time_list = []
    divisions_list = []
    table2 = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table2) == 0:
                    if all(n % i for i in range(2, n >> 1)):
                        table2.append(n)
                else:
                    point = len(table2) >> 1
                    if all(n % i for i in table2[:point]):
                        table2.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
            # primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Half Lambda RShift Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table2)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half Lambda RShift Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half lambda rshift passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Lambda started."
    print_lock(msg, rlock)

    my_file = "files_runs/normal_sqrt_lambda_time.txt"
    txt_output = open(my_file, "a")
    my_file2 = "files_runs/normal_sqrt_lambda_divisions.txt"
    txt_output2 = open(my_file2, "a")
    my_file3 = "files_runs/normal_sqrt_lambda_primes.txt"
    txt_output3 = open(my_file3, "a")
    time_list = []
    divisions_list = []
    table3 = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        for n in range(2, my_max):
            if n % 2 == 0 and n > 2:
                continue
            else:
                if len(table3) == 0:
                    if all(n % i for i in range(2, int(sqrt(n)))):
                        table3.append(n)
                else:
                    point = (int(sqrt(len(table3))))
                    if all(n % i for i in table3[:point]):
                        table3.append(n)
        # for i in tmp:
            # divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))
            # primes.append(i)

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Normal Sqrt Lambda Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    # for item in list(set(divisions_list)):
    #     txt_output2.write(item)
    # txt_output2.close()

    for prime in list(set(table3)):
        pr = "{0}\n".format(prime)
        txt_output3.write(pr)
    txt_output3.close()

    overall_end = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt Lambda Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_end.year, overall_end.month, overall_end.day, overall_end.hour, overall_end.minute, overall_end.second, overall_end.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound lambda passes was {1} seconds.".format(num_loops, average_time)
    txt_output.write(msg)
    print_lock(msg, rlock)
    txt_output.close()
