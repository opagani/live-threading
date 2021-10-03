import multiprocessing
import time
import requests
import queue

q = multiprocessing.Queue()

urls = ['https://python.org',
        'https://nytimes.com',
        'https://lerner.co.il',
        'https://manning.com',
        'https://pydata.org',
        'https://podia.com',
        'https://getdrip.com']


def get_url_length(one_url):
    r = requests.get(one_url)
    q.put((one_url, len(r.content)))


# launch all processes to download info from URLs
all_processes = []
for one_url in urls:
    p = multiprocessing.Process(target=get_url_length, args=(
        one_url,), name=f'process-{one_url}')
    all_processes.append(p)
    p.start()

# join all of the processes
while all_processes:
    for one_process in all_processes:
        start_wait = time.time()
        one_process.join(0.001)
        if not one_process.is_alive():
            print(
                f'\tTerminated process {one_process.name} after {time.time() - start_wait} secs')
            all_processes.remove(one_process)

    print('Done!')


# consumer


def print_queue_contents():
    while True:
        print(q.get())


multiprocessing.Process(target=print_queue_contents).start()

for one_process in all_processes:
    one_process.join()

end_time = time.perf_counter()

print(f'We took {end_time - start_time} seconds')
