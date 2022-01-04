# coding=utf-8
import os
import json
from config import LIBS_PATH
from log import log

class Files(object):
    def __init__(self):
        if not os.path.exists(LIBS_PATH):
            os.mkdir(LIBS_PATH)
        self.path = LIBS_PATH

    def create(self, filename, data):
        with open(self.path + '/' + filename + '.json', 'w+', encoding = 'utf-8') as lib:
            lib.seek(0)
            lib.truncate()
            data = json.dumps(data, sort_keys=False, ensure_ascii=False, indent=4, separators=(",", ":"))
            lib.write(data)
        log(f"File - {filename} Created")

files = Files()

