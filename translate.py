from utils import Progress
from config import LENGTH_LIMIT, FORCE_WRITE
from dics import search
from dics import split, search, onlineSearch

class Translater(object):

    def translate(self, libInfo):

        steps = len(libInfo['methods']) + len(libInfo['params'])
        if steps == 0:
            return None
        self.progress = Progress(steps)

        lib = {}
        lib['name'] = libInfo['name']
        lib['zpy'] = search(libInfo['name'])
        lib['functions'] = []
        lib['args'] = []

        methods = self.pruning(libInfo['methods'])
        params = self.pruning(libInfo['params'])
        
        lib['functions'] = self.getLines(methods)
        lib['args'] = self.getLines(params)
        self.progress.done()
        self.progress = None
        return lib
    
    def getLines(self, wordList):

        prunedWords = self.pruning(wordList)
        longWords = []
        if not FORCE_WRITE:
            for word in prunedWords:
                if len(word) > LENGTH_LIMIT:
                    longWords.append(word)
            words = longWords
            if len(words) < 1:
                return []
        else:
            words = prunedWords

        waitTranslate = []

        for word in words:
            localWord = search(word)
            if localWord:
                waitTranslate.append(localWord)
            else:
                waitTranslate.append(split(word))

        translated = onlineSearch(waitTranslate)
        data = []

        for i in range(len(translated)):
            data.append({
                'name': words[i],
                'zpy': translated[i]
            })
            self.progress.update()
        return data
    
    def pruning(self, wordList):
        return list(set(wordList))
        
translater = Translater()

def translate(lib):
    return translater.translate(lib)