#!/usr/bin/env python3
"""
This module contains type-annotated function that creates a multiplier function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ creates a multiplier function """

    def mult_func(x: float) -> float:
        """ function performs the multiplication """

        return x * multiplier

    return mult_func
