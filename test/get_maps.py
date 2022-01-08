import sys
if ".." not in sys.path: sys.path.insert(0,"..")

from lib import lib
print(lib.pyLibs)
lib.load('time', 'zpy')
print(lib.zpyMap)