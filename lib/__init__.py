from .lib import Lib

from .__builtin__ import BUILT_IN
from .standard import STANDARD

lib = Lib(BUILT_IN)

lib.use(STANDARD)



