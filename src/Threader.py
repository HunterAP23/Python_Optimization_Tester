# Native Libs
import argparse as argp
import multiprocessing as mp
import os
import time

# Custom Funcs
import Primes.Find_Nth_Prime_Python_Function as Prime_Normal_Func
import Primes.Find_Nth_Prime_Python_Local as Prime_Normal_Loc
import Primes.Find_Nth_Prime_Python_Function_Lambda as Prime_Normal_Func_Lambda
import Primes.Find_Nth_Prime_Python_Local_Lambda as Prime_Normal_Loc_Lambda
# import Find_Nth_Prime_Python_LRU
#
# import Find_Nth_Prime_Python_Numpy
# import Find_Nth_Prime_Python_Numpy_Lambda
# import Find_Nth_Prime_Python_Numpy_LRU

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


def run_in_parallel(fns, args, sema, rlock):
    proc = []
    # i = 0
    for name, fn in fns.items():
        # if i == 0:
        #     namer = "Normal_Default_Function"
        # elif i == 1:
        #     namer = "Normal_Half_Function"
        # elif i == 2:
        #     namer = "Normal_Sqrt_Function"
        # elif i == 3:
        #     namer = "Compiled_Default_Function"
        # elif i == 4:
        #     namer = "Compiled_Half_Function"
        # elif i == 5:
        #     namer = "Compiled_Sqrt_Function"
        # elif i == 6:
        #     namer = "Optimized_Default_Function"
        # elif i == 7:
        #     namer = "Optimized_Half_Function"
        # elif i == 8:
        #     namer = "Optimized_Sqrt_Function"
        # elif i == 9:
        #     namer = "Normal_Default_Function_LRU"
        # elif i == 10:
        #     namer = "Normal_Half_Function_LRU"
        # elif i == 11:
        #     namer = "Normal_Sqrt_Function_LRU"
        # elif i == 12:
        #     namer = "Compiled_Default_LRU"
        # elif i == 13:
        #     namer = "Compiled_Half_Function_LRU"
        # elif i == 14:
        #     namer = "Compiled_Sqrt_Function_LRU"
        # elif i == 15:
        #     namer = "Optimized_Default_Function_LRU"
        # elif i == 16:
        #     namer = "Optimized_Half_Function_LRU"
        # else:
        #     namer = "Optimized_Sqrt_Function_LRU"
        # namer = "{0}_{1}".format(fn.__module__, fn.__name__)
        p = mp.Process(target=time_function, args=(fn, args, name, sema, rlock))
        proc.append(p)
        # i += 1

    for p in proc:
        p.start()

    for p in proc:
        p.join()


def parse_arguments():
    parser = argp.ArgumentParser(description="Cython & LRU Cache Tester", add_help=False)

    optional_args = parser.add_argument_group("optional arguments")
    optional_args.add_argument("-t", "--threads", default=mp.cpu_count(), type=int, required=False, help="send the email report, skip email prompts.", dest="Threads")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    manager = mp.Manager()
    return_dict = manager.dict()
    sema = manager.Semaphore(args.Threads)
    rlock = manager.RLock()
    print("Availble CPU Cores: {0}".format(args.Threads))

    user_max = input("Enter the maximum number to calculate primes up to: ")
    num_loops = input("How many loops do you want to go through for each test? ")

    try:
        os.mkdir("files_runs")
    except FileExistsError:
        pass

    testing_start = time.time()

    funcs = dict()

    # CPYTHON
    try:
        os.mkdir("files_runs/normal_function")
    except FileExistsError:
        pass
    funcs["Normal_Default_Function"] = Prime_Normal_Func.main_def
    funcs["Normal_Half_Function"] = Prime_Normal_Func.main_half
    funcs["Normal_Sqrt_Function"] = Prime_Normal_Func.main_sqrt

    try:
        os.mkdir("files_runs/normal_local")
    except FileExistsError:
        pass
    funcs["Normal_Default_Local"] = Prime_Normal_Loc.main_def
    funcs["Normal_Half_Local"] = Prime_Normal_Loc.main_half
    funcs["Normal_Sqrt_Local"] = Prime_Normal_Loc.main_sqrt

    try:
        os.mkdir("files_runs/normal_function_lambda")
    except FileExistsError:
        pass
    funcs["Normal_Default_Function_Lambda"] = Prime_Normal_Func_Lambda.main_def
    funcs["Normal_Half_Function_Lambda"] = Prime_Normal_Func_Lambda.main_half
    funcs["Normal_Sqrt_Function_Lambda"] = Prime_Normal_Func_Lambda.main_sqrt

    try:
        os.mkdir("files_runs/normal_local_lambda")
    except FileExistsError:
        pass
    funcs["Normal_Default_Local_Lambda"] = Prime_Normal_Loc_Lambda.main_def
    funcs["Normal_Half_Local_Lambda"] = Prime_Normal_Loc_Lambda.main_half
    funcs["Normal_Sqrt_Local_Lambda"] = Prime_Normal_Loc_Lambda.main_sqrt
    #
    # try:
    #     os.mkdir("files_runs/normal_lru")
    # except FileExistsError:
    #     pass
    # funcs.append(Find_Nth_Prime_Python_LRU.main_def)
    # funcs.append(Find_Nth_Prime_Python_LRU.main_half)
    # funcs.append(Find_Nth_Prime_Python_LRU.main_sqrt)

    # NUMPY
    # try:
    #     os.mkdir("files_runs/normal_numpy")
    # except FileExistsError:
    #     pass
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy.main_sqrt)
    #
    # try:
    #     os.mkdir("files_runs/normal_numpy_lambda")
    # except FileExistsError:
    #     pass
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy_Lambda.main_sqrt)
    #
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_def)
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_half)
    # funcs.append(Find_Nth_Prime_Python_Numpy_LRU.main_sqrt)

    arguments = [user_max, num_loops, return_dict]

    run_in_parallel(funcs, arguments, sema, rlock)

    testing_total = time.time() - testing_start

    for k, v in return_dict.items():
        result_file = None

        # if k == "Normal_Default_Function":
        #     result_file = open("files_runs/normal_default_function_time.txt", "w")
        # elif k == "Normal_Half_Function":
        #     result_file = open("files_runs/normal_half_function_time.txt", "w")
        # elif k == "Normal_Sqrt_Function":
        #     result_file = open("files_runs/normal_sqrt_function_time.txt", "w")
        # elif k == "Compiled_Default_Function":
        #     result_file = open("files_runs/compiled_default_function_time.txt", "w")
        # elif k == "Compiled_Half_Function":
        #     result_file = open("files_runs/compiled_half_function_time.txt", "w")
        # elif k == "Compiled_Sqrt_Function":
        #     result_file = open("files_runs/compiled_sqrt_function_time.txt", "w")
        # elif k == "Optimized_Default_Function":
        #     result_file = open("files_runs/optimized_default_function_time.txt", "w")
        # elif k == "Optimized_Half_Function":
        #     result_file = open("files_runs/optimized_half_function_time.txt", "w")
        # elif k == "Optimized_Sqrt_Function":
        #     result_file = open("files_runs/optimized_sqrt_function_time.txt", "w")
        # elif k == "Normal_Default_Function_LRU":
        #     result_file = open("files_runs/normal_default_LRU_function_time.txt", "w")
        # elif k == "Normal_Half_Function_LRU":
        #     result_file = open("files_runs/normal_half_LRU_function_time.txt", "w")
        # elif k == "Normal_Sqrt_Function_LRU":
        #     result_file = open("files_runs/normal_sqrt_LRU_function_time.txt", "w")
        # elif k == "Compiled_Default_Function_LRU":
        #     result_file = open("files_runs/compiled_default_LRU_function_time.txt", "w")
        # elif k == "Compiled_Half_Function_LRU":
        #     result_file = open("files_runs/compiled_half_LRU_function_time.txt", "w")
        # elif k == "Compiled_Sqrt_Function_LRU":
        #     result_file = open("files_runs/compiled_sqrt_LRU_function_time.txt", "w")
        # elif k == "Optimized_Default_Function_LRU":
        #     result_file = open("files_runs/optimized_default_LRU_function_time.txt", "w")
        # elif k == "Optimized_Half_Function_LRU":
        #     result_file = open("files_runs/optimized_half_LRU_function_time.txt", "w")
        # elif k == "Optimized_Sqrt_Function_LRU":
        #     result_file = open("files_runs/optimized_sqrt_LRU_function_time.txt", "w")

        result_file = open("files_runs/{0}.txt".format(k), "w")

        result_file.write("{0} took {1}H:{2}M:{3:0.2f}S".format(k, int(v / 3600), int(v / 60), v))
        result_file.close()
        print("-" * 80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-" * 80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_total / 3600), int(testing_total / 60), testing_total))
