#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=lambda key: a_dictionary[key])
    return max_key


def best_score(a_dictionary):
    if not a_dictionary:  # Check if the dictionary is empty
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_key = key
            best_value = value

    return best_key
