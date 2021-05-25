#!/usr/bin/env python

import argparse as argp
import json
import multiprocessing as mp
import os

# import Tester_Logger as log
import Tester_Main as TM


def _validate_file(args):
    config_file = None
    if args.File:
        file_path = os.path.join(__file__, args.File)
        if os.path.exists(file_path):
            config_file = open(file_path, "r")
        else:
            print("ERROR: Settings file \"{}\" does not exist.".format(file_path))
    else:
        file_path = os.path.join(__file__, "Settings.json")
        if os.path.exists(file_path):
            config_file = open(file_path, "r")
        else:
            print("ERROR: Settings file \"{}\" does not exist.".format(file_path))
    config = json.load(config_file)
    config_file.close()
    return config


def _validate_threads(threads, config):
    if threads:
        if threads > mp.cpu_count():
            msg = "ERROR: User specified {0} threads which is more than the number the system supports ({1}), clamping the value to the available number of threads on this system."
            print(msg.format(threads, mp.cpu_count()))
            threads = mp.cpu_count()
    else:
        if "global" not in config:
            print("ERROR: \"global\" key does not exist in the configuration file. Manually asking user for input...")
            threads = mp.cpu_count()
        else:
            if "threads" not in config["global"]:
                print("ERROR: \"threads\" key does not exist in the \"global\" section of the configuration file. Goign with default value of all threads ({})".format(mp.cpu_count()))
                threads = mp.cpu_count()
            else:
                try:
                    threads_int = int(config["global"]["threads"])
                    if threads_int > mp.cpu_count():
                        msg = "ERROR: Configuration file specified {0} threads which is more than the number the system supports ({1}), clamping the value to the available number of threads on this system."
                        print(msg.format(threads, mp.cpu_count()))
                        threads = mp.cpu_count()
                    else:
                        threads = threads_int
                except ValueError:
                    print("ERROR: Value ({0}) for \"threads\" key is not an integer. Defaulting to all CPU threads ({1}).".format(config["global"]["threads"], mp.cpu_count()))
                    threads = mp.cpu_count()

    return threads


def _validate_suites(suites, config):
    suites_choices = ["primes"]
    if suites:
        for test in suites:
            if test.lower() not in suites_choices:
                print("ERROR: \"{}\" is not a valid test suite, removing this from the user input.".format(test))
                suites.remove(test)
    return suites


def _validate_os(my_OS, config):
    options = ["Linux", "MacOS_ARM", "MacOS_x86", "Windows"]
    if my_os not in options:



def parse_args():
    parser = argp.ArgumentParser(description="Run benchmarking test suite for combinations of CPython, Cython, Anaconda, and PyPy.", formatter_class=argp.RawTextHelpFormatter, add_help=False)

    optional_args = parser.add_argument_group("Optional arguments")
    optional_args.add_argument("-s", "--suites", dest="Suites", metavar="SUITES", nargs="+", required=False, help="Override the list of test suites specified in the settings.json file with space/comma separated ones.\n")
    optional_args.add_argument("-t", "--threads", dest="Threads", metavar="THREADS", type=int, required=False, help="Number of CPU threads to utilize in the benchmarks (defaults to all threads).\n")
    optional_args.add_argument("-f", "--file", dest="File", metavar="FILE", default="Settings.json", required=False, help="Specify different JSON file for getting settings.\n")
    optional_args.add_argument("-o", "--os", dest="OS", metavar="OS", options=["Linux", "MacOS_ARM", "MacOS_x86", "Windows"], required=False, help="Specify the OS & architecture to compile for. If not specified, the program wil lattempt to autodetect it for you.\n")

    misc_args = parser.add_argument_group("Miscellaneous arguments")
    misc_args.add_argument("-d", "--debug", dest="Debug", action="store_true", required=False, help="Print verbose statements.\n")
    misc_args.add_argument("-v", "--version", action="version", version="%(prog)s 2020-07-10")
    misc_args.add_argument("-h", "--help", action="help", default=argp.SUPPRESS, help="Show this help message and exit.\n")

    args = parser.parse_args()

    config = _validate_file(args)

    args.Threads = _validate_threads(args.Threads, config)

    args.Suites = _validate_suites(args.Suites, config)

    print("{}".format(args))

    return (config, args.Threads, args.Suites,)


def main():
    args = parse_args()
    TM.main(args)


if __name__ == "__main__":
    main()
