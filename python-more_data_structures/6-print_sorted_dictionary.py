#!/usr/bin/python3
def print_sorted_dictionary(dic):
    keys = list(dic.keys())
    keys.sort()
    for i in keys:
        print('{}: {}'.format(i, dic[i]))
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
