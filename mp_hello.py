#!/usr/bin/env python3

import multiprocessing
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!\n', end='')


all_processes = []
for i in range(10):
    p = multiprocessing.process(target=hello, args=(i,), name=f'hello-{i}')
    p.start()
    all_processes.append(p)

while all_threads:
    for one_thread in all_threads:
        start_wait = time.time()
        print(f'Now waiting on thread {one_thread.name}')
        one_thread.join(0.001)
        if not one_thread.is_alive():
            print(
                f'\tTerminated thread {one_thread.name} after {time.time() - start_wait} secs')
            all_threads.remove(one_thread)

print('Done!')
