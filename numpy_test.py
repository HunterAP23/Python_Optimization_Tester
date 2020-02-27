import multiprocessing.dummy as mp
import numpy as np


table = np.empty((1,), dtype=int)
table[0] = 2

table2 = np.empty((1,), dtype=int)
table2[0] = 2

table3 = np.empty((1,), dtype=int)
table3[0] = 2


def split(arr, cond):
  # return [arr[cond], arr[~cond]]
  return arr[cond]


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(num):
    global table
    if num <= 1:
        return [False, 0]
    else:
        x = np.divide(num, table)
        np.mod(x, 1, out=x)
        mask = (x == 0)

        is_prime = True
        for i in x:
            if np.any(mask):
                is_prime = False
                break
        if is_prime:
            table.resize((table.size + 1,))
            table[-1] = num


def is_prime_half(num):
    global table2

    if num <= 1:
        return [False, 0]
    else:
        # x, y = split(table2, np.divide(table2, num) < num / 2)
        x = split(table2, np.divide(table2, num) < num / 2)
        x = np.divide(num, x)
        np.mod(x, 1, out=x)
        mask = (x == 0)

        is_prime = True
        for i in x:
            if np.any(mask):
                is_prime = False
                break
        if is_prime:
            table2.resize((table2.size + 1,))
            table2[-1] = num

def is_prime_sqrt(num):
    global table3

    if num <= 1:
        return [False, 0]
    else:
        # x, y = split(table3, np.divide(table3, num) < np.sqrt(num))
        x = split(table3, np.divide(table3, num) < np.sqrt(num))
        x = np.divide(num, x)
        np.mod(x, 1, out=x)
        mask = (x == 0)

        is_prime = True
        for i in x:
            if np.any(mask):
                is_prime = False
                break
        if is_prime:
            table3.resize((table3.size + 1,))
            table3[-1] = num

def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Default started."
    print_lock(msg, rlock)

    time_list = []
    divisions_list = []

    for j in range(num_loops):
        for i in range(3, my_max):
            tmp = is_prime(i)

def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Half started."
    print_lock(msg, rlock)

    time_list = []
    divisions_list = []

    for j in range(num_loops):
        for i in range(3, my_max):
            tmp = is_prime_half(i)

def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt started."
    print_lock(msg, rlock)

    time_list = []
    divisions_list = []

    for j in range(num_loops):
        for i in range(3, my_max):
            tmp = is_prime_sqrt(i)

if __name__ == '__main__':
    # print("table: {0}".format(table))

    manager = mp.Manager()
    rlock = manager.RLock()

    main_def(100000, 1, rlock)
    print("Table1 elements:")
    print(table)

    main_half(100000, 1, rlock)
    print("Table2 elements:")
    print(table2)

    main_sqrt(100000, 1, rlock)
    print("Table3 elements:")
    print(table3)
