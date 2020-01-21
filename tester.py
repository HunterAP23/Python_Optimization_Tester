# Native Libs
import multiprocessing as mp
import os
import time
import uuid

# Custom Funcs
import Find_Nth_Prime
import Find_Nth_Prime1
import Find_Nth_Prime2
import Find_Nth_Prime_LRU
import Find_Nth_Prime1_LRU
import Find_Nth_Prime2_LRU

def time_function(func, argoos, name):
    start = time.time()
    func(int(argoos[0]), int(argoos[1]))
    total = time.time() - start
    argoos[2][name] = total

def run_in_parallel(fns, args):
    proc  = []
    i = 0
    for fn in fns:
        if i == 0:
            namer = "Default"
        elif i == 1:
            namer = "Compiled"
        elif i == 2:
            namer = "Optimized"
        elif i == 3:
            namer = "Default_LRU"
        elif i == 4:
            namer = "Compiled_LRU"
        else:
            namer = "Optimized_LRU"
        p = mp.Process(target=time_function, args=(fn, args, namer))
        proc.append(p)
        p.start()
        i += 1
    print("-"*80)
    for p in proc:
        p.join()
    pass

if __name__ == '__main__':
    global return_dict
    manager = mp.Manager()
    return_dict = manager.dict()

    user_max = input("Enter the maximum number to calculate primes up to: ")
    num_loops = input("How many loops do you want to go through for each test? ")

    try:
        os.mkdir("files_runs")
    except FileExistsError as fee:
        pass

    testing_start = time.time()

    funcs = [Find_Nth_Prime.main, Find_Nth_Prime1.main, Find_Nth_Prime2.main, Find_Nth_Prime_LRU.main, Find_Nth_Prime1_LRU.main, Find_Nth_Prime2_LRU.main]
    arguments = [user_max, num_loops, return_dict]

    run_in_parallel(funcs, arguments)

    testing_total = time.time() - testing_start

    for k, v in return_dict.items():
        result_file = None
        if k == "Default":
            result_file = open('files_runs/default_total_time.txt', 'a')
        elif k == "Compiled":
            result_file = open('files_runs/compiled_total_time.txt', 'a')
        elif k == "Optimized":
            result_file = open('files_runs/optimized_total_time.txt', 'a')
        elif k == "Default_LRU":
            result_file = open('files_runs/default_LRU_total_time.txt', 'a')
        elif k == "Compiled_LRU":
            result_file = open('files_runs/compiled_LRU_total_time.txt', 'a')
        elif k == "Optimized_LRU":
            result_file = open('files_runs/optimized_LRU_total_time.txt', 'a')
        result_file.write("{0} took {1}H:{2}M:{3:0.2f}S".format(k, int(v / 3600), int(v / 60), v))
        result_file.close()
        print("-"*80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-"*80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_total / 3600), int(testing_total / 60), testing_total))
