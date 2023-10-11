def common_elements(set_1, set_2):
    result = set_1.intersection(set_2)
    return result


def common_elements(set_1, set_2):
    unique = []
    for num in set_1:
        for nums in set_2:
            if num == nums:
                unique.append(num)
    return list(unique)


def common_elements(set_1, set_2):
    common_elements = set()
    for num in set_1:
        if num in set_2:
            common_elements.add(num)
    return common_elements


def common_elements(set_1, set_2):
    result = [num for num in set_1 if num in set_2]
    # Convert the result to a set to remove duplicates if needed
    return set(result)


def common_elements(set_1, set_2):
    return set_1 & set_2
