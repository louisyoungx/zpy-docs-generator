import os

DEBUG = True
URL = 'https://docs.python.org/zh-cn/3.10/library/'
PATH = os.path.dirname(os.path.abspath(__file__))

# [Libs Storage Settings]
LIB_NAME = 'libs'
LIBS_PATH = os.path.join(PATH, LIB_NAME)

# [Dictionary Settings]
DICS_PATH = os.path.join(PATH, 'dics')
DICS_NAME = 'dictionary_lite.csv' # dictionary_lite.csv / dictionary_full.csv
ONLINE_QUERY_INTERVAL = 0.5
LENGTH_LIMIT = 3
FORCE_WRITE = False

