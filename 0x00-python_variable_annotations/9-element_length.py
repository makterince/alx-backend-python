#!/usr/bin/env python3
"""
module is correcting a function provided
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ Calculate the length of elements in a list of strings. """

    return [(i, len(i)) for i in lst]
