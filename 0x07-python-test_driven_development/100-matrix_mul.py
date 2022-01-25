#!/usr/bin/python3
"""Module to find the max integer in a list
"""


from typing import Type


def matrix_mul(m_a, m_b):
    """
    Raises:
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for items in m_a:
        if not isinstance(m_a, list):
            raise TypeError("m_a must be a list of list")

    for items in m_b:
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list of list")
    result = []
    for x in range(len(m_a)):
        col = 0
        row_result = []
        while col != len(m_b[0]):
            row, res = 0, 0
            for y in range(len(m_a[0])):
                res += m_a[x][y] * m_b[row][col]
                if row == len(m_b) - 1:
                    row_result.append(res)
                    col += 1
                    res, y = 0, 0
                row += 1
        result.append(row_result)
    return result
