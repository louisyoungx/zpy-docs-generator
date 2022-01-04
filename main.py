from module import getModule
from lib import getLibs
from translate import translate
from files import files


def downloadAllLib():
    # libs - ['string.html', 're.html', 'difflib.html', 'textwrap.html']
    libs = getLibs()
    for lib in libs:
        module = getModule(lib)
        if module is not None:
            data = translate(module)
            files.create(module['name'], data)


def downloadSingleLib(lib):
    # lib - 'math.html'
    module = getModule(lib)
    if module is not None:
        data = translate(module)
        if data:
            files.create(module['name'], data)

downloadAllLib()