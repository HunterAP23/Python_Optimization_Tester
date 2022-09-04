#!/usr/bin/env python

# Native Libs
import concurrent.futures as cf
import importlib
import math
import multiprocessing as mp
import os
import shutil
import statistics as stat
import sys
from datetime import timedelta as td
from itertools import chain
from traceback import print_exc

# from typing import *


def validate_primes(config):
    should_ask_max = False
    should_ask_loops = False
    if "primes" not in config:
        print("ERROR: 'primes' key does not exist in the configuration file. Manually asking user for input...")
        should_ask_max = True
        should_ask_loops = True
    else:
        if "max" not in config["primes"]:
            print(
                "ERROR: 'max' key does not exist in the 'primes' section of the configuration file. Manually asking user for input..."
            )
            should_ask_max = True
        else:
            try:
                value_int = int(config["primes"]["max"])
                value_max = value_int
            except ValueError:
                print(
                    "ERROR: Value ({0}) for 'max' in 'primes' category is not an integer. Asking for user input...".format(
                        config["primes"]["max"]
                    )
                )
                should_ask_max = True

        if "loops" not in config["primes"]:
            print(
                "ERROR: 'loops' key does not exist in the 'primes' section of the configuration file. Manually asking user for input..."
            )
            should_ask_loops = True
        else:
            try:
                loops_int = int(config["primes"]["loops"])
                num_loops = loops_int
            except ValueError:
                print(
                    "ERROR: Value ({0}) for 'loops' in 'primes' category is not an integer. Asking for user input...".format(
                        config["primes"]["loops"]
                    )
                )
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

    return (
        int(value_max),
        int(num_loops),
    )


def calculate_primes(func, group, boundary, value_max, num_loops, runtime, compilation, call_type, subcall):
    data_list = func(value_max, num_loops, boundary, runtime, compilation, call_type, subcall)

    for i in range(num_loops):
        time_total = math.fsum(data_list[i]["times"])
        time_average = stat.fmean(data_list[i]["times"])
        time_median = stat.median(data_list[i]["times"])
        with open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), boundary).lower(), "w") as time_output:
            msg = ""
            for i, v in enumerate(data_list[i]["times"]):
                msg += "{0} {1} Pass {2} took {3} seconds.\n".format(group, boundary, i + 1, v)
            msg = "Total time it took to calculate {0} passes of {1} {2} was {3} seconds.\n".format(
                num_loops, group, boundary, time_total
            )

            msg += "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(
                num_loops, group, boundary, time_average
            )

            msg += "Median time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(
                num_loops, group, boundary, time_median
            )

            time_output.write(msg)

        with open(
            "files_runs/{0}/divisions_{1}.txt".format(group.replace(" ", "_"), boundary).lower(), "w"
        ) as div_output:
            for n, div in data_list[i]["divisions"].items():
                msg = "Primality Test for {0} took {1} divisions.\n\n".format(n, div)
                div_output.write(msg)

        with open(
            "files_runs/{0}/primes_{1}.txt".format(group.replace(" ", "_"), boundary).lower(), "w"
        ) as primes_output:
            for prime in data_list[i]["primes"]:
                primes_output.write("{0}\n".format(prime))

    times = list(chain.from_iterable(data_list["times"]))
    divs = list(chain.from_iterable(data_list["divisions"]))
    primes = list(chain.from_iterable(data_list["primes"]))

    return (
        times,
        divs,
        primes,
    )


def run_in_parallel(mapping, value_max, num_loops, threads, sema):
    procs = dict()
    cf_handler = cf.ThreadPoolExecutor(max_workers=threads)
    try:
        for group, data in mapping.items():
            # p = mp.Process(target=calculate_primes, args=(fn, ret_dict, args, name))
            sema.acquire()
            procs[
                cf_handler.submit(
                    calculate_primes,
                    func=data["func"],
                    group=group,
                    runtime=data["runtime"],
                    compilation=data["compilation"],
                    call_type=data["call_type"],
                    subcall=data["subcall"],
                    boundary=data["boundary"],
                    value_max=value_max,
                    num_loops=num_loops,
                )
            ] = {
                "group": group,
            }
            sema.release()
    except (KeyboardInterrupt, cf.CancelledError, Exception) as e:
        if type(e) in [KeyboardInterrupt, cf.CancelledError]:
            print("KeyboardInterrupt detected, working on shutting down pool...")
        else:
            print_exc()
        cf_handler.shutdown(wait=False, cancel_futures=True)
        exit(1)

    results = dict()
    for task in cf.as_completed(procs):
        times, divs, primes = task.result()
        group = procs[task]
        results[group] = {
            "times": times,
            "divisions": divs,
            "primes": primes,
        }
    cf_handler.shutdown()
    return results


def main(config=dict(), threads=0, suites=dict()):
    manager = mp.Manager()
    sema = manager.Semaphore(threads)

    value_max, num_loops = validate_primes(config)

    print("Creating directory structure...")
    try:
        os.mkdir("files_runs")
    except FileExistsError:
        pass

    mapping = dict()

    # TS.ValueError_Handler(1, 1, int)
    if suites is None or "primes" in suites:
        if "tests" in config["primes"]:
            tests = config["primes"]["tests"]
            # runtime = [cpython, anaconda, pypy]
            # compilation = [normal, cython, optimized]
            for runtime, compilation in tests.items():
                # comp = compilation
                # call_type = [inline, function]
                for comp, call_type in compilation.items():
                    # call = call_type
                    # subcall = any of the test boundaries for the given call_type
                    # subcalls include std, lambda, list, map, etc.
                    for call, subcall in call_type.items():
                        # sb = subcall
                        # data = [boundary, package, library]
                        for sb, data in subcall.items():
                            if any([enabled for enabled in data["boundary"].values() if enabled == 1]):
                                import_status = None
                                try:
                                    if data["library"] in sys.modules:
                                        print("{0} module has already been loaded.".format(data["library"]))
                                    else:
                                        lib = importlib.import_module(data["library"], package=data["package"])
                                        print("Loaded module '{0}'.".format(data["library"]))
                                    import_status = 0
                                except ModuleNotFoundError:
                                    print("ERROR: Could not find module '{0}'.".format(data["library"]))
                                    import_status = 1

                                if import_status == 0:
                                    results_dir = "{0}_{1}_{2}_{3}".format(runtime, comp, call, sb).lower()
                                    try:
                                        os.mkdir("files_runs/{0}".format(results_dir))
                                    except FileExistsError:
                                        shutil.rmtree("files_runs/{0}".format(results_dir))
                                        os.mkdir("files_runs/{0}".format(results_dir))

                                    for bound, enabled in data["boundary"].items():
                                        if enabled == 1:
                                            group = "{0}_{1}_{2}_{3}_{4}".format(runtime, comp, call, sb, bound)
                                            try:
                                                mapping[group] = dict()
                                                if call == "Function":
                                                    mapping[group]["func"] = vars(lib)["Main"]
                                                else:
                                                    mapping[group]["func"] = vars(lib)["Main_{0}".format(bound)]
                                            except KeyError as ke:
                                                print(
                                                    "{0} is not a valid function inside '{1}'".format(ke, lib.__name__)
                                                )
                                                exit(1)
                                            mapping[group]["runtime"] = runtime
                                            mapping[group]["compilation"] = comp
                                            mapping[group]["call_type"] = call
                                            mapping[group]["subcall"] = sb
                                            mapping[group]["boundary"] = bound

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

    results_dict = run_in_parallel(mapping, value_max, num_loops, threads, sema)

    time_program_total = td(seconds=0)

    for group, results in results_dict.items():
        times = results["times"]
        divs = results["divisions"]
        result_file = open(f"files_runs/{group}.txt", "w")

        time_total = td(seconds=math.fsum(times))
        time_mean = td(seconds=stat.fmean(times))
        time_median = td(seconds=stat.median(times))
        time_worst = td(seconds=max(times))
        time_best = td(seconds=min(times))

        divs_total = sum(divs)

        time_program_total += time_total

        # result_file.write("{0} took {a1}H:{2}M:{3:0.2f}S".format(group, stat.fmean(times) / 3600, stat.fmean(times) / 60, stat.fmean(times)))
        msg = f"{group} total time: {time_total}\n"
        msg += f"{group} mean time: {time_mean}\n"
        msg += f"{group} median time: {time_median}\n"
        msg += f"{group} fastest calculation: {time_best}\n"
        msg += f"{group} slowest calculation: {time_worst}\n"
        msg += f"{group} total number of divisions: {divs_total}\n"
        result_file.write(msg)
        print("-" * 80)
        print(msg)

    print("-" * 80)
    # print(
    #     "Total Run Time was {0}H:{1}M:{2:0.2f}S".format(
    #         int(testing_total / 3600), int(testing_total / 60), testing_total
    #     )
    # )
    print(f"Total CPU time spent finding prime numbers was {time_program_total}")
