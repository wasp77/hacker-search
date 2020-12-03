#!/usr/bin/env python3

import requests
import store
from bs4 import BeautifulSoup

r = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith('http'):
       subR = requests.get(url)
       store.save(url, subR.text)


