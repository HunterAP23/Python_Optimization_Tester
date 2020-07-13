#!/usr/bin/env python

# Native Libraries
import logging as lg
import sys
import os

# Levels:
# 0 -> DEBUG
# 1 -> INFO
# 2 -> WARNING
# 3 -> ERROR
# 4 -> CRITICAL


def create_log(the_date, debug=False):
    log_file = os.path.join(os.getcwd(), str(the_date) + ".log")
    try:
        if not os.path.exists(log_file):
            open(log_file, 'a').close()
            os.chmod(log_file, 0o777)
    except OSError as ose:
        print("Could not create log file " + str(log_file))
        print("OSError({0}): {1}".format(ose.errno, ose.strerror))
        print("Your user may not have permission to create files in that location.")
        return (1, None)

    my_log = lg.getLogger()

    # c_handler = lg.StreamHandler(sys.stdout)
    c_handler = lg.StreamHandler(sys.stderr)
    f_handler = lg.FileHandler(log_file)

    if debug:
        c_handler.setLevel(lg.DEBUG)
    else:
        c_handler.setLevel(lg.INFO)
    f_handler.setLevel(lg.DEBUG)

    c_format = lg.Formatter('%(asctime)s %(threadName)s [%(levelname)s]: %(message)s')
    f_format = lg.Formatter('%(asctime)s %(threadName)s [%(levelname)s]: %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    my_log.addHandler(c_handler)
    my_log.addHandler(f_handler)

    my_log.setLevel(lg.NOTSET)

    # lg.basicConfig(
    #     level=lg.DEBUG,
    #     format="%(asctime)s|%(levelname)s: %(name)s - %(message)s",
    #     filename="/tmp/reports/script.log"
    # )

    # my_log = lg.getLogger()

    return (0, my_log)


def write_log(message, the_log):
    message = message.replace("\r", "").replace("\n", "")
    the_log.info(message)


# def thread_log():
#     my_log = lg.getLogger()
#     c_handler = lg.StreamHandler(sys.stdout)
#     c_handler.setLevel(lg.INFO)
#     c_format = '%(asctime)s [%(levelname)s] %(threadName)s: %(message)s'
#     c_handler.setFormatter(c_format)
#     my_log.addHandler(c_handler)
#
#     return my_log
