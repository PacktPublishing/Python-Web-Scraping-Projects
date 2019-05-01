from time import time

import click
from nytimes.consume import Consumer
from nytimes.discover import Discover

"""
This is click command line interface wrapper around Discover and consumer crawlers.
It takes in date range and starts crawling to specified json lines file
It appends results.
"""


@click.command()
@click.argument('from_date', type=click.DateTime(['%Y-%m-%d']))
@click.argument('to_date', type=click.DateTime(['%Y-%m-%d']))
@click.argument('output_file', type=click.Path(dir_okay=False))
@click.option('--concurrency', type=click.INT, default=30)
def main(from_date, to_date, output_file, concurrency):
    """Crawl nytimes articles from a date range to a json lines file"""
    start = time()
    discovery = Discover(
        from_date=from_date,
        to_date=to_date,
    )
    urls = discovery.get_urls()
    print(f'Discovered {len(urls)} in {time() - start:.2f} seconds')

    start = time()
    consumer = Consumer(
        filename=output_file,
        concurrency=concurrency
    )
    results = consumer.crawl(urls)
    print(f'crawled total: {len(results)} in {time() - start:.2f} seconds')

