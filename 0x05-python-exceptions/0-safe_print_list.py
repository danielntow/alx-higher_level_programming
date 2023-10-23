#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break
    print()
    return printed_count


def safe_print_list(my_list=[], x=0):
    printed_count = 0
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break
        i += 1
    print()
    return printed_count


def safe_print_list(my_list=[], x=0):
    printed_count = 0
    for i, item in enumerate(my_list):
        if i >= x:
            break
        try:
            print("{}".format(item), end=" ")
            printed_count += 1
        except IndexError:
            break
    print()
    return printed_count


def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of elements printed
    try:
        for item in my_list:
            if count >= x:
                break  # Exit the loop once x elements are printed
            print(item, end=" ")  # Print the element followed by a space
            count += 1  # Increment the counter
        print()  # Print a new line after all elements
    except IndexError:
        pass  # Handle the case where x is larger than the length of my_list
    return count  # Return the count of printed elements


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
