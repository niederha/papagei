"""This file contains classes for a simpler an easier print/log handeling"""

import warnings
from enum import IntEnum


class AutoNumber(IntEnum):
    """ Super class for auto numbering the Enumeration"""
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = int.__new__(cls)
        obj._value_ = value
        return obj


class VerboseLevel(AutoNumber):
    """ Used to check on the different verbose levels. Auto-numbered for easy changes"""
    SILENT = ()
    ERROR = ()
    WARNING = ()
    INFO = ()
    DEBUG = ()
    FRIVOLOUS = ()


class PapageiError(Exception):
    """ Error class to return actual errors"""
    def __init__(self, args):
        # Formats the arguments into a string for display (takes a tuple as input)
        self.msg = _format_string_from_tuple(args)

    def __str__(self):
        return self.msg


VERBOSE = VerboseLevel.FRIVOLOUS  # Change this variable to change the verbose level


def error(*args):
    if VERBOSE.value <= VerboseLevel.ERROR.value:
        raise PapageiError(args)


def mock_error(*args):
    if VERBOSE.value <= VerboseLevel.ERROR.value:
        print(*args)


def warning(*args):
    if VERBOSE.value <= VerboseLevel.WARNING.value:
        msg = _format_string_from_tuple(args)
        warnings.warn(msg)

def mock_warning(*args):
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

def _format_string_from_tuple(string_tuple):
    """ Gets a tuple and reformats it as a string """
    msg = ''
    for arg in string_tuple:
        msg += str(arg) + ' '
    msg = msg[:-1]  # Get rid of the last space
    return msg
