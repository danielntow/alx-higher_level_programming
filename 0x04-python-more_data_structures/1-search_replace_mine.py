#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            item = replace
        new_list.append(item)
    return new_list


#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list


def search_replace(my_list, search, replace):
    result = list(map(lambda x: replace if x == search else x, my_list))
    return result


def search_replace(my_list, search, replace):
    def replace_item(item):
        return replace if item == search else item
    return list(map(replace_item, my_list))


def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]
