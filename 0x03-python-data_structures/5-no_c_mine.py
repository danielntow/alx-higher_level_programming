def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result


def no_c(my_string):
    return ''.join(char for char in my_string if char not in ('c', 'C'))


def no_c(my_string):
    i = 0
    result = ""
    while i < len(my_string):
        if my_string[i] not in ('c', 'C'):
            result += my_string[i]
        i += 1
    return result
