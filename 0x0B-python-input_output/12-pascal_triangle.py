#!/usr/bin/python3

"""
python module
"""


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
