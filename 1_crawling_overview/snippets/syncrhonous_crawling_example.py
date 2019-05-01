import requests
from pprint import pprint


def fetch_url(session, url):
    """return html body of url"""
    return session.get(url).text


def fetch_all_urls(session, urls):
    """return html bodies of multiple urls"""
    return [fetch_url(session, url) for url in urls]


def get_htmls(urls):
    """
    download html contents of supplied urls synchronously
    """
    session = requests.session()
    htmls = fetch_all_urls(session, urls)
    return dict(zip(urls, htmls))


def crawl():
    urls = [f'http://httpbin.org/links/100/{i}' for i in range(10)]
    data = get_htmls(urls)
    pprint(data)
