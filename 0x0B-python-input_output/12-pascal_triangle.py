#!/usr/bin/python3

"""
python module
"""


def pascal_triangle_dynamic(n):
    """
    Generates Pascal's Triangle using a dynamic programming approach.

    Args:
        n (int): Number of rows for the Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1]
                         for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle


def pascal_triangle_recursive(n):
    """
    Generates Pascal's Triangle using a recursive approach.

    Args:
        n (int): Number of rows for the Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle_recursive(n - 1)
        new_row = [1]
        for i in range(1, len(triangle[-1])):
            new_row.append(triangle[-1][i - 1] + triangle[-1][i])
        new_row.append(1)
        triangle.append(new_row)
        return triangle


def pascal_triangle_algebraic(n):
    """
    Generates Pascal's Triangle using an algebraic approach.

    Args:
        n (int): Number of rows for the Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = row[j - 1] * (i - j) // (j)
        triangle.append(row)

    return triangle


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of n rows.

    Args:
        n (int): Number of rows for the Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initializing each row with 1s
        if i >= 2:
            # Calculating elements in between the ends of the rows
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
