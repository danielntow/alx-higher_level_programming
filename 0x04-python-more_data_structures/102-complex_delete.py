#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    if a_dictionary == {} or value is None:
        return a_dictionary

    for key, val in a_dictionary.items():
        if val != value:
            new_dict[key] = val

    return new_dict


def complex_delete(a_dictionary, value):
    return {key: val for key, val in a_dictionary.items() if val != value}


# correct one
def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        a_dictionary.pop(key, None)
    return a_dictionary
