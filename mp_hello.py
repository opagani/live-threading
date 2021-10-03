#!/usr/bin/env python3

import multiprocessing
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!\n', end='')


all_processes = []
for i in range(10):
    p = multiprocessing.Process(target=hello, args=(i,), name=f'hello-{i}')
    p.start()
    all_processes.append(p)

while all_processes:
    for one_process in all_processes:
        start_wait = time.time()
        print(f'Now waiting on process {one_process.name}')
        one_process.join(0.001)
        if not one_process.is_alive():
            print(
                f'\tTerminated process {one_process.name} after {time.time() - start_wait} secs')
            all_processes.remove(one_process)

print('Done!')
