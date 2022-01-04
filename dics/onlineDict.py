import requests
import hashlib
import random
import time
from config import ONLINE_QUERY_INTERVAL
from log import log

class OnlineDictionary(object):
    def __init__(self):
        self.https_url = "https://openapi.youdao.com/api"  # Api的https地址
        self.app_key = "0feea8d9170c2a8a"  # 应用ID
        self.secret_key = "UiXzbLvNDhxMbxiO1f2epTw7w0vSaWCx"  # 应用密钥
        self.api_docs = "http://ai.youdao.com/docs/api.s#"  # 有道翻译api和说明文档
        self.language = {  # 语言转换表
            "zh-CHS": "中文",
            "ja": "日文",
            "en": "英文",
            "ko": "韩语",
            "fr": "法语",
            "ru": "俄语",
            "pt": "葡萄牙",
            "es": "西班牙文",
            "EN": "英文",
            "zh": "中文"
        }

    def get(self, wordList):
        query = ''
        for word in wordList:
            query += word + ',\n'
        result = self.translate(query)[0: -1]
        result = result.replace(',', '')
        result = result.replace('，', '')
        translated = result.split('\n')
        return translated

    def translate(self, word):
        salt = str(random.randint(12345, 56789))  # 生成随机数
        sign = self.to_sign(word, salt)  # 生成签名
        api_url = self.get_api_url(query=word, sign=sign, salt=salt)
        try:
            translation_json = requests.get(api_url)
            time.sleep(ONLINE_QUERY_INTERVAL)
        except Exception as e:
            log("没有网络连接:" + e)
            return word
        if not translation_json.ok:
            log("网络查询错误:" + translation_json)
            return word
        result = self.resolve_res(src=word, trans_json=translation_json.json())
        return result

        # 生成md5签名
    def to_sign(self, query, salt):
        """
        签名要进行UTF-8编码(否则中文无法翻译)
        :param q: 翻译文本
        :param salt: 随机数
        :return: sign: md5签名
        """
        sign = self.app_key + query + salt + self.secret_key
        m = hashlib.md5()
        m.update(sign.encode('utf-8'))
        sign = m.hexdigest()
        return sign


    # 生成api_url
    def get_api_url(self, sign, salt, query="Hello World", from_lang="en", to_lang="zh-CHS"): # from_lang="auto", to_lang="auto"
        api_url = "{}?q={}&sign={}&from={}&to={}&appKey={}&salt={}".format(self.https_url, query, sign, from_lang, to_lang, self.app_key, salt)
        return api_url


    # 解析返回的json字段生成翻译
    def resolve_res(self, src, trans_json):
        """
        把API返回的json字段解析成文字
        :param trans_json: json
        :return: string
        """
        try:
            result = trans_json['translation'][0]
            return result
        except:
            return src