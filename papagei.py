"""This file contains classes for a simpler an easier print/log handeling"""

from warnings import warn
from enum import IntEnum


class AutoNumber(IntEnum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = int.__new__(cls)
        obj._value_ = value
        return obj


class VerboseLevel(AutoNumber):
    SILENT = ()
    ERROR =()
    WARNING = ()
    INFO = ()
    DEBUG = ()
    FRIVOLOUS = ()


VERBOSE = VerboseLevel.FRIVOLOUS


def error(*args):
    if VERBOSE.value <= VerboseLevel.ERROR.value:
        print(*args)


def mock_error(*args):
    if VERBOSE.value <= VerboseLevel.ERROR.value:
        print(*args)


def mock_warning(*args):
    if VERBOSE.value <= VerboseLevel.WARNING.value:
        print(*args)


def warning(*args):
    if VERBOSE.value <= VerboseLevel.WARNING.value:
        print(*args)


def info(*args):
    if VERBOSE.value <= VerboseLevel.INFO.value:
        print(*args)


def debug(*args):
    if VERBOSE.value <= VerboseLevel.DEBUG.value:
        print(*args)


def frivolity(*args):
    if VERBOSE.value <= VerboseLevel.FRIVOLOUS.value:
        print(*args)


