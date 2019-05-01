import math
import re
from datetime import datetime

import requests


class DiscoverGraphql:
    search_url = 'https://www.nytimes.com/search'
    graphql_url = 'https://samizdat-graphql.nytimes.com/graphql/v2'
    base_form = {
        "operationName": "SearchRootQuery",
        "variables": {
            "first": 100,
            "sort": "oldest",
            "beginDate": "20180101",  # change this
            "endDate": "20180201",  # change this
            "cursor": "YXJyYXljb25uZWN0aW9uOjI5",  # change this
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "c1bcbffdd277354a36f6bae9ec896a962c870533829c6d1b174b14b0b78b6407"
            }
        }
    }
    headers = {
        'nyt-token': "",  # change this
        'nyt-app-type': "project-vi",
        'nyt-app-version': "0.0.3",
        'accept-encoding': "gzip, deflate, br",
        'content-type': "application/json",
    }

    def __init__(self, from_date: datetime, to_date: datetime):
        # self.from_date = from_date
        # self.to_date = to_date
        self.base_form['variables']['beginDate'] = from_date.strftime('%Y%m%d')
        self.base_form['variables']['endDate'] = to_date.strftime('%Y%m%d')

    def get_urls(self):
        form = self.base_form.copy()
        # first request has no page cursor
        form['variables'].pop('cursor')
        # lets find our `nyt-token` header
        resp = requests.get(self.search_url)
        nyt_token = re.findall(f'"nyt-token":"(.+?)"', resp.text)[0]
        self.headers['nyt-token'] = nyt_token

        # _crawl pages in a loop
        session = requests.Session()
        page = 1
        total_pages = 'unknown'
        print(f"crawling in date range: {form['variables']['beginDate']} to {form['variables']['endDate']}")
        while True:
            print(f'crawling page {page}/{total_pages}')
            # make post request to graphql api with our form and headers
            resp = session.post(self.graphql_url, json=form, headers=self.headers)

            # parse data for article urls
            data = resp.json()['data']['legacySearch']['hits']
            if 'cursor' not in form['variables']:
                total_pages = math.ceil(data['totalCount'] / form['variables']['first'])
            for article in data['edges']:
                url = article['node']['node']['url']
                yield url

            # parse data for next page cursor
            next_page = data['pageInfo']
            if not next_page['hasNextPage']:
                # if there's no next page quit!
                break

            assert next_page['endCursor'] != form['variables'].get('cursor')
            form['variables']['cursor'] = next_page['endCursor']
            page += 1
