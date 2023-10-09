#!/usr/bin/python3

# def max_integer(my_list=[]):
#     if len(my_list) == 0:
#         return None
#     max = 0
#     for i in range(len(my_list)):
#         if my_list[i] > max:
#             max = my_list[i]
#     return max

def max_integer(my_list=[]):
    if not my_list:
        return None
    return sorted(my_list, reverse=True)[-1]
