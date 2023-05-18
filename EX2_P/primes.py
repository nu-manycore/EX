#!/usr/bin/env python3

import numpy as np
import time

# DATA_NUM should be larger if you like to get better speed-up
DATA_NUM = 100
primes = np.zeros(DATA_NUM)

# Check
def check(max_num):
    for i in range(2, max_num):
        limit = int(np.sqrt(i))
        for j in range(2, limit):
            if primes[j] == 0 and i % j == 0:
                primes[i] = 1
                break;

# Output
def output(max_num):
    for i in range(2, max_num):
        if primes[i] == 0:
            print("%d" % i, end = " ")
    print("")

# main
start = time.time()
check(DATA_NUM)
stop = time.time()
print('%.2f seconds' % (stop - start))
output(DATA_NUM)
