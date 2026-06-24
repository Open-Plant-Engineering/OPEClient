import os
import sys

_inner_pkg_path = os.path.join(os.path.dirname(__file__), "OPE_CLIENT")

__path__ = [_inner_pkg_path]

if _inner_pkg_path not in sys.path:
    sys.path.insert(0, _inner_pkg_path)

from OPE_CLIENT import *  