import os
import base64
import shelve

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

def writeToDoc (path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()

def save(url, content):
    addToForwardIndex(url)
    firstDir = getDir(url)
    path = getPath(url, firstDir)
    writeToDoc(path, content)

