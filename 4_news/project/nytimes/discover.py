import gzip
import re
from datetime import datetime
from urllib.parse import urlparse

import requests
from parsel import Selector

"""
This module contains crawler that discovers article urls of nytimes.com 
using sitemap strategy.
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


class Discover:
    sitemaps_root_url = 'https://www.nytimes.com/sitemaps/www.nytimes.com/sitemap.xml.gz'

    def __init__(self, from_date: datetime, to_date: datetime):
        self.from_date = from_date
        self.to_date = to_date

    def _get_sitemaps(self):
        """get sitemaps in discovery time range"""
        urls = download_sitemap(self.sitemaps_root_url)
        for url in urls:
            try:
                year, month = re.findall('sitemap_(\d+)_(\d+)', url)[0]
            except IndexError:
                continue
            url_datetime = datetime(year=int(year), month=int(month), day=1)
            # we want to only compare year and months here
            if self.to_date.replace(day=1) >= url_datetime >= self.from_date.replace(day=1):
                yield url

    def get_urls(self):
        """get urls in discovery time range"""
        all_urls = []
        for sitemap in self._get_sitemaps():
            urls = download_sitemap(sitemap)
            for url in urls:
                try:
                    year, month, day = re.findall('(\d+)/(\d+)/(\d+)', url)[0]
                except IndexError:
                    # urls that don't follow this pattern aren't articles
                    continue
                url_datetime = datetime(year=int(year), month=int(month), day=int(day))
                if self.to_date >= url_datetime >= self.from_date:
                    all_urls.append(url)
        return all_urls
