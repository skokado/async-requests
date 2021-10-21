from concurrent.futures import ThreadPoolExecutor
import time

import requests

URLs = (
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
)


def main():
    start = time.time()

    futures = []
    with ThreadPoolExecutor(max_workers=len(URLs)) as executor:
        futures = [executor.submit(requests.get, url)
                   for url in URLs]
        results = [future.result() for future in futures]
    for result in results:
        print(result)

    print('Finished, during={}sec'.format(time.time() - start))


if __name__ == '__main__':
    main()
