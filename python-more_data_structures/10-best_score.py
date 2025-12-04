#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    (a_key, a_value) = next(iter(a_dictionary.items()))
    for key, value in a_dictionary.items():
        if value > a_value:
            a_value = value
            a_key = key
    return a_key
