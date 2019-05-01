import requests
import re

"""
This snippet example show how to download and parse sitemaps using `parsel` and `requests` packages.
"""


def find_json_key_in_url(url, key):
    response = requests.get(url)
    return re.findall(f'"{key}":"(.+?)"', response.text)[0]


if __name__ == '__main__':
    print(find_json_key_in_url('https://www.nytimes.com/search', "nyt-token"))
