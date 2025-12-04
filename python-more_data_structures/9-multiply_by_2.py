#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp_dictionary = dict(a_dictionary)
    for x in cp_dictionary:
        cp_dictionary[x] *= 2
    return cp_dictionary
