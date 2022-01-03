# Doing a search using Urllib
import requests
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from duckduckgo_search import ddg

params = dict(q='India', format='json')
handle = urlopen(f'http://api.duckduckgo.com?{urlencode(params)}')
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)

print('Using Urllib')
results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(f"{r['FirstURL']} - {r['Text']}")


print('using Request\n')
# Doing a search using Request Library
parsed_req = requests.get('http://api.duckduckgo.com/', params=params).json()

results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(f"{r['FirstURL']} - {r['Text']}")

print('Using DuckDuck Go Library\n')
results = ddg('India', max_results=5)
for r in results:
    print(f"{r['href']} - {r['title']}")