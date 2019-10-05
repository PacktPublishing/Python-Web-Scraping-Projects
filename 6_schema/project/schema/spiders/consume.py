from pprint import pprint

import requests
from extruct import JsonLdExtractor, MicrodataExtractor, OpenGraphExtractor, RDFaExtractor
from schema.parsers.microdata import format_microdata
from schema.parsers.opengraph import format_og
from schema.parsers.rdfa import format_rdfa
from schema.parsers.jsonld import format_jsonld

"""
"""


class SchemaCrawler:
    """
    """
    default_headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/66.0.3359.181 Safari/537.36",
    }

    def __init__(self, headers=None):
        self.extractors = [
            # ordered from most reliable to least
            (JsonLdExtractor(), format_jsonld),
            (MicrodataExtractor(), format_microdata),
            (RDFaExtractor(), format_rdfa),
            (OpenGraphExtractor(), format_og),
        ]
        if headers:
            self.headers = headers
        else:
            self.headers = self.default_headers
        self.session = requests.session()

    def crawl(self, url):
        resp = self.session.get(url, headers=self.headers)
        assert resp.status_code == 200
        results = {}
        for extractor, parser in self.extractors[::-1]:
            extracted_nodes = extractor.extract(resp.text)
            if parser:
                extracted_nodes = [parser(node) for node in extracted_nodes]
            results[type(extractor).__name__] = [node for node in extracted_nodes if node]
        return results

    def crawl_flat(self, url):
        flat = {}
        for extracted_nodes in self.crawl(url).values():
            for result in extracted_nodes:
                flat.update(result)
        return flat

    def crawl_merged(self, url):
        merged = []
        for extracted_nodes in sorted(self.crawl(url).values(), key=len):
            for i, result in enumerate(extracted_nodes):
                try:
                    merged[i].update(result)
                except IndexError:
                    merged.append(result)
        return merged


