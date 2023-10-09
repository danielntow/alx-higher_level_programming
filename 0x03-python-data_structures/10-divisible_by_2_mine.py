def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]


def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result


def divisible_by_2(my_list=[]):
    return list(map(lambda num: num % 2 == 0, my_list))
