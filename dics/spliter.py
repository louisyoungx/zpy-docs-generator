import wordninja
import jieba

def split(word):
    splitWord = ''
    jiebaResult = list(jieba.cut(word, cut_all=True))
    if len(jiebaResult) > 1:
        
        for word in jiebaResult:
            if '_' not in word and '-' not in word:
                splitWord += word + ' '
        splitWord = splitWord[0: -1]
    else:
        wordninjaResult = wordninja.split(word)
        if len(wordninjaResult) > 1:
            splitWord = ''
            for word in wordninjaResult:
                if '_' not in word and '-' not in word:
                    splitWord += word + ' '
            splitWord = splitWord[0: -1]
    return splitWord

print(split('initial_indent'))