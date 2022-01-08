import os
import json
from lib import Lib
from lib.__builtin__ import BUILT_IN
from lib.standard import STANDARD

lib = Lib(BUILT_IN, 'error')

LIB_DIR = '/standard'

PATH = lib.path + LIB_DIR

libList = []

for root, dirs, files in os.walk(PATH):
    for file in files:
        if file.split('.')[-1] == 'json':
            libList.append(PATH + '/' + file)
            print(file)

print("=" * 50)

for libFile in libList:
    with open(libFile) as file:
        content = file.read()
        file.close()
    libContent = json.loads(content)
    if libContent == None:
        os.remove(libFile)
        print(f'已删除: {libFile}')
    for item in libContent['functions']:
        if item['name'] in lib.pyMap:
            print(item['name'])



