#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    for i in matrix:
        a = map(lambda num: num**2, i)
        lst.append(list(a))
    return lst
