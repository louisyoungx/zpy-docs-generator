import sys
if ".." not in sys.path: sys.path.insert(0,"..")

from lib import Lib

from lib.__builtin__ import BUILT_IN
from lib.standard import STANDARD
from lib.requests import REQUESTS

lib = Lib(BUILT_IN, 'warn')

lib.use(STANDARD).use(REQUESTS)

lib.load('time', 'zpy')
lib.load('requests', 'zpy')
