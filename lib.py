import requests
from scrapy import Selector

from config import URL
from log import log

def getLibs():

    libs = ['functions.html', 'constants.html', 'stdtypes.html', 'exceptions.html']

    return libs
