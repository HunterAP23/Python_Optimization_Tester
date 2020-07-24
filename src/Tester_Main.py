#!/usr/bin/env python

# Native Libs
import importlib
import multiprocessing as mp
import os
import shutil
import sys
import time
from typing import *
# cimport cython


def time_function(func, ret_dict, args, name, sema, rlock):
    sema.acquire()
    start = time.time()
    func(
        int(args[name]["value_max"]),
        int(args[name]["num_loops"]),
        rlock,
        args[name]["runtime"],
        args[name]["compilation"],
        args[name]["call_type"],
        args[name]["subcall"],
        args[name]["case"])
    total = time.time() - start
    ret_dict[name] = total
    sema.release()


def run_in_parallel(fns, ret_dict, threads, args, sema, rlock):
    proc = []
    for name, fn in fns.items():
        p = mp.Process(target=time_function, args=(fn, ret_dict, args, name, sema, rlock))
        proc.append(p)

    for p in proc:
        p.start()

    for p in proc:
        try:
            p.join()
        except Exception as x:
            print("EXCEPTION")

    # with mp.Pool(threads) as pool:
    #     rets = dict()
    #     for name, fn in fns.items():
    #         rets[name] = pool.apply_async(func=time_function, args=(fn, ret_dict, args, name, sema, rlock))
    #
    #     try:
    #         pool.close()
    #         pool.join()
    #     except KeyboardInterrupt:
    #         print("Caught KeyboardInterrupt, terminating all child processes.")
    #         pool.terminate()
    #         # pool.join()
    #         exit(1)


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
    arguments = dict()

    # TS.ValueError_Handler(1, 1, int)
    if suites is None or "primes" in suites:
        primes = config["primes"]
        if "tests" in primes:
            tests = primes["tests"]
            # runtime = [cpython, anaconda, pypy]
            # compilation = [normal, cython, optimized]
            for runtime, compilation in tests.items():
                # comp = compilation
                # call_type = [local, function, function_separated]
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
                                        lib = importlib.import_module(info["library"], package=info["package"])
                                        print("Loaded module '{0}'.".format(info["library"]))
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
                                            group = "{0}_{1}_{2}_{3}_{4}".format(runtime, comp, call, sb, cs)
                                            try:
                                                if call == "Function" or call == "Function_Separated":
                                                    funcs[group] = vars(lib)["Main"]
                                                else:
                                                    funcs[group] = vars(lib)["Main_{0}".format(cs)]
                                            except KeyError as ke:
                                                print("{0} is not a valid function inside '{1}'".format(ke, lib.__name__))
                                                exit(1)
                                            arguments[group] = dict()
                                            arguments[group]["value_max"] = value_max
                                            arguments[group]["num_loops"] = num_loops
                                            arguments[group]["runtime"] = runtime
                                            arguments[group]["compilation"] = comp
                                            arguments[group]["call_type"] = call
                                            arguments[group]["subcall"] = sb
                                            arguments[group]["case"] = cs

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

    run_in_parallel(funcs, return_dict, threads, arguments, sema, rlock)

    testing_total = time.time() - testing_start

    for k, v in return_dict.items():
        result_file = open("files_runs/{0}.txt".format(k), "w")

        result_file.write("{0} took {1}H:{2}M:{3:0.2f}S".format(k, int(v / 3600), int(v / 60), v))
        result_file.close()
        print("-" * 80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-" * 80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_total / 3600), int(testing_total / 60), testing_total))
