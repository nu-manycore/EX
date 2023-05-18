#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

num_list = [25000000, 20000000, 20076000, 14500000]
Is_Submit = False

# application just taking long time
def killing_time(number):
    return_list = []
    for i in range(1, number + 1):
        if number % i == 1:
            if i <= 9999:
                return_list.append(i)
    return return_list

# Sequential
start = time.time()
for num in num_list:
    killing_time(num)
stop = time.time()
print('Sequential: %.2f seconds' % (stop - start))

# Thread: may be no speed-up due to python GIL
start = time.time()
if Is_Submit == True:
    # Using submit
    executor = ThreadPoolExecutor(max_workers=4)
    futures = []
    for num in num_list:
        future = executor.submit(killing_time, num)
        futures.append(future)
    executor.shutdown()
else:
    # Using map
    with ThreadPoolExecutor(max_workers=4) as excuter:    
        result_list = list(excuter.map(killing_time, num_list))

stop = time.time()
print('Thread: %.2f seconds' % (stop - start))

# Process
start = time.time()
if Is_Submit == True:
    # Using submit
    executor = ProcessPoolExecutor(max_workers=4)
    futures = []
    for num in num_list:
        future = executor.submit(killing_time, num)
        futures.append(future)
    executor.shutdown()
else:
    # Using map
    with ProcessPoolExecutor(max_workers=4) as excuter:    
        result_list = list(excuter.map(killing_time, num_list))
stop = time.time()
print('Process: %.2f seconds' % (stop - start))
