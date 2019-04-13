"""This file contains classes for a simpler an easier print/log handeling"""

from warnings import warn
from enum import IntEnum, unique


@unique
class VerboseLevel(IntEnum):
    SILENT = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3

