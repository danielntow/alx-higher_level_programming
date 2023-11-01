#!/usr/bin/python3
"""
Module that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.

    Returns:
        np.ndarray: The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, a list of lists,
        or if one element in the lists is not an integer or a float.
        ValueError: If m_a or m_b is empty or
        if the matrices cannot be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for row in m_a + m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or \
floats or m_b should contain only integers or floats")
    if any(
        len(row) != len(m_a[0]) for row in m_a
    ) or any(
            len(row) != len(m_b[0]) for row in m_b):
        raise TypeError(
            "each row of m_a must be of the same size or each \
row of m_b must be of the same size")
    try:
        np_mat_a = np.array(m_a)
        np_mat_b = np.array(m_b)
        result = np.matmul(np_mat_a, np_mat_b)
        result = np.dot(m_a, m_b)

        # Convert the result from NumPy array to a Python list
        result_list = result.tolist()
        return result_list

    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")


if __name__ == "__main__":
    print("jel")
