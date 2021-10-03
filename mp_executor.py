#!/usr/bin/env python3

# let's do the same thing, but in a more compact way

import concurrent.futures

urls = ['https://python.org',
        'https://nytimes.com',
        'https://lerner.co.il',
        'https://manning.com',
        'https://pydata.org',
        'https://podia.com',
        'https://getdrip.com']


def get_url_length(one_url):
    r = requests.get(one_url)
    return f'{one_url}: {len(r.content)}\n'


start_time = time.perf_counter()

with ProcessPoolExecutor(max_workers=10) as executor:
    all_futures = []
    for one_url in urls:
        f = executor.submit(get_url_length, one_url)
        all_futures.append(f)

    for one_future in concurrent.futures.as_completed(all_futures):
        print(one_future.result())

end_time = time.perf_counter()
print(f'It took {end_time - start_time} secs')
