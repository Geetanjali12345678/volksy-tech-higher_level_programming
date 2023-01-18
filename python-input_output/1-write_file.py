#!/usr/bin/python3
"""ddoc string"""



def number_of_lines(filename=""):
    """oooo"""

    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
