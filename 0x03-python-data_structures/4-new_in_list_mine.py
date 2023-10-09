# Using list slicing to create a new list with the element replaced
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    else:
        new_list = my_list[:]  # Create a copy of the original list
        new_list[idx] = element  # Replace the element at the specified index
        return new_list

# Using list comprehension to create a new list with the element replaced
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    else:
        new_list = [my_list[i] if i != idx else element for i in range(len(my_list))]
        return new_list

# Using a loop to create a new list with the element replaced
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    else:
        new_list = my_list[:]  # Create a copy of the original list
        new_list[idx] = element  # Replace the element at the specified index
        return new_list
