import asyncio
import random

"""
This is a simple illustration of how to run coroutines concurrently with asyncio.gather
"""

async def download_page(number):
    await asyncio.sleep(random.randint(0, 100) / 100)
    print(f'downloaded page {number}')

if __name__ == '__main__':
    all_pages = asyncio.gather(*[download_page(i) for i in range(10)])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(all_pages)
