import Primes.Compiled.Function.Standard as std
import multiprocessing as mp


if __name__ == "__main__":
    manager = mp.Manager()
    return_dict = manager.dict()
    # sema = manager.Semaphore(threads)
    rlock = manager.RLock()

    std.Main(1000000, 1, rlock, "CPython", "Compiled", "Local", "Standard", "Default")
