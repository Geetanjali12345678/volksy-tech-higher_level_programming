#!/usr/bin/python3
st = "DCCVII"
d1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
sum =0

for i in range(len(st)):
    value = d1[st[i]]
    if i+1 < len(st) and d1[st[i+1]] > value:
        sum -= value
    else:
        sum += value
