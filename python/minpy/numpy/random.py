from numpy import random
from . import numpy_wrapper

numpy_wrapper.wrap_namespace(random.__dict__, globals())
