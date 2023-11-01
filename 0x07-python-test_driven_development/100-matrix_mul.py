#!/usr/bin/python3
"""
this is a module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.

    Returns:
        list: The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, a list of lists, \
        or if one element in the lists is not an integer or a float.
        ValueError: If m_a or m_b is empty or if \
        the matrices cannot be multiplied.
    """
    # Function to check if a variable is a list of lists
    def is_list_of_lists(matrix):
        return isinstance(
            matrix, list
        ) and all(isinstance(row, list) for row in matrix)

    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a is a list of lists
    if not is_list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if not is_list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    # Check if elements are integers or floats
    for row in m_a + m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats or \
m_b should contain only integers or floats")

    # Check if matrices are rectangular
    if any(
        len(row) != len(m_a[0]) for row in m_a
    ) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError(
            "each row of m_a must be of the same size or \
each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = [[sum(a * b for a, b in zip(m_a_row, m_b_col))
               for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return result
