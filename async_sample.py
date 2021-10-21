import asyncio
import time
from typing import NamedTuple

import aiohttp


class FetchedData(NamedTuple):
    status: int
    text: str


URLs = (
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/3',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/1',
)


async def fetch(session, url, i) -> FetchedData:
    print(f'start fetching i={i}')
    async with session.get(url) as response:
        text = await response.text()
        print(f'finished fetching i={i}')
        return response.status, text


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = [asyncio.ensure_future(fetch(session, url, i))
                 for i, url in enumerate(URLs)]
        responses = await asyncio.gather(*tasks)
        for status, text in responses:
            pass
            # print(status, text)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print('Finished, during={}sec'.format(time.time() - start))
