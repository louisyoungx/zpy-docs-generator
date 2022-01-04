import requests
from scrapy import Selector

from config import URL
from log import log

def getModule(name):

    url = URL + name
    r = requests.get(url)
    r.encoding = r.apparent_encoding

    response = r.text
    html = Selector(text=response)

    name = html.xpath("//code[@class='xref py py-mod docutils literal notranslate']//span[@class='pre']//text()").get()
    methods = html.xpath("//code[@class='sig-name descname']//text()").getall()
    params = html.xpath("//span[@class='n']//text()").getall()

    result = {
        'encoding': r.encoding,
        'status-code': r.status_code,
        'name': name,
        'methods': methods,
        'params': params
    }

    if name and methods is not []:
        log('\n' + '=' * 20)
        log('Module: ' + name)
        log('Encoding: ' + r.encoding)
        log('Status Code: ' + str(r.status_code))
        # log('Methods: \n' + str(methods))
        # log('Params: \n' + str(params))
        log('=' * 20 + '\n')
        return result
    else:
        log(f"Error: {name} Not Found")
        return None

