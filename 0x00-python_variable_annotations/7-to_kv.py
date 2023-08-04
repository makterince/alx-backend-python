#!/usr/bin/env python3
"""
module contains type-annotated function that creates a tuple string and
square of an int/float.
"""


from typing import Union, Tuple

def to_kv(k: str, v: union[int, float]) -> Tuple[str, float]:
    """ Create a tuple with a string and the square of an int/float."""

    return k, v ** 2.0
