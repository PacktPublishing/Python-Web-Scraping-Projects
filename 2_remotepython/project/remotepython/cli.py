import csv
import click
from remotepython.crawler import crawl

BASE_URL = 'https://www.remotepython.com/jobs/?q={}'.format

@click.command()
@click.argument('file', type=click.File('w'))
@click.argument('keyword', required=False)
def main(file, keyword):
    """Crawler for remotepython.com jobs"""
    start_url = BASE_URL(keyword)
    csv_writer = None
    for job in crawl(start_url):
        if not csv_writer:
            csv_writer = csv.DictWriter(file, job)
            csv_writer.writeheader()
        csv_writer.writerow(job)


if __name__ == '__main__':
    main()
