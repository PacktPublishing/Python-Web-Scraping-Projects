import click
from click import echo
from shopify.discover import Discover
from shopify.consume import Consumer


@click.command()
@click.argument('domain')
@click.argument('output_file', type=click.Path(dir_okay=False))
@click.option('--concurrency', type=click.INT, default=30)
def main(domain, output_file, concurrency):
    discover = Discover(domain)
    urls = discover.get_urls()
    if not urls:
        echo(f"could not discover any product urls for: {domain}")
        exit(1)
    echo(f'discovered {len(urls)} urls')
    consumer = Consumer(output_file, concurrency=concurrency)
    crawled_urls = consumer.crawl(urls)
    echo(f'saved {len(crawled_urls)} products to {output_file}')
    exit(0)

