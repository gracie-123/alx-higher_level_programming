#!/usr/bin/python3
"""define function"""


def append_write(filename="", text=""):
    """function appends a string at end of a text file (UTF8) and
    returns the number of characters added"""
    with open(filename, "a", encoding="UTF-8") as f:
        return (f.write(text))
