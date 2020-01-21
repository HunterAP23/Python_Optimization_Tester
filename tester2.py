# Native Libs
import cProfile
import multiprocessing
import os
import re
import time
#import tqdm
import uuid

# Custom Funcs
import Find_Nth_Prime
import Find_Nth_Prime1
# import Find_Nth_Prime2
import Find_Nth_Prime_LRU
import Find_Nth_Prime1_LRU
# import Find_Nth_Prime2_LRU

def timeFunction(func, argoos, name):
    start = time.time()
    func(int(argoos[0]), int(argoos[1]))
    end = time.time()
    total = end - start
    argoos[2][name] = total

def runInParallel(fns, args):
    proc  = []
    i = 0
    for fn in fns:
        if i == 0:
            namer = "Default"
        elif i == 1:
            namer = "Compiled"
        else:
            namer = "Optimized"
        p = multiprocessing.Process(target=timeFunction, args=(fn, args, namer))
        proc.append(p)
        cProfile.run('re.compile("p.start()")')
        i += 1
    print("-"*80)
    for p in proc:
        p.join()
    pass

if __name__ == '__main__':
    global returnDict
    manager = multiprocessing.Manager()
    returnDict = manager.dict()

    userMax = input("Enter the maximum number to calculate primes up to: ")
    numLoops = input("How many loops do you want to go through for each test? ")

    try:
        os.mkdir("files")
    except FileExistsError as fee:
        pass

    testing_Start = time.time()

    #funcs = [Find_Nth_Prime.main, Find_Nth_Prime1.main, Find_Nth_Prime2.main]
    funcs = [Find_Nth_Prime.main, Find_Nth_Prime1.main,]
    arguments = [userMax, numLoops, returnDict]

    runInParallel(funcs, arguments)

    testing_End = time.time()
    testing_Total = testing_End - testing_Start

    for k, v in returnDict.items():
        if k == "Default":
            myDefault = open('files_runs/default_total_time.txt', 'a')
            myDefault.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myDefault.close()
        elif k == "Compiled":
            myCompiled = open('files_runs/compiled_total_time.txt', 'a')
            myCompiled.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myCompiled.close()
        elif k == "Optimized":
            myOptimized = open('files_runs/optimized_total_time.txt', 'a')
            myOptimized.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myOptimized.close()
        if k == "Default_LRU":
            myDefault = open('files_runs/default_LRU_total_time.txt', 'a')
            myDefault.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myDefault.close()
        elif k == "Compiled_LRU":
            myCompiled = open('files_runs/compiled_LRU_total_time.txt', 'a')
            myCompiled.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myCompiled.close()
        elif k == "Optimized_LRU":
            myOptimized = open('files_runs/optimized_LRU_total_time.txt', 'a')
            myOptimized.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myOptimized.close()
        print("-"*80)
        print(str(k) + " took " + str(v / 3600) + "H:" + str(v / 60) + "M:" + str(v) + "S")

    print("-"*80)
    print("Total Run Time was " + str(testing_Total / 3600) + "H:" + str(testing_Total / 60) + "M:" + str(testing_Total) + "S")
