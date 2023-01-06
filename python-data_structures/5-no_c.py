#!/usr/bin/python3
def no_c(my_string):
    copy = []
    for i in my_string:
        if i != "C" and i != "c":
            copy.append(i)
    return ''.join(copy)
