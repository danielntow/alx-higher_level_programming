#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total_count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                total_count += 1
            else:
                continue
        except IndexError:
            break
    print()
    return total_count


def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integers printed
    for item in my_list:
        if count >= x:
            break  # Exit the loop once x integers are printed
        try:
            print("{:d}".format(item), end="")
            count += 1  # Increment the counter
        except (ValueError, TypeError):
            pass  # Skip non-integer values
    print()  # Print a new line after all integers
    return count
