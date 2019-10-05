import gzip
import re
from urllib.parse import urlparse

import requests
from parsel import Selector


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
    products_sitemap_identifier = re.compile('sitemap_products_\d+')
    product_url_identifier = re.compile('/products/')

    def __init__(self, domain):
        self.domain = domain
        self.sitemap_url = f'http://{domain}/sitemap.xml'

    def get_urls(self):
        sitemap_urls = download_sitemap(self.sitemap_url)
        product_urls = []
        for url in sitemap_urls:
            if not self.products_sitemap_identifier.search(url):
                continue
            found_products = download_sitemap(url)
            product_urls.extend([url for url in found_products if self.product_url_identifier.search(url)])
        return product_urls

