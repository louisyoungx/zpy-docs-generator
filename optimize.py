lib_dir = 'standard'

unload_exist = False  # 导入所有已启用文件的映射
skip_exist = True  # 不处理已经启用的文件

check_conflict = True  # 检查冲突
rewrite_conflict = True  # 修复冲突，将改动写回文件

rebuild = False  # 检查zname合法性，重建文件
delete_none = True  # 删除空文件
rewrite_rebuild = False  # 将改动写回文件

build_init = True # 构建__init__.时间.py文件
rewrite_init = True  # 生成文件





def itemHandler(item, libFile):
    name = item['name']
    zname = item['zpy']
    if name in lib.pyMap:
        zname = lib.pyMap[item['name']]
    elif zname == '':
        item['zpy'] = name
    elif pure_english(zname):
        item['zpy'] = name
    elif not vaild_variable(zname):
        newName = zname
        if not pure_english(zname[0]):
            newName = re.sub(r'\(.*\)', '', newName)
            newName = re.sub(r';.*$', '', newName)
            newName = re.sub(r'；.*$', '', newName)
            newName = re.sub(r'\W', '', newName)
            if vaild_variable(newName):
                item['zpy'] = newName
            else:
                # print(newName, "-" * 10, name, "-" * 10, libFile)
                item['zpy'] = name
        else:
            newName = re.sub(r'\(.*\)', '', newName)
            newName = re.sub(r';.*$', '', newName)
            newName = re.sub(r'；.*$', '', newName)
            newName = re.sub(r'\W', '', newName)
            
            if vaild_variable(newName):
                item['zpy'] = newName
            else:
                # print(newName, "-" * 10, name, "-" * 10, libFile)
                item['zpy'] = name
    else:
        # print(zname)
        pass
    return item
        
def pure_english(keyword):  
    return all(ord(c) < 128 for c in keyword)

def vaild_variable(zname):
    if zname[0].isalpha() or zname[0] == '_':
        for i in zname[1:]:
            if not(i.isalnum() or i == '_'):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    import os
    import json
    import re
    import time
    from lib import Lib
    from lib.__builtin__ import BUILT_IN
    from lib.standard import STANDARD

    lib = Lib(BUILT_IN, 'none')
    lib.use(STANDARD)

    if unload_exist:
        for libName in lib.pyLibs:
            lib.load(libName, 'zpy')

    path = lib.path + '/' + lib_dir
    libList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            fileType = file.split('.')[-1]
            fileName = file[:-5]
            if fileType == 'json':
                # print(fileName)
                if skip_exist and fileName in lib.pyLibs:
                    # print(fileName)
                    pass
                else:
                    libList.append(path + '/' + file)
                    # print(file)

    # print("=" * 50)

    if check_conflict:
        for libFile in libList:
            with open(libFile) as file:
                content = file.read()
                file.close()
            libContent = json.loads(content)
            if libContent == None:
                os.remove(libFile)
                print(f'已删除: {libFile}')
            for item in libContent['functions']:
                if item['name'] in lib.pyMap and item['zpy'] != lib.pyMap[item['name']]:
                    item['zpy'] = lib.pyMap[item['name']]
                    print('检查到冲突: ', item['zpy'])
            for item in libContent['args']:
                if item['name'] in lib.pyMap and item['zpy'] != lib.pyMap[item['name']]:
                    item['zpy'] = lib.pyMap[item['name']]
                    print('检查到冲突: ', item['zpy'])
            if rewrite_conflict:
                with open(libFile, 'w+', encoding='utf-8') as file:
                    file.seek(0)
                    file.truncate()
                    data = json.dumps(
                        libContent, sort_keys=False, ensure_ascii=False, indent=4, separators=(",", ":"))
                    file.write(data)
                print(f"File - {libContent['name']}.json Created")

    if rebuild:
        for libFile in libList:
            with open(libFile) as file:
                content = file.read()
                file.close()
            libContent = json.loads(content)
            if delete_none and libContent == None:
                os.remove(libFile)
                print(f'已删除: {libFile}')
            if libContent['zpy'] is None:
                libContent['zpy'] = libContent['name']
            item = {
                'name': libContent['name'],
                'zpy': libContent['zpy']
            }
            item = itemHandler(item, libFile)
            libContent['name'] = item['name']
            libContent['zpy'] = item['zpy']
            for item in libContent['functions']:
                item = itemHandler(item, libFile)
            for item in libContent['args']:
                item = itemHandler(item, libFile)
            if rewrite_rebuild:
                with open(libFile, 'w+', encoding='utf-8') as file:
                    file.seek(0)
                    file.truncate()
                    data = json.dumps(
                        libContent, sort_keys=False, ensure_ascii=False, indent=4, separators=(",", ":"))
                    file.write(data)
                print(f"File - {libContent['name']}.json Created")

    if build_init:
        timeStr = str(time.time())[:-8]
        filename = f'{path}/__init__.{timeStr}.py'
        libJList = []
        for libFile in libList:
            libDict = {}
            with open(libFile) as file:
                content = file.read()
                file.close()
            libContent = json.loads(content)
            libDict['name'] = libContent['name']
            libDict['zname'] = libContent['zpy']
            libDict['filetype'] = 'json'
            libDict['path'] = lib_dir + '/' + libContent['name'] + '.json'
            libJList.append(libDict)
        if rewrite_init:
            with open(filename, 'w+', encoding='utf-8') as file:
                file.seek(0)
                file.truncate()
                data = json.dumps(
                    libJList, sort_keys=False, ensure_ascii=False, indent=4, separators=(",", ":"))
                file.write(data)
            print(f"File - {filename} Created")

