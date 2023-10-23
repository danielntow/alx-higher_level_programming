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
