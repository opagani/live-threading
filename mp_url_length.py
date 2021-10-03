import multiprocessing
import time
import requests


def get_url_length(u, q):
    r = requests.get(u)
    q.put((u, len(r.content)))


if __name__ == '__main__':

    q = multiprocessing.Queue()

    urls = ['https://python.org',
            'https://nytimes.com',
            'https://lerner.co.il',
            'https://manning.com',
            'https://pydata.org',
            'https://podia.com',
            'https://getdrip.com']

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
                all_processes.remove(one_process)

    print('Done!')

    while not q.empty():
        print(q.get())
