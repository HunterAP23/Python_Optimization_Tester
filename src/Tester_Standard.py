#!/usr/bin/env python
import psutil


def ValueError_Handler(var, exp, var_type):
    val_exp = None
    val_var = None
    if "<class 'type'>" == str(type(var_type)):
        try:
            val_exp = var_type(var)
        except ValueError:
            print("ERROR: Could not cast value of '{0}' to type '{1}'.".format(var, var_type))
            return None

        try:
            val_var = var_type(exp)
        except ValueError:
            print("ERROR: Could not cast value of '{0}' to type '{1}'.".format(exp, var_type))
            return None

        if val_var == val_exp:
            return True
        else:
            return False
    else:
        print("ERROR: '{0}' is a not a type class.")
        return None


def measure_memory_usage(func):
    def process_memory():
        process = psutil.Process()
        mem_info = process.memory_info()
        return mem_info.rss

    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        return result, mem_after - mem_before

    return wrapper
