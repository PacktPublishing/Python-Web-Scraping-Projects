"""
This is a snippet example of how to parse robots.txt in python
"""
# python already comes with a robots.txt parser
from urllib import robotparser


url = 'https://www.nytimes.com/robots.txt'
parser = robotparser.RobotFileParser(url)
print(f'reading robots.txt from: {url}')
# Download and parser robots.txt file
parser.read()
# the parser goes through lines and updates itself with appropriate filters
# You can see entries it creates with:
print(f'found these entries: {parser.entries}')

# Then we can use parser to determine whether we're allowed can _crawl something
useragent = 'Firefox'
print(f'can we crawl: {url} as {useragent}?')
print(parser.can_fetch(useragent, url))

