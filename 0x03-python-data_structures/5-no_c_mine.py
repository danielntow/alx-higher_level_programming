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

def no_c(my_string):
  """Removes all occurrences of the characters 'c' and 'C' from a string.

  Args:
    my_string: A string.

  Returns:
    A string with all occurrences of the characters 'c' and 'C' removed.
  """

  result = ''.join(char for char in my_string if char not in 'cC')
  return result




def no_c(my_string):
    result = ''.join(map(lambda x: x if x not in 'cC' else '', my_string))
    return result
