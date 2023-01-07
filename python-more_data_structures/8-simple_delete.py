#!/usr/bin/python3
def simple_delete(dic, k):
    if k in dic:
        dic.pop(k)
        return dic
    else:
        return dic
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'tr')
