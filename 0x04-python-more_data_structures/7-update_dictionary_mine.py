def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def update_dictionary(a_dictionary, key, value):
    a_dictionary.setdefault(key, value)
    return a_dictionary
