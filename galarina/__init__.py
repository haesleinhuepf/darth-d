__version__ = "0.1.0"

try:
    from ._ipython_plugin import gala
except:
    pass
from ._gala import galarina
from ._vary import vary

