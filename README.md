# Zpy Docs Generator

## Quick Start

clone this repo
```shell
git clone https://github.com/louisyoungx/zpy-docs-generator.git
cd zpy-docs-generator
```

install dependences
```shell
pip install requests, scrapy, jieba, wordninja
```

download dictionary
```
wget https://resource.rocke.top/zpy/dictionary_lite.csv
mv dictionary_lite.csv dics
```

checkout to requests branch
```shell
git checkout requests
```

### Requests Lib

generate requests lib docs
```shell
python3 main.py
```

requests lib docs in `requests-libs` directory
```shell
ls requests-libs
```