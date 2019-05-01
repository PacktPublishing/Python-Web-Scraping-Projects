import asyncio
from pprint import pprint
from aiohttp import ClientSession, TCPConnector


async def fetch_url(session, url):
    """return html body of url"""
    async with session.get(url, timeout=60 * 60) as response:
        return await response.text()


async def fetch_all_urls(session, urls):
    """return html bodies of multiple urls"""
    # futures for response html content
    futures = [fetch_url(session, url) for url in urls]
    # gather all responses as one future
    futures = asyncio.gather(*futures, return_exceptions=True)
    return await futures


def get_htmls(urls, concurrency=100):
    """
    download html contents of supplied urls asynchronously
    :param concurrency: amount of concurrent requests
    """
    loop = asyncio.get_event_loop()
    connector = TCPConnector(limit=concurrency)
    session = ClientSession(loop=loop, connector=connector)
    htmls = loop.run_until_complete(fetch_all_urls(session, urls))
    loop.run_until_complete(session.close())
    return dict(zip(urls, htmls))


def crawl():
    urls = [f'http://httpbin.org/links/100/{i}' for i in range(10)]
    data = get_htmls(urls)
    pprint(data)
