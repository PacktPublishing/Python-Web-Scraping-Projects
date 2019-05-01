import gzip
from urllib.parse import urlparse

import requests
from parsel import Selector

"""
This snippet example show how to download and parse sitemaps using `parsel` and `requests` packages.
"""


def download_sitemap(url):
    response = requests.get(url)
    text = response.text
    # if url points to a gzipped file - decompress it
    if urlparse(response.url).path.endswith('.gz'):
        text = gzip.decompress(response.content).decode(response.encoding or 'utf8')
    selector = Selector(text)
    # urls are under <loc> tag
    # if they are direct articles they have <url> tag parent
    urls = selector.xpath('//url/loc/text()').extract()
    if not urls:
        urls = selector.xpath('//loc/text()').extract()
    return urls


if __name__ == '__main__':
    # for example try nytimes sitemaps!
    urls = download_sitemap('https://www.nytimes.com/sitemaps/www.nytimes.com/sitemap.xml.gz')
    print('\n'.join(urls[:4]))
