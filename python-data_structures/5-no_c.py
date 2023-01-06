#!/usr/bin/python3
def no_c(my_string):
    a=[]
    for i in my_string:
        if i !=  "C" and i != "c":
            a.append(i)
    return a
