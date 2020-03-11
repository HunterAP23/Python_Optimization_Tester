import multiprocessing.dummy as mp
import os
import time

import Find_Nth_Prime_Python_Lambda_LRU as func

times = dict()

def time_function(func, max_num, num_loops, rlock):
    start = time.time()
    func(max_num, num_loops, rlock)
    total = time.time() - start
    times[str(func)] = total

if __name__ == "__main__":
    try:
        os.mkdir("files_runs")
    except FileExistsError as fee:
        pass

    manager = mp.Manager()
    rlock = manager.RLock()

    # funcs = [func.main_def, func.main_half, func.main_sqrt, func1.main_def, func1.main_half, func1.main_sqrt]

    # proc = []
    # for func in funcs:
    #     p = mp.Process(target=time_function, args=(func, 100000, 5, rlock))
    #     proc.append(p)
    #
    # for p in proc:
    #     p.start()
    # time_function(func.main_def, 49999, 5, rlock)
    # time_function(func.main_half, 49999, 5, rlock)
    # time_function(func.main_sqrt, 49999, 5, rlock)
    func.main_def(49999, 5, rlock)
