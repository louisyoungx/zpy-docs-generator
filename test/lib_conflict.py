import sys
if ".." not in sys.path: sys.path.insert(0,"..")

from lib import Lib

from lib.__builtin__ import BUILT_IN
from lib.standard import STANDARD

lib = Lib(BUILT_IN, 'error')

lib.use(STANDARD)

lib.load('time', 'zpy')
