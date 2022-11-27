
__title__ = "chat.py"
__author__ = "sus2790"
__copyright__ = "sus2790 2022-present"
# __verison__

import logging

from .webhook import *

logging.getLogger(__name__).addHandler(logging.NullHandler())
