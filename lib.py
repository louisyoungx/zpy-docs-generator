import requests
from scrapy import Selector

from config import URL
from log import log

def getLibs():

    url = URL
    r = requests.get(url)
    r.encoding = r.apparent_encoding

    log('Encoding: ' + r.encoding)
    log('Status Code: ' + str(r.status_code))

    response = r.text
    html = Selector(text=response)

    libs = html.xpath("//li[@class='toctree-l2']//a[@class='reference internal']/@href").getall()[22:]

    return libs
