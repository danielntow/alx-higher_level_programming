#!/usr/bin/python3
"""
this is a module for that divides lements in matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list: The new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Error handling for matrix and its elements
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")

    # Error handling for the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements and rounding to 2 decimal places
    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list: The new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Error handling for matrix and its elements
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")

    # Error handling for the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements and rounding to 2 decimal places
    return list(
        map(
            lambda row: list(
                map(lambda element: round(element / div, 2), row)
            ),
            matrix
        )
    )


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list: The new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Error handling for matrix and its elements
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a list of lists of integers/floats")

    # Error handling for the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements and rounding to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list: The new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Error handling for an empty matrix
    if not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Ensure matrix is a list of lists
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Error handling for the matrix and its elements
    if not all(
        isinstance(element, (int, float))
        for row in matrix
        for element in row
    ):
        raise TypeError("matrix must be a list of lists of integers/floats")

    # Error handling for the len of matrix
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Error handling for the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements and rounding to 2 decimal places
    return [[round(
        float(element) / div, 2
    ) for element in row] for row in matrix]
