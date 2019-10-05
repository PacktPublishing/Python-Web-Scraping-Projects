import requests
import extruct


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'


def identify_schema_formats(url):
    """
    Identifies what schema.org formats webpage supports
    possible results:
    microdata, json-ld, opengraph, microformat, rdfa
    """
    resp = requests.get(url, headers={'User-Agent': USER_AGENT})
    data = extruct.extract(resp.text, base_url=url, encoding=resp.encoding)
    found = []
    for format, value in data.items():
        if value:
            found.append(format)
    return sorted(found)



