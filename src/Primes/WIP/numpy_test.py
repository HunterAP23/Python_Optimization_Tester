import multiprocessing.dummy as mp
import os
import time

import Find_Nth_Prime as func
import Find_Nth_Prime_Numpy as func1

times = dict()


def time_function(func, max_num, num_loops, rlock):
    start = time.perf_counter()
    func(max_num, num_loops, rlock)
    total = time.perf_counter() - start
    times[str(func)] = total


if __name__ == "__main__":
    try:
        os.mkdir("files_runs")
    except FileExistsError as fee:
        pass

    manager = mp.Manager()
    rlock = manager.RLock()

    # funcs = [func.Main_Default, func.Main_Half, func.Main_Sqrt, func1.Main_Default, func1.Main_Half, func1.Main_Sqrt]

    # proc = []
    # for func in funcs:
    #     p = mp.Process(target=time_function, args=(func, 100000, 5, rlock))
    #     proc.append(p)
    #
    # for p in proc:
    #     p.start()
    time_function(func1.Main_Default, 50000, 5, rlock)
    time_function(func1.Main_Half, 50000, 5, rlock)
    time_function(func1.Main_Sqrt, 50000, 5, rlock)
