#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        result.append(new_row)
    return result


def square_matrix_simple(matrix=[]):
    result = [[num ** 2 for num in row] for row in matrix]
    return result


def square_matrix_simple(matrix=[]):
    # Use map with a lambda function to compute the square values
    result = list(map(lambda row: list(
        map(lambda value: value ** 2, row)), matrix))
    return result


def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        result.append([x**2 for x in row])
    return result
