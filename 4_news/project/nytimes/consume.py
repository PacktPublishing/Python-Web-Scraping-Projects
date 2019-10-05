import asyncio
import json

from aiohttp import ClientSession, TCPConnector
from parsel import Selector

"""
This module contains Consumer crawler which takes in article urls and
downloads, parses and saves them to a file.
"""


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

    def __init__(self, filename, concurrency=60):
        """
        :param filename: jsonline filename where results will be appended
        :param concurrency: concurrent request count
        :param max_retries: how many times to retry non 200 responses
        """
        self.connector = TCPConnector(limit=concurrency)
        self.filename = filename

    def parse_article(self, url, html) -> dict:
        """Parse html for data"""
        sel = Selector(text=html)
        data = {
            'url': url,
            'date': sel.css('time::attr(datetime)').extract_first(),
            'title': sel.css('h1 ::text').extract_first(),
        }
        return data

    async def _crawl(self, urls):
        """Crawl nytime.com articles from given urls"""
        # open output file in append mode
        with open(self.filename, 'a') as file:
            # open a connection session
            async with ClientSession(connector=self.connector, headers=self.headers) as session:
                results = (self._crawl_article(url, session, file) for url in urls)
                return await asyncio.gather(*results, return_exceptions=True)

    async def _crawl_article(self, url, session, file):
        """Crawl article"""
        async with session.get(url, timeout=60) as response:
            html = await response.text()
            parsed = self.parse_article(url, html)
            file.write(json.dumps(parsed) + '\n')
            print(f'crawled: {url}')
            return parsed['url']

    def crawl(self, urls):
        """_crawl articles asynchronously"""
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self._crawl(urls))

