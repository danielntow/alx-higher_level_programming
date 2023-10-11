# Option 1: Using the len() function on the dictionary's keys
def number_keys(a_dictionary):
    return len(a_dictionary.keys())

# Option 2: Iterating through the dictionary and counting keys


def number_keys(a_dictionary):
    count = 0
    for key in a_dictionary:
        count += 1
    return count

# Option 3: Using a list comprehension to count keys


def number_keys(a_dictionary):
    keys = [key for key in a_dictionary]
    return len(keys)

# Option 4: Using the enumerate() function


def number_keys(a_dictionary):
    return len(list(enumerate(a_dictionary)))

# Option 5: Converting dictionary to a list of key-value pairs and counting


def number_keys(a_dictionary):
    items = list(a_dictionary.items())
    return len(items)

# Option 6: Using a generator expression


def number_keys(a_dictionary):
    return sum(1 for _ in a_dictionary)

# Option 7: Using a while loop


def number_keys(a_dictionary):
    count = 0
    iterator = iter(a_dictionary)
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    return count
