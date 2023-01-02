#!/usr/bin/python3
def uppercase(str):
    """Print a string a upper case"""
    for c in str:
        of ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) -32)
        print("{}.format(c), end="")
    print("")
