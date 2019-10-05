import asyncio
import json
from json import JSONDecoder

from aiohttp import ClientSession, TCPConnector
from parsel import Selector

"""
This module contains Consumer crawler which takes in article urls and
downloads, parses and saves them to a file.
"""


def json_from_text(text, decoder=JSONDecoder()):
    """Find JSON objects in text"""
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            if result:
                yield result
            pos = match + index
        except ValueError:
            pos = match + 1


class Consumer:
    """
    Asynchronous crawler that takes in urls, crawls pages, parses them
    and store results in a jsonlines file
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/66.0.3359.181 Safari/537.36",
    }
    product_keys = {'id', 'title', 'description'}

    def __init__(self, filename, concurrency=60):
        """
        :param filename: jsonline filename where results will be appended
        :param concurrency: concurrent request count
        :param max_retries: how many times to retry non 200 responses
        """
        self.connector = TCPConnector(limit=concurrency)
        self.filename = filename

    def parse_product(self, url, html) -> dict:
        """Parse html for data"""
        script_text = '\n'.join(Selector(text=html).xpath('//script/text()').extract())
        for data in json_from_text(script_text):
            if all(k in data for k in self.product_keys):
                return {'url': url, **data}

    async def _crawl(self, urls):
        """Crawl coroutine that concurrently crawls, parses and saves scraped data from provided urls"""
        # open output file in append mode
        with open(self.filename, 'a') as file:
            # open a connection session
            async with ClientSession(connector=self.connector, headers=self.headers) as session:
                results = (self._crawl_product(url, session, file) for url in urls)
                return await asyncio.gather(*results, return_exceptions=True)

    async def _crawl_product(self, url, session, file):
        """Crawl coroutine that scrapes a product and saves it to file"""
        async with session.get(url, timeout=60) as response:
            html = await response.text()
            print(f'crawled: {url}')
            parsed = self.parse_product(url, html)
            if parsed:
                file.write(json.dumps(parsed) + '\n')
                return parsed['url']

    def crawl(self, urls):
        """_crawl articles asynchronously"""
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self._crawl(urls))
