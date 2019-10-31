import Find_Nth_Prime
import Find_Nth_Prime1
import Find_Nth_Prime2
import time
import os
import uuid
import multiprocessing
#import tqdm

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
        p.start()
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

    testing_Start = time.time()

    funcs = [Find_Nth_Prime.main, Find_Nth_Prime1.main, Find_Nth_Prime2.main]
    #funcs = [Find_Nth_Prime.main, Find_Nth_Prime1.main,]
    arguments = [userMax, numLoops, returnDict]

    runInParallel(funcs, arguments)

    testing_End = time.time()
    testing_Total = testing_End - testing_Start

    for k, v in returnDict.items():
        if k == "Default":
            myDefault = open('default_total_time.txt', 'a')
            myDefault.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myDefault.close()
        elif k == "Compiled":
            myCompiled = open('compiled_total_time.txt', 'a')
            myCompiled.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myCompiled.close()
        else:
            myOptimized = open('optimized_total_time.txt', 'a')
            myOptimized.write(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))
            myOptimized.close()
        print("-"*80)
        print(str(k) + " took {0}H:{1}M:{2:0.2f}S".format(int(v / 3600), int(v / 60), v))

    print("-"*80)
    print("Total Run Time was {0}H:{1}M:{2:0.2f}S".format(int(testing_Total / 3600), int(testing_Total / 60), testing_Total))
