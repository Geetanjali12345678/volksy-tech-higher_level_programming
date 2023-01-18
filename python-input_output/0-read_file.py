#!/usr/bin/python3
"""docstring"""


def read_file(filename=""):
    """frgt"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
