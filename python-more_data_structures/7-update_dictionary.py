def update_dictionary(dic, k, v):
    dic[k] = v
    return dic
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
