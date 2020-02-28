# Native Libs
import argparse as argp
import multiprocessing as mp
import os
import time

# Custom Funcs
import Find_Nth_Prime_Python
import Find_Nth_Prime_Python_Lambda
import Find_Nth_Prime_Python_LRU

import Find_Nth_Prime_Python_Numpy
import Find_Nth_Prime_Python_Numpy_Lambda
import Find_Nth_Prime_Python_Numpy_LRU

# import Find_Nth_Prime_Cython
# import Find_Nth_Prime_Cython_Lambda
# import Find_Nth_Prime_Cython_LRU

# import Find_Nth_Prime_Cython_Numpy
# import Find_Nth_Prime_Cython_Numpy_Lambda
# import Find_Nth_Prime_Cython_Numpy_LRU

# import Find_Nth_Prime_Optimized
# import Find_Nth_Prime_Optimized_Lambda
# import Find_Nth_Prime_Optimized_LRU

# import Find_Nth_Prime_Optimized_Numpy
# import Find_Nth_Prime_Optimized_Numpy_Lambda
# import Find_Nth_Prime_Optimized_Numpy_LRU


def time_function(func, argoos, name, sema, rlock):
    sema.acquire()
    start = time.time()
    func(int(argoos[0]), int(argoos[1]), rlock)
    total = time.time() - start
    argoos[2][name] = total
    sema.release()


def run_in_parallel(fns, args, rlock):
    proc = []
    i = 0
    for fn in fns:
        if i == 0:
            namer = "Normal_Default"
        elif i == 1:
            namer = "Normal_Half"
        elif i == 2:
            namer = "Normal_Sqrt"
        elif i == 3:
            namer = "Compiled_Default"
        elif i == 4:
            namer = "Compiled_Half"
        elif i == 5:
            namer = "Compiled_Sqrt"
        elif i == 6:
            namer = "Optimized_Default"
        elif i == 7:
            namer = "Optimized_Half"
        elif i == 8:
            namer = "Optimized_Sqrt"
        elif i == 9:
            namer = "Normal_Default_LRU"
        elif i == 10:
            namer = "Normal_Half_LRU"
        elif i == 11:
            namer = "Normal_Sqrt_LRU"
        elif i == 12:
            namer = "Compiled_Default_LRU"
        elif i == 13:
            namer = "Compiled_Half_LRU"
        elif i == 14:
            namer = "Compiled_Sqrt_LRU"
        elif i == 15:
            namer = "Optimized_Default_LRU"
        elif i == 16:
            namer = "Optimized_Half_LRU"
        else:
            namer = "Optimized_Sqrt_LRU"
        p = mp.Process(target=time_function, args=(fn, args, namer, rlock))
        proc.append(p)
        i += 1

    for p in proc:
        p.start()

    for p in proc:
        p.join()


def parse_arguments():
    parser = argp.ArgumentParser(description="Cython & LRU Cache Tester", add_help=False)

    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument('-t', '--threads', default=mp.cpu_count(), type=int, required=False, help="send the email report, skip email prompts.", dest="Threads")

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    manager = mp.Manager()
    return_dict = manager.dict()
    sema = manager.Semaphore(1)
    rlock = manager.RLock()
    print("Availble CPU Cores: {0}".format(args.Threads))

    user_max = input("Enter the maximum number to calculate primes up to: ")
    num_loops = input("How many loops do you want to go through for each test? ")

    try:
        os.mkdir("files_runs")
    except FileExistsError:
        pass

    testing_start = time.time()

    funcs = []

    #CPYTHON
    funcs.append(Find_Nth_Prime_Python.main_def)
    funcs.append(Find_Nth_Prime_Python.main_half)
    funcs.append(Find_Nth_Prime_Python.main_sqrt)

    funcs.append(Find_Nth_Prime_Python_Lambda.main_def)
    funcs.append(Find_Nth_Prime_Python_Lambda.main_half)
    funcs.append(Find_Nth_Prime_Python_Lambda.main_sqrt)

    funcs.append(Find_Nth_Prime_Python_LRU.main_def)
    funcs.append(Find_Nth_Prime_Python_LRU.main_half)
    funcs.append(Find_Nth_Prime_Python_LRU.main_sqrt)

    # NUMPY
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_sqrt)

    # funcs.append(Find_Nth_Prime1.main_def)
    # funcs.append(Find_Nth_Prime1.main_half)
    # funcs.append(Find_Nth_Prime1.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime2.main_def)
    # funcs.append(Find_Nth_Prime2.main_half)
    # funcs.append(Find_Nth_Prime2.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime_LRU.main_def)
    # funcs.append(Find_Nth_Prime_LRU.main_half)
    # funcs.append(Find_Nth_Prime_LRU.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime1_LRU.main_def)
    # funcs.append(Find_Nth_Prime1_LRU.main_half)
    # funcs.append(Find_Nth_Prime1_LRU.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime2_LRU.main_def)
    # funcs.append(Find_Nth_Prime2_LRU.main_half)
    # funcs.append(Find_Nth_Prime2_LRU.main_sqrt)

    arguments = [user_max, num_loops, return_dict]

    run_in_parallel(funcs, arguments, rlock)

    testing_total = time.time() - testing_start

    for k, v in return_dict.items():
        result_file = None

        if k == "Normal_Default":
            result_file = open('files_runs/normal_default_time.txt', 'a')
        elif k == "Normal_Half":
            result_file = open('files_runs/normal_half_time.txt', 'a')
        elif k == "Normal_Sqrt":
            result_file = open('files_runs/normal_sqrt_time.txt', 'a')
        elif k == "Compiled_Default":
            result_file = open('files_runs/compiled_default_time.txt', 'a')
        elif k == "Compiled_Half":
            result_file = open('files_runs/compiled_half_time.txt', 'a')
        elif k == "Compiled_Sqrt":
            result_file = open('files_runs/compiled_sqrt_time.txt', 'a')
        elif k == "Optimized_Default":
            result_file = open('files_runs/optimized_default_time.txt', 'a')
        elif k == "Optimized_Half":
            result_file = open('files_runs/optimized_half_time.txt', 'a')
        elif k == "Optimized_Sqrt":
            result_file = open('files_runs/optimized_sqrt_time.txt', 'a')
        elif k == "Normal_Default_LRU":
            result_file = open('files_runs/normal_default_LRU_time.txt', 'a')
        elif k == "Normal_Half_LRU":
            result_file = open('files_runs/normal_half_LRU_time.txt', 'a')
        elif k == "Normal_Sqrt_LRU":
            result_file = open('files_runs/normal_sqrt_LRU_time.txt', 'a')
        elif k == "Compiled_Default_LRU":
            result_file = open('files_runs/compiled_default_LRU_time.txt', 'a')
        elif k == "Compiled_Half_LRU":
            result_file = open('files_runs/compiled_half_LRU_time.txt', 'a')
        elif k == "Compiled_Sqrt_LRU":
            result_file = open('files_runs/compiled_sqrt_LRU_time.txt', 'a')
        elif k == "Optimized_Default_LRU":
            result_file = open('files_runs/optimized_default_LRU_time.txt', 'a')
        elif k == "Optimized_Half_LRU":
            result_file = open('files_runs/optimized_half_LRU_time.txt', 'a')
        elif k == "Optimized_Sqrt_LRU":
            result_file = open('files_runs/optimized_sqrt_LRU_time.txt', 'a')

        result_file.write("{0} took {1}H:{2}M:{3:0.2f}S".format(k, int(v / 3600), int(v / 60), v))
        result_file.close()
        print("-" * 80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-" * 80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_total / 3600), int(testing_total / 60), testing_total))
