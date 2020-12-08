#!/usr/bin/env python3

import requests
import store
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from aiohttp import ClientSession


async def getAndSaveDocument(url, session):
    if url.startswith('http'):
        try:
            subR = await session.request(method='GET', url=url)
            text = await subR.text()
            await store.save(url, text)
        except:
            print('something went wrong with ' + url)


async def main():
    async with ClientSession() as session:
        tic = time.process_time()
        r = await session.request(method="GET", url='https://news.ycombinator.com/')
        text = await r.text()
        soup = BeautifulSoup(text, 'html.parser')
        links = soup.find_all('a')
        urls = []
        for link in links:
            urls.append(link.get('href'))
        await asyncio.gather(*[getAndSaveDocument(url, session) for url in urls])
        toc = time.process_time()
        print(toc - tic)

asyncio.run(main())

