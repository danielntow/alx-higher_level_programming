#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                elem1 = my_list_1[i]
                elem2 = my_list_2[i]
                if not isinstance(elem1, (int, float)) or not isinstance(elem2, (int, float)):
                    print("wrong type")
                    result.append(0)
                elif elem2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(elem1 / elem2)
            except IndexError:
                print("out of range")
                result.append(0)

    finally:
        return result
