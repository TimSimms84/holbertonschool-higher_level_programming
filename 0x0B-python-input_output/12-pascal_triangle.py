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
        angle = 11 ** i
        tri = [int(j) for j in str(angle)]
        triangle.append(tri)
    return triangle
