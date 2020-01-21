cimport cython
import datetime as dt
import decimal
import functools as ft
import math
import numbers
import time
#import tqdm

global table
table = []

global table2
table2 = []

global table3
table3 = []

def is_prime(int a):
    global table
    cdef int checks = 0

    if a <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        for j in range(0, len(table), 1):
            checks = checks + 1
            if a % table[j] == 0:
                return [False, checks]
            else:
                continue
        table.append(a)
        return [True, checks]

def is_prime_half(int a):
    global table2
    cdef int checks = 0

    if a <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = math.floor(a / 2)
        for j in range(0, len(table2), 1):
            if table2[j] <= boundary:
                checks = checks + 1
                if a % table2[j] == 0:
                    return [False, checks]
                else:
                    continue
        table2.append(a)
        return [True, checks]

def is_prime_sqrt(int a):
    global table3
    cdef int checks = 0

    if a <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = int(math.floor(math.sqrt(a)))
        for j in range(0, len(table3), 1):
            if table3[j] <= boundary:
                checks = checks + 1
                if a % table3[j] == 0:
                    return [False, checks]
                else:
                    continue
        table3.append(a)
        return [True, checks]

def main(int myMax, int numLoops):
    print("Optimized started.")

    myFile = "files_runs/optimized_main_time.txt"
    myFile2 = "files_runs/optimized_main_divisions.txt"
    txt_output = open(myFile, 'a')
    txt_output2 = open(myFile2, 'a')
    timeList = []
    divisionsList = []

    for j in range(0, numLoops, 1):
        global table
        main_Time_Start = time.time()
        for i in range(myMax):
            tmp = is_prime(i)
            if tmp[0] == True:
                #data1 = str("is_prime(" + str(i) + ") = " + str(tmp[0]) + "\n")
                data1 = str(str(i) +'\n')
                #data2 = str("There are " + str(len(table) - 1) + " many primes less than " + str(i) + "\n")
                data3 = str("This took " + str(tmp[1]) + " divisions by previous primes to complete!" + "\n\n")
                #myData = data1 + data2 + data3
                myData = data1 + data3
                divisionsList.append(myData)


        main_Time_End = time.time()
        main_Time_Overall = (main_Time_End - main_Time_Start)

        timerCount = str("Optimized Normal Pass " + str(j + 1) + ": " + str(main_Time_Overall) + " seconds.\n")
        txt_output.write(timerCount)
        timeList.append(main_Time_Overall)
        main_Time_Overall = 0
        main_Time_End = 0
        main_Time_Start = 0
        table = []

    for item in divisionsList:
        txt_output2.write(item)

    timerAverage = ft.reduce(lambda a, b: a + b, timeList) / len(timeList)
    txt_output.write("The average time it took to calulcate " + str(numLoops) + " optimized normal passes was " + str(timerAverage))
    timerAverage = 0
    timeList = []
    divisionsList = []
    txt_output.close()
    txt_output2.close()

    #2nd Attempt with Half function
    myFile = "files_runs/optimized_half_time.txt"
    myFile2 = "files_runs/optimized_half_division.txt"
    txt_output = open(myFile, 'a')
    txt_output2 = open(myFile2, 'a')

    for j in range(0, numLoops, 1):
        global table2
        main_Time1_Start = time.time()
        for i in range(myMax):
            tmp = is_prime_half(i)
            if tmp[0] == True:
                #data1 = str("is_prime(" + str(i) + ") = " + str(tmp[0]) + "\n")
                data1 = str(str(i) +'\n')
                #data2 = str("There are " + str(len(table2) - 1) + " many primes less than " + str(i) + "\n")
                data3 = str("This took " + str(tmp[1]) + " divisions by previous primes to complete!" + "\n\n")
                #myData = data1 + data2 + data3
                myData = data1 + data3
                divisionsList.append(myData)

        main_Time1_End = time.time()
        main_Time1_Overall = (main_Time1_End - main_Time1_Start)
        #print("Compiled Half Pass " + str(j + 1) + ": " + str(main_Time1_Overall) + " seconds.")

        timerCount1 = str("Optimized Half Pass " + str(j + 1) + ": " + str(main_Time1_Overall) + " seconds.\n")
        txt_output.write(timerCount1)
        timeList.append(main_Time1_Overall)
        main_Time1_Overall = 0
        main_Time1_End = 0
        main_Time1_Start = 0
        table2 = []

    for item in divisionsList:
        txt_output2.write(item)

    timerAverage = ft.reduce(lambda a, b: a + b, timeList) / len(timeList)
    txt_output.write("The average time it took to calulcate " + str(numLoops) + " optimized half passes was " + str(timerAverage))
    timerAverage = 0
    timeList = []
    divisionsList = []
    txt_output.close()
    txt_output2.close()

    #3rd Attempt with Sqrt function
    myFile = "files_runs/optimized_sqrt_time.txt"
    myFile2 = "files_runs/optimized_sqrt_divisions.txt"
    txt_output = open(myFile, 'a')
    txt_output2 = open(myFile2, 'a')

    for j in range(numLoops):
        global table3
        main_Time2_Start = time.time()
        for i in range(myMax):
            tmp = is_prime_sqrt(i)
            if tmp[0] == True:
                #data1 = str("is_prime(" + str(i) + ") = " + str(tmp[0]) + "\n")
                data1 = str(str(i) +'\n')
                #data2 = str("There are " + str(len(table3) - 1) + " many primes less than " + str(i) + "\n")
                data3 = str("This took " + str(tmp[1]) + " divisions by previous primes to complete!" + "\n\n")
                #myData = data1 + data2 + data3
                myData = data1 + data3
                divisionsList.append(myData)

        main_Time2_End = time.time()
        main_Time2_Overall = (main_Time2_End - main_Time2_Start)
        #print("Compiled Sqrt Pass " + str(j + 1) + ": " + str(main_Time2_Overall) + " seconds.")

        timerCount2 = str("Optimized Sqrt Pass " + str(j + 1) + ": " + str(main_Time2_Overall) + " seconds.\n")
        txt_output.write(timerCount2)
        timeList.append(main_Time2_Overall)
        main_Time2_Overall = 0
        main_Time2_End = 0
        main_Time2_Start = 0
        table3 = []

    for item in divisionsList:
        txt_output2.write(item)

    timerAverage = ft.reduce(lambda a, b: a + b, timeList) / len(timeList)
    txt_output.write("The average time it took to calulcate " + str(numLoops) + " optimized square root passes was " + str(timerAverage))
    timerAverage = 0
    timeList = []
    divisionsList = []
    txt_output.close()
    txt_output2.close()

    nowTime = dt.datetime.now()
    print("-"*80)
    print("Optimized Finished at " + str(nowTime.year) + "/" + str(nowTime.month) + "/" + str(nowTime.day) + " " + str(nowTime.hour) + ":" + str(nowTime.minute) + ":" + str(nowTime.second) + ":" + str(nowTime.microsecond))
