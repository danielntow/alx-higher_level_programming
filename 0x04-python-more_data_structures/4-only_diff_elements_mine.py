def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2


def only_diff_elements(set_1, set_2):
    return [num for num in set_1 if num not in set_2] + [num for num in set_2 if num not in set_1]


def only_diff_elements(set_1, set_2):
    return (set_1 - set_2) | (set_2 - set_1)


def only_diff_elements(set_1, set_2):
    return set([x for x in set_1 if x not in set_2] + [x for x in set_2 if x not in set_1])
