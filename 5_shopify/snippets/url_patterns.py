from collections import Counter
from urllib.parse import urlparse
from shopify.discover import Discover

"""
Function for finding url patterns from a list of urls
"""


def find_url_patterns(urls, n=4):
    patterns = Counter()
    for url in urls:
        path = urlparse(url).path.split('/')
        for i in range(1, len(path)):
            patterns['/'.join(path[:i+1])] += 1
    return patterns.most_common(n)


if __name__ == '__main__':
    urls = Discover('redbullshopus.com').get_urls()
    print(find_url_patterns(urls))
    urls = Discover('store.nytimes.com').get_urls()
    print(find_url_patterns(urls))
