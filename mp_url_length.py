import threading
import time
import requests
import queue

q = queue.Queue()

urls = ['https://python.org',
        'https://nytimes.com',
        'https://lerner.co.il',
        'https://manning.com',
        'https://pydata.org',
        'https://podia.com',
        'https://getdrip.com']

start_time = time.perf_counter()


def get_url_length(one_url):
    r = requests.get(one_url)
    q.put((one_url, len(r.content)))


all_threads = []

# producer
for one_url in urls:
    t = threading.Thread(target=get_url_length, args=(
        one_url,), name=f'thread-{one_url}')
    all_threads.append(t)
    t.start()

# consumer


def print_queue_contents():
    while True:
        print(q.get())


threading.Thread(target=print_queue_contents, daemon=True).start()

for one_thread in all_threads:
    one_thread.join()

end_time = time.perf_counter()

print(f'We took {end_time - start_time} seconds')
