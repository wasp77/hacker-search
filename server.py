#!/usr/bin/env python3

from flask import Flask
from markupsafe import escape
from flask_cors import CORS
import shelve
from functools import reduce

app = Flask(__name__)
CORS(app)
inverseIndex = shelve.open('index-inverse')

@app.route('/search/<query>')
def search(query):
    safeQuery = escape(query)
    queryDocs = {}
    for term in safeQuery.split():
        if term in inverseIndex:
            queryDocs[term] = inverseIndex[term]
    results = {}
    for queryTerm in queryDocs:
        for doc in queryDocs[queryTerm]:
            if doc in results:
                results[doc] += queryDocs[queryTerm][doc]
            else:
                results[doc] = queryDocs[queryTerm][doc]
    return results

if __name__ == '__main__':
    app.run(port=5001)
