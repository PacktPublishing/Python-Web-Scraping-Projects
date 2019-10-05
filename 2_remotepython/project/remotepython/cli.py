import csv
import click
from remotepython.crawler import crawl

BASE_URL = 'https://www.remotepython.com/jobs/?q={}'.format


@click.command()
@click.argument('outfile', type=click.File('w'))
@click.argument('search_keyword', required=False)
def main(outfile, search_keyword):
    """Crawler for remotepython.com jobs"""
    start_url = BASE_URL(search_keyword)
    csv_writer = None
    for job in crawl(start_url):
        if not csv_writer:
            csv_writer = csv.DictWriter(outfile, job)
            csv_writer.writeheader()
        csv_writer.writerow(job)


if __name__ == '__main__':
    main()
