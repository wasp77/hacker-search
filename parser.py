#!/usr/bin/env python3

import shelve
import store
import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def readFromDoc (path):
    file = open(path, 'r')
    return file.read()

stopWords = set(stopwords.words('english'))

d = shelve.open('index', writeback=True)
for url in d:
    firstDir = store.getDir(url)
    path = store.getPath(url, firstDir)
    if os.path.exists(path):
        html = readFromDoc(path)
        soup = BeautifulSoup(html, features="html.parser")
        tokens = word_tokenize(soup.get_text())
        filteredTokens = filter(lambda x: x not in stopWords and x.isalpha(), tokens)
        for token in list(filteredTokens):
            if token not in d[url]:
                d[url][token] = 1
            else:
                d[url][token] += 1
d.close()


