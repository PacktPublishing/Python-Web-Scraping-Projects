import json
import re
from pathlib import Path

import click
from click import echo
from schema.spiders.consume import SchemaCrawler
from schema.spiders.identify import identify_schema_formats
import requests_cache

CACHE_DIR = str(Path('~/.cache/schema_requests').expanduser())


@click.group()
@click.option('--cache', '-c', is_flag=True, help='enable requests caching')
def main(cache):
    """
    General schema.org information crawler that supports
    json-ld, opengraph, rdfa, microdata and microformat formats
    """
    if cache:
        requests_cache.install_cache(CACHE_DIR, backend='sqlite')


@main.command('identify')
@click.argument('urls', nargs=-1)
@click.option('--json', 'as_json', is_flag=True, help='show as json')
def identify(urls, as_json):
    """identify schema.org formats of provided urls"""
    header = f'{"url":<70}|{"jld":^5}|{"og":^5}|{"rdfa":^5}|{"mdata":^5}|{"mformat":^5}'
    if as_json:
        json_result = {}
    else:
        echo('-' * len(header))
        echo(header)
        echo('-' * len(header))
    for url in urls:
        results = identify_schema_formats(url)
        if as_json:
            json_result[url] = results
            continue
        has_json_ld = '+' if 'json-ld' in results else ''
        has_opengraph = '+' if 'opengraph' in results else ''
        has_rdfa = '+' if 'rdfa' in results else ''
        has_microdata = '+' if 'microdata' in results else ''
        has_microformat = '+' if 'microformat' in results else ''
        url = re.sub('https*://', '', url)
        url = re.sub('www\d*\.', '', url)
        if len(url) > 70:
            url = url[:30] + '...' + url[-37:-1]
        echo(f'{url:<70}|{has_json_ld:^5}|{has_opengraph:^5}|{has_rdfa:^5}|{has_microdata:^5}|{has_microformat:^5}')
    if as_json:
        echo(json.dumps(json_result, indent=2))
    exit(0)


@main.command('crawl')
@click.argument('urls', nargs=-1)
@click.option('--flat', 'as_flat', help='flatten output', is_flag=True)
@click.option('--merged', 'as_merged', help='merge output', is_flag=True)
def crawl(urls, as_flat, as_merged):
    """crawl schema data of provided urls"""
    crawler = SchemaCrawler()
    results = {}
    for url in urls:
        if as_flat:
            results[url] = crawler.crawl_flat(url)
        elif as_merged:
            results[url] = crawler.crawl_merged(url)
        else:
            results = crawler.crawl(url)
    if len(results) == 1:
        results = results[list(results.keys())[0]]
    echo(json.dumps(results, indent=2))
    exit(0)
