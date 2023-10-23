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


def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(0, list_length):
            try:
                result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
                continue
            except TypeError:
                result.append(0)
                print("wrong type")
                continue
            except IndexError:
                result.append(0)
                print("out of range")
                continue
    finally:
        return result


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]
            division_result = elem1 / elem2 if (isinstance(
                elem1, (int, float)) and isinstance(elem2, (int, float)) and elem2 != 0) else 0
            result.append(division_result)
        except (IndexError, ZeroDivisionError):
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
    return result
