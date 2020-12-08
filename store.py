import os
import base64
import shelve
import asyncio
from aiofile import async_open

BASE_DIR = 'documents'

def addToForwardIndex(url):
    d = shelve.open('index')
    d[url] = {}
    d.close


def getDir (url):
    fileHash = hash(url)
    mask = 255
    firstDir = str(fileHash & mask)
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)
    path = BASE_DIR + '/' + firstDir
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def getPath (url, firstDir):
    fileName = base64.b64encode(url.encode('utf-8'), b'_-').decode()
    path = firstDir + '/' + fileName
    return path

async def writeToDoc (path, content):
    async with async_open(path, 'w') as file:
        await file.write(content)

async def save(url, content):
    addToForwardIndex(url)
    firstDir = getDir(url)
    path = getPath(url, firstDir)
    await writeToDoc(path, content)

