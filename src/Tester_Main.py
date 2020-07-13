#!/usr/bin/env python

# Native Libs
import importlib
import multiprocessing as mp
import os
import shutil
import sys
import time

# import Tester_Standard as TS

# # Function - Lists
# import Primes.Python_Normal_Function_List as CPy_Norm_Function_List
# # Function - Lambdas & Maps
# import Primes.Python_Normal_Function_Lambda_Map as CPy_Norm_Function_Lambda_Map
# # Function - LRU Caching
# import Primes.Python_Normal_Function_LRU as CPy_Norm_Function_LRU
# # Function - Lambdas & LRU Caching
# import Primes.Python_Normal_Function_Lambda_LRU as CPy_Norm_Function_Lambda_LRU
# # Function - Lists & LRU Caching
# import Primes.Python_Normal_Function_List_LRU as CPy_Norm_Function_List_LRU
# # Function - Lambdas & LRU Caching & Maps
# import Primes.Python_Normal_Function_Lambda_LRU_Map as CPy_Norm_Function_Lambda_LRU_Map


# import Primes.Python_Normal_Function_LRU as CPy_Norm_Function_LRU
# import Primes.Python_Normal_Function_Lambda_LRU as CPy_Norm_Function_Lambda_LRU

# import Python_Normal_Numpy
# import Python_Normal_Numpy_Lambda
# import Python_Normal_Numpy_LRU

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


def time_function(func, args, name, sema, rlock):
    sema.acquire()
    start = time.time()
    func(int(args[0]), int(args[1]), rlock)
    total = time.time() - start
    args[2][name] = total
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


def validate_primes(config):
    should_ask_max = False
    should_ask_loops = False
    if "primes" not in config:
        print("ERROR: 'primes' key does not exist in the configuration file. Manually asking user for input...")
        should_ask_max = True
        should_ask_loops = True
    else:
        if "max" not in config["primes"]:
            print("ERROR: 'max' key does not exist in the 'primes' section of the configuration file. Manually asking user for input...")
            should_ask_max = True
        else:
            try:
                value_int = int(config["primes"]["max"])
                value_max = value_int
            except ValueError:
                print("ERROR: Value ({0}) for 'max' in 'primes' category is not an integer. Asking for user input...".format(config["primes"]["max"]))
                should_ask_max = True

        if "loops" not in config["primes"]:
            print("ERROR: 'loops' key does not exist in the 'primes' section of the configuration file. Manually asking user for input...")
            should_ask_loops = True
        else:
            try:
                loops_int = int(config["primes"]["loops"])
                num_loops = loops_int
            except ValueError:
                print("ERROR: Value ({0}) for 'loops' in 'primes' category is not an integer. Asking for user input...".format(config["primes"]["loops"]))
                should_ask_loops = True

    if should_ask_max:
        tries_left = 3
        while tries_left > 0:
            try:
                value_max = input("Enter the maximum number to calculate primes up to: ")
                max_int = int(value_max)
                value_max = max_int
                break
            except ValueError:
                print("ERROR: User input for 'maximum prime' is not an integer.")
                tries_left -= 1
        if tries_left == 0:
            exit(1)
    if should_ask_loops:
        tries_left = 3
        while tries_left > 0:
            try:
                num_loops = input("How many loops do you want to go through for each test? ")
                max_int = int(value_max)
                value_max = max_int
                break
            except ValueError:
                print("ERROR: User input for 'number of loops' is not an integer.")
                tries_left -= 1
        if tries_left == 0:
            exit(1)

    return (value_max, num_loops,)


def main(args):
    config = dict(args[0])
    threads = args[1]
    suites = args[2]
    manager = mp.Manager()
    return_dict = manager.dict()
    sema = manager.Semaphore(threads)
    rlock = manager.RLock()

    value_max, num_loops = validate_primes(config)

    print("Creating directory structure...")
    try:
        os.mkdir("files_runs")
    except FileExistsError:
        pass

    testing_start = time.time()

    funcs = dict()

    # TS.ValueError_Handler(1, 1, int)
    if "primes" in suites:
        primes = config["primes"]
        if "tests" in primes:
            tests = primes["tests"]
            # runtime = [cpython, anaconda, pypy]
            # compilation = [normal, cython, optimized]
            for runtime, compilation in tests.items():
                # comp = compilation
                # call_type = [local, function]
                for comp, call_type in compilation.items():
                    # call = call_type
                    # subcall = any of the test cases for the given call_type
                    # subcalls include std, lambda, list, map, etc.
                    for call, subcall in call_type.items():
                        # sb = subcall
                        # info = [case, package, library]
                        for sb, info in subcall.items():
                            if any([enabled for cs, enabled in info["case"].items() if enabled == 1]):
                                import_status = None
                                try:
                                    if info["library"] in sys.modules:
                                        print("{0} module has already been loaded.".format(info["library"]))
                                    else:
                                        print("Loaded module '{0}'.".format(info["library"]))
                                        lib = importlib.import_module(info["library"], package=info["package"])
                                    import_status = 0
                                except ModuleNotFoundError:
                                    print("ERROR: Could not find module '{0}'.".format(info["library"]))
                                    import_status = 1

                                if import_status == 0:
                                    results_dir = "{0}_{1}_{2}_{3}".format(runtime, comp, call, sb).lower()
                                    try:
                                        os.mkdir("files_runs/{0}".format(results_dir))
                                    except FileExistsError:
                                        shutil.rmtree("files_runs/{0}".format(results_dir))
                                        os.mkdir("files_runs/{0}".format(results_dir))

                                    for cs, enabled in info["case"].items():
                                        if enabled == 1:
                                            # print("{0}_{1}_{2}_{3}_{4}_{5}".format(runtime, comp, call, sb, cs, "Main_{0}".format(cs)))
                                            funcs["{0}_{1}_{2}_{3}".format(runtime, comp, call, sb)] = vars(lib)["Main_{0}".format(cs)]

        ############################################################################

        # NUMPY
        # try:
        #     os.mkdir("files_runs/normal_numpy")
        # except FileExistsError:
        #     pass
        # funcs["Numpy_Default_"] = Python_Normal_Numpy.Main_Default
        # funcs.append(Python_Normal_Numpy.Main_Half)
        # funcs.append(Python_Normal_Numpy.Main_Sqrt)

        # try:
        #     os.mkdir("files_runs/normal_numpy_lambda")
        # except FileExistsError:
        #     pass
        # funcs.append(Python_Normal_Numpy_Lambda.Main_Default)
        # funcs.append(Python_Normal_Numpy_Lambda.Main_Half)
        # funcs.append(Python_Normal_Numpy_Lambda.Main_Sqrt)

        # funcs.append(Python_Normal_Numpy_LRU.Main_Default)
        # funcs.append(Python_Normal_Numpy_LRU.Main_Half)
        # funcs.append(Python_Normal_Numpy_LRU.Main_Sqrt)

    # for k, v in funcs.items():
    #     print("{0}: {1}".format(str(k), str(v)))
    # exit()

    arguments = [value_max, num_loops, return_dict]

    run_in_parallel(funcs, arguments, sema, rlock)

    testing_total = time.time() - testing_start

    for k, v in return_dict.items():
        result_file = open("files_runs/{0}.txt".format(k), "w")

        result_file.write("{0} took {1}H:{2}M:{3:0.2f}S".format(k, int(v / 3600), int(v / 60), v))
        result_file.close()
        print("-" * 80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-" * 80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_total / 3600), int(testing_total / 60), testing_total))

    # with open("files_runs/normal_local_lambda/default_primes.txt", "r") as main:
    #     with open("files_runs/normal_local_lambda/map_primes.txt", "r") as map:
    #         main_list = []
    #         for line in main:
    #             main_list.append(line.strip())
    #
    #         map_list = []
    #         for line in map:
    #             map_list.append(line.strip())
    #
    #         set_main = set(main_list)
    #         set_map = set(map_list)
    #         same = set_main.difference(set_map)
    #         same.discard('\n')
    #         print("file diff:")
    #         for line in same:
    #             print(line)
