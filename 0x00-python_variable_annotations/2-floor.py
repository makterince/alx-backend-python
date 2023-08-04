#!/usr/bin/env python3
"""
This module contains a type-annotated function calculates the floor of a float.
"""


def floor(n: float) -> int:
    """
    Calculate the floor of a float.
    Args:
        n (float): The input float.
    Returns:
        int: The floor of the input float.
    """

    return int(n // 1)
