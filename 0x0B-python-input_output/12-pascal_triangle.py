#!/usr/bin/python3
"""
Pascal's Triangle using Magic 11s
"""


def pascal_triangle(n):
    """
    Returns: list of pascal's Triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        sum = 11 ** i
        tri = [j for j in str(sum)]
        triangle.append(tri)
    return triangle
