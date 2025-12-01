#!/usr/bin/python3
def no_c(my_string):
    cp_string = ""
    for x in my_string:
        if x == "c" or x == "C":
            cp_string += ""
        else:
            cp_string += x
    return cp_string
