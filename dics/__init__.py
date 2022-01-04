from .localDict import LocalDictionary
from .onlineDict import OnlineDictionary
from .spliter import split
from log import log

localDic = LocalDictionary()
onlineDict = OnlineDictionary()

def search(word):
    localWords = localDic.get(word)
    if localWords != []:
        return localWords[0]

def onlineSearch(wordList):
    return onlineDict.get(wordList)