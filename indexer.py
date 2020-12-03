#!/usr/bin/env python3

import shelve

forwardIndex = shelve.open('index')
inverseIndex = shelve.open('index-inverse', writeback=True)
"""
Inverted index = {<word>: {<documents>: <occurance number>}}
"""

for url in forwardIndex:
    for token in forwardIndex[url]:
        if token not in inverseIndex:
            inverseIndex[token] = {}
        inverseIndex[token][url] = forwardIndex[url][token]

print(inverseIndex['space'])

forwardIndex.close()
inverseIndex.close()


