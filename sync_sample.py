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

    # takes 5 seconds
    responses = [
        requests.get(url)
        for url in URLs
    ]
    print('Finished, during={}sec'.format(time.time() - start))


if __name__ == '__main__':
    main()
